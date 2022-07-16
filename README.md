# PhraseBook (Django-based)

## Requirements
* python3+ (known to work with 3.8, 3.9)
* (other dependencies are listed in `requirements.txt`)

## Initial Development Setup
```sh
# clone the repo and enter the working directory
git clone <phrasebook.git>
cd phrasebook

# and run the setup
./setup/dev_initial.sh
# see file contents for details

# run development server
./manage.py runserver
# and go to http://127.0.0.1:8000/admin
# and http://127.0.0.1:8000/api/phrasebook
```

## Incremental Development Setup (after pulling changes)
```sh
# enter the working directory and pull changes
cd phrasebook
git pull
cd phrasebook

# run the setup
./setup/dev_incremental.sh
# see file contents for details

# run development server
./manage.py runserver
# and go to http://127.0.0.1:8000/admin
# and http://127.0.0.1:8000/api/phrasebook
```