# Network Hunt

Network Hunt is a website that lets you manage the job applications and networking you've been doing or will do.

# Techs used

This project was made using Html, Css, Javascript and Bootstrap for the frontend. I used Python and Django to make the backend, and Postgresql for the database.

## Installation

``Keep in mind the examples below are Window's commands. Mac and Linux have different commands when doing the installation.``

Create a virtual environment using [python](https://www.python.org/):

```bash
python -m venv example
```

Now activate the virtual environment.

```bash
example/Scripts/activate
```

You should be in ``\Network-Hunt\``, so to do that change directory to Network-Hunt. Now use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.txt file. While the virtual environment is activated.

```bash
cd Network-Hunt
pip install -r requirements.txt
```

## Django allauth Regular Account Login and Registration

You will be able to use the regular login and registration functionality right from the get-go as long as you install the packages required in the requirements.txt file. You can find more information on it [here](https://docs.allauth.org/en/latest/account/index.html). To navigate the html pages and forms make sure to read the documentation. I do not have it configured for this project.

## Django allauth Social Account Login and Registration

Social account login and registration functionality need to be configured separately by you. Navigate to the settings.py file in the networkhunproject folder: ``\Network-Hunt\networkhuntproject\networkhuntproject\settings.py``. You will see the code to configure it:

```python
SOCIALACCOUNT_PROVIDERS = {
    'google': {

        'APP': {
            'client_id': os.environ['Google_client_id'],
            'secret': os.environ['Google_secret'],
            'key': ''
        }

    },

    'github': {

        'APP': {
            'client_id': os.environ['Github_client_id'],
            'secret': os.environ['Github_secret'],
            'key': ''
        }
    },


}
```

You can find the information to configure it [here](https://docs.allauth.org/en/latest/socialaccount/index.html) in the Django allauth documentation. Replace the os.environ[''] with the client's id and secret, the key is usually left empty. They will be in a string format like so:

```python
'APP': {
            'client_id': 'hi12hh4i2',
            'secret': '11242124',
            'key': ''
        }
```

## Running the Project

To run the project make sure to be in the right directory. You should be in the following directory: ``\Network-Hunt\networkhuntproject``

Now you should makemigrations and then migrate.

```python
python manage.py makemigrations

python manage.py migrate
```

Then finally, you can run the server.

```python
python manage.py runserver
```

Additionally you can also create a superuser.

```python
#optional
python manage.py createsuperuser
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
