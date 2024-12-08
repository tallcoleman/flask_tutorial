#!/bin/bash
uv run --no-dev flask db upgrade
exec uv run --no-dev gunicorn -b :8080 --access-logfile - --error-logfile - microblog:app