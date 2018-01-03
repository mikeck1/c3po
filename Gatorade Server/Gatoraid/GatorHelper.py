# This file is a class of functions used to
# read text from Gator/ Simbad
# Written by Michael Kaufman and Marcos 2017

# START OF LIBRARY - ' GatorHelper.py '

# DESIGNED FOR GATOR's CSV DATA
# USED FOR CSV WEB DATA - RETURNS OBJECTS ID'S
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
# DESIGNED FOR GATOR's CSV DATA
# USED FOR CSV WEB DATA - RETURNS OBJECTS
def get_matrix(CSV_URL):
    csv_url = CSV_URL
    import requests  # pypenv install requests
    import csv # To read CSV
    with requests.Session() as s:
        download = s.get(CSV_URL)

        decoded_content = download.content.decode('utf-8')

        d = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(d[1:])
        i=0
        matrix = []
        for line in range(127):
            matrix.append(my_list)
            i+=1
        return (matrix)
# DESIGNED FOR GATOR's CSV DATA
# USED FOR CSV WEB DATA - RETURNS OBJECTS
# NOT USED AT THE MOMENT
def get_item(CSV_URL):
    csv_url = CSV_URL
    import requests  # pypenv install requests
    import csv # To read CSV
    matrix= []
    matrix = get_matrix(CSV_URL)
    j=0

    item1=[]
    for tt in range(127):
        item1 = matrix[0][0][j]
        j+=1
    return item1
# DESIGNED FOR A LOCAL FILE
# USED FOR LOCAL FILE DATA - RETURNS FILE LINES
# Written by Marcos
def read_txt_to_lines(fileName):
    with open(fileName, 'rU') as f:
        import csv
        fileLines = f.readlines()
        dataLines = []
        i=0
        for line in fileLines:
            l = line.strip().split('\t')
            i+=1
            dataLines.append(l)
        
        return dataLines
# DESIGNED FOR A LOCAL FILE
# USED FOR LOCAL FILE DATA - RETURNS FILE LINES
# Written by Michael
def read_ids(fileName):
    fileLines = read_txt_to_lines(fileName)
    dataLines = []
    finalLines = []
    # Format data for python.
    i=0
    for line in fileLines:
        l = line.strip("\n").replace(" ", "").split('\t')
        dataLines.append(l)
        finalLines= dataLines[0]
        i+=1
    return finalLines