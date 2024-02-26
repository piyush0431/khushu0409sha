import random
import string
import json

def generate_random_data():
    return random.randint(10**12, 10**13 - 1)

def generate_random_hash():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(100)).replace("\\", ":").replace("\"", "*").replace(" ", "5")

def generate_alphabet_json(to_hash):
    alphabet_json = {}
    for letter in to_hash:
        data_value = generate_random_data()
        hash_value = generate_random_hash()
        alphabet_json[letter] = {
            "target": letter,
            "data": data_value,
            "hash": hash_value
        }

    return {"alphabets": alphabet_json}

def save_to_json_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    toHash = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # toHash = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    # toHash = ["!", "\\", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", ":", ";", "'", "\"", "<", ">", ",", ".", "?", "/"]
    # toHash = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = generate_alphabet_json(toHash)
    json_filename = "alphabet_sm.json"
    save_to_json_file(result, json_filename)
    print(f"Generated JSON data saved to {json_filename}")
