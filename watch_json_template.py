import json

# Name for json file to be created
file_name = input("List brand and AKA (e.g. Aquacy_BronzeBond) for file name: ")

# Sample attributes in future DB
stats = {
        "name or aka" : "",
        "brand" : "",
        "model": "",
        "movement" :"",
        "caliber" : "",
        "type" : "",
        "materials": {
                "case": "",
                "crystal": "",
                "strap/band" : ""
                }
        }

# To limit user error
no_mistakes = False
while no_mistakes == False:
    for attribute in stats:
        stats[attribute] = input(f"insert {attribute}: ")

        if attribute == stats["materials"]:
            for material in materials["materials"]:
                materials[material] = input(f"insert {materials}: ")

    print(stats)
    all_good = eval(input("Is this correct (write True or False)?: "))
    if all_good == True:
        no_mistakes = True

# Create json file
data = stats
with open(f"{file_name}.json", "w") as write_file:
    json.dump(data, write_file,indent=4)
