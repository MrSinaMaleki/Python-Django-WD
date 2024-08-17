# Template inheritance:

{{ block ... }}
{{ endblock }}


{{ extends ... }}
{{ include ... }}

You can create an app called core in your project to deal with the basic utils that are gonna be used in multible apps 
for example you can build a dynamic menu.
1. Create a new app called core
2. create a file called template.py

```python

menu = [
    dict(title="Home", link="/"),
    dict(title="About", link= "/about/")
]

# check the fun from mryazdans Github!
```
# Don't  forget to use the "/" in you urls.


Also you need to add this to your template in order to have it in all of you pages.









