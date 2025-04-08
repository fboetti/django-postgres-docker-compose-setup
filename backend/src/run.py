import os
import typer

from utils.startup import run_django_server

typer_app = typer.Typer()


@typer_app.command()
def run_migrations(
    make: bool = False,
    migrate: bool = False,
) -> None:
    """
    Run the Django migrations.
    """
    if make:
        print("🛠️ Making migrations...")
        os.system("python manage.py makemigrations")
    if migrate:
        print("🚀 Running migrations...")
        os.system("python manage.py migrate")


@typer_app.command()
def run_server(
    migrate: bool = False,
) -> None:
    print("🚀 Starting backend...")
    run_django_server(migrate=migrate)


if __name__ == "__main__":
    typer_app()
