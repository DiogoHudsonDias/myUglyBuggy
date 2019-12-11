from flask import Flask
import urllib


app = Flask(__name__)

params = 'DRIVER={ODBC Driver 17 for SQL Server};' \
         'SERVER=(LocalDb)\MSSQLLocalDB;' \
         'PORT=1433;' \
         'DATABASE=UglyBuggy;' \
         'UID=usrUglyBuggy;' \
         'PWD=PASS****word***buggyUgly&&&&&951753;'\
         'MARS_Connection=Yes;'

params = urllib.parse.quote_plus(params)

strConexao = 'mssql+pyodbc:///?odbc_connect=%s' % params

app.config['SQLALCHEMY_DATABASE_URI'] = strConexao

from controller import *

if __name__ == '__main__':
    app.debug=True
    app.run(host="0.0.0.0", port=80)
