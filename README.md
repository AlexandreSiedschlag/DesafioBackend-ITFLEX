# DesafioBackend-ITFLEX

# What the company asked for  :green_circle:
The goal of this challenge is to create an aplication that lists, adds, edits and deletes data from DataBase using the requirements below.

## Requirements:shopping_cart:
Python 3<br/>
REST API<br/>
Save data in a SQLITE DB<br/>
README<br/>
Deploy into Heroku<br/>

## Extra :rocket:
Clean Architecture<br/>
SQLAlchemy for DB<br/>
SQL-Migrate to build DB<br/>

# The project itself :green_circle:
## Technologys used :electron:
Python 3.10 (Backend)<br />
Django 4.0 (Project)<br />
SQLite3 (DataBase)<br />
Heroku (Deploy)<br />

## How to use :arrow_forward:
1- Access [Main Page](https://arcane-refuge-76371.herokuapp.com/)

2- Access [/list](https://arcane-refuge-76371.herokuapp.com/list) to see all data

3- Access [/create](https://arcane-refuge-76371.herokuapp.com/create) to send a JSON format text to create data in data base.

{"username":"username", "name":"Full name", "description":"Random text", "expiration":10}
Username = Unique, cant be duplicated

4- Access [/update](https://arcane-refuge-76371.herokuapp.com/update/id) to update information to any item, change the 'id' for any positve integer available item.

5- Access [/delete](https://arcane-refuge-76371.herokuapp.com/update/id) to delete information to any item, change the 'id' for any positive integer available item.

6- Access [/filterby/username](https://arcane-refuge-76371.herokuapp.com/filterby/username) to filter information by username.

6- Access [/filterby/name](https://arcane-refuge-76371.herokuapp.com/filterby/name) to filter information by name.

## Requirements acomplished :brain:
Django aplication. (:heavy_check_mark: done) <br /> 
Data must be saved in a SQLite DataBase. (:heavy_check_mark: done)<br />
List data collected. (:heavy_check_mark: done)<br />
Allow to List/Add/Edit/Delete items. (:heavy_check_mark: done)<br />
Upload your code in a GitHub repo(Public Acess). (:heavy_check_mark: done)<br />
Write the step-by-step on README. (:heavy_check_mark: done)<br />
Simple code(Readable). (:heavy_check_mark: done)<br />
Heroku deploy([Deployed Page](https://arcane-refuge-76371.herokuapp.com/)) (:heavy_check_mark: done)<br />
