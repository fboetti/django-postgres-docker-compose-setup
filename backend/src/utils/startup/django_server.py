import os
import sys

__all__ = [
    "run_django_server",
]


def run_django_server(
    migrate: bool,
) -> None:
    """
    Run the Django server.
    """

    # Set the default settings module for the 'django' program.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_setup.settings")
    # Add the project directory to the Python path.
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # Import the Django management module.
    # Execute the command line arguments.

    if migrate:
        os.system("python manage.py migrate")
    
    # Run the Django development server on all interfaces at port 8000.
    os.system("python manage.py runserver 0.0.0.0:8000")
