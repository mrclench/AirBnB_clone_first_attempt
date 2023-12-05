# AirBnB_clone
![img.png](img.png)

<B>Description</B>

This project aims to clone Airbnb's application and websites, utilizing a Python console as the central interface. The project is managed through the command line (cmd) interface, and data is stored, retrieved, and exchanged using JSON and SQL. We leverage the Flask web framework to expose a RESTful API, enabling communication between the console, backend, and a static web frontend.

Key Features:

User Authentication: Users can create accounts, log in, and manage their profiles.
Property Listing: A comprehensive property listing showcasing available spaces.
Reservation Management: Users can make reservations and manage their booking history.
Tech Stack:

Backend: Flask web framework for Python
Templating Engine: Jinja2 for rendering dynamic web pages
Database: SQL for structured data storage, MongoDB for JSON files
Frontend: HTML and JavaScript for static and dynamic web pages
Project Structure:

console/: Python console application handling core functionality.
static/: Directory for static web content.
templates/: HTML templates rendered using Jinja2.
api/: Flask RESTful API for communication with the frontend.
Serialization and Database:

JSON: Serialization/deserialization of data for console interactions.
SQL: Structured data storage for user accounts and reservations.
MongoDB: Storage for JSON files, providing flexibility for various data structures.
User Stories/Use Cases:

Users can register accounts, log in, and manage profiles.
Property seekers can browse listings and view detailed information.
Users can make reservations, view booking history, and manage upcoming stays.
By implementing a RESTful API with Flask, we enable seamless communication between the console and the frontend. The frontend, built with HTML and JavaScript, utilizes both static web pages for general content and dynamic pages for interactive features powered by JSON data retrieved from the API.

This structured approach ensures a modular and scalable development process, with Flask facilitating backend operations, Jinja2 managing dynamic content, and a RESTful API handling data exchange between the console and the web frontend.

<B>License</B>

Public Domain, no copyright protection

Feedback and contributors are welcomed. Reach out to either authors