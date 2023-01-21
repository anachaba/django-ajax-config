# django-ajax-config
head start copy and paste ajax implementation


### start <br/>
`python -m venv venv`<br/>


### Activate env
`path to /project name/venv/Scripts/Activate.ps1`<br/>

### if env can't activate 

### set up powershell policies to allow venv <br/>
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned -Force`<br/>

### install django <br/>
`pip install django==4.1.4`<br/>
`django-admin startproject config .`<br/>

### Install Required libraries
`pip install mssql-django`<br/>
`pip install django-mssql-backend`<br/>
`pip install pyodbc`<br/>
`pip install django-pyodbc-azure-2019`<br/>




### post models creation <br/>
`python manage.py makemigrations` <br/>
`python manage.py migrate` <br/>
### create superadmin <br/>
`python manage.py createsuperuser` <br/>
