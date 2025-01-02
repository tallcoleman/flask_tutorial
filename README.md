# flask_tutorial
 
## How to run

```bash
# local development
$ uv run task dev

# test build
$ uv run task docker_run
$ uv run task docker_stop
```

### Migrations

```bash
$ uv run flask db migrate -m "DESCRIPTION HERE"
$ uv run flask db upgrade
```

## Steps to building a feature

- need to update template file(s)
- need to update view function
- may need to add a form class
- may need to update the database schema