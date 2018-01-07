# This program sets up the server and routes requests to server to html or json data.
from flask import Flask, render_template, jsonify, request, redirect, flash, url_for, session, logging
from flask.ext.pymongo import PyMongo

# Used for Data from MongoDB ( Saving Data )
from bson import json_util
from bson.objectid import ObjectId
import json
import bson
from pymongo import Connection, MongoClient

# Used for forms
from flask_wtf.file import FileField, FileRequired
from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from werkzeug.utils import secure_filename
# Middleware used for data encryption and templates
from passlib.hash import sha256_crypt
from functools import wraps

# Used for the File upload function
UPLOAD_FOLDER = '/Users/Michael/Desktop/School/c3po_final/Gatoraid Server/temp'
ALLOWED_EXTENSIONS = set(['txt', 'pdf','tsv'])
import os
import os.path
import time

# Used for multithreading for file upload in add_regions route
from threading import Thread
from FileUpload import get_data

# First part of router is for website.
# Second part is the API used for CRUD and get data for other clients.
#Flask is the code used for routing, render_template to display html etc, file content

#functions
def toJson(data):
    """Convert Mongo object(s) to JSON"""
    return json.dumps(data, default=json_util.default)

#initializes server object
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
MONGO_URL= "localhost"
MONGO_PORT = 27017

# Initializing Mongo
print "Connecting to DB: ", MONGO_URL,MONGO_PORT, "\n"
client = MongoClient(MONGO_URL,MONGO_PORT)  # 27017 is the default port number for mongod
db = client.test



# Routes


# Main Route
@app.route('/')
def index():
    return render_template('home.html')

# About
@app.route('/about')
def about():
    return render_template('about.html')

# Register Form Class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match.')
        ])
    confirm = PasswordField('Confirm Password.')
# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        #Get user input from form
        col = db.accounts
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        col.insert({'name' : name, 'email' : email, 'username' : username, 'password' : password})
        flash('You are now logged in.', 'success')
        return  redirect(url_for('login'))
    return  render_template('register.html', form=form)

# login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #get from fields
        col = db.accounts
        # Gets form fields.
        username = request.form['username']
        password_candidate = request.form['password']
        # Grabs first username from database and calls it data.
        data = col.find_one({'username':username})
        # If any rows in found, or in result.
        if data > 0:
            #Gets password from data
            password = data['password']
            try:
                # Verifies password is correct with database.
                if sha256_crypt.verify(password_candidate, password):
                    session['logged_in'] = True
                    session['username'] = username
                    flash('Success!', 'success')
                    return redirect(url_for('dashboard'))
                else:
                    flash('Invalid Password.', 'danger')
                    return redirect(url_for('login'))
            except: 
                app.logger.info("error")
        else:
            flash('Invalid username.', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

# Check if user is logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

# Logout
@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out!', 'success')
    return redirect(url_for('login'))

# Dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    return render_template('dashboard.html')

# Region Form Class
class RegionForm(Form):
    name = StringField('name', [validators.Length(min=3, max=50)])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Add Region
@app.route('/add_region', methods=['GET', 'POST'])
@is_logged_in
def add_region():
    col = db.c3po
    form = RegionForm(request.form)
    # IF POST REQUEST
    if request.method == 'POST':
        #  IF SUBMIT BY NAME
        if request.form['btn'] == 'Submit' and form.validate():
            name = form.name.data
            col.insert({'name' : name})
            flash('Region Created.','success')
            return redirect(url_for('dashboard'))
        else: 
            # CHECK IF UPLOAD BY FILE
            if request.form['btn'] == 'Upload':
                file = request.files['file']
                # if user does not select file, browser also
                # submit a empty part without filename
                if file.filename == '':
                    flash('No selected file', 'danger')
                    return redirect(url_for('add_region'))
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    app.logger.info("filename")
                    app.logger.info(filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    while not os.path.exists('/Users/Michael/Desktop/School/c3po_final/Gatoraid Server/temp/'+filename):
                        flash("waiting for file...",'success')
                        app.logger.info("waiting for file...")
                        time.sleep(1)
                    if os.path.isfile('/Users/Michael/Desktop/School/c3po_final/Gatoraid Server/temp/'+filename):
                        app.logger.info("loading thread...")
                        flash("loading file...",'success')
                        result = Thread( target=get_data, args=(filename,) )
                        result.start()
                        flash("file being proccessed...",'success')
            else: 
                return render_template('add_region.html', form=form)
    # IF GET REQUEST
    return render_template('add_region.html', form=form)

# Used for the Region data
class RegionForm(Form):
    searchkey = StringField('searchkey', [validators.Length(min=1, max=50)])
    searchfield = StringField('searchfield', [validators.Length(min=1, max=50)])
    obj2ID = StringField('_id', [validators.Length(min=1, max=50)])
    objID = StringField('_id', [validators.Length(min=1, max=50)])
    MagR = StringField('MagR', [validators.Length(min=1, max=25)])
    bib = StringField('bib', [validators.Length(min=1, max=25)])
    MagV = StringField('MagV', [validators.Length(min=1, max=25)])
    MagU = StringField('MagU', [validators.Length(min=1, max=25)])
    MagI = StringField('MagI', [validators.Length(min=1, max=25)])
    nnot = StringField('not', [validators.Length(min=1, max=25)])
    MagB = StringField('MagB', [validators.Length(min=1, max=25)]) 
    DEC = StringField('DEC', [validators.Length(min=1, max=25)]) 
    Type = StringField('Type', [validators.Length(min=1, max=25)]) 
    Identifier = StringField('Identifier', [validators.Length(min=1, max=25)]) 
    name = StringField('name', [validators.Length(min=1, max=25)]) 
    RA = StringField('RA', [validators.Length(min=1, max=25)]) 
    spec = StringField('spec', [validators.Length(min=1, max=25)]) 

# Edit Region
@app.route('/edit_region')
@is_logged_in
def edit_regions():
    form = RegionForm(request.form)
    username = form.username.data
    col = db.c3po
    cursor = col.find()
    return render_template('regions.html', region = doc)

# Display all Regions page
@app.route('/regions')
def regions():
    col = db.c3po
    doc = col.find()
    return render_template('regions.html', region = doc)

# Edit Regions
@app.route('/region/edit/', methods=['GET', 'POST'])
@is_logged_in
def Editregions():
    form = RegionForm(request.form)
    if request.method == 'POST':
        name = form.name.data
        col = db.c3po
        names = col.find({'name':name}, {'GatorObjects':0})
        a=[]
        if request.form['btn'] == 'Upload':
            idd = form.objID.data
            Identifier = form.Identifier.data
            form = RegionForm(request.form)
            name = form.name.data
            app.logger.info(Identifier)
            add_id = col.update(
            {'name':bson.ObjectId(oid=str(idd))},
            {
            "$set": {
            "name":name,
            "Identifier":Identifier
            }
            }
            )
        i=0
        for name in names:
            i+=1
            a.append(name)
        count = col.find({'name':name}).count()
        if i>0:
            app.logger.info(count)
            flash('Found '+str(i) +' region(s) with that name.', 'success')
            return render_template('edit_region.html', form=form, name=name)
        else:
            flash('Found '+str(count) +' region with that name', 'danger')
            return render_template('edit_region.html', form=form, name=name)
    # doc=col.find_one({'_id':bson.ObjectId(oid=str(id))})
    return render_template('edit_region.html', form=form)

# Dynamic routing for regions
@app.route('/region/<string:id>/')
def region(id):
    col = db.c3po
    doc=col.find_one({'_id':bson.ObjectId(oid=str(id))})
    return render_template('region.html', id=id, region=doc)

# Dynamic routing for stars
@app.route('/region/<string:id>/star/<test>')
def GatorObjects(id,test):
    col = db.c3po
    doc=col.find_one({'_id':bson.ObjectId(oid=str(id))})
    # stardoc = col.find({{ 'GatorObjects.id': star_iden }})
    return render_template('gatorObjects.html', id=id, region=doc, test=test)












































# BACKEND API

# Get all names
@app.route('/api/name', methods=['GET'])
def get_all_names():
    col = db.c3po

    results = col.find()
    json_results = []
    for result in results:
      json_results.append(result)
    return toJson(json_results)

# Get all Stars
@app.route('/api/stars', methods=['GET'])
def get_all_stars():
    col = db.c3po

    results = col.find()
    json_results = []
    for result in results:
      json_results.append(result)
    return toJson(json_results)

# Add a named region.
@app.route('/api/addregion', methods=['POST'])
def add_star():
    add = db.c3po
    name = request.json['name']
    language = request.json['language']

    add_id = add.insert({'name' : name, 'language' : language})
    new_add = add.find_one({'_id' : add_id})

    output = {'name' : new_add['name'], 'language' : new_add['language']}
    return jsonify({'result': output})

# This is used to add stars to each named region.
@app.route('/api/add/object/<string:id>', methods=['PUT'])
def ApiEditstars(id):
    col = db.c3po
    pol = db.c3po
    name = request.json['name']
    results = pol.find()
    json_results = []
    for result in results:
      json_results.append(result)

    add_id = col.update(
        {'_id':bson.ObjectId(oid=str(id))},
        {
        "$set": {
            "name":name,
            "GatorObject": json_results
        }
        }
    )

    output = {'result' : add_id}
    return jsonify({'result': output})

# Search a star by RA and DEC
@app.route('/api/stars/<ra>/<dec>', methods=['GET'])
def get_one_Star(ra, dec):
    col = db.c3po
    output= {}
    q=col.find_one({ 'ra': ra, 'dec': dec })
    if q:
        output=col.find_one({ 'ra': ra, 'dec': dec })
    else:
        output='No Results found.'
    return toJson(output)



# By Michael Kaufman

# Executes server
if __name__ == '__main__':
    app.secret_key='123'
    app.run(debug=True)