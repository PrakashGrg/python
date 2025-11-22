### Django ORM Examples


```
# Create
i = Item(name="Book", price=199.99)
i.save()

# Read
items = Item.objects.all()

# Update
i.price = 150
i.save()

# Delete
i.delete()
```


### Deployment Essentials

- Use Gunicorn / uWSGI (Linux)
- Use Nginx reverse proxy
- Set environment variables
- Use .env files
- Collect static files


```
python manage.py collectstatic
```