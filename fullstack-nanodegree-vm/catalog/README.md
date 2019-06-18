# UDACITY CATALOG PROJECT

# Requirements 

 - Python 2.7
 - Flask
 - Flask-SeaSurf
 - SQLAlchemy
 - httplib2
 - apiclient
 - google-api-python-client
 - httplib2

# Setup 

 - Download and extract this project.
 - Setup VM by doing the following:
 	Open terminal
 	Path to the location of the vagrantfile from the project
 	Run:
 		vagrant up
 		vagrant ssh
 	Navigate to the catalog folder

 - Setup Google Credentials
 	Go to https://console.cloud.google.com
 	Setup a new project by using the following information:
 		https://localhost:5000 for the Authorized JavaScript origins field 
 		https://localhost:5000/goauth2redirect for the authorized redirect URIs
 		Download the available json file and rename as g_client_secrets.json. Then replace the file in the project directory.

 - Setup Facebook Credentials
 	Go to https://developers.facebook.com/apps 
 	Setup a new app and add Facebook Login
 		https://localhost:5000 in the Valid OAuth redirect URI	
 	Replace the Client id and secret in the fb_client_secret.json file

 - Install requirements on VM
 	The requirements.txt file contains a list of all the necessary packages
 	In order to install, run the following command:
 		$ pip install -r requirements.txt

# Run the project

 - Navigate back to the catalog folder in the VM

 - Initialize the database : 
		$ python database_setup.py

 - Populate the database: 
 		$ python lotsofcategories.py

 - Run server and application: 
 		$ python catalog.py

 - Open browser on host and go to http://localhost:5000

# Access to JSON endpoing

 - There are two methods to access the JSON endpoint:
 	1. Use the JSON button on the app accessed via the browser

 	2. Go to http://localhost:5000 on the host browser


# Notes

 - For some reason, my computer would not allow me to access port 8000, but i was able to use port 5000 instead
 - Google login is a bit unreliable on my end. Facebook login works 100%.

# Help

 - After accessing the application, an unauthorized user is able to view, but not edit, the categories and items
 - After logging in, the user is able to create items in specific categories
 - An authorized user may only alter or delete items that the same user has created.