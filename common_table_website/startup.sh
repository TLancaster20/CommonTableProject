#!/bin/bash
python manage.py collectstatic && gunicorn --workers 2 common_table_website.wsgi