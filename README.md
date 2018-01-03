# c3po - Gatoraid (Easy data access tool for land and space based telescope datas) #Python #Flask #Pymongo
![Alt text](https://i.imgur.com/zQKR426.png)
![Alt text](https://i.imgur.com/94oF12j.png)
![Alt text](https://i.imgur.com/LFC5v32.png)
 <code>readsimbad.py</code> downloads regions by region name from <code>http://simbad.u-strasbg.fr/simbad/</code><br></br>
 then downloads stars from for eah region name from <code>http://irsa.ipac.caltech.edu/applications/Gator/</code><br></br>
 <code>app.py</code> runs an API for data access and a website to manage the data with a GUI</br>
 <b><code>You may have to install some dependencies.</code><br></br></b>
 <code>pip install -r requirements.txt</code><br></br>
  <code>python readsimbad.py</code><br></br>
 <code>python app.py</code>
