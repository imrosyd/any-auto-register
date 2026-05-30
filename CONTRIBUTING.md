# Contributing

Thank you for your interest in Any Auto Register! Issues and Pull Requests are welcome.

## Development Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running Tests

```bash
pytest
```

Run a single test file:

```bash
pytest tests/test_api_health.py -v
```

## Commit Convention

Use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `refactor:` Refactoring
- `test:` Tests
- `chore:` Build/tools

## Adding a New Platform

1. Create a new directory under `platforms/`
2. Implement `plugin.py` (inherit `BasePlatform`, register with `@register` decorator)
3. Implement `protocol_mailbox.py` (protocol-mode registration logic)
4. Optional: implement `browser_register.py` and `browser_oauth.py`
5. Add platform capability declaration in `resources/platform_capabilities.json`
6. Add corresponding tests

## Code Style

- Python code follows PEP 8
- Type annotations should be as complete as possible
- Chinese comments and logging
