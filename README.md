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

