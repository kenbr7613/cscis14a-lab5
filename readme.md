## Lab 4

Welcome! This week we will be working with user logins and sessions.

1. If you need to install packages into your environment:
    + `pip install -r requirements.txt`
    + The only new library is [passlib](https://passlib.readthedocs.io/en/stable/)

2. Let's start by setting up our DB with Postgres (paying attention to the foreign key):
    + psql: `CREATE DATABASE lab5;`
    + psql: `\c lab5`
    + psql: `CREATE TABLE users(uid SERIAL NOT NULL PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL);`
    + psql: `CREATE TABLE posts(pid SERIAL NOT NULL PRIMARY KEY, author SERIAL NOT NULL, content TEXT NOT NULL, FOREIGN KEY (author) REFERENCES users(uid));`
    + psql: `INSERT INTO users (username, password) VALUES ('Michelle', 'test_pw1');`
    + psql: `INSERT INTO users (username, password) VALUES ('Jasmine', 'test_pw2');`
    + psql: `INSERT INTO posts (author, content) VALUES (1, 'test_post_1');`
    + psql: `INSERT INTO posts (author, content) VALUES (2, 'test_post_2');`
    
    OR
    
    + psql: `CREATE DATABASE lab5;`
    + psql: `\c lab5`
    + psql: `\i lab5.sql`
   
3. Everything else we have setup for you in the directory :^). However you will need to uncomment in app.py to discover how this code works out in the app.

4. Tasks
    + Implement [Message Flashing](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/).
    + Create your own stylesheet!
    + Replace 'Author number' with real name.
    + Implement [dates](https://docs.sqlalchemy.org/en/13/core/type_basics.html) in your models
    + Test the performance of your app (submit one page report as markdown file):
        + If you can deploy your app to Heroku, check performance and identify bottlenecks: https://developers.google.com/speed/pagespeed/insights/.Add a page with a description of your project. Identify keywords that your projects should be found on the Google search. Do the Search Engine Optimization (SEO). Check the results at:
            - https://www.seobility.net/en/seocheck/
            - https://neilpatel.com/seo-analyzer/
            - https://www.seotesteronline.com/
            - https://sitechecker.pro/
            - https://seositecheckup.com/
            - https://www.woorank.com/
        + If you CANNOT deploy your app to Heroku, check the performance and identify bottlenecks using Developer Tools (Chrome, Firefox, or Safari). Profile your app using the cProfile (check the following tutorial): https://julien.danjou.info/guide-to-python-profiling-cprofile-concrete-case-carbonara/).