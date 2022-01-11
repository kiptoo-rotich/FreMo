#  FreMo Medical and Birth Centre

#### Author: [Kiptoo Rotich](https://github.com/kiptoo-rotich)

## Screenshot
### Landing page
![Screenshot from 2022-01-11 06-51-18](https://user-images.githubusercontent.com/48821300/148938505-9a42e7c9-64fe-4ce3-bfbb-b4c83d1c5ec6.png)

### Book appointment
![Screenshot from 2022-01-11 06-52-21](https://user-images.githubusercontent.com/48821300/148938151-dc83760f-a1b8-40c0-ad1d-0008adf48759.png)

### Payments
![Screenshot from 2022-01-11 06-52-44](https://user-images.githubusercontent.com/48821300/148938260-4c3564cc-94f5-48d6-bc9a-b129bf74b670.png)


## Description
This a hospital website that shows details about FreMo Medical and Birth Centre with FreMo School included.



## Setup and installations
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.9 manage.py runserver`
* Access the live site using the local host provided
* Create your superuser account `python manage.py createsuperuser` inside virtual environment.

## Getting started

### Prerequisites
* python3.9
* virtual environment
* pip
* postgresql
  

#### Clone the Repo and rename it to suit your needs.
```bash
git clone `https://github.com/kiptoo-rotich/FreMo`
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.8 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY = 'your secret key'
DEBUG=True
DB_NAME='<your database name>>'
DB_USER='<your username>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='*'
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.9 manage.py check
python3.9 manage.py makemigrations web
python3.9 manage.py migrate web 0001
python3.9 manage.py migrate
```

#### Run the app
```bash
python3.8 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)



## Testing the Application
`python manage.py test projects`
        
## Built With

* [Python3.8](https://docs.python.org/3/)
* Django==3.2.5
* Postgresql 
* Boostrap
* HTML
* CSS


### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license)