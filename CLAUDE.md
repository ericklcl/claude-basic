# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
uv run main.py        # Run the application
uv add <package>      # Add a dependency
uv sync               # Install dependencies from uv.lock
```

## Architecture

Single-file project (`main.py`) managed with `uv`. Dependencies are declared in `pyproject.toml` and locked in `uv.lock`.

- `main.py` — entry point; contains all logic
- `pyproject.toml` — project metadata and dependencies (Python >=3.12)

Currently fetches current weather data from the [Open-Meteo API](https://open-meteo.com/) (no API key required) for a hardcoded coordinate and prints temperature, wind speed, and weather code.
