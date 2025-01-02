#!/bin/bash
uv run flask db upgrade
exec uv run flask run --debug --host 0.0.0.0