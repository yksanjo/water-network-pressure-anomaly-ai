# Deployment

## Commands

```bash
pip install -e .[dev]
pytest -q
python -m src.main
```

## Readiness

1. CI passing.
2. Health endpoint monitored.
3. Rollback command prepared.
