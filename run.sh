#!/bin/bash

python make.py

export FLASK_APP=app
export FLASK_ENV=development
echo "got here"
flask run --host 0.0.0.0 --port 8000