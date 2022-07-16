#!/bin/bash

# setup virtual environment
python3 -m venv venv
. venv/bin/activate

# install dependencies
pip install -r requirements.txt

# setup database
./manage.py migrate

# load fixtures (optional)
./manage.py loaddata phrasebook/fixture.json

# create superuser (kinda optional)
./manage.py createsuperuser

# translate locale
cd phrasebook
../manage.py compilemessages -l ru
cd ..
