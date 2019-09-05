#################
#### imports ####
#################

from flask import Flask, render_template, request
import json

################
#### config ####
################

app = Flask(__name__, instance_relative_config=True)

###############
#### routs ####
###############

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/about')
def about():
   return render_template('about.html')


@app.route('/plus_one')
def plus_one():
   x = int(request.args.get('x', 1))
   return json.dumps({'x': x + 1})

@app.route('/square')
def square():
   x = int(request.args.get('x', 1))
   return json.dumps({'x': x * x})

############################
#### custom error pages ####
############################
