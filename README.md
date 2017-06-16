# Apollo Health

## Running the vagrant (Everytime)
1. Start Up the VM:

+ Change directories to where your vagrant is

+ $ vagrant up

+ $ vagrant ssh

2. Set up the vagrant once ssh'ed in:

+ $ cd /vagrant

+ $ source venv/bin/activate

3. Navigate to where your shared files are. Mine are in a folder named "ApolloHealth"

4. To leave the vagrant: $ exit

5. To halt the vagrant: $ vagrant halt

## Setting up git (Only need to do once)
**It is very important that you are in your working folder (for instance, ApolloHealth/)**
1. Initialize local repo: $ git init

2. Add the origin: $ git remote add origin https://github.com/raynicho/ApolloHealth/

3. Pull the files: $ git pull origin master
**Be sure to use your github credentials for whatever account has access to this repo.**

## Starting up the app
To start the server, do the following:

1. Navigate to the **mysite** directory

2. Inside the directory: $ python manage.py runserver 0.0.0.0:3000

3. Access the site in your web browser at: http://localhost:3000/

## Our Models and Populating Them

### Models Overview

1. **Pharmacy**: auto increment id, address, name

2. **Doctor**: auto increment id, name, address, specialty, days available, times available

3. **User**: auto increment id, name, address, pharmacy foreign key, doctor foreign key

4. **Prescription**: refills number, dosage description, warnings, name, user foreign key

5. **Event**: doctor foreign key, user foreign key, date, start time, end time


### Populating the Tables

The table should already be fully populated. If you wish to populate it more, uncomment the populate_db method in views.py and change it as you wish. Then uncomment the route in the urls.py, start the server, and navigate to "localhost:3000/populate". This will apply your populations. **Make sure not to populate the table with duplicates.**

### Viewing the Tables

If you wish to easily view your sqlite3 table, this (http://inloop.github.io/sqlite-viewer/) allows you to drop the db.sqlite3 file and view the tables.

### Resetting the Tables

If you wish to reset the tables because you made a models change or you wish to cleanse the data, delete the db.sqlite3 file and run **python manage.py syncdb** to sync the database. I leave username and email blank, **root** as password.
