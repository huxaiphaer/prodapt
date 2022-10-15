# Prodapt app.

This is a weather application.

### Requirements for setting up the project.

1. Python3. 
2. Django
3. Virtualenv.
4. Docker.
5. Postgres DB
6. Celery.
7. Bandit.
8. Isort.



### Installation Manually.

Clone the project as below :

```
$ git clone https://github.com/huxaiphaer/prodapt.git
```

then, cd into the folder prodapt :

```
$ cd prodapt
```

install, the dependencies of the project :

```
$ pip install -r requirements.txt
```

then before running the project, add a `.env` file and copy the variables from a file `.env.txt`

after that, then populate the DB with some remote data with the following command :

```
$ ./manage.py generate_data
```

after that then run the project with :

```
$ ./manage.py runserver
```

Further more, inorder to auto get the Weather updates you need to open another 2 terminals and execute the 2 commands below
independently :

```
$  celery -A prodapt beat -l info
```

and :


```
$ celery -A prodapt worker -l info
```

Finally, you can the weather updates via the endpoint below :

**NOTE**:
- _You need to provide a Bearer token to the endpoints before accessing them_

```
 http://127.0.0.1:8000/api/v1/weatherforecast/
```

You can search a city with this endpoint :

```
 http://127.0.0.1:8000/api/v1/weatherforecast/?search=Berlin&order_by=asc
```

_Read the table below for more endpoints._

### Installation on Mac or linux with Docker.

Run the project with Docker.

#### Requirements.

- Ensure that you have installed docker on your machine.

After, installing , then run the following command in the root folder of the 
project to spin the container.

```
 $ docker-compose up -d
```

Then, the host and the port will be `http://0.0.0.0:8070/` 


 #### Endpoints.

| HTTP Method | End Point                                      | Action                          |
|-------------|------------------------------------------------|---------------------------------|
| POST        | api/v1/create/                                 | Sign up                         |
| GET         | api/v1/login/                                  | Login                           |
| GET         | api/v1/weatherforecast/                        | Get all weather forecast        |
| GET         | api/v1/weatherforecast/?search=berlin&order_by=desc | Search city in descending order |
| GET         | api/v1/weatherforecast/?search=berlin&order_by=asc | Search city in ascending order  |


**NB :**

For the `api/v1/create/` **POST** endpoint,  the **BODY** is :

```
{
    "email": "test@gmail.com",
    "username": "test",
    "password": "namungoona"
}
```

then for `api/v1/login/` body is :

```
{
    "email": "test@gmail.com",
    "username": "test",
    "password": "namungoona"
}
```


### Running tests of the project.

```
$ ./manage.py test
```


### Contributors 

* [Lutaaya Idris](https://github.com/huxaiphaer)
