Recipe Management API
This project is a Django REST Framework-based API for managing recipes with CRUD operations, user authentication, and filtering features.

Functional Requirements
CRUD for recipes and users
Recipe search by title, category, and ingredients
Filter by cooking time, servings, and preparation time
Technical Requirements
Django ORM for database interaction
Built-in authentication
RESTful API design with DRF
Deployment on Heroku or PythonAnywhere
Pagination and sorting support

Setup
Clone the repository
Install dependencies: pip install -r requirements.txt
Run migrations: python manage.py migrate
Create superuser: python manage.py createsuperuser
Run server: python manage.py runserver

Endpoints
POST /api/users/
POST /api/token/
POST /api/recipes/
GET /api/recipes/?search=Dessert
GET /api/recipes/?ordering=preparation_time