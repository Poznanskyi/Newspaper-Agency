Newspaper-Agency
This site is in the early stages of production, it will post news that does not exist, made up for fun.

You can use following superuser (or create another one by yourself):

Credentials for testing:

Username: qwerty
Password: qpwoeiruty1234

Installation & Run
Set up the environment

On Windows:
python -m venv venv 
venv\Scripts\activate

On UNIX or macOS:
python3 -m venv venv 
source venv/bin/activate

Install requirements:
pip install -r requirements.txt

Create a superuser (optional)
If you want to perform all available features, create a superuser account:

python manage.py createsuperuser

Set enviroment variable

Run the project
python manage.py runserver
Go to site http://127.0.0.1:8000/
