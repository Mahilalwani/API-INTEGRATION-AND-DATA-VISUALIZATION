# Important libraries to be imported for data visualization and api integration
import requests
import matplotlib.pyplot as plt
import datetime

#Api settings 
API_KEY="f828147b9ce7430208266407c9dbff76" #from openweathermap
CITY="Indore"
URL=f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&units=metrics&appid={API_KEY}"

#fetch data
response=requests.get(URL)
data=response.json()

#using datetime library to fetch time and date details
timestamps=[datetime.datetime.fromtimestamp(entry["dt"]) for entry in data["list"]]
temperature=[entry["main"]["temp"] for entry in data ["list"]]

#plot
plt.figure(figsize=(10,5))
plt.plot(timestamps,temperature,marker='o',linestyle="-",color="b", label="Temperature(deg F)")
plt.xlabel("Date and time")
plt.ylabel("Temperature(deg F)")
plt.title(f"Temperature forecast for {CITY}")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()