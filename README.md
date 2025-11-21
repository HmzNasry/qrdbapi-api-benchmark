# QRDBAPI Benchmarking Tool

## Part 1: Setup and Running

### Virtual Environment

Create venv:

```bash
python -m venv .venv
```

Activate venv (Linux/macOS):

```bash
source .venv/bin/activate
```

Activate venv (Windows):

```bash
.venv\Scripts\activate
```
### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Benchmarks

Run all systems:

```bash
python main.py start
```

Run a specific system:

```bash
python main.py start --system fastapi
```

### Generate Charts

Visualize latest run:

```bash
python main.py visualize
```

Visualize a specific file:

```bash
python main.py visualize outputs/results_2025-11-21_14-00.json
```

## Part 2: Configuration

All configuration lives in `inputs/benchmarks.json`.

### Global Settings

```json
"config": {
  "iterations": 50,
  "remove_outliers": true,
  "timeout_seconds": 60
}
```

### Systems (Base URLs)

```json
"systems": {
  "mm": "https://dbapimm.quranresearch.org",
  "fastapi": "http://127.0.0.1:8000",
  "dotnet_ssd": "https://dotnet-ssd.example.com"
}
```

### Scenarios (Endpoints)

```json
{
  "name": "Get User Details",
  "endpoints": {
    "mm": "/users?id=1",
    "fastapi": "/api/v1/users/1",
    "dotnet_ssd": null
  }
}
```

* Use null to skip a system.

## Part 3: File Structure

* **inputs/benchmarks.json**: All configuration settings.
* **outputs/**: Stores JSON results and HTML charts.
* **main.py**: CLI entry point.

