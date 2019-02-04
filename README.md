**Project structure**
1. static folder - all .css files and images
2. templates folder - all HTML files
3. database_setup.py - a python file for creating a database and tables
4. lotsofmenus.py - a python file for creating initial data
5. application.py - a python file for running the application
6. client_secrets.json - a json file used for gmail login and authentication
7. fb_client_secrets.json - a json file used for facebook account login and authentication (to be ignored)
8. projectoutput.doc - a word document with snapshots of the application
9. jsonlinks.txt - a text document for the JSON links
10. pg_config - a shell script file to be ignored

**Database details**
1. Database name - catalogappdb
2. Table names
    a. user - to store new user details
    b. category - to store sports category details
    c. item - to store sports items belonging to different categories

**Changes to be made for the application to run**
1. Open lotsofmenus.py
2. At line number - 30, change the name and email
    This is just to make sure we have some items in the database to display and perform CRUD operations

**Steps to be followed to run the application**
1. open git bash
2. navigate to the folder with the name .Vagrant
3. run the following commands
    a. vagrant init
    b. vagrant up
    c. vagrant ssh
    d. cd /vagrant
4. navigate to the folder catalog
    The command 'ls' should display the contents mentioned in the project structure
5. run the following commands
    a. python database_setup.py
    b. python lotsofmenus.py
    c. python application.py
6. An application would be hosted at http://localhost:5000/


