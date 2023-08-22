/**
 * Function to insert a Monty-Python image into the element with id "pythonTarget".
 * The image used is one of three, chosen based on which button was clicked to
 * call the function.  The button used is passed to the function as buttonElt.
 */
function insertPython(buttonElt) {
    let contents = '<p>Something different... blah blah blah...</p>';
    if (buttonElt.innerHTML === "Mario time!") {
        contents += '<img src="https://media1.giphy.com/media/ZdKa3AjRMS5vGZvxQW/giphy.gif" alt="MarioTime">';
    }
    else if (buttonElt.innerHTML === "Snake?") {
        contents += '<img src="https://media.tenor.com/8z6raUxggBwAAAAC/snake-metal.gif" alt="Snake!">';
    }
    else {
        contents += '<img src="https://media2.giphy.com/media/xUPOqo6E1XvWXwlCyQ/giphy.gif?cid=6c09b952swxo0bf9xsxnnkbx8os8ufrwcie5bydugo30sdc4&rid=giphy.gif&ct=g" alt="ThatsAll">';
    }

    let targetElt = document.getElementById('pythonTarget');
    pythonTarget.innerHTML = contents;
}

function findGCD(a, b) {
    while (b != 0) {
        let tmp = a;
        a = b;
        b = tmp % b;
    }
    return Math.abs(a);
}

// Function to get the parameters for the GCD calculation and display the result
function showGCD() {
    let num1 = parseInt(document.getElementById('num1').value);
    //console.log(num1);
    let num2 = parseInt(document.getElementById('num2').value);
    //console.log(num2);
    document.getElementById('GCDtarget').innerHTML = findGCD(num1, num2).toString();
}

/**
 * Function to create a multiplication table from 0 to maxValue and insert it into
 * the element timesTableTarget.
 * 
 * @param {*} maxValue 
 */
function timesTable(maxValue) {
    let tableString = '<table><thead><tr><th></th>';
    for (let i = 0; i <= maxValue; i++) {
        tableString += '<th>' + i.toString() + '</th>';
    }
    tableString += '</tr></thead><tbody>';

    for (let i = 0; i <= maxValue; i++) {
        tableString += '<tr><th>' + i.toString() + '</th>';
        for (let j = 0; j <= maxValue; j++) {
            tableString += '<td>' + (i*j).toString() + '</td>';
        }

        tableString += '</tr>';
    }


    tableString += '</tbody></table>';
    document.getElementById('timesTableTarget').innerHTML = tableString;
}