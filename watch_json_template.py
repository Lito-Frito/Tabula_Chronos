import json

# Name for json file to be created
file_name = input("List brand and AKA (e.g. Aquacy_BronzeBond) for file name: ")

# Sample attributes in future DB
stats = {
        "name or aka" : "",
        # "brand" : "",
        # "model": "",
        # "movement" :"",
        # "caliber" : "",
        # "jewels" : "",
        # "type (e.g. chronograph)" : "",
        # "power reserve" : "",
        # "water resistance (e.g. 5M)" : "",
        # "warranty" : "",
        # "retail value" : "",
        }

case = {
        "case material" : "",
        # "case diameter" : "",
        # "case size (lug to lug)" : "",
        # "case thickness" : "",
        # "case crystal" : "",
        # "crown"  : "",
        }

dial = {
        "color" : "",
        "diameter" : "",
        "markers" : "",
        "lume" : "",
}

band = {
        "strap/band material" : "",
        "clasp" : "",
        "width" : "",
}

def get_stats(stats):
    for attribute in stats:
        stats[attribute] = input(f"insert {attribute}: ")

def get_case_stats(case):
    for attribute in case:
        case[attribute] = input(f"insert {attribute}: ")

get_stats(stats)
get_case_stats(case)
stats.update(case)
print(stats)    

# # To limit user error
# no_mistakes = False
# while no_mistakes == False:
#     # Create a loop that renames lines in JSON file based on user input
#     for attribute in stats:
#         stats[attribute] = input(f"insert {attribute}: ")
#
#     # Have user dbl chk
#     print(stats)
#     all_good = eval(input("Is this correct (write True or False)?: "))
#     if all_good == True or all_good == 'T':
#         no_mistakes = True
#     else:
#         all_good = False
#         no_mistakes = False



# Create json file and add stats
with open(f"{file_name}.json", "w") as write_file:
    json.dump(stats, write_file,indent=4)



# # Add case
# with open(f"{file_name}.json", "w") as write_file:
#     json.dump(case, write_file,indent=4)
