import requests
import pandas as pd
city=input("Enter Your City : ")
APIKey='599d55b51f11471c93963600241205'
url=f'http://api.weatherapi.com/v1/current.json?key={APIKey}&q={city}'

response=requests.get(url)
json_data=response.json()
if 'error' in json_data:
    print(json_data['error']['message'])
else:
    data=pd.json_normalize(json_data)
    csv_data=data.to_csv(index=False)
    print(csv_data)