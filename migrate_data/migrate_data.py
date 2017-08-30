import csv

# def load_brands(apps, schema_editor):
#     with open("brand.csv", "r") as f:
#         dict_reader = csv.DictReader(f, fieldnames= ['name'])
#         Brand = apps.get_model("diag_app", "Brand")
#         for row in dict_reader:
#             brand_object = Brand(**row)
#             brand_object.save()
#
#
# def load_systems(apps, schema_editor):
#     with open("system.csv", "r") as f:
#         dict_reader = csv.DictReader(f, fieldnames= ['name'])
#         System = apps.get_model("diag_app", "System")
#         for row in dict_reader:
#             system_object = System(**row)
#             system_object.save()


def load_models(apps, schema_editor):
    with open("../migrate_data/models.csv", "r") as f:
        dict_reader = csv.DictReader(f, fieldnames= ['brand','name','year'])
        Model = apps.get_model("diag_app", "Model")
        for row in dict_reader:
            model_object = Model(**row)
            model_object.save()




operations = [
    # migrations.RunPython(load_brands),
    # migrations.RunPython(load_systems),
    migrations.RunPython(load_models),
]
