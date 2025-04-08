# django-postgres-docker-compose-setup
An example of how we can setup a containerized backend-environment based on Django framework with Postgresql database


## Database Migrations

To perform database migrations, run these two following commands from the root folder:

- MAKE      -> "docker compose run --rm backend run-migrations --make"
- MIGRATE   -> "docker compose run --rm backend run-migrations --migrate"