# My django project's intro codes with subdomain conf
Django projelerime başlarken işimi kolaylaştırmak adına oluşturduğum bir repositorydir.

Repository'de bulunanlar:

Django Rest Framework (api servisi için)
django-hosts (özel subdomain yönlendirmeleri için)



İsteğe bağlı virtualenv paket kurulumu: 

```powershell
pip install virtualenv
```

Daha sonrasında gereken paketleri kuruyoruz. Gereken paketleri görmek için requirements.txt dosyasını inceleyebilirsiniz

```powershell
pip install -r requirements.txt
```


Account custom user modelinin ve veritabanının oluşturulması için alttaki komutları sırasıyla çalıştırın.
```powershell
cd devstone
python manage.py makemigrations
python manage.py migrate
```


## Klasörler

### api 

Bu klasör api subdomaininin yönlendirmeleri ve kodlarını yazmak içindir.

**urls.py** dosyasının içerisine: 
```python
path('helloworld/', views.index ,name='index')
```
şeklinde path ekleyebilirsiniz. Host Domainimizin localhost:8000 olduğunu düşünürsek eğer `api.localhost:8000/helloworld` şeklinde yazdığınız url çağrılabilir. 

### account 

Bu klasör içerisinde kendi yarattığım custom user model bulunmaktadır. İsteğe göre düzenlenebilir.


## API endpoints
=============

Basic
-----

- /rest-auth/login/ (POST)

    - username
    - email
    - password

    Returns Token key

- /rest-auth/logout/ (POST)

    .. note:: ``ACCOUNT_LOGOUT_ON_GET = True`` to allow logout using GET - this is the exact same configuration from allauth. NOT recommended, see: http://django-allauth.readthedocs.io/en/latest/views.html#logout

- /rest-auth/password/reset/ (POST)

    - email

- /rest-auth/password/reset/confirm/ (POST)

    - uid
    - token
    - new_password1
    - new_password2

    .. note:: uid and token are sent in email after calling /rest-auth/password/reset/

- /rest-auth/password/change/ (POST)

    - new_password1
    - new_password2
    - old_password

    .. note:: ``OLD_PASSWORD_FIELD_ENABLED = True`` to use old_password.
    .. note:: ``LOGOUT_ON_PASSWORD_CHANGE = False`` to keep the user logged in after password change

- /rest-auth/user/ (GET, PUT, PATCH)

    - username
    - first_name
    - last_name

    Returns pk, username, email, first_name, last_name


Registration
------------

- /rest-auth/registration/ (POST)

    - username
    - password1
    - password2
    - email

- /rest-auth/registration/verify-email/ (POST)

    - key


Social Media Authentication
---------------------------

Basing on example from installation section :doc:`Installation </installation>`

- /rest-auth/facebook/ (POST)

    - access_token
    - code

    .. note:: ``access_token`` OR ``code`` can be used as standalone arguments, see https://github.com/Tivix/django-rest-auth/blob/master/rest_auth/registration/views.py

- /rest-auth/twitter/ (POST)

    - access_token
    - token_secret