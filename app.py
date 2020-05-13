from flask import Flask, render_template, request, redirect, jsonify, \
    url_for
import random
import string
import logging
import json
from flask import make_response
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'appstockdb'

mysql = MySQL(app)
company_name = []

with open("companies.txt", 'r') as f:
    company_list = [line.rstrip() for line in f]
    company_list.sort()
    
with app.app_context():
    cur = mysql.connection.cursor()
    cur.execute('SELECT Name FROM company')
    company_name = cur.fetchall()
    cur.close()
    company_name = [x for x, in company_name]

# ** Example 1 ** 
# Autocomplete method - called from Jinja template
@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    
	search = request.args.get('q')
    
	# results = [{'value': 'MIR:00000466', 'label': 'WormBase RNAi'}, \
		# {'value': 'MIR:00000031', 'label': 'Wormpep'}, {'value': 'MIR:00000186', 'label': 'Xenbase'}, \
		# {'value': 'MIR:00000111', 'label': 'Resource 1'}, {'value': 'MIR:00000222', 'label': 'Resource 2'}, \
		# {'value': 'MIR:00000333', 'label': 'Resource 3'}, {'value': 'MIR:00000444', 'label': 'Resource 4'}, \
		# {'value': 'MIR:00000555', 'label': 'Resource 5'}, {'value': 'MIR:00000666', 'label': 'Resource 6'}]

	return jsonify(matching_results=company_name)
	#results = ["car", "carriage", "horse", "dog"]
	#return jsonify(matching_results=results)

# Route to home page
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def show_home():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM company')
    fetchdata = cur.fetchall()
    cur.close()
    
    # cur.execute('EXEC sp_columns `company`')
    
    
    return render_template('index.html', data = fetchdata)
    
# Main Method
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)