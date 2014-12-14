#!/usr/bin/env python
import os
import sys
import os
import django
from polls import models



#  print(models.MyModel.objects.get(pk=1))

if __name__ == "__main__":
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Progetto_django.settings")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
    django.setup()
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
