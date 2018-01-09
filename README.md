# c3po - Gatoraid (Easy data access tool for land and space based telescope datas) #Python #Flask #Pymongo
![image](https://i.imgur.com/Sg8MwGn.png) with <img src="https://i.imgur.com/Sg8MwGn.png" width="960" height="600">
Import data from the internet into the MongoDB server
<br>
<b>NEW IN VERSION 2!</b> Add via website
![](https://i.imgur.com/Sg8MwGn.png | width=350)
 <br></br>
Regions are displayed in all regions
![Alt text](https://i.imgur.com/94oF12j.png) 
<br></br>
All stars per region are added as 'GatorObjects' for each region.
![Alt text](https://i.imgur.com/LFC5v32.png)
Details for each star<br></br>
![Alt text](https://i.imgur.com/8xUA8TT.png)
![Alt text](https://i.imgur.com/1n2GmhY.png)<br><br>

 Abstract:<br>
 To add data register an account and in your dashboard select 'add regions by file' and use file 'simbad_new.tsv' for reference.
 For new data go to <code>http://simbad.u-strasbg.fr/simbad/</code> and replicate the file named 'simbad_new.tsv', which
contains region data from the simbad app. This data is added to the database and <code>http://irsa.ipac.caltech.edu/applications/Gator/</code> API is used to find stars for each region name.<br></br>
 
  ______________________________________________________________________________________________________<br><br>
  <code>app.py</code> runs an API for data access and a website to manage the data with a GUI</br><br>
  <code>pipenv install requests</code><br>
  <code>pip install -r requirements.txt</code><br></br>
   <b><code>You may need to install additional dependencies.</b></code><br></br>
  <code>python app.py</code><br><br>
  ______________________________________________________________________________________________________<br><br>
<br>
A list of all availible API commands will be posted soon<br>
<code><b>GET: </b>localhost:5000/api/region_by_name/HD%2010700</code><br>
<code><b>GET: </b>localhost:5000/api/stars/069.40055143/-02.47354857</code>



