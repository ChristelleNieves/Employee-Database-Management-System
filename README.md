# Employee-Database-Management-System

A small-scale flask application that represents an employee database management system using SQLite3.<br>
Incorporates user authentication, role-based access for users, and password encryption.<br>
The user has the ability to log in and according to their security level (1, 2, 3) they will be granted different permissions within the site.<br>
Users with security level 1 represent admin users and have the ability to add/remove employees from the database.<br>
Users with security level 2 have the ability to view all employees but cannot add/remove employees.<br>
Users with security level 3+ do not have permissions to add/remove or view employees in the database.<br>
<br>
If you decide to test the application on your own machine, the test login is: username = Test, password = password<br>


<img width="941" alt="login" src="https://user-images.githubusercontent.com/29238419/107166284-8c469400-6983-11eb-8359-dacce3b670f8.png">
<br>
<img width="891" alt="home" src="https://user-images.githubusercontent.com/29238419/107166292-91a3de80-6983-11eb-90c5-361fafac5da3.png">
<br>
<img width="855" alt="add_employee" src="https://user-images.githubusercontent.com/29238419/107166300-96689280-6983-11eb-98b1-243c4d641254.png">
<br>
<img width="872" alt="view_employees" src="https://user-images.githubusercontent.com/29238419/107166305-9a94b000-6983-11eb-81c8-97ce0942a102.png">
<br>
<img width="874" alt="remove_employee" src="https://user-images.githubusercontent.com/29238419/107166310-9c5e7380-6983-11eb-83d1-33c86c028e60.png">
<br>
<img width="856" alt="logged_out" src="https://user-images.githubusercontent.com/29238419/107166315-9ff1fa80-6983-11eb-8a85-5866df1442fe.png">
