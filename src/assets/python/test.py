import random
import json


# necessary functions
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


class autogen:
    def username(name):
        name = name
        if len(name) >= 3:
            name = name[:3]
            num = str(random.randint(100, 999))
            name = name + num
        return name


with open("src\\assets\\json\\hashed.json", "r") as file:
    hashData = json.load(file)


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


def make_user():
    # take input
    personName = input("Enter Name: ")
    pas = input("Enter Password: ")
    personEmail = input("Enter Email: ")

    # auto generated
    hash = hash_pass(pas, 1)
    hashNumber = hash_pass(pas, 2)
    personUsername = autogen.username(personName)

    with open("user.json", "a+") as file:
        user_data = {
            "name": personName,
            "password": pas,
            "email": personEmail,
            "username": personUsername,
            "security_number": hashNumber,
            "password_hash": hash,
        }
        file.seek(0)
        try:
            existing_data = json.load(file)
        except json.decoder.JSONDecodeError:
            existing_data = []

        existing_data.append(user_data)

        file.seek(0)
        file.truncate()
        json.dump(existing_data, file, indent=4)
        file.write("\n")

try:
    with open("user.json", "r") as f1:
        userData = json.load(f1)
except Exception:
    pass


def search_user(user):
    found_pass = 0
    found_key = 0
    hashedPass = hash_pass(user, 1)
    hashedKey = hash_pass(user, 2)
    position = 0
    i = 0
    while i < len(userData):  # Fix: Ensure the loop doesn't run indefinitely
        if userData[i]["password_hash"] == hashedPass:
            found_pass += 1
            if userData[i]["security_number"] == hashedKey:
                found_key += 1
                position = i
        i += 1  # Fix: Increment the loop counter

    if found_pass == 1 and found_key == 1:
        print(
            f"Hi {userData[position]['name']}!!"
        )  # Fix: Print user's name instead of password hash
    else:
        print("User not found!!")


def make_user_hash():
    # take input
    personName = input("Enter Name: ")
    pas = input("Enter Password: ")

    # auto generated
    hash = hash_pass(pas, 1)
    hashNumber = hash_pass(pas, 2)
    personUsername = autogen.username(personName)

    with open("user.json", "a+") as file:
        user_data = {
            "name": hash_pass(personName, 1),
            "username": personUsername,
            "security_number": hashNumber,
            "password_hash": hash,
        }
        file.seek(0)
        try:
            existing_data = json.load(file)
        except json.decoder.JSONDecodeError:
            existing_data = []

        existing_data.append(user_data)

        file.seek(0)
        file.truncate()
        json.dump(existing_data, file, indent=4)
        file.write("\n")

import json

def handmade_split(x):
    elements = []
    element = ''
    for char in x:
        if char == ' ':
            elements.append(element)
            element = ''
        else:
            element += char
    if element:
        elements.append(element)
    return elements


def unhashData(x, data):
    result = ''
    x = handmade_split(x)
    for element in x:
        for category in data:
            for key, value in data[category].items():
                if str(value['data']) == element or value['hash'] == element:
                    result += key
    return result


x = "UxluN-H@gt*1|<[=>vm`M#=ZOQG`]i40vf|*b&EX=u:T`v4OCn~SmX8/JY0.|mm2#@)T[~;DXnrO(:og;o(dSRFzfJl!$:`FD-&. 51~uy(!xS_~?OsHs%;%TI:`}Y5Ft9e*o)^Ba0MDZZHmoFkW{rFR$.`n-?f$Nxd%5+y33y[F]G5MeG*n>|:9|*Gel-Izdma9q?Rt[ Q;bgM+;?4VB%:7Hcwkiou*aDk~zL5t[hV:8=K9/F,790y(+3~]sY-X^4F<b)u#7[HDEO6S$@YOfN7De,8n`0e|DRk7O?`LJqm_vX |qRZ9zCH+hle:nwT>~coWjo)AVib,?%]D_@c%](cT..7R&+as&yMy|t)^!vwyvB4LZ=+;79l6XFR5gCW+5noh^s(O__(a=,&IiYh =Wg`*zkkGEu1~D0J!rh^YEaepM%pYn*)R/WFP]Ij^KDT$rDn*x9oT-,LAxZT.e#|;}k$]s-v0xVjbll*ABr+:~_bS{5N^5#uRI,f |qRZ9zCH+hle:nwT>~coWjo)AVib,?%]D_@c%](cT..7R&+as&yMy|t)^!vwyvB4LZ=+;79l6XFR5gCW+5noh^s(O__(a=,&IiYh Q;bgM+;?4VB%:7Hcwkiou*aDk~zL5t[hV:8=K9/F,790y(+3~]sY-X^4F<b)u#7[HDEO6S$@YOfN7De,8n`0e|DRk7O?`LJqm_vX |qRZ9zCH+hle:nwT>~coWjo)AVib,?%]D_@c%](cT..7R&+as&yMy|t)^!vwyvB4LZ=+;79l6XFR5gCW+5noh^s(O__(a=,&IiYh >J_SB.nn?5-o{&D:kAqI2[>DVJa=L/9_s`d`;t*zsIiN^gsRkt<l|:G~rI-s1a{c!tZx{vAGtuq3(4).[`c##@,`U9,0nSXslO8{ "

result = unhashData(x, hashData)
print(result)