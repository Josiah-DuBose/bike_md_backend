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


def getURL(**args):
    """Return URL for given action and params"""
    #Instantiate url string
    url = ''

    if (args["action"] == "makes"):
        url="https://vpic.nhtsa.dot.gov/api/vehicles/GetMakesForVehicleType/Motorcycle?format=json"
    if (args["action"] == "models"):
        url = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeyear/make"

    return url


def tableCleanUp(**args):
    conn = args["conn"]
    cur = conn.cursor()

    #Remove old records and Truncate IDs
    sql = """TRUNCATE TABLE {} RESTART IDENTITY CASCADE;""".format(args["name"])
    cur.execute(sql)
    conn.commit()


def updateModels(makes):
    print("updateModels")
    ###Retrieve models and store them in the DB###

    #DB connect and cursor creation
    conn = dbConnect()
    cur = conn.cursor()

    #DB house keeping
    tableCleanUp(conn=conn, name="diag_app_model")

    #Get all the years from the DB
    cur.execute("""SELECT * from diag_app_year;""")
    rows = cur.fetchall()

    baseURL = getURL(action="models")
    for row in rows:
        for make in makes:
            #Get all models for each make
            models = []
            try:
                #Build URL and make request 
                url = "{}/{}/modelyear/{}?format=json".format(baseURL,make["brand"],row[1])
                # print("ULR: {}").format(url)
                response = requests.get(url)

                #Skip if no models or less then 5  models found for make
                if (response.json()["Count"] == 0 or response.json()["Count"] < 5): 
                    continue

                #Terminal output
                print("Year: {} adding {} models for {}".format(row[1], response.json()["Count"], make["brand"]))
                models = response.json()["Results"]

            except:
                continue

            #Insert all models for make into DB
            for model in models:
                name = model["Model_Name"]

                #If we get a really long name move on to the next iteration 
                if (len(name) > 20):
                    continue

                #Clean up name
                clean_name = re.sub('\'', '', name)

                #Insert into DB
                sql = """INSERT INTO diag_app_model (name, brand_id, year_id) 
                VALUES ('{}', '{}', '{}')""".format(clean_name, make["id"], row[0])
                try:
                    cur.execute(sql)
                except psycopg2.Error as e:
                    print(e.pgerror)
                conn.commit() 

def updateMakes():
    ###Retrieve makes and store them in the DB###

    #DB connect and cursor creation
    conn = dbConnect()
    cur = conn.cursor()

    all_makes = {}
    make_response_array = []

    #Call external API for current make data
    try:
        all_makes = requests.get(getURL(action="makes"))
        make_response_array = all_makes.json()["Results"]
    except:
        print(all_makes)

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
        
        #If we get a really long name or name shorter then 3 move on to the next iteration 
        if (len(clean_name) > 15 or len(clean_name) < 3):
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

