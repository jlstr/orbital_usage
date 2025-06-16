# Orbital Usage API

> This project has been deployed to [Render Cloud Application Platform](https://render.com/) and can be found here: [https://orbital-usage.onrender.com/usage](https://orbital-usage.onrender.com/usage). ⚠️ Disclaimer: Render's Free Tier shuts down after 15 minutes of inactivity, you may see  a screen like this one if the service stopped and it's restarting...

![Render loading screen](https://ibb.co/jkr1s7b8)

## 📦 Installation of Required Dependencies

> Note: This project was developed and tested on macOS with Python 3.11. Installation steps might differ slightly for Linux or Windows environments. All commands below are intended to be executed from the Terminal.

### 1. Install Homebrew (macOS Only)

Homebrew is a package manager for macOS, which simplifies the installation of development tools and libraries.

To install Homebrew, run:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
More information: https://brew.sh

### 2. Install Python 3.11

Ensure you have Python 3.11 installed:

```
brew install python@3.11
```

### 3. Install Poetry

Poetry is a dependency and virtual environment manager for Python.

```
brew install poetry
```

More info: https://python-poetry.org

### 4. Install Project Dependencies

Navigate to the root of the project and run:

```
poetry install
```

This will:

- Create and activate a virtual environment
- Install all required dependencies specified in `pyproject.toml`, including:

  - `fastapi` – the main web framework (see: https://fastapi.tiangolo.com/)
  - `pydantic` – for data validation
  - `pytest`, `pytest-asyncio` – for testing
  - `httpx`,  - Async Http Request module
  - `uvicorn` - Web Server compatible with Render

To activate the Poetry virtual environment:

```
source .venv/bin/activate
```

### 🏗️ Project Structure

```
orbital_usage_api/
│
├── pyproject.toml                 # Poetry project definition & dependencies
├── poetry.lock
│
├── src/
│   └── orbital_usage_api/
│       ├── usage_logic.py         # Core async logic for assembling usage reports
│       ├── models.py              # Pydantic models: UsageRecord, UsageResponse
│       ├── data.py                # Data access functions (fetch messages, reports)
│       └── calculations.py        # Logic to calculate credit usage from messages
│       └── main.py                # Public API endpoints including /usage
│
├── tests/
│   ├── test_usage_logic.py        # Unit tests for usage logic
│   └── test_models.py             # Model validation tests
│   └── test_calculations.py       # Unit tests for credit calculation per message
│
└── README.md
```
### ✅ Running Tests

To execute all tests, simply run from the root:

```
poetry run pytest
```

This command will:

- Discover all test_*.py files under the tests/ folder
- Run both sync and async test functions
- Report results with detailed failure tracebacks if needed

Sample Output:

```
============================= test session starts =============================
platform darwin -- Python 3.13.5, pytest-8.4.0, pluggy-1.6.0
rootdir: /Users/jose/Desktop/orbital-usage-api
configfile: pyproject.toml
plugins: anyio-4.9.0, asyncio-1.0.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 21 items

tests/test_calculationspy .............                              [ 61%]
tests/test_modes.py ...................                              [ 85%]
tests/test_usage_logic.py .............                              [100%]
============================= 21 passed in 0.29s =============================
```

### 🚀 Running the Project Locally

For this instantiate the Uvicorn web server using the following command:

```
poetry run uvicorn src.orbital_usage_api.main:app --reload
```

Sample run:

```
INFO:     Will watch for changes in these directories: ['/Users/jose/Desktop/orbital-usage-api']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [41812] using StatReload
INFO:     Started server process [41817]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Once Uvicorn has started successfully, you may access the `/usage` endpoint in a browser like Chrome by visiting the following URL(s):

[http://127.0.0.1:8000/usage](http://127.0.0.1:8000/usage)

OR

[http://localhost:8000/usage](http://localhost:8000/usage)

### 📝 Notes

- Python isn’t my main language, but I’m comfortable working with it, if something looks off please bear with me.

- I have worked mostly in other languages recently, so if anything seems non-idiomatic Python, I’m happy to adjust.

- The Tech Stack for this Challenge I had to learn in a short timespan.

### ⚠️ Assumptions

- FastAPI framework was used for API building (`/usage` endpoint)

  FastAPI is a modern, high-performance Python web framework for building APIs with automatic validation and OpenAPI generation. See: https://fastapi.tiangolo.com/

- Pydantic powers schema validation.

  Both `UsageRecord` and `UsageResponse` are defined using Pydantic models, making them directly serializable to and from JSON.

- Testing uses pytest and asyncio.

  All async logic is tested using `pytest` with the help of `pytest-asyncio`. Tests are structured and readable

- Built for mocking and testability.

  The core `compute_usage_report()` function is pure and async. It takes no parameters but depends on externally swappable data providers, making it ideal for unit tests.