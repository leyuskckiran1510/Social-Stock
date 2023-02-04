#!./../virtual/bin/python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    if len(sys.argv) < 2:
        sys.argv = [sys.argv[0], "runserver"]
    if sys.argv[1] == "make":
        sys.argv[1] = "makemigrations"
    if sys.argv[1] == "mi":
        sys.argv[1] = "migrate"
    if sys.argv[1] == "f":
        sys.argv[1] = "flush"
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
