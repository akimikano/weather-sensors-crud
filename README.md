# Weather sensors managing CRUD


## Table of Contents
- [Introduction](#-introduction)
- [Used technologies](#-used-technologies)
- [Architecture](#-architecture)
- [Running](#-running)
- [API Documentation](#-api-documentation)

## Introduction
RESTful API
to manage a list of users and weather sensors. The API allows 
users and sensors to be created, read, updated, and deleted. 
Basic authentication and authorization 
for API access. The service is able to 
process simultaneous requests from multiple 
clients and ensure high data availability.

## Used technologies

`Python`, `FastAPI`, `PostgreSQL`, `Docker`

## Architecture

Clean Architecture is a software design philosophy that emphasizes 
the separation of concerns to make systems more flexible, 
maintainable, and testable. The core idea is to structure your 
system in layers, where the inner layers contain business rules and 
logic, while outer layers handle external concerns such as databases, 
UI, or frameworks. The system's core is independent of external 
technologies, making it easier to adapt and change parts of the 
system without affecting the whole.


```
src                                 → Application sources 
  └ application                     → Application services layer
       └ repositories               → Repository interfaces
       └ use_cases                  → Application business rules 
  └ controllers                     → Route handlers
  └ domain                          → Enterprise core business layer such as domain model objects (Entities, Value Objects)
       └ entities                   → Core business model objects
       └ services                   → Core business logic
  └ infrastructure                  → Frameworks, drivers and tools such as Database, the Web Framework, mailing/logging/glue code etc.
       └ authentication             → Logic related to authentication
       └ database                   → Database ORM models and Repository implementations
          └ sqlalchemy              → Database interface made with Sqlalchemy
              └ models              → ORM models
              └ repositories        → Implementation of domain repository interfaces
              └ selectors           → Standalone database queries
       └ webserver                  → Express.js Web server configuration (server, routes etc.)
          └ middleware              → Middlwares for authenticating, validating etc.
          └ routers                 → Server routes
          └ schemas                 → Schemas for validating incoming data

 └ requirements.txt                 → Dependencies
 └ main.py                          → Main application entry point
```

## Running

Run the following command to run the system locally:
```sh
docker-compose up -d
```

## API Documentation

BASE URL: http://localhost:8000/api

API Documentation http://localhost:8000/api/docs/swagger.yml

<br>

#### Endpoints to manage users

POST _/users/ Create User_

GET _/users/ Get Users_

GET _/users/{user_id} Get User_

PUT _/users/{user_id} Update User_

DELETE _/users/{user_id} Delete User_

POST _/users/register Register_

POST _/users/jwt-create Create Jwt_

GET _/users/profile/me_

<br>

#### Endpoints to manage sensors

GET
_/sensors/ Get Sensors_


POST
_/sensors/ Create Sensor_


GET
_/sensors/{sensor_id} Get Sensor_


PUT
_/sensors/{sensor_id} Update Sensor_


DELETE
_/sensors/{sensor_id} Delete Sensor_
