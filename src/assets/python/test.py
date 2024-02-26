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


def unhashData(input_str):
    # Ensure input_str is a string, then split it into a list of hash values
    hashes = input_str.split()

    # Load the JSON data from data1.json
    with open('src\\assets\\json\\hashed.json', 'r') as file:
        data = json.load(file)

    result = ''
    
    # Iterate through the hash values and find corresponding keys in the JSON data
    for hash_value in hashes:
        for category, values in data.items():
            for key, value in values.items():
                if value['hash'] == hash_value or str(value['data']) == hash_value:
                    result += key

    return result

# Example usage:
# x = "aC=&aP>>5juK5DuqFUSNV_Y'CkuV5B|$XV/L;s^dmRVnl)c,}5Ly*+aO27N'3*8~2so;EowSR!?:ToKXyu`X%W*BLW4Bt:r2jZT: RD,(D4v#O]1zLKZ6SsRJfWl:GKBvT([ds9};Et*k;g$X+T}5o*FIE~HrgRDO.5gm):^It=/Z!K`b2,F!`[/O#M8Lyr*yk{0[+;8* 0)~t=n9k%-*!Q;ZJ-U?%`V*z4g>~5d?P!**Eawsx[h$5v=sm>tkD#Of']cd^-zFMIRuP)z!ZCY]'itbAQnEIx<OeiR_CyKVcKH2[ fx`4Ls,HcIKRNICO</|:!.G>1x;K0f=;xyM&`bdk,[N(4-JU?x#&pi(/4>K|NeS?P~FQn+I<5TFz*%U~`Z6Ms~NI:Kai+8&weFg` RD,(D4v#O]1zLKZ6SsRJfWl:GKBvT([ds9};Et*k;g$X+T}5o*FIE~HrgRDO.5gm):^It=/Z!K`b2,F!`[/O#M8Lyr*yk{0[+;8* 3.}9p(pworpDb~wHm?-L1x,6b,(.yq>MRXc$7gW?TBtpGd<he9D$Yu#t0NER4cCy<Cx35kL_1=_.r}T1)JDAzt>h@6n1s6$s`F1: ",
# # or 
# # x = hash_pass("khushi", 1)
# result = unhashData(x)
# print(result)
make_user_hash()
# make_user()