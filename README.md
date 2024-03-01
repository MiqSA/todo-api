# TODO API

This is an API build in [FastAPI](https://fastapi.tiangolo.com/) for random TODO tasks. 

## About

To have the tasks the user should sign up and log in to their account to get the access token, with this token it's possible to get the todos tasks.  To see the API swagger just access `/docs`.

The initial approach just provides five tasks that the user should do, but it's possible have more just increasing the `limit`. The source of TODO's task it's [here](https://jsonplaceholder.typicode.com/todos). 

## Stacks

- Python
- Docker
- Postgres
- FastAPI
- Pytest

## How To Use?

Clone this repo.
```
git clone https://github.com/MiqSA/todo-api.git
```
Enter in folder
```
cd todo-api/
```
With the docker running in your machine do this:
```
make deps-up
```
The API will be running at `http://localhost:8010`

## Tests

You can use the `http://localhost:8010/docs` to check all endpoints and test directly. You also run the unit and integration tests using Pytest, to do this just write:
```
make test
```
To check the coverage use this
```
make cover
```
To see the coverage details in html use this
```
make cover-html
```
## About the Endpoints

There are four endpoints:

### GET - `v1/health`
A simple check if the API is running correctly.

```
curl --location 'http://localhost:8010/v1/health'
```
### POST - `v1/signup`
Register the user with the basic pieces of information like username, email, and password.

```
curl --location 'http://localhost:8010/v1/signup' \
--header 'Content-Type: application/json' \
--data-raw '{
  "username": "user1",
  "email": "user1@gmail.com",
  "password": "123"
}'
```
### POST - `v1/login`
Pass the email and password to get the access_token.

```
curl --location 'http://localhost:8010/v1/login' \
--header 'Content-Type: application/json' \
--data-raw '{
  "email": "user1@gmail.com",
  "password": "123"
}'
```
### GET - `v1/todo`
With the access_token you can get the TODOs tasks.

```
curl --location 'http://localhost:8010/v1/todo' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDkyNDc1MDAsInN1YiI6ImE3NjlhMWMzLTBlYjAtNGY2Ni04N2YyLTdhNTRlODJlZGQ0OCJ9.aL3s7A3Knq2bfeOVPryXEUgCTGx3H1vPmIZ8Y-lMB8g'
```

## Improvements

Here are some improvements to the current API state:
- Keep the coverage high: The last coverage test is at 93%. Maintain this level or increase.
- Increase unit tests: The current tests are more integration tests. But it's good practice to have a lot of unit tests. Increase the coverage of unit tests.
- New auth endpoints: Some endpoints like `v1/change-password` can be add.



