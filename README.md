# django-ajax-config
head start copy and paste ajax implementation

start 
pip install django==4.1.4
django-admin startproject config .
virtualenv env
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned -Force
path to /project name/venv/Scripts/Activate.ps1
pip install mssql-django
pip install django-mssql-backend
pip install pyodbc
pip install django-pyodbc-azure-2019

after creating models
python manage.py makemigrations
python manage.py migrate
create superadmin
python manage.py createsuperuser
