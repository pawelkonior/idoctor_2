---
<center>This project is only for training purpose. This is not production code.</center>

---

# iDoctor

## Dictionary

- CDN - content delivery network
- TDD - test driven development (red-green-refactor)

# Create new feature:

1. create new app ```dce backend ./manage.py startapp <name>```
    - if you have wrong configuration of your linux system -> change owner -> ```sudo chown -hR <group>:<user> <path>```
2. model if needed
8. add to settings -> installed apps
3. form if needed
4. admin panel if needed
5. view
6. templates if needed
7. urls local
8. urls global
9. unit test + functional tests

# ORM

Database | OOP
:---:|:---:
Table | Class
Column | Class/Object field
Row | Object

# Commands

```bash
dce db psql --host=db --username=postgres --dbname=postgres
```

```SQL

\d appname_classname

```

----------------------------------------------------------------------------
"THE BEER-WARE LICENSE" (Revision 42):\
<pawel.konior@gmail.com> wrote this file. As long as you retain this notice you\
can do whatever you want with this stuff. If we meet some day, and you think\
this stuff is worth it, you can buy me a beer in return Pawel Konior\
----------------------------------------------------------------------------
 

