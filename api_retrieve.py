import requests
import json
import psycopg2
import re

###
# Retrieve all brands and models from https://vpic.nhtsa.dot.gov/api/
# and insert in the database. Will delete any brands that do not currently 
# have models, or do no meet the name requirements.
###

def dbConnect():
    # Return DB connection and cursor.
    try:
        conn = psycopg2.connect("dbname='bmd' user='' host='localhost' password=''")
    except:
        print("I am unable to connect to the database")
    return (conn, conn.cursor())


def getURL(action):
    """Return URL for given action"""
    #Instantiate url string
    url = ''

    if (action == "makes"):
        url="https://vpic.nhtsa.dot.gov/api/vehicles/GetMakesForVehicleType/Motorcycle?format=json"
    if (action == "models"):
        url = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeyear/make"

    return url


def tableCleanUp(name):
    #DB connect and cursor creation
    conn, cur = dbConnect()

    #Remove all old records and Truncate ID
    sql = """TRUNCATE TABLE {} RESTART IDENTITY CASCADE;""".format(name)
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print(e.pgerror)
    print("{} cleared and id sequence re-set.".format(name))
    conn.commit()


def cleanUpBrands(makes):
    #DB connect and cursor creation
    conn, cur = dbConnect()

    #Remove unneeded brands from DB.
    for make in makes:
        sql = """DELETE FROM diag_app_brand WHERE name='{}';""".format(make)
        print("delete", sql)
        cur.execute(sql)
        conn.commit()


def updateModels():
    ###Retrieve models and store them in the DB###

    #DB connect and cursor creation
    conn, cur = dbConnect()

    #DB house keeping
    tableCleanUp("diag_app_model")

    #Get all the years from the DB
    cur.execute("""SELECT * from diag_app_year;""")
    years = cur.fetchall()

    #Get all makes from the DB.
    cur.execute("""SELECT * from diag_app_brand""")
    makes = cur.fetchall()

    baseURL = getURL("models")
    brand_to_remove = []
    for year in years:
        for make in makes:
            #Get all models for each make
            models = []
            try:
                #Build URL and make request 
                url = "{}/{}/modelyear/{}?format=json".format(baseURL,make[1],year[1])
                model_response = requests.get(url)

                #Skip if no models or less then 5  models found for make
                if (model_response.json()["Count"] == 0 or model_response.json()["Count"] < 5):
                    brand_to_remove.append(make[1])
                    continue

                #Terminal output
                print("Year: {} adding {} models for {}".format(year[1], model_response.json()["Count"], make[1]))
                models = model_response.json()["Results"]

            except:
                continue

            #Insert all models for make into DB
            for model in models:
                name = model["Model_Name"]

                #If we get a name longer then 20, move on to the next iteration 
                if (len(name) > 20):
                    continue

                #Clean up name
                clean_name = re.sub('\'', '', name)

                #Insert into DB
                sql = """INSERT INTO diag_app_model (name, brand_id, year_id) 
                VALUES ('{}', '{}', '{}')""".format(clean_name, make[0], year[0])
                try:
                    cur.execute(sql)
                except psycopg2.Error as e:
                    print(e.pgerror)
                conn.commit()

    #Remove any brands that don't have models in the DB
    cleanUpBrands(brand_to_remove)
    

def updateMakes():
    ###Retrieve makes and store them in the DB###

    #DB connect and cursor creation
    conn, cur = dbConnect()

    all_makes = {}
    make_response_array = []

    #Call external API for current make data
    try:
        all_makes = requests.get(getURL("makes"))
        make_response_array = all_makes.json()["Results"]
    except:
        print(all_makes)

    #DB house keeping
    tableCleanUp("diag_app_brand")

    #Perform insert for each Make retrieved from API
    for make in make_response_array:
        name = make["MakeName"]
        makeID = make["MakeId"]

        #Clean up name
        clean_name = re.sub('\'', '', name)
        
        #If we get a really long name or name shorter then 3 move on to the next iteration
        allowed_three_chars = ["KTM", "BMW", "ATK"]
        if (len(clean_name) > 15 or (len(clean_name) <= 3 and clean_name not in allowed_three_chars)):
            continue

        #Build statement and insert 
        sql = """INSERT INTO diag_app_brand (name, make_id) VALUES ('{}', '{}');""".format(clean_name, makeID)
        try:
            cur.execute(sql)
        except psycopg2.Error as e:
            print(e.pgerror)
        conn.commit()
    
    #Update models for the brands retrieved
    updateModels()

    #Close cursor and DB connection 
    cur.close()
    conn.close()


def main():
    updateMakes()

if __name__ == "__main__":
    main()

