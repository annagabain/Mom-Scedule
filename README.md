# Mom Schedule
## A Time Planning Tool for Busy Mothers

## Main Technologies
HTML, CSS, JavaScript, Python+Django
Postgres Relational database 

Live View https://mom-schedule.herokuapp.com/

## Portfolio Project 4

Full-Stack Toolkit
Project purpose:

In this project, you'll build a Full-Stack site based on business logic used to control a centrally-owned dataset. You will set up an authentication mechanism and provide role-based access to the site's data or other activities based on the dataset.

- address the user persona from my previous projects. https://github.com/annagabain/Mom-Lifehacks#User-Experience-and-User-Interface-Design-UX-and-UI
- includes a calendar, event editing, creating task cards.


## User Stories

- As a site user I can register so that I can have a unique and private schedule

- As a site user I can login so that I can view my own schedule

- As a site user I can see the schedule so that I can overview my tasks

- As a site user I can View an individual task so that I can read the details of it

- As a site user I can Edit an individual task so that I can adapt it to my needs

- As **a site Admin** I can **login** so that I can **view and manage the users and tasks**

All user stories as part of a project: https://github.com/users/annagabain/projects/7/views/1


## Desktop Wireframes

*Today View*

<img width="50%" alt="wireframe" src="wireframes/mom-schedule-wireframe-desktop-today-view.png"> 

*Login / Register View*

<img width="50%" alt="wireframe" src="wireframes/mom-schedule-wireframe-desktop-register-login-view.png"> 

*Edit Task View*

<img width="50%" alt="wireframe" src="wireframes/mom-schedule-wireframe-desktop-task-edit.png"> 

*This Week View*

<img width="50%" alt="wireframe" src="wireframes/mom-schedule-wireframe-desktop-week-view.png">

*PgSQL Relational Database Diagram*

<img width="50%" alt="wireframe" src="wireframes/drawSQL-mom-schedule-database-diagram-export-2023-02-02.png">

## Debugging

Static files weren't included by Heroku after deployment. Using WhiteNoise package fixed the issue.

<img width="30%" alt="debugging" src="documentation/static_css_heroku.jpg"> <img width="30%" alt="debugging" src="documentation/static_css_local.jpg">


## Tools

Wireframes: https://www.figma.com/
Bootstrap grid: https://getbootstrap.com/docs/4.1/layout/grid/

## Sources

User Specific Pages: https://www.techwithtim.net/tutorials/django/user-specific-pages-data/

Setup Bootstrap messages for Django: https://ordinarycoders.com/blog/article/django-messages-framework

Django project base template: https://stackoverflow.com/questions/14720464/django-project-base-template#:~:text=Yes%2C%20you%20can%20use%20%7B%25,where%20to%20place%20the%20base.

A guide to user registration: https://ordinarycoders.com/blog/article/django-user-register-login-logout

Using WhiteNoise with Django: https://whitenoise.evans.io/en/stable/django.html

Django and Static Assets: https://devcenter.heroku.com/articles/django-assets?fbclid=IwAR16j_4bi-WEMxrA-VwWmFUfPOFP9ef2Kqzb6lM1pVCiKti_dhwoku1ceEg

Django models: https://docs.djangoproject.com/en/4.1/topics/db/models/

How to create a calendar with Django:  https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html

Develop a Simple Python Django ToDo App in 1 minute: https://dev.to/nditah/develop-a-simple-python-django-todo-app-in-1-minute-4908

## Acknowledgments

Richard Wells - the course mentor for friendly guidance, help with refactoring some code and numerous project feedback sessions
