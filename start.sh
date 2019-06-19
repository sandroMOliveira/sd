#!/usr/bin/env bash
echo Starting Gunicorn.
exec gunicorn gulugulu.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3