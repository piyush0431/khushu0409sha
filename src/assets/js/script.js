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
    const response = await fetch('https://raw.githubusercontent.com/piyush0431/khushu0409sha/main/src/assets/json/hashed.json');
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
    const response = await fetch('https://raw.githubusercontent.com/piyush0431/khushu0409sha/main/src/further/user.json');
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

async function handmadeSplit(x) {
    const elements = [];
    let element = '';
    for (const char of x) {
        if (char === ' ') {
            elements.push(element);
            element = '';
        } else {
            element += char;
        }
    }
    if (element) {
        elements.push(element);
    }
    return elements;
}

async function unhashData(x) {
    let result = '';
    const response = await fetch('https://raw.githubusercontent.com/piyush0431/khushu0409sha/main/src/assets/json/hashed.json');
    const data = await response.json();

    const elements = await handmadeSplit(x);
    console.log(elements);
    for (const element of elements) {
        for (const category in data) {
            for (const [key, value] of Object.entries(data[category])) {
                if (String(value['data']) === element || value['hash'] === element) {
                    result += key;
                }
            }
        }
    }
    return result;
}

// Usage
const x = "UxluN-H@gt*1|<[=>vm`M#=ZOQG`]i40vf|*b&EX=u:T`v4OCn~SmX8/JY0.|mm2#@)T[~;DXnrO(:og;o(dSRFzfJl!$:`FD-&. 51~uy(!xS_~?OsHs%;%TI:`}Y5Ft9e*o)^Ba0MDZZHmoFkW{rFR$.`n-?f$Nxd%5+y33y[F]G5MeG*n>|:9|*Gel-Izdma9q?Rt[ Q;bgM+;?4VB%:7Hcwkiou*aDk~zL5t[hV:8=K9/F,790y(+3~]sY-X^4F<b)u#7[HDEO6S$@YOfN7De,8n`0e|DRk7O?`LJqm_vX |qRZ9zCH+hle:nwT>~coWjo)AVib,?%]D_@c%](cT..7R&+as&yMy|t)^!vwyvB4LZ=+;79l6XFR5gCW+5noh^s(O__(a=,&IiYh =Wg`*zkkGEu1~D0J!rh^YEaepM%pYn*)R/WFP]Ij^KDT$rDn*x9oT-,LAxZT.e#|;}k$]s-v0xVjbll*ABr+:~_bS{5N^5#uRI,f |qRZ9zCH+hle:nwT>~coWjo)AVib,?%]D_@c%](cT..7R&+as&yMy|t)^!vwyvB4LZ=+;79l6XFR5gCW+5noh^s(O__(a=,&IiYh Q;bgM+;?4VB%:7Hcwkiou*aDk~zL5t[hV:8=K9/F,790y(+3~]sY-X^4F<b)u#7[HDEO6S$@YOfN7De,8n`0e|DRk7O?`LJqm_vX |qRZ9zCH+hle:nwT>~coWjo)AVib,?%]D_@c%](cT..7R&+as&yMy|t)^!vwyvB4LZ=+;79l6XFR5gCW+5noh^s(O__(a=,&IiYh >J_SB.nn?5-o{&D:kAqI2[>DVJa=L/9_s`d`;t*zsIiN^gsRkt<l|:G~rI-s1a{c!tZx{vAGtuq3(4).[`c##@,`U9,0nSXslO8{ ";
unhashData(x).then(result => console.log(result));