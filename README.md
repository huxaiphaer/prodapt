# Prodapt app.

This is a weather application.

### Requirements for setting up the project.

1. Python3. 
2. Django
3. Virtualenv.
4. Docker.
5. Postgres DB
6. Celery.

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

| HTTP Method | End Point                                          | Action                          |
|-------------|----------------------------------------------------|---------------------------------|
| POST        | api/v1/create/                                     | Sign up                         |
| GET         | api/v1/login/                                      | Get all Vehicles.               |
| GET         | api/v1/trips/                                      | Get all trips.                  |
| GET         | api/v1/weatherforecast/?                           | Get allweather forecast         |
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
