# Apollo Health - Back End

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

## Routes
All routes return a json object.

### Pharmacy Routes
**/get_pharmacy/**: Returns all pharmacies.

**/get_pharmacy/?pharmacy_id=x**: Returns pharmacy with the matching pharmacy_id.

**/create_pharmacy/?name=Name&address=Address**: Creats a pharmacy with the given name and address.

**/edit_pharmacy/?pharmacy_id=X&name=Name&address=Address**: Edits the pharmacy with the given pharmacy_id.

**/delete_pharmacy/?pharmacy_id=X**: Deletes the pharmacy with the given pharmacy_id.

### Doctor Routes
**/get_doctor/**: Returns all doctors.

**/get_doctor/?doctor_id=X**: Returns doctor with given doctor_id.

**/create_doctor/?address=Address&name=Name&specialty=Special&days_available=Days&times_available=Times**: Creates a doctor.

**/edit_doctor/?doctor_id=X&address=Address&name=Name&specialty=Special&days_available=Days&times_available=Times**: Edits the doctor with the given doctor_id.

**/delete_doctor/?doctor_id=X**: Deletes the doctor with the given doctor_id.

### User Routes
**/get_user/**: Gets all users.

**/get_user/?user_id=X**: Gets the user with the given user_id.

**/create_user/?address=Address&name=Name&pharmacy_id=X&doctor_id=Y**: Creates a user.

**/edit_user/?user_id=X&address=Address&name=Name&pharmacy_id=X&doctor_id=Y**: Edits a user with the given user_id.

**/delete_user/?user_id=X**: Deletes the user with the given user_id.

### Prescription Routes
**/get_script/**: Gets all prescriptions.

**/get_script/?user_id=X**: Get all prescriptions for that user_id.

**/get_script/?prescription_id=X**: Get the prescription with that prescription_id.

**/create_script/?user_id=X&name=Name&refills=Y&dosage=Dosage&warnings=Warnings**: Creates a prescription.

**/edit_script/?prescription_id=Z&user_id=X&name=Name&refills=Y&dosage=Dosage&warnings=Warnings**: Edits a prescription.

**/delete_script/?prescription_id=X**: Deletes a script.

### Event Routes
**/get_event/**: Gets all events.

**/get_event/?event_id=X**: Gets event with a given event_id.

**/get_event/?doctor_id=X**: Gets all events for a given doctor.

**/get_event/?user_id=X**: Gets all events for a given user.

**/get_event/?doctor_id=X&user_id=Y**: Gets all events for a given doctor and all events for a given user.

**/create_event/?user_id=X&name=Name&doctor_id=Y&date=00-00-0000&start_time=00:00:00&end_time=00:00:00**: Creates an event.

**/edit_event/?event_id=Z&user_id=X&name=Name&doctor_id=Y&date=00-00-0000&start_time=00:00:00&end_time=00:00:00**: Edits an event.

**/delete_event/?event_id=X**: Deletes an event.

### Pharmacy Event Routes

**/get_pharm_event/**: Gets all pharmacy events.

**/get_pharm_event/?user_id=X**: Gets all pharmacy events for a given user.

**/get_pharm_event/?pharm_event_id=X**: Gets a pharmacy event.

**/create_pharm_event/?user_id=X&name=Name&pharmacy_id=Y&date=00/00/0000&pickup_time=00:00:00**: Creates a pharmacy event.

**/create_pharm_event/?pharm_event_id=Z&user_id=X&name=Name&pharmacy_id=Y&date=00/00/0000&pickup_time=00:00:00**: Edits a pharmacy event.

**/delete_pharm_event/?pharm_event_id=X**: Deletes a pharmacy event.
