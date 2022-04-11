# DesafioBackend-ITFLEX

# What the company asked for  :green_circle:
The goal of this challenge is to create an aplication that lists, adds, edits and deletes data from DataBase using the requirements below.

## Requirements:shopping_cart:
Python 3
REST API
Save data in a SQLITE DB
README
Deploy into Heroku

## Extra :rocket:
Clean Architecture
SQLAlchemy for DB
SQL-Migrate to build DB

# The project itself :green_circle:
## Technologys used :electron:
Python 3.10 (Backend)<br />
Django 4.0 (Project)<br />
SQLite3 (DataBase)<br />
Heroku (Deploy)<br />

## How to use :arrow_forward:
1- Access [Main Page](https://arcane-refuge-76371.herokuapp.com/)
2- Access [List](https://arcane-refuge-76371.herokuapp.com/list) to see all data
3- Access [Create](https://arcane-refuge-76371.herokuapp.com/create) to send a JSON format text to create data in data base.
{"username":"username", "name":"Full name", "description":"Random text", "expiration":10}
4- Access [Update](https://arcane-refuge-76371.herokuapp.com/update/id) to update information to any item, change the 'id' for any positve integer available item.
5- Access [Delete](https://arcane-refuge-76371.herokuapp.com/update/id) to delete information to any item, change the 'id' for any positive integer available item.

## How to makey your own API(step-by-step) :arrow_forward:
1- Clone this repo in your machine.<br />
2- Open it.<br />
3- Cd into the project directory, "ThisIsTheProject", or until you find a folder with the file "manage.py" in the same folder. <br />
4- Run this code to start the application.<br />
```python manage.py runserver```

5- This will make the program run in Localhost.<br />
6- If you wish, deploy it with heroku with any YT tutorial.<br /><br />


## Requirements acomplished :brain:
Django aplication. (:heavy_check_mark: done) <br /> 
Data must be saved in a SQLite DataBase. (:heavy_check_mark: done)<br />
List data collected. (:heavy_check_mark: done)<br />
Allow to Add/Edit/Delete itens in this list. (:heavy_check_mark: done)<br />
Upload your code in a GitHub repo(Public Acess). (:heavy_check_mark: done)<br />
Write step-by-step the execution on README. (:heavy_check_mark: done)<br />
Simple code(Readable). (:heavy_check_mark: done)<br />
Heroku deploy([Deployed Page](https://arcane-refuge-76371.herokuapp.com/))


# Issues
CSS not working properly, i made the link from settings, django, html and css. But for some reason when i make some changes, its not updating properly. (1)

1- After sometime i found out that my browser's cache was full, so i did Ctrl+F5 to hard refresh and solved the problem. Now Css is working properly

Check my LinkedIn: https://www.linkedin.com/in/alexandre-siedschlag-19309b215/
