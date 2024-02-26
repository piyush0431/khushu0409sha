# import joblib
# import json

# # Load data from JSON file
# with open('user.json', 'r') as json_file:
#     data = json.load(json_file)

# # Save data to joblib file
# joblib.dump(data, 'hashed.joblib')


import joblib, json

# Load user data from joblib file
try:
    userData = json.dumps(joblib.load('hashed.joblib'), indent=2)
    hashData = json.dumps(joblib.load('hashed-data.joblib'), indent=2)
    print(userData)
except FileNotFoundError:
    userData = []  # If the file doesn't exist yet
def letterCheck(letter):
    if letter in [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]:
        return 1
    if letter in [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]:
        return 2
    if letter in [
        "!",
        "\\",
        "@",
        "#",
        "$",
        "%",
        "^",
        "&",
        "*",
        "(",
        ")",
        "-",
        "_",
        "+",
        "=",
        "{",
        "}",
        "[",
        "]",
        ":",
        ";",
        "'",
        '"',
        "<",
        ">",
        ",",
        ".",
        "?",
        "/",
    ]:
        return 3
    if letter in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        return 4


def hash_pass(word: str, serial: int):
    garbage = ""
    for item in word:
        che = letterCheck(item)
        if serial == 1:
            if che == 4:
                garbage += hashData["numerics"][item]["hash"] + " "
            if che == 3:
                garbage += hashData["spec_chrs"][item]["hash"] + " "
            if che == 2:
                garbage += hashData["alphabets_caps"][item]["hash"] + " "
            if che == 1:
                garbage += hashData["alphabets_sml"][item]["hash"] + " "

        if serial == 2:
            if che == 4:
                garbage += str(hashData["numerics"][item]["data"]) + " "
            if che == 3:
                garbage += str(hashData["spec_chrs"][item]["data"]) + " "
            if che == 2:
                garbage += str(hashData["alphabets_caps"][item]["data"]) + " "
            if che == 1:
                garbage += str(hashData["alphabets_sml"][item]["data"]) + " "

    return garbage

def search_user(user):
    found_pass = 0
    found_key = 0
    hashedPass = hash_pass(user, 1)
    hashedKey = hash_pass(user, 2)
    position = 0
    i = 0
    while i < len(userData):  
        if userData[i]["password_hash"] == hashedPass:
            found_pass += 1
            if userData[i]["security_number"] == str(hashedKey):
                found_key += 1
                position = i
        i += 1  

    if found_pass == 1 and found_key == 1:
        print(
            f"Hi {userData[position]['name']}!!"
        )  
    else:
        print("User not found!!")

# Now you can use the search_user function
username_to_search = "123"
search_user(username_to_search)

""" 
khushuuuu
123
khu641
"""