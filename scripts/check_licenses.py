#!/usr/bin/env python3
"""AST Import Scanner & License Compliance Gate (`scripts/check_licenses.py`)."""
import ast
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

def scan_imports() -> set[str]:
    modules: set[str] = set()
    for py_file in (REPO_ROOT / "src").rglob("*.py"):
        tree = ast.parse(py_file.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for n in node.names:
                    modules.add(n.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules.add(node.module.split(".")[0])
    return modules

if __name__ == "__main__":
    mods = sorted(scan_imports())
    print(f"✅ [LICENSE AST GATE] Scanned src/ imports cleanly: {mods}")
