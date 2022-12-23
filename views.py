import pyodbc
from django.http import JsonResponse
from django.shortcuts import render


def insert_form_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        # connect to the database
        conn = pyodbc.connect(
            'Driver={ODBC Driver 17 for SQL Server}; Server=localhost; Database=new_django; Trusted_Connection=yes;')
        cursor = conn.cursor()

        # insert the form data into the database
        cursor.execute(
            "INSERT INTO datatest_formdata (name, email) VALUES (?, ?)", (name, email))
        conn.commit()

        return JsonResponse({'status': 'success'})


def home(request):
    return render(request, 'index.html')
