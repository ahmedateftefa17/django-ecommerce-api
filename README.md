# Ecommerce API using Django, Django REST Framework and MySQL

## Steps to get the project up and running

1. Make sure you have Python v3.10 installed on your machine to run this project without issues
2. Make virtual env to project using the following command
```
python3.10 -m venv env
```
3. Install project requirements using the following command
```
python -m pip install requirements.txt
```
4. Make your MySQL database and update database settings in settings.py file
```
{project_path}/app/settings.py
```
5. Migrate your database using the following command
```
python manage.py migrate
```
6. Create super user using the following command then enter your super user password (Make sure you remember this password)
```
python manage.py createsuperuser --email admin@ecommerce.django.com --username admin
```
7. Run server to start using admin & api using the following command
```
python manage.py runserver
```
8. Go to this url http://127.0.0.1:8000/admin and login then add products


## PostMan Collection for APIs
https://documenter.getpostman.com/view/3741025/2s93JtQ3zP

## API Endpoints
```
{api_url} = http://127.0.0.1:8000/api
```

### Register:
```
[POST] {api_url}/auth/register/
```
Fields:
* username: (REQUIRED)
* password: (REQUIRED)
* password2: (REQUIRED)
* email: (REQUIRED)
* first_name: (REQUIRED)
* last_nam: (REQUIRED)

---

### Login:
```
[POST] {api_url}/auth/token/
```
#### Fields:
* username (REQUIRED)
* password (REQUIRED)

---

### List Products:
```
[GET] {api_url}/products/
```
#### Headers:
* Authorization: Token {token}
#### Params:
* sort_by_price: (optional) "lth" for sorting Low to High Price & "htl" for sorting High to Low Price
* search_term: (optional) Search Term (Searches in name)

---

### Add Product to Cart:
```
[POST] {api_url}/cart_items/
```
#### Headers:
* Authorization: Token {token}
#### Fields:
* product: (REQUIRED) Product ID

---

### Get Cart Items:
```
[GET] {api_url}/auth/cart_items/
```
#### Headers:
* Authorization: Token {token}

---

### Convert Cart to Order:
```
[POST] {api_url}/orders/
```
#### Headers:
* Authorization: Token {token}

---

### Get Order Details:
```
[GET] {api_url}/orders/<pk>
```
#### Headers:
* Authorization: Token {token}

---

### List Orders:
```
[GET] {api_url}/orders/
```
#### Headers:
* Authorization: Token {token}
