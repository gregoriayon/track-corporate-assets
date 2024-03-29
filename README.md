# Corporate Asset Tracking Django App

This Django app is designed to track corporate assets such as phones, tablets, laptops, and other gears handed out to employees.

## Admin Login

To access the Django admin interface:

- **URL:** Admin Login URL (e.g., http://127.0.0.1:8000/admin/)
- **Username:** admin
- **Password:** admin

## API Documentation

The API endpoints provided by this app are documented using Swagger/OpenAPI. You can access the API documentation using the following URLs:

- **Swagger UI:** [API Docs](http://127.0.0.1:8000/)
- **API Links:** [API Root](http://127.0.0.1:8000/api/)
- **ReDoc:** [API Docs (ReDoc)](http://127.0.0.1:8000/redoc/)

## API Endpoints

The following are the main API endpoints available in this project:

1. **Companies API:**
   - Endpoint: `/api/companies/`
   - Methods: GET, POST, PUT, DELETE

2. **Employees API:**
   - Endpoint: `/api/employees/`
   - Methods: GET, POST, PUT, DELETE

3. **Devices API:**
   - Endpoint: `/api/devices/`
   - Methods: GET, POST, PUT, DELETE

4. **Device Logs API:**
   - Endpoint: `/api/devicelogs/`
   - Methods: GET, POST, PUT, DELETE
  
5. **Users API:**
   - Endpoint: `/api/users/`
   - Methods: GET, POST, PUT, DELETE

## Installation and Setup
- Create virtual environment
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

