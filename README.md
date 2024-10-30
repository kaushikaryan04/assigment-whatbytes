## assigment whatbytes
First make a virtual env  
```
virtualenv env
```
Activate this env 
```
source env/bin/activate
```
Download required packages 
```
pip install -r requirements.txt
```
Now migrate  
```
python manage.py makemigrations
python manage.py migrate
```
Run server
```
python manage.py runserver
```
## upon running the server go to this url 
url -> http://localhost:8000/accounts/signup/  
Make an account and then you can test out  

