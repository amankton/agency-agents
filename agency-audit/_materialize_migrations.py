from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

import _generate_agency_audit as audit


ROOT = audit.ROOT
AUDIT = audit.AUDIT
PROMOTED_ROOT = AUDIT / "promoted-agents"
LEGACY_ROOT = AUDIT / "legacy-agents"


MANAGED_FIELDS = {
    "description",
    "migration_batch",
    "migration_decision",
    "migration_runtime_status",
    "migration_status",
    "migration_canonical_agent_id",
    "migration_refactored_prompt",
    "migration_acceptance_tests",
    "migration_promoted_path",
}


def split_frontmatter(text: str) -> tuple[list[str], str]:
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("malformed frontmatter")
    frontmatter = [line.rstrip("\n") for line in parts[1].strip("\n").splitlines()]
    return frontmatter, parts[2].lstrip("\n")


def safe_scalar(value: str) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    value = value.replace(": ", " - ")
    value = value.replace("#", "number")
    return value


def update_frontmatter(lines: list[str], updates: dict[str, str]) -> list[str]:
    retained = []
    for line in lines:
        key = line.split(":", 1)[0].strip() if ":" in line else ""
        if key not in MANAGED_FIELDS:
            retained.append(line)
    for key, value in updates.items():
        retained.append(f"{key}: {safe_scalar(value)}")
    return retained


def batch_records() -> list[dict]:
    agents = audit.discover_agents()
    by_path = {agent["file_path"]: agent for agent in agents}
    records: list[dict] = []
    for batch_id, group in audit.batch_groups():
        for batch in group:
            batch["batch_id"] = batch_id
            batch["agent"] = by_path[batch["file_path"]]
            batch["slug"] = audit.slugify(Path(batch["file_path"]).stem)
            records.append(batch)
    return records


def routing_lines(batch: dict) -> str:
    status = audit.runtime_status(batch["decision"])
    targets = audit.route_targets(batch)
    canonical = batch["agent"]["agent_id"] if status == "active" else audit.slugify(targets[0]) if targets else batch["agent"]["agent_id"]
    target_text = ", ".join(targets) if targets else batch["agent"]["agent_name"]
    return f"""## Migration Routing
- Migration batch: `{batch["batch_id"]}`
- Decision: `{batch["decision"]}`
- Runtime status: `{status}`
- Canonical agent id: `{canonical}`
- Routes to: {target_text}
"""


def promoted_body(batch: dict) -> str:
    body = audit.refactored_prompt(batch).strip()
    marker = "\n## Identity\n"
    if marker in body:
        return body.replace(marker, f"\n{routing_lines(batch)}\n## Identity\n", 1) + "\n"
    return body + "\n\n" + routing_lines(batch) + "\n"


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8", newline="\n")


def materialize(promote_source: bool) -> dict:
    records = batch_records()
    summary = {
        "total_agents": len(records),
        "promoted_overlays": 0,
        "promoted_sources": 0,
        "legacy_backups": 0,
        "decisions": {},
        "files": [],
    }
    for batch in records:
        rel = Path(batch["file_path"])
        source = ROOT / rel
        source_text = source.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
        frontmatter, _body = split_frontmatter(source_text)

        status = audit.runtime_status(batch["decision"])
        targets = audit.route_targets(batch)
        canonical = batch["agent"]["agent_id"] if status == "active" else audit.slugify(targets[0]) if targets else batch["agent"]["agent_id"]
        promoted_rel = Path("agency-audit/promoted-agents") / rel
        updates = {
            "description": batch["function"],
            "migration_batch": batch["batch_id"],
            "migration_decision": batch["decision"],
            "migration_runtime_status": status,
            "migration_status": "promoted_source" if promote_source else "promoted_overlay",
            "migration_canonical_agent_id": canonical,
            "migration_refactored_prompt": f"agency-audit/refactored-agents/{batch['slug']}.md",
            "migration_acceptance_tests": f"agency-audit/acceptance-tests/{batch['slug']}.tests.md",
            "migration_promoted_path": str(promoted_rel).replace("\\", "/"),
        }
        migrated_frontmatter = update_frontmatter(frontmatter, updates)
        migrated = "---\n" + "\n".join(migrated_frontmatter) + "\n---\n\n" + promoted_body(batch)

        overlay_path = PROMOTED_ROOT / rel
        write_text(overlay_path, migrated)
        summary["promoted_overlays"] += 1
        summary["decisions"][batch["decision"]] = summary["decisions"].get(batch["decision"], 0) + 1

        record = {
            "agent_id": batch["agent"]["agent_id"],
            "decision": batch["decision"],
            "runtime_status": status,
            "source_path": str(rel).replace("\\", "/"),
            "promoted_path": str(promoted_rel).replace("\\", "/"),
        }

        if promote_source:
            backup_path = LEGACY_ROOT / rel
            if not backup_path.exists():
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, backup_path)
                summary["legacy_backups"] += 1
            write_text(source, migrated)
            summary["promoted_sources"] += 1
            record["legacy_backup_path"] = str(Path("agency-audit/legacy-agents") / rel).replace("\\", "/")

        summary["files"].append(record)

    summary_path = AUDIT / "migration_promotion_summary.json"
    write_text(summary_path, json.dumps(summary, indent=2, ensure_ascii=True))
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Materialize audited agent migrations.")
    parser.add_argument("--promote-source", action="store_true", help="Also replace canonical source prompt files after writing promoted overlays.")
    args = parser.parse_args()
    summary = materialize(promote_source=args.promote_source)
    print(json.dumps({k: v for k, v in summary.items() if k != "files"}, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    main()
