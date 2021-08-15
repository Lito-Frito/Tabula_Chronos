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
        "jewels" : "",
        "type (e.g. chronograph)" : "",
        "power reserve" : "",
        "water resistance (e.g. 5M)" : "",
        "warranty" : "",
        "retail value" : "",
        "accuracy" : ""
        }

case = {
        "case material" : "",
        "case diameter" : "",
        "case size (lug to lug)" : "",
        "case thickness" : "",
        "case crystal" : "",
        "crown"  : "",
        "bezel" :""
        }

dial = {
        "dial color" : "",
        "dial diameter" : "",
        "dial markers" : "",
        "dial/hands lume" : "",
}

band = {
        "strap/band material" : "",
        "clasp" : "",
        "width" : "",
}

features = {
        "Day complication (include language complications)?": "",
        "Date complication?": ""
}

def get_stats(stats):
    for attribute in stats:
        stats[attribute] = input(f"insert {attribute}: ")

    print("-" * 40)
    print("\nPrinting stats:")

    for key, value in stats.items():
        print(key, ":", value)

    no_mistakes = False
    while no_mistakes == False:
        check = input("\nIs the above correct (Y/N)?: ")
        if check == "Y" or check == "y":
            break
        if check == "N" or check == "n":
            return get_stats(stats)
        else:
            print("Please type Y or N.")


def get_case_stats(case):
    for attribute in case:
        case[attribute] = input(f"insert {attribute}: ")

    print("-" * 40)
    print("\nPrinting stats:")

    for key, value in case.items():
        print(key, ":", value)

    no_mistakes = False
    while no_mistakes == False:
        check = input("\nIs the above correct (Y/N)?: ")
        if check == "Y" or check == "y":
            break
        if check == "N" or check == "n":
            return get_case_stats(case)
        else:
            print("Please type Y or N.")


def get_dial_stats(dial):
    for attribute in dial:
        dial[attribute] = input(f"insert {attribute}: ")

    print("-" * 40)
    print("\nPrinting stats:")

    for key, value in dial.items():
        print(key, ":", value)

    no_mistakes = False
    while no_mistakes == False:
        check = input("\nIs the above correct (Y/N)?: ")
        if check == "Y" or check == "y":
            break
        if check == "N" or check == "n":
            return get_dial_stats(dial)
        else:
            print("Please type Y or N.")


def get_band_stats(band):
    for attribute in band:
        band[attribute] = input(f"insert {attribute}: ")

    print("-" * 40)
    print("\nPrinting stats:")

    for key, value in band.items():
        print(key, ":", value)

    no_mistakes = False
    while no_mistakes == False:
        check = input("\nIs the above correct (Y/N)?: ")
        if check == "Y" or check == "y":
            break
        if check == "N" or check == "n":
            return get_band_stats(band)
        else:
            print("Please type Y or N.")


def get_features(features):
    for feature in features:
        features[feature] = input(f"{feature}: ")

    print("-" * 40)
    print("\nPrinting stats:")

    for key, value in features.items():
        print(key, ":", value)

    no_mistakes = False
    while no_mistakes == False:
        check = input("\nIs the above correct (Y/N)?: ")
        if check == "Y" or check == "y":
            break
        if check == "N" or check == "n":
            return get_features(stats)
        else:
            print("Please type Y or N.")



get_stats(stats)
get_case_stats(case)
get_dial_stats(dial)
get_band_stats(band)
get_features(features)

stats.update(case)
stats.update(dial)
stats.update(band)
stats.update(features)

# Create json file and add stats
with open(f"{file_name}.json", "w") as write_file:
    json.dump(stats, write_file,indent=4)
