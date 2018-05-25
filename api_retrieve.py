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

cur.execute("SELECT * FROM diag_app_brand;")
print(cur.fetchall())



#Retrieve makes and store them in the DB.
all_makes = requests.get(URLmakes)
make_response_array = all_makes.json()["Results"]

# cur.execute("""TRUNCATE TABLE diag_app_model RESTART IDENTITY CASCADE;""")
for make in make_response_array:
    name = make["MakeName"]
    sql = """INSERT INTO diag_app_brand (name) VALUES ('%s');""" % name
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print(e.pgerror)
        
    conn.commit()

