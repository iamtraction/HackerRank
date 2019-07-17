'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(str => str.trim());

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the timeConversion function below.
 */
function timeConversion(s) {
    /*
     * Write your code here.
     */
    let hour = parseInt(s.substr(0, 2));
    if (s.endsWith("PM")) {
        let newHour = hour < 12 ? hour + 12 : hour;
        hour = hour < 10 ? "0" + hour : hour;
        s = s.replace(hour, newHour);
    } else {
        if (hour == 12) s = s.replace(hour, "00");
    }
    s = s.replace(/[AP]M/, "");
    return s;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const s = readLine();

    let result = timeConversion(s);

    ws.write(result + "\n");

    ws.end();
}
