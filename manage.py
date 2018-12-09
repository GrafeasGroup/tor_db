import sys

# noinspection PyUnresolvedReferences
from tor_db import settings

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
