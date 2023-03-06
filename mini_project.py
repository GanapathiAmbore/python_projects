import requests
import pandas as pd
url = 'http://universities.hipolabs.com/search?country=United+States'
response = requests.get(url)
result = response.json()
data = []
for each in result:
    output = {}
    output["state_province"]=each['state-province']
    output["domains"] = each['domains'][0]
    output["country"]=each['country']
    output["web_pages"]=each['web_pages'][0]
    output["name"]=each['name']
    output["alpha_two_code"]=each['alpha_two_code']
    data.append(output)
df = pd.DataFrame(data)
df.to_csv("university.csv")

