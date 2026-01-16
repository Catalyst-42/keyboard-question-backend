#!/bin/bash
echo "Building the project..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput --clear
echo "Build complete."
