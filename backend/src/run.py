if __name__ == "__main__":
    # Run django migrations ('python manage.py migrate') 
    # and runserver command ('python manage.py runserver')
    import os
    import sys

    # Set the default settings module for the 'django' program.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_setup.settings")
    # Add the project directory to the Python path.
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # Import the Django management module.
    # Execute the command line arguments.
    os.system("python manage.py migrate")
    os.system("python manage.py runserver 0.0.0.0:8000")
