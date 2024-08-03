# Create a virtual environment named 'env'
python -m venv env

# Activate the virtual environment
# On Windows:
source env/Scripts/activate


# Apply the database migrations to set up your database schema
python manage.py migrate

# Create a superuser 
python manage.py createsuperuser

# Start the Django development server
python manage.py runserver
