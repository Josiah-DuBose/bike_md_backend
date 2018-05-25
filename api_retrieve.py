import requests
import json
import psycopg2
import re

def dbConnect():
    # DB connect and cursor.
    try:
        conn = psycopg2.connect("dbname='bmd' user='' host='localhost' password=''")
    except:
        print("I am unable to connect to the database")
    return conn


def getURLs(**args):
    print("getURLs")
    print(args)
    """Return URL for given action and params"""
    #Instantiate url string
    url = ''
    if (args["action"] == "makes"):
        url="https://vpic.nhtsa.dot.gov/api/vehicles/GetMakesForVehicleType/Motorcycle?format=json"
    if (args["action"] == "models"):
        url = "https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeIdYear/"

    return url


def tableCleanUp(**args):
    conn = args["conn"]
    cur = conn.cursor()

    #Remove old records and Truncate IDs
    sql = """TRUNCATE TABLE {} RESTART IDENTITY CASCADE;""".format(args["name"])
    cur.execute(sql)
    conn.commit()


def updateModels(brands):
    ###Retrieve models and store them in the DB###

    #DB connect and cursor creation
    conn = dbConnect()
    cur = conn.cursor()


def updateMakes():
    ###Retrieve makes and store them in the DB###

    #DB connect and cursor creation
    conn = dbConnect()
    cur = conn.cursor()

    #Call external API for current make data
    all_makes = requests.get(getURLs(action="makes"))
    make_response_array = all_makes.json()["Results"]

    #DB house keeping
    tableCleanUp(conn=conn, name="diag_app_brand")

    #Makes array for call to get models
    makes = []

    #Perform insert for each Make retrieved from API
    for make in make_response_array:
        name = make["MakeName"]
        makeID = make["MakeId"]

        #Clean up name
        clean_name = re.sub('\'', '', name)
        
        #If we get a really name move on to the next iteration 
        if (len(clean_name) > 15):
            continue

        #Build statement and insert 
        sql = """INSERT INTO diag_app_brand (name, make_id) VALUES ('{}', '{}');""".format(clean_name, makeID)
        try:
            cur.execute(sql)
            # Add make to makes array
            makes.append({"brand": clean_name, "id": makeID})
        except psycopg2.Error as e:
            print(e.pgerror)
        conn.commit()
    
    #Update models for the brands retrieved
    updateModels(makes)

    #Close cursor and DB connection 
    cur.close()
    conn.close()


def main():
    updateMakes()

if __name__ == "__main__":
    main()

