# CS 3450 project Group 4 Parking Genie

## Organization and Name Scheme:
- All documentation will be in the docs/ directory
- Out team will follow the Django directory organization and naming scheme.
- Each template will be named according to the corresponding route.

## Version-Control:
- Each team member will fork this repository to make changes. Once their changes are complete, they will create a pull request for the rest of the team to review. When the pull request is approved, they will merge their changes into master.
- All changes will be pushed to this repository.
- All releases are tagged with their release number.

## Tool Stack:
We will develop our website using Django. Using Django will simplify our application's database interactions and organization.

## Setup Instructions
- Clone this repository:<br>
<code> git clone https://github.com/katiecorcoran/cs3450-group-4.git </code>
- Navigate to the "src" directory and create a new virtual environment: (if you don't have pip installed already, you probably need to install Python on your machine)<br>
<code> pipenv shell </code><br>
<code> pip install -r requirements.txt </code>

## Build Instructions:
- If you have not set up the virtual environment already, follow the setup instructions above.
- Activate the virtual environment:<br>
<code> pipenv shell </code>
- Navigate into the outter 'parkinggenie' directory
- Start the project:<br>
<code> python manage.py runserver </code>
- The project will run at http://localhost:8000.

## Unit Testing:
We will use the built-in testing framework provided by Django.
Some of the tests we will write include:
- Testing all views to ensure they return the expected HttpResponse and pull the correct values from the database.
- Testing the "add funds" functionality to ensure that the correct amount of money is put into the user account.
- Testing the "add space" functionality to ensure that parking admins can add parking spaces to a lot.
This list will be amended as functionality is added.

## System Testing:
We will write testing procedures to run for each release.
The test steps will be written to cover all use cases of the application. Some of these use case include:
- Reserving a parking spot
- Adding a parking spot
- Adding funds
- Cancelling a parking splot reservation
