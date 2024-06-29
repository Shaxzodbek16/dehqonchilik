#!/bin/bash

echo "Migrations running"
python manage.py makemigrations

sleep 2

echo "Migrating"
python manage.py migrate

sleep 2

echo "Running"
python manage.py runserver

