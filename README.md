# file-permission-auditor

Audit file permissions from a listing CSV: world-writable files are HIGH risk, group-writable MEDIUM, the rest OK — highest risk first.

## How to run

```sh
python3 main.py files.csv
```

## Example output

```
/srv/shared/notes.txt (666): WORLD-WRITABLE [HIGH]
/etc/hosts (644): OK [LOW]
```

Standard library only. Run the tests with `python3 -m unittest discover`.
