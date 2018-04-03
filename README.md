# Pug or Ugh API

## Requirements

Use the provided `requirements.txt` to install needed packages for this project in a virtual environment. The easiest way to do this is with `pip install -r requirements.txt` while your virtualenv is activated.

### Start Application
After installing the required packages, run Project from your terminal on your local server.

```bash
$ python manage.py runserver
```

## Models

The JavaScript application expects the following models.

* `Dog` - This model represents a dog in the app.

	Fields:

	* `name`
	* `image_filename`
	* `breed`
	* `age`, integer for months
	* `gender`, "m" for male, "f" for female, "u" for unknown
	* `size`, "s" for small, "m" for medium, "l" for large, "xl" for extra
	  large, "u" for unknown

* `UserDog` -  This model represents a link between a user an a dog

	Fields:

	* `user`
	* `dog`
	* `status`, "l" for liked, "d" for disliked

* `UserPref` - This model contains the user's preferences

	Fields:

	* `user`
	* `age`, "b" for baby, "y" for young, "a" for adult, "s" for senior
	* `gender`, "m" for male, "f" for female
	* `size`, "s" for small, "m" for medium, "l" for large, "xl" for extra
	  large

	`age`, `gender`, and `size` can contain multiple, comma-separated values

## Routes

The following routes are expected by the JavaScript application.

* To get the next liked/disliked/undecided dog

	* `/api/dog/<pk>/liked/next/`
	* `/api/dog/<pk>/disliked/next/`
	* `/api/dog/<pk>/undecided/next/`

* To change the dog's status

	* `/api/dog/<pk>/liked/`
	* `/api/dog/<pk>/disliked/`
	* `/api/dog/<pk>/undecided/`

* To change or set user preferences

	* `/api/user/preferences/`

## Authentication

The supplied project includes Token-Based Authentication, that functionality should be maintained.

## Unit Tests
Unit tests written to test that the models, classes, and other functions behave as expected.
