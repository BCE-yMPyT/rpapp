**This is a simple application for developing / administering a real estate site, 
which includes real estate, contracts, customers, and functionality for working with them.
You can process necessary objects through the administrator panel (preferably due to saving files in different directories)
or through your own form, which will be easy to configure (less preferable method due to the need to store all
files in the media folder).**
***
For runing this app(locally):
- Install all packages from requirements.txt;
- Add to django/templates/defaultfilters.py next:;
```
@register.filter(is_safe=False)
def sub(value, arg):
    """Subtracts the arg from the value"""
    return int(value) - int(arg)
```
- Go to rpapp directory with command line;
- Create superuser, desirable:;
```
python(3) manage.py createsuperuser
#python3 or python, depending of version you OS
```
- Run the local server:;
```
python(3) manage.py runserver
```
- Go to: http://127.0.0.1:8000/;
- Log in (preferably:)) on the ADMIN PANEL tab;
- Enjoy (seems:)).
***
* At the ADMIN PANEL, you can find all of you need for creating all of objects;
* At the ALL POSTS, you can find all of your created posts;
* At the ALL CONTRACTS, you can find all of your created contracts;
* At the ALL CLIENTS, you can find all of your created clients;
* At the Free objects, you can find all of your real property which free now;
* At the Leased objects, you can find all of your real property which leased now;
* +OBJECT icon calling form for adding the real property object;
* +CONTRACT icon calling form for adding the contract object;
* +CLIENT icon calling form for adding the client object;
* Last, on the left from +CLIENT, icon calling form for posting post with real property object, which will be visible for visitors;
