from flask import Flask, url_for, redirect, request, render_template
from flask_mysqldb import MySQL
import MySQLdb.cursors


app = Flask(__name__) 
UPLOAD_FOLDER = "/Users/rihanna/Documents/Canadian_Business_College/Project/07-Python/uploads/"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '***'
app.config['MYSQL_DB'] = 'flask_db_blog1'
mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def hello_world(): 
    if request.method == "GET":
        return "Hello GET"
    if request.method == "POST":
        return "Hello POST"
    
@app.route('/form', methods=['GET', 'POST'])
def form_world(): 
    if request.method == "GET":
        return render_template("blogForm.html")
    if request.method == "POST":
        author_server = request.form['author_name']
        h1_server = request.form['h1_title']
        intro_server = request.form['intro_paragraph']
        industry_server = request.form['industry']
        first_h2_server = request.form['first_h2']
        first_h2_para_server = request.form['first_h2_paragraph']
        second_h2_server = request.form['second_h2']
        second_h2_para_server = request.form['second_h2_paragraph']
        conclusion_server = request.form['conclusion']

        #save data to database
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        #cursor.execute("INSERT INTO blog_info VALUES ('test1', 'dfdf', 'Toronto');") 
        #here we are just testing if the data gets inserted into the databasecursor.execute("INSERT INTO blog_info (author_name, h1_title, intro_paragraph) VALUES (%s, %s, %s);", (author_server, h1_server, intro_server))
        cursor.execute("INSERT INTO blog_info VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}');".format(author_server, h1_server, intro_server, industry_server, first_h2_server, first_h2_para_server, second_h2_server, second_h2_para_server, conclusion_server))
        mysql.connection.commit()
        return render_template("blogResult.html", author = author_server, h1 = h1_server)

@app.route('/blog_list', methods=['GET', 'POST'])
def blog_list(): 
    if request.method == "GET":
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) #we get a dictionary as output in the terminal. If the bracket is empty, we get a topple of topples
        cursor.execute("SELECT * FROM blog_info")
        account = cursor.fetchall()
        print(account)
        return render_template("c.html", blog_list = account)

@app.route('/blog_info/<title>', methods=['GET', 'POST'])
def blog_info(title): 
    if request.method == "GET":
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM blog_info WHERE h1_title = '{0}'".format(title))
        account = cursor.fetchall() 
        print(account)
        return render_template("d.html", blog_list = account)

@app.route('/category/Health', methods=['GET'])
def category_health():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM blog_info WHERE industry = 'Health'")
    blogs = cursor.fetchall()
    return render_template("category.html", category="Health", blog_list=blogs)

@app.route('/category/DigitalMarketing', methods=['GET'])
def category_digital_marketing():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM blog_info WHERE industry = 'Digital Marketing'")
    blogs = cursor.fetchall()
    return render_template("category.html", category="Digital Marketing", blog_list=blogs)

@app.route('/category/Insurance', methods=['GET'])
def category_insurance():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM blog_info WHERE industry = 'Insurance'")
    blogs = cursor.fetchall()
    return render_template("category.html", category="Insurance", blog_list=blogs)

@app.route('/category/Tech', methods=['GET'])
def category_tech():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM blog_info WHERE industry = 'Tech'")
    blogs = cursor.fetchall()
    return render_template("category.html", category="Tech", blog_list=blogs)

if __name__ == '__main__': 
    print("hello")
    app.run(port=8080, debug=True)