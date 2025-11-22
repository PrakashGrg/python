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