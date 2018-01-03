# VARIOUS CODE USED

# Take data and make into object
# TAKE OBJECT AND PUT IN MONGODB
# VARIOUS CODE USED

# Take data and make into object
# TAKE OBJECT AND PUT IN MONGODB
from GatorHelper import read_txt_to_lines, get_matrix, get_id
import json
import bson
from bson import json_util
from bson import json_util
#functions
def toJson(data):
    """Convert Mongo object(s) to JSON"""
    return json.dumps(data, default=json_util.default)

def RecoverandLog():
    return 0
#functions

def toJson(data):
    """Convert Mongo object(s) to JSON"""
    return json.dumps(data, default=json_util.default)

# LIBRARY FOR READING CSV FROM URL
def get_matrix(CSV_URL):
    csv_url = CSV_URL
    import requests  # pypenv install requests
    import csv # To read CSV
    with requests.Session() as s:
        download = s.get(CSV_URL)

        decoded_content = download.content.decode('utf-8')

        dictObj = csv.DictReader(decoded_content.splitlines(), delimiter=',')
        return dictObj


def get_id(CSV_URL):
    csv_url = CSV_URL
    import requests  # pypenv install requests
    import csv # To read CSV
    with requests.Session() as s:
        download = s.get(CSV_URL)

        decoded_content = download.content.decode('utf-8')

        d = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(d)
        i=0
        id_ = []
        for line in range(127):
            id_.append(my_list[0][i])
            i+=1
        return (id_)




# MONGO CLIENT



# CONSTANTS FOR READING CSV FROM URL
textFileName= "H2D2list_376.txt"
CSV_URL = 'https://irsa.ipac.caltech.edu/SCS?table=fp_psc&RA=180.0&DEC=0.0&SR=0.05&format=csv'
headers = get_id(CSV_URL)
dictData = get_matrix(CSV_URL)

MONGO_URL= "localhost"
MONGO_PORT = 27017

# Initializing Mongo
from pymongo import MongoClient
print "Connecting to DB: ", MONGO_URL,MONGO_PORT, "\n"
client = MongoClient(MONGO_URL,MONGO_PORT)  # 27017 is the default port number for mongod
db = client.test
col = db.c3po

# for d in dictData:
#     print d

# # print toJson(freshd)
# print headers[10]





# ANOTHER CLIENT




# CONSTANTS FOR READING CSV FROM URL
regions = read_txt_to_lines("simbad_new.tsv")

# for region in regions:
#     print region

# Initializing Mongo
from pymongo import Connection, MongoClient
print "Connecting to DB: ", MONGO_URL,MONGO_PORT, "\n"
client = MongoClient(MONGO_URL,MONGO_PORT)  # 27017 is the default port number for mongod
db = client.test
col = db.person

# Make a list of URL's for Gator
CSV_URL = 'https://irsa.ipac.caltech.edu/SCS?table=fp_psc&RA=180.0&DEC=0.0&SR=0.05&format=csv'



nameslist = []
# Enter all Regions into DB
for region in regions:
    coords = region[4].strip()
    nameslist.append(region[1])
    coords = coords.strip().split()
    region.pop(4)
    region.insert(4, coords[0])
    region.insert(5, coords[1])

# Make URL LIST
URLlist = []
for region in regions:
    URLlist.append('https://irsa.ipac.caltech.edu/SCS?table=fp_psc&RA='+region[4]+'&DEC='+region[5]+'&SR=0.05&format=csv') 


# # UPLOAD TO MONGO
region_id = []
i=0
for region in regions:
    region_id.append(col.insert({
              "name": region[1],
            "Identifier": region[2],
            "Type": region[3],
            "RA": region[4],
            "DEC": region[5],
            "MagU": region[6],
            "MagB": region[7],
            "MagV": region[8],
            "MagR": region[9],
            "MagI": region[10],
            "spec": region[11],
            "bib": region[11],
            "not": region[12],
            "GatorObjects": []
            
        }) )
    i+=1

for d in dictData:
        print d[headers[0]]
    
print "hi"

# # Create a list of URL's and use it to get all the stars in each Region
headers = []
headers = get_id(CSV_URL)
count =0
i=0
for URL in URLlist:
    # for URL in URLlist:
    dictData = get_matrix(URL) 
    add_id = []
    count1=0
    count2 =0
    gatorObjects = []

    for d in dictData:
        try:
            gatorObjects.append({
                headers[0]:d[headers[0]],
                headers[1]:d[headers[1]],
                headers[2]:d[headers[2]],
                headers[3]:d[headers[3]],
                headers[4]:d[headers[4]],
                headers[5]:d[headers[5]],
                headers[6]:d[headers[6]],
                headers[7]:d[headers[7]],
                headers[8]:d[headers[8]],
                headers[9]:d[headers[9]],
                headers[10]:d[headers[10]],
                headers[11]:d[headers[11]],
                headers[12]:d[headers[12]],
                headers[13]:d[headers[13]],
                headers[14]:d[headers[14]],
                headers[15]:d[headers[15]],
                headers[16]:d[headers[16]],
                headers[17]:d[headers[17]],
                headers[18]:d[headers[18]],
                headers[19]:d[headers[19]],
                headers[20]:d[headers[20]],
                headers[21]:d[headers[21]],
                headers[22]:d[headers[22]],
                headers[23]:d[headers[23]],
                headers[24]:d[headers[24]],
                headers[25]:d[headers[25]],
                headers[26]:d[headers[26]],
                headers[27]:d[headers[27]],
                headers[28]:d[headers[28]],
                headers[29]:d[headers[29]],
                headers[30]:d[headers[30]],
                headers[31]:d[headers[31]],
                headers[32]:d[headers[32]],
                headers[33]:d[headers[33]],
                headers[34]:d[headers[34]],
                headers[35]:d[headers[35]],
                headers[36]:d[headers[36]],
                headers[37]:d[headers[37]],
                headers[38]:d[headers[38]],
                headers[39]:d[headers[39]],
                headers[40]:d[headers[40]],
                headers[41]:d[headers[41]],
                headers[42]:d[headers[42]],
                headers[43]:d[headers[43]],
                headers[44]:d[headers[44]],
                headers[45]:d[headers[45]],
                headers[46]:d[headers[46]],
                headers[47]:d[headers[47]],
                headers[48]:d[headers[48]],
                headers[49]:d[headers[49]],
                headers[50]:d[headers[50]],
                headers[51]:d[headers[51]],
                headers[52]:d[headers[52]],
                headers[53]:d[headers[53]],
                headers[54]:d[headers[54]],
                headers[55]:d[headers[55]],
                headers[56]:d[headers[56]],
                headers[57]:d[headers[57]],
                headers[58]:d[headers[58]],
                headers[59]:d[headers[59]],
                headers[60]:d[headers[60]],
                headers[61]:d[headers[61]],
                headers[62]:d[headers[62]],
                headers[63]:d[headers[63]],
                headers[64]:d[headers[64]],
                headers[65]:d[headers[65]],
                headers[66]:d[headers[66]],
                headers[67]:d[headers[67]],
                headers[68]:d[headers[68]],
                headers[69]:d[headers[69]],
                headers[70]:d[headers[70]],
                headers[71]:d[headers[71]],
                headers[72]:d[headers[72]],
                headers[73]:d[headers[73]],
                headers[74]:d[headers[74]],
                headers[75]:d[headers[75]],
                headers[76]:d[headers[76]],
                headers[77]:d[headers[77]],
                headers[78]:d[headers[78]],
                headers[79]:d[headers[79]],
                headers[81]:d[headers[81]],
                headers[82]:d[headers[82]],
                headers[83]:d[headers[83]],
                headers[84]:d[headers[84]],
                headers[85]:d[headers[85]],
                headers[86]:d[headers[86]],
                headers[87]:d[headers[87]],
                headers[88]:d[headers[88]],
                headers[89]:d[headers[89]],
                headers[90]:d[headers[90]],
                headers[91]:d[headers[91]],
                headers[92]:d[headers[92]],
                headers[93]:d[headers[93]],
                headers[94]:d[headers[94]],
                headers[95]:d[headers[95]],
                headers[96]:d[headers[96]],
                headers[97]:d[headers[97]],
                headers[98]:d[headers[98]],
                headers[99]:d[headers[99]],
                headers[100]:d[headers[100]],
                headers[101]:d[headers[101]],
                headers[102]:d[headers[102]],
                headers[103]:d[headers[103]],
                headers[104]:d[headers[104]],
                headers[105]:d[headers[105]],
                headers[106]:d[headers[106]],
                headers[107]:d[headers[107]],
                headers[108]:d[headers[108]],
                headers[109]:d[headers[109]],
                headers[110]:d[headers[110]],
                headers[111]:d[headers[111]],
                headers[112]:d[headers[112]],
                headers[113]:d[headers[113]],
                headers[114]:d[headers[114]],
                headers[115]:d[headers[115]],
                headers[116]:d[headers[116]],
                headers[117]:d[headers[117]],
                headers[118]:d[headers[118]],
                headers[119]:d[headers[119]],
                headers[120]:d[headers[120]],
                headers[121]:d[headers[121]],
                headers[122]:d[headers[122]],
                headers[123]:d[headers[123]],
                headers[124]:d[headers[124]],
                headers[125]:d[headers[125]],
                headers[126]:d[headers[126]]
                })

        except:
            print "Error at ",region_id[i]
    
    col.update(
                {'_id':bson.ObjectId(oid=str(region_id[i]))},
                {
                    "$set":{"GatorObjects":gatorObjects
                
                }}) 
    print "Working Great at ",region_id[i]
    count +=1
    i+=1
print count