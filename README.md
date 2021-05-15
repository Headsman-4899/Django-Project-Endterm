PlayStore - computer games store with low prices.


steps to install project:
1) download archive or make git clone.
   open git terminal and write: git clone https://github.com/Headsman-4899/Django-Project-Endterm.git
2) You need to setup your database and change database settings in setting.py:
   it looks like this:
   
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gamesdb',
        'USER': 'postgres',
        'PASSWORD': 'database123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

3) install requirements in project folder:
   python -m pip install -r requirements.txt.
4) you can create superuser: python manage.py createsuperuser 
   then run server: python manage.py runserver
   open localhost:8000/admin and create your users and games!
   

Link to postman:
https://www.getpostman.com/collections/bad18c8616e28cbf067f
