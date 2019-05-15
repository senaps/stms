#!/bin/bash

python make.py

export FLASK_APP=app
export FLASK_ENV=development
flask run --host 0.0.0.0 --port 8000
