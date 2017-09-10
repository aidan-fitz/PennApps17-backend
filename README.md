# PennApps17-backend
Back end for PennApps F17 project

## API Documentation

- `GET /user/<username>`
  - Retrieves information about user `<username>` in JSON format.
- `PUT /user/<username>`
  - Updates informaton about user `<username>` from the data in the request body.
- `POST /user/`
  - Creates a new user on the server from the data in the request body.

## Setup instructions

To setup `virtualenv` with Python 3.x, navigate to the root directory of this repo and type:

```
$ virtualenv -p python3 .
```

Activate `virtualenv`:
```
$ source bin/activate
```

Deactivate `virtualenv`:
```
$ deactivate
```

Note: `virtualenv` creates a bunch of directories, which have been added to `.gitignore`. Do not remove them from `.gitignore`.

## Adding and updating dependencies

To add a dependency, simply run `pip3 install <dependency_name>` from within the virtualenv.

Export the list of dependencies:
```
$ pip3 freeze -r requirements.txt > requirements.txt
```

Install or update dependencies from the list:
```
$ pip install -r requirements.txt
```

Warning: Do not remove `requirements.txt` from `.gitignore`!

## Running the server

Before you run it, you must set the `FLASK_APP` environment variable. Within virtualenv, run:
```
$ export FLASK_APP=main.py
```

Then, you can run `$ flask run`. This works even if you deactivate and re-activate the environment.
