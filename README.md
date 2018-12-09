# tor_db
###### because sometimes we need an exercise in what is probably a bad idea

This package is effectively the Django ORM without Django. It seems like we need an ORM for ToR, as `caroline` can't support foreign keys, and Django provides a super easy-to-use and fast-to-develop-in ORM.

While most projects use the Django ORM in... well, Django projects, just using the ORM is not unheard of. In fact, there are lots of suggestions from the Django crew on exactly how to pull this off in the appropriate ways, and their suggestions have been implemented here.

Usage:
```python

from tor_db.models import Volunteer

Volunteer.objects.create(
    username='samwisegamgee'
)

print(Volunteer.objects.filter(username='samwisegamgee'))
# 
```

