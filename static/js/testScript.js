// Single line comment

/* This is multi line comment 
you can comment many line as you want*/

var a = "10"; // string
var b = "20"; // string
var result = a + b
var newA = 10; // number
var newB = 20; // number
var result2 = newA + newB;
console.log("Total1:",result)
console.log("Total2:",result2)

// loop
for (let i = 1; i <= 10; i += 2) {
    console.log("Loop is Running")
    console.log(i)
}

// Create a function
function getNum() {
    var val1 = 50;
    var val2 = 40;
    var result = val1 - val2;
    console.log("result is:", result)
}

// Call a function
getNum();

function myFunc1() {
    document.getElementById("id1").innerHTML = "Change to STACKPYTHON";
}

function myFunc2() {
    document.getElementById("id2").style.fontSize = "140px"
}

// conditional statement and function
function myFunc3() {
    var msg;
    if(confirm("You must click OK to continue or CANCEL to cancel")) {
        msg = "You press OK"
    }
    else {
        msg = "You pressed CANCEL"
    }
    document.getElementById("id3").innerHTML = msg;
}
