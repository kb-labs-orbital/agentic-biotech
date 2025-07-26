# 📦 Project Structure & Import Path Setup

This project follows the **standardized `src/` layout** for Python packages. This design improves clarity, prevents accidental relative imports, and ensures predictable behavior across environments, tests, and deployments.

By default, Python does not look inside the `src/` folder when resolving imports. Therefore, we explicitly configure paths and tooling to recognize our package structure.

---

## 🧭 Why `src/` Layout?

Using a top-level `src/` directory helps prevent:

- Accidental imports from local files shadowing packages (e.g. `biotech.py` vs. `biotech/`).
- Confusion between test and production modules.
- Bugs in CI/CD pipelines caused by inconsistent path resolution.

---

## 🔐 Gold-Standard Configuration

| Element               | Best Practice                                                                 |
|-----------------------|--------------------------------------------------------------------------------|
| **Project layout**     | Use `src/` layout                                                              |
| **Poetry config**      | `packages = [{ include = "biotech", from = "src" }]` in `pyproject.toml`       |
| **PYTHONPATH setup**   | Set via `PYTHONPATH=src` or via `pytest.ini`                                  |
| **Test structure**     | Keep all `tests/` outside `src/`                                               |
| **Imports**            | Use absolute imports (`from biotech.llm.loader import load_model`)            |

---

## ✅ Setup Instructions

### 1. Configure `pyproject.toml` for Poetry

Add this under the `[tool.poetry]` section:

```toml
packages = [{ include = "biotech", from = "src" }]

### 2. Set Up Pytest

Create or edit a `pytest.ini` file in the project root:

```ini title="pytest.ini"
[pytest]
python_paths = src


