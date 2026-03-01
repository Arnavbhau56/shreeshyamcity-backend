@echo off
echo ========================================
echo Shree Shyam City Backend Setup
echo ========================================
echo.

echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo Running migrations...
python manage.py makemigrations
python manage.py migrate

echo.
echo Setup complete!
echo.
echo To create a superuser, run: python manage.py createsuperuser
echo To start the server, run: python manage.py runserver
echo.
pause
