django-project-template
=======================

My personal django project template, for use with paster.

This is probably not useful as-is to other people, but hopefully it'll give you a starting point for creating your own, similar template.

This includes buildout project files, a default fabfile for deployments and a webfaction configuration file for webfaction project setup.

Here are the basic steps I take to get started with a new Django project:

1. `mkvirtualenv my_project`
2. `mkdir my_project`
3. `cd my_project`
4. `pip install git+https://`
5. `paster create -t django_project my_project`
6. `cd my_project`
7. `git init`
8. `python bootstrap.py`
9. `./bin/buildout -c devel.cfg`
10. Setup settings.py
11. `./bin/django syncdb --migrate`
12. `./bin/django runserver`
