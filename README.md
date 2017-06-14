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
