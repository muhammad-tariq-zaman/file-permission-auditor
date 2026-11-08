"""Audit file permissions from a directory listing.

Usage: python3 main.py files.csv
CSV columns: path,mode (octal, e.g. 644),owner.
WORLD-WRITABLE is HIGH risk, GROUP-WRITABLE MEDIUM, otherwise OK.
Highest risk first.
"""
import argparse, csv, sys

def audit(rows):
    out = []
    for row in rows:
        mode = int(row["mode"].strip(), 8)
        if mode & 0o002:
            verdict, risk = "WORLD-WRITABLE", "HIGH"
        elif mode & 0o020:
            verdict, risk = "GROUP-WRITABLE", "MEDIUM"
        else:
            verdict, risk = "OK", "LOW"
        out.append((row["path"], row["mode"].strip(), verdict, risk))
    order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    return sorted(out, key=lambda r: order[r[3]])

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        for path, mode, verdict, risk in audit(list(csv.DictReader(f))):
            print(f"{path} ({mode}): {verdict} [{risk}]")
    return 0

if __name__ == "__main__":
    sys.exit(main())
