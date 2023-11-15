# Network Hunt

Network Hunt is a website that lets you manage the job applications and networking you've been doing or will do.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to create a virtual environment:

```bash
python -m venv example 
```
Now activate the virtual environment and install the requirements.txt file. The example below is for Windows. Mac and Linux have different commands to activate a virtual environment.

```bash
example/Scripts/activate

pip install -r requirements.txt
```

## Django allauth Regular Account Login and Registration

You will be able to use the regular login and registration functionality right from the get-go as long as you install the packages required in the requirements.txt file. You can find more information on it [here](https://docs.allauth.org/en/latest/account/index.html).

## Django allauth Social Account Login and Registration

Social account login and registration functionality need to be configured separately by you. Navigate to the settings.py file in the networkhunproject folder and you will see the code to configure it:
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

To run the project make sure to makemigrations and migrate first.
```python
python manage.py makemigrations

python manage.py migrate
```
Then finally, you can run the server. Additionally you can also create a superuser.
```python
python manage.py runserver

#optional
python manage.py createsuperuser
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.


## License

[MIT](https://choosealicense.com/licenses/mit/)