### Django Templates

```View
# myapp/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```



### Template


```
<!-- myapp/templates/home.html -->
<h1>Hello from Django Template!</h1>
```

