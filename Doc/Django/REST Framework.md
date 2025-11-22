### Django REST Framework (Important)


```Install
pip install djangorestframework
```

```Enable
# myproject/settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```


### API View


```
# myapp/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_home(request):
    return Response({"message": "Hello API"})
```


### API URL:

```
# myproject/urls.py
path('api/', views.api_home)
```