## Theatre-project
The Theatre API service, built on Django REST,
allows visitors of the Theatre to make Reservations online and choose needed seats without going physically to the Theatre.
This API provides comprehensive details on plays, performances, theatre halls, tickets, reservations, and more.

## Installing using GitHub
Before you begin, ensure you have met the following requirements:
Docker must be already installed for running the server with docker-compose.
Python3 must be already installed.
Run the project locally without Docker
Clone the repository:

```shell
git clone https://github.com/SashaKisliy/theatre-api.git
```
#### Go to the project directory:
```shell
cd theatre_api
```
#### Create a virtual Python environment and activate it:
```shell
python -m venv .venv 
source .venv/bin/activate   # on macOS
.\.venv\Scripts\activate    # on Windows
```
#### Set the project dependencies:
```shell
pip install -r requirements.txt
```
## Environment Setup

To configure the project, create a .env file in the root directory of your project
and add the following variables or check .env.sample file:

```dotenv
POSTGRES_PASSWORD=your-password
POSTGRES_USER=your-username
POSTGRES_DB=your-database
POSTGRES_HOST=your-host
POSTGRES_PORT=your-port
PGDATA=your-database-data

SECRET_KEY=your-secret-key
```

## Starting the server
1. Create database migrations:
```shell
python manage.py makemigrations
python manage.py migrate
```
2. Start the development server:
```shell
python manage.py runserver
```
The API should now be accessible at http://localhost:8080/


## Run with Docker
Docker should be installed

```shell
docker-compose build
docker-compose up
```
The API should now be accessible at http://localhost:8081/


## Getting access

#### Create a user via api/user/register/
#### Or use Admin credentials:
```
email: admin@admin.com
password: 123123
```
#### Get access token via api/user/token/
#### To authenticate, include the obtained token in your request headers with the format:

makefile
Authorization: Bearer <your-token>

## API Documentation
The API is documented using the OpenAPI standard. Access the API documentation by running the server and navigating to:

* Swagger
* Redoc

## Features of the project:
* Information Restriction: Communication between administrators and regular users is limited, ensuring users access only entitled information.

* Play Details: Retrieve comprehensive data on plays, including names, descriptions, and associated genres and actors.

* Performance Insights: Access details about different performances, including the play, theatre hall, and show times.

* Theatre Hall Details: Retrieve information about theatre halls, such as their names, number of rows, and seats per row.

* Ticket Overview: Obtain detailed ticket information, including seat numbers, performance details, and associated reservations. Filter the ticket list by performance for added convenience.

* Order Status: Authenticated users can review their reservation information.

* Reservation Details: Facilitates the creation of reservations, allowing users to specify their desired seats and performance.

* Authentication Mechanism: Users can create profiles by providing an email address and password. The API employs JWT (JSON Web Tokens) authentication to safeguard sensitive data.

* Docker Integration: Use of Docker and Docker Compose for consistent development and deployment environments.

* API Documentation: Extend and enhance API documentation using drf-spectacular, providing clear and interactive API documentation.

* Advanced Querying: Complex querying capabilities with support for filtering, searching, and ordering on various fields related to performances, plays, and theatre halls.

* Access Control: Implement custom permissions to restrict access based on user roles, ensuring sensitive operations are limited to authorized personnel.

