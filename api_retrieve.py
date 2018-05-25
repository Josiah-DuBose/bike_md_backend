import requests
import json
import psycopg2

# DB connect and cursor.
try:
    conn = psycopg2.connect("dbname='bmd' user='' host='localhost' password=''")
except:
    print("I am unable to connect to the database")
cur = conn.cursor()


#URLs
baseURLmodels = "https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeIdYear/"
# Concat the rest the URL like this.
# makeId/474/modelyear/2015/vehicleType/Motorcycle?format=json
URLmakes = "https://vpic.nhtsa.dot.gov/api/vehicles/GetMakesForVehicleType/Motorcycle?format=json"



#Retrieve makes and store them in a list.
all_makes = requests.get(URLmakes)
make_response_array = all_makes.json()["Results"]
makes = []

for make in make_response_array:
    makes.append(make["MakeName"])

makes.sort()
# print(makes)

