# report-management-system
Report management system project.

This project contains:
1 - Report CRUD.
2 - Group CRUD.
3 - User CRUD.
4 - Role management CRUD (Groups)
5 - Admin panel that contains full permissions to view, create, edit, and delete any of database records on: http://127.0.0.1:8000/admin

System requirement:
1 - docker
2 - git

Steps to run the project:
1 - Clone the project.
2 - Run 'cd /path/to/the/project>'
3 - Run 'docker build .'
4 - Run 'docker-compose build'
5 - Go to app/settins.py then configure gmail smtp to your gmail account (you must enable two factor authentication then create app password and use it as password for the account)
6 - Run 'docker-compose run --rm app sh -c "python manage.py createsuperuser"' to create first admin account.
6 - After creating super user run 'docker-compose up'
7 - Open http://127.0.0.1:8000/admin on your browser to access admin panel or http://127.0.0.1:8000/ to access the app.
8 - Go to the admin panel and login then go to Groups under Authentication and Authorization then add Admin group with full permissions and add User group with:
    auth|user|Can change user
    auth|user|Can view user
    core|attachment|can add attachment
    core|attachment|can change attachment
    core|attachment|can view attachment
    core|attachment|can delete attachment
    core|group|can view group
    core|profile|can change attachment
    core|profile|can view attachment
    core|report|can add report
    core|report|can change report
    core|report|can view report
    core|report|can delete report
    core|tag|can add tag
    core|tag|can view tag


Notes:
1 - To make user able to access the admin panel -> as admin go to admin panel then login then go to Users then go to user that you want to make him access the admin panel then check is_staff and is_superuser and add Admin group to the user and remove user group from the user.
2 - To make user unable to access the admin panel -> as admin go to admin panel then login then go to Users then go to user that you want to make him unable to access the admin panel then remove checks in is_staff and is_superuser and add User group to the user and remove Admin group from the user.
3 - After login to the system you can view, add, edit, and delete any report within your groups permissions.
4 - To add multiple reports once: login as admin then go to: http://127.0.0.1:8000/reports/new/
5 - I assumed when you add multiple reports, you add all of them to excel file and upload it.
6 - To add one report: login to http://127.0.0.1:8000/ and click create new report and fill the form and submit it.