<div align="center">

# teo-pytest-config-shared

**Shared pytest and coverage configuration for teo-garcia Python templates**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/teo-pytest-config-shared?color=blue)](https://pypi.org/project/teo-pytest-config-shared)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)](https://python.org)

Part of the [@teo-garcia/templates](https://github.com/teo-garcia/templates) ecosystem

</div>

---

## Settings

| Setting | Value |
| --- | --- |
| **asyncio_mode** | auto |
| **testpaths** | tests |
| **addopts** | --strict-markers |
| **coverage omit** | tests/* |
| **coverage fail_under** | 80 |

---

## Requirements

- Python 3.12+
- pytest 8.3+
- pytest-cov 6.0+

---

## Usage

Install as a dev dependency:

```bash
uv add --dev teo-pytest-config-shared
```

Get the path to the installed config file:

```bash
uv run teo-pytest-config-path
```

pytest does not support config inheritance natively. The recommended pattern is to copy the canonical settings into your `pyproject.toml` and extend them:

```toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]
addopts = "--strict-markers"
markers = ["e2e: end-to-end tests requiring live services"]

[tool.coverage.run]
source = ["app"]
omit = ["tests/*"]

[tool.coverage.report]
show_missing = true
fail_under = 80
```

Use `teo-pytest-config-path` to inspect the canonical baseline whenever you update your project config.

---

## Related Packages

| Package | Description |
| --- | --- |
| `teo-ruff-config-shared` | Ruff lint and format settings |
| `teo-mypy-config-shared` | mypy type-checking settings |

---

## License

MIT

---

<div align="center">
  <sub>Built by <a href="https://github.com/teo-garcia">teo-garcia</a></sub>
</div>
