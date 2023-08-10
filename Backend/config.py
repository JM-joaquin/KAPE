from flask_mysqldb import MySQL
from run import app

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'kape'
app.config['MYSQL_PORT'] = 3308

mysql = MySQL(app)
