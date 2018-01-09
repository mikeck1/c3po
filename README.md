# c3po - Gatoraid (Easy data access tool for land and space based telescope datas) #Python #Flask #Pymongo

Import data from the internet into the MongoDB server
<br>
<b>NEW IN VERSION 2!</b> Add via website
<img src="https://i.imgur.com/Sg8MwGn.png" width="75%" height="75%">
 <br>
Regions are displayed
<br>
<img src="https://i.imgur.com/94oF12j.png" width="75%" height="75%">
<br>
All stars per region are added as 'GatorObjects' for each region.
<br>
<img src="https://i.imgur.com/LFC5v32.png" width="75%" height="75%">
<br>
Details for each star
<br>
![Alt text](https://i.imgur.com/8xUA8TT.png)
![Alt text](https://i.imgur.com/1n2GmhY.png)<br><br>
<br><br>
 Read Me:
 <br>
 To add data register an account and in your dashboard select 'add regions by file' and use file 'simbad_new.tsv' for reference.
 For new data go to <code>http://simbad.u-strasbg.fr/simbad/</code> and replicate the file named 'simbad_new.tsv', which
contains region data from the simbad app. This data is added to the database and <code>http://irsa.ipac.caltech.edu/applications/Gator/</code> API is used to find stars for each region name.<br>
  ______________________________________________________________________________________________________<br><br>
  Install and run MongoDB Server: 
  <br>
   <code><b>Choose your Platform: </b>https://docs.mongodb.com/manual/installation/</code><br>
  <br><br>
  Install Python and pip:
  <br>
  <code><b>Windows (Follow this guide): </b>https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/</code><br>
  <code><b>OS X/ Linux: </b>sudo easy_install pip</code><br>
  Run the website and API:
  <br>
  app.py runs an API and website that manages and displays land and space telescope data from caltech.gator and simbad API's.
  <br>
  <code>pipenv install requests</code>
  <br>
  <code>pip install -r requirements.txt</code>
  <br><br>
  <b><code>You may need to install additional dependencies.</b></code>
  <br>
  <code>python app.py</code>
  <br><br>
  ______________________________________________________________________________________________________<br><br>
<br>
A list of all availible API commands will be posted soon<br>
<code><b>GET: </b>localhost:5000/api/region_by_name/HD%2010700</code><br>
<code><b>GET: </b>localhost:5000/api/stars/069.40055143/-02.47354857</code>



