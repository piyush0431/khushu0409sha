function letterCheck(letter) {
    const lowerCaseLetters = "abcdefghijklmnopqrstuvwxyz";
    const upperCaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const specialCharacters = "!\\@#$%^&*()-_+={}[]:;\"<>,.?/";
    const digits = "0123456789";

    if (lowerCaseLetters.includes(letter)) {
        return 1;
    }
    if (upperCaseLetters.includes(letter)) {
        return 2;
    }
    if (specialCharacters.includes(letter)) {
        return 3;
    }
    if (digits.includes(letter)) {
        return 4;
    }
}

async function fetchData() {
    const response = await fetch('hashed.json');
    const hashData = await response.json();
    return hashData;
}

async function hash_pass(word, serial) {
    const hashData = await fetchData();
    let garbage = "";

    for (const item of word) {
        const che = letterCheck(item);

        if (serial === 1) {
            if (che === 4) {
                garbage += hashData["numerics"][item]["hash"] + " ";
            }
            if (che === 3) {
                garbage += hashData["spec_chrs"][item]["hash"] + " ";
            }
            if (che === 2) {
                garbage += hashData["alphabets_caps"][item]["hash"] + " ";
            }
            if (che === 1) {
                garbage += hashData["alphabets_sml"][item]["hash"] + " ";
            }
        }

        if (serial === 2) {
            if (che === 4) {
                garbage += hashData["numerics"][item]["data"] + " ";
            }
            if (che === 3) {
                garbage += hashData["spec_chrs"][item]["data"] + " ";
            }
            if (che === 2) {
                garbage += hashData["alphabets_caps"][item]["data"] + " ";
            }
            if (che === 1) {
                garbage += hashData["alphabets_sml"][item]["data"] + " ";
            }
        }
    }

    return garbage;
}

async function fetchUserData() {
    const response = await fetch('user.json');
    const userData = await response.json();
    return userData;
}

async function search_user(user) {
    const userData = await fetchUserData();
    let found_pass = 0;
    let found_key = 0;

    const [hashedPass, hashedKey] = await Promise.all([
        hash_pass(user, 1),
        hash_pass(user, 2)
    ]);
    let position = 0;
    let i = 0;
    while (i < userData.length) {
        if (hashedPass === userData[i]["password_hash"]) {
            found_pass += 1;
            if (userData[i]["security_number"] == hashedKey) {
                found_key += 1;
                position = i;
            }
        }
        i += 1;
    }

    if (found_pass === 1 && found_key === 1) {
        console.log(`Hi ${userData[position]['name']}!!`);
    } else {
        console.log("User not found!!");
    }
}


let x = prompt('pass:')
search_user(x)