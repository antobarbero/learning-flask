# Learning Flask #

Learning Flask with the tutorial: http://flask.pocoo.org/docs/1.0/tutorial



### Clonation of repository ###

$ git clone https://github.com/antobarbero/learning-flask.git
________________________________________________________________________


### How do I get set up? ###

1 . Install python3

2 . Create a virtual environment and activate it.

```
$ python3 -m venv venv

$ . venv/bin/activate
```

3 . Install the project requirements

```
$ pip install -r requirements.txt

```

or install the project in development mode

```
$ pip install -e .
```

________________________________________________________________________

### Initialize the db file ###

```
$ flask init-db
```
________________________________________________________________________

### Run the application ###

Development mode

```
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run
```
________________________________________________________________________

### How to run tests ###

```
$ pytest
```

To measure the code coverage

```
$ coverage run -m pytest
$ coverage report
```
________________________________________________________________________

### Build and install ###

Build a wheel distribution file
```
$ python setup.py bdist_wheel
```


To install

1 . Setup a virtual environment and install the built file using pip
```
$ pip install flaskr-1.0.0-py3-none-any.whl
```
Pip will install your project along with its dependencies.

2 . Run init-db to create the database in the instance folder.

```
$ export FLASK_APP=flaskr
$ flask init-db
```

3 . Configure the Secret Key.

Create the config.py file in the instance folder, which the factory will read from if it exists.

venv/var/flaskr-instance/config.py
```
SECRET_KEY = b'secretkey'
```

________________________________________________________________________

#### Used libraries and frameworks: ####
* Flask==1.0.2
* Click==7.0
* coverage==4.5.3
* itsdangerous==1.1.0
* Jinja2==2.10
* MarkupSafe==1.1.1
* pkg-resources==0.0.0
* Werkzeug==0.14.1
* pytest==4.3.1
* wheel==0.33.1
