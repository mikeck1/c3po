# c3po - Gatoraid (Easy data access tool for land and space based telescope datas) #Python #Flask #Pymongo

Import data from the internet into the MongoDB server
<br>
<b>NEW IN VERSION 2!</b> Add via website
![Alt text](https://i.imgur.com/Sg8MwGn.png)
 <br></br>
Regions are displayed in all regions
![Alt text](https://i.imgur.com/94oF12j.png) 
<br></br>
All stars per region are added as 'GatorObjects' for each region.
![Alt text](https://i.imgur.com/LFC5v32.png)
Details for each star<br></br>
![Alt text](https://i.imgur.com/8xUA8TT.png)
![Alt text](https://i.imgur.com/1n2GmhY.png)<br><br>
 <b><code>You may need to install additional dependencies.</code><br></br></b>
<code>pipenv install requests</code><br>
<code>python readsimbad.py</code><br>
<p align="center">
 <code>readsimbad.py</code> reads regions by region name from a file created from a txt file of names sent to <code>http://simbad.u-  strasbg.fr/simbad/</code><br></br>
  then downloads stars from for each region name from <code>http://irsa.ipac.caltech.edu/applications/Gator/</code><br></br>
 
  ______________________________________________________________________________________________________<br>
  <code>app.py</code> runs an API for data access and a website to manage the data with a GUI</br>
  <code>pip install -r requirements.txt</code><br></br>
  <code>python app.py</code><br>
  ______________________________________________________________________________________________________<br>
</p>
A list of all availible API commands will be posted soon<br>
<code><b>GET: </b>localhost:5000/api/region_by_name/HD%2010700</code><br>
<code><b>GET: </b>localhost:5000/api/stars/069.40055143/-02.47354857</code>



