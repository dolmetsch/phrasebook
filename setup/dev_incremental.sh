#!/bin/bash

# activate the virtual environment
. venv/bin/activate

# install dependencies
pip install -r requirements.txt

# migrate database if needed
./manage.py migrate

# translate locale
cd phrasebook
../manage.py compilemessages -l ru
cd ..
