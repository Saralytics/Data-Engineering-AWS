import pandas as pd
import requests

# URL of your endpoint
URL = " https://vsgb5ptlaj.execute-api.me-south-1.amazonaws.com/prod/ingestion"

#read the testfile
data = pd.read_csv('~/Desktop/hub/Data-Engineering-AWS/dataset/test_set.csv', sep = ',',encoding='unicode_escape')

# write a single row from the testfile into the api
#export = data.loc[2].to_json()
#response = requests.post(URL, data = export)
#print(response)

# write all the rows from the testfile to the api as put request
for i in data.index:
    try:
        # convert the row to json
        export = data.loc[i].to_json()

        #send it to the api
        response = requests.post(URL, data = export)

        # print the returncode
        print(export)
        print(response)
    except:
        print(data.loc[i])