#!/bin/bash
uwsgi --ini /etc/uwsgi/development.ini & 
python3 /site/start.py
wait 
