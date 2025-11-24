### Django Admin


```
# myapp/admin.py
from django.contrib import admin
from .models import Item

admin.site.register(Item)
```



### Create Superuser

```
python manage.py createsuperuser
```

### What happens next

1. Django will prompt you to enter:

- Username

- Email (optional, depending on your settings)

- Password (twice)

2. Once completed, the superuser can log in at:

```
http://127.0.0.1:8000/admin/
```

- You need to have django.contrib.admin in INSTALLED_APPS (default in a new project).

- You also need to run migrations before using it:

```
python manage.py migrate
```



1. Using changepassword

Run this command in your project directory:
```
python manage.py changepassword <username>
```

- Replace <username> with your superuser’s username.

- Django will prompt you to enter a new password twice.

# Example:
```
python manage.py changepassword admin
```

2. Using the shell (alternative)

- If you prefer, you can reset the password using the Django shell:
```
python manage.py shell
```

# Then in the shell:
```
from django.contrib.auth.models import User

# Replace 'admin' with your superuser username
user = User.objects.get(username='admin')
user.set_password('newpassword123')  # set a new password
user.save()
```

- Now you can log in with the new password.