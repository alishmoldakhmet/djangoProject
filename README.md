# STORE
## Moldakhmet Alisher
## DOCUMENTATION
http://localhost:8000/docs
## Installation

Clone repository

cd project-name


FIRST PART:
setup virtualenv and install requirements

virtualenv venv
cd Scripts/activate
pip install -r requirements.txt

SECOND PART:
run makemigration and migrate

python manage.py makemigrations
python manage.py migrate


THIDRD PART:
python manage.py runserver
