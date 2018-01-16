import csv

def load_brands(apps, schema_editor):
    with open("brand.csv", "r") as f:
        dict_reader = csv.DictReader(f, fieldnames= ['name'])
        Brand = apps.get_model("diag_app", "Brand")
        for row in dict_reader:
            brand_object = Brand(**row)
            brand_object.save()


def load_systems(apps, schema_editor):
    with open("system.csv", "r") as f:
        dict_reader = csv.DictReader(f, fieldnames= ['name'])
        System = apps.get_model("diag_app", "System")
        for row in dict_reader:
            system_object = System(**row)
            system_object.save()

def load_years(apps, schema_editor):
    with open("year.csv", "r") as f:
        dict_reader = csv.DictReader(f, fieldnames= ['name'])
        Year = apps.get_model("diag_app", "Year")
        for row in dict_reader:
            year = Year(**row)
            year.save()


def load_models(apps, schema_editor):
    with open("../migrate_data/model_year_id.csv", "r") as f:
        dict_reader = csv.DictReader(f, fieldnames= ['brand_id','name','year_id'])
        Model = apps.get_model("diag_app", "Model")
        for row in dict_reader:
            model_object = Model(**row)
            model_object.save()




operations = [
    migrations.RunPython(load_brands),
    migrations.RunPython(load_systems),
    migrations.RunPython(load_years),
    migrations.RunPython(load_models),
]
