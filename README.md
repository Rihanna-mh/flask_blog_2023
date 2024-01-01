Flask Blog Project
This is a simple Flask web application for creating, listing, and viewing blogs. The application uses a MySQL database to store blog information, such as the author's name, title, content, and category.

Prerequisites
Make sure you have the following installed on your machine:

Python
Flask
MySQL
Flask-MySQLdb
You can install the required Python packages using:
pip install Flask Flask-MySQLdb


Setup
1. Clone the repository:

git clone https://github.com/your-username/your-repository.git
cd your-repository

1. Set up the MySQL database:

Create a MySQL database named flask_db_blog1.

Update the MySQL configuration in flask_server.py with your database credentials:

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your-username'
app.config['MYSQL_PASSWORD'] = 'your-password'
app.config['MYSQL_DB'] = 'flask_db_blog1'

2. Run the Flask application:
python flask_server.py

Visit http://127.0.0.1:8080 in your web browser to access the application.

Usage
Visit the home page to submit a new blog by filling out the form.
Navigate to the blog list to see all submitted blogs.
Click on a blog title to view its details.
Use the category buttons to filter blogs by industry.

Project Structure
flask_server.py: Main Flask application file.
templates/: HTML templates for rendering pages.
blogForm.html: Form for submitting a new blog.
blogResult.html: Page displayed after successful blog submission.
c.html: Page for listing all blogs.
d.html: Page for displaying blog details.
category.html: Page for listing blogs by category.

Acknowledgments
This project is a simple example of a Flask web application. Feel free to customize and extend it based on your requirements.