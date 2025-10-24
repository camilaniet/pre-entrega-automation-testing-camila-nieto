# run_test.py
import pytest
from pathlib import Path

def main():
    repo_root = Path(__file__).resolve().parent
    reports_dir = repo_root / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    test_files = [
        repo_root / "tests" / "test_login.py",
        repo_root / "tests" / "test_inventory.py",
        repo_root / "tests" / "test_cart.py",
    ]

    args = [str(p) for p in test_files] + [
        "-v",
        f"--html={reports_dir / 'reporte.html'}",
        "--self-contained-html",
    ]
    return pytest.main(args)

if __name__ == "__main__":
    raise SystemExit(main())