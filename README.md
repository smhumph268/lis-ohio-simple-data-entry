# lis-ohio-simple-data-entry

Notes:
- For the .gitignore I'm following some of what's in [here](https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/#:~:text=If%20you%20are%20using%20Git,has%20access%20to%20your%20code).
- I used the PyCharm IDE community edition for development and am using a sqlite database
- I developed this on a Windows machine, I've not tested it on any other operating systems


## Setup Instructions
- Clone the repo to a location of your choice

- Make sure Python is installed. Download [here](https://www.python.org/downloads/). I followed all defaults in the setup wizard and checked "Add Python X.Y to PATH".

- Make sure Django is installed. These [install instructions](https://docs.djangoproject.com/en/4.2/topics/install/#installing-official-release) and [how to for windows](https://docs.djangoproject.com/en/4.2/howto/windows/) are useful.
	- py -m pip install Django

- Get the database set up
	- python manage.py makemigrations
	- python manage.py migrate

- If you'd like to run any of the unit tests, you can run the following command:
	- py manage.py test people

- Try to get a test server running
	- Open a command prompt and navigate to the folder path that contains the 'manage.py' file for the project
	- run this command:
		- py manage.py runserver 0.0.0.0:8000
	- Navigate to 127.0.0.1:8000 in a browser (preferably Chrome, that's the browser I used while developing)
	- You should be all set to start using the data entry application
