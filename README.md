# Zomentium_backend-assessment

The project is done with the help of flask for creating a backend API and sqlarSQLAlchemy for providing the database support.

All the functionalities are shown with the help of screenshots those can be found with this repository.
All the test cases can also be looked upon with the help of screenshots.

Functions performing respective tasks in app.py file-

- Insert function = query() : books a ticket for the given time for a user with his phone number and name.(Also checks for count greater then 20)

- Update time for a ticket = update() : based on phone number and name updates the time of a ticket.

- View tickets for a particular time = allattime().

- Delete a particular ticket= deleteparticular() : based on phone number delete the ticket which matches with the phone number.

- View the user’s details based on the ticket id = findusingid().

- Mark a ticket as expired if there is a diff of 8 hours between the ticket timing and current
  time = deletegreat8().

There are two template files:
1. show.html helps to print all the results.
2. query.html helps to perform the actions/tasks.


All the testing has been done on a localhost server with the help of html files.

For implementing it on different system:
Use anaconda prompt or command line to run the app.py file with the command python app.py.



