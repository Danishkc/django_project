Django Web Application - User Authentication and Profile Management

Project Overview
This Django web application provides user authentication, registration, and profile management functionalities. Users can log in, register, and update their profile information, including their bio and profile picture.

Project Structure
.Django Project Name: mywebapp
.Django App Name: profiles

Features

1.Login Page:
Users can log in using their username/email and password.
Utilizes Django's built-in authentication system.
Successful login redirects users to their profile page.

2.Registration Page:
New users can sign up with a username, email, and password.
Utilizes Django's User model for creating new user accounts.

3.Profile Update Page:
Users can update their profile information, including bio and profile picture.
Profile picture can be uploaded and stored on the server.

4.API Endpoints:
Login API: /api/login/
cURL: curl -X POST -d "username=myuser&password=mypassword" http://localhost:8000/api/login/
Register API: /api/register/
cURL: curl -X POST -d "username=newuser&email=newuser@example.com&password=mypassword" http://localhost:8000/api/register/
Profile Update API: /api/profile/update/
cURL: curl -X PUT -H "Authorization: Bearer <your_token>" -d "bio=New bio" -F "profile_picture=@path/to/image.jpg" http://localhost:8000/api/profile/update/

Setup Instructions

1.Clone the repository:
git clone https://github.com/your-username/django_project.git
2.Navigate to the project directory:
cd django_project
3.Create and activate a virtual environment (optional but recommended):
python -m venv venv
venv\Scripts\activate
4.Install dependencies
5.Run migrations:
python manage.py makemigrations
python manage.py migrate
6.Create a superuser for administrative access (optional):
python manage.py createsuperuser
7.Run the development server:
python manage.py runserver

