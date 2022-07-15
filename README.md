# PhraseBook (Django-based)

## Requirements
* python3+ (tested with 3.9)

## Development setup
```sh
git clone <phrasebook.git>
cd phrasebook
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py loaddata phrasebook/fixture.json
./manage.py createsuperuser
./manage.py runserver
# and go to http://127.0.0.1:8000/admin
# and http://127.0.0.1:8000/api/phrasebook
```
