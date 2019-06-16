# Customers
A Django Application that lets the user Create a Customer and do CRUD operations on it.

# Framework Used
- Django 2.2.2 
- postgres 11 
- django-rest-framework 
- djangorestframework-jwt

# STARTING APP
### Start the application
```
docker-compose up
```
### Create a Super user
```
docker-compose run web python manage.py createsuperuser
```
# API REFRENCES(With Examples)
- token : This endpoint is for getting the Bearer Token which is to be used for all API calls eg: 
```
curl -H "Content-Type: application/json" -d '{"username":your_username,"password":your_password}' -XPOST  http://0.0.0.0:8000/token/
```
- LIST(GET) : This Api returns all the Customers which are present in our local database eg : curl -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN_RECIEVED IN THE PREVIOUS STEP" -XGET http://0.0.0.0:8000/api/customers/
- CREATE(POST) : This Api returns all the Customers which are present in our local database eg : ```
curl -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN_RECIEVED IN THE PREVIOUS STEP" -d '{"name": "John Doe", "dob":"1970-01-01"}' -XPOST http://0.0.0.0:8000/api/customers/
```



