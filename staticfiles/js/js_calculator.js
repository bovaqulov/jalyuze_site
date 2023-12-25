
var clickCount = 0;


function multiplyNumbers() {
    // var prise = parseInt(document.getElementById('prises1').value);
    var number1 = parseFloat(document.getElementById('number1').value);
    var number2 = parseFloat(document.getElementById('number2').value);
    var number3 = parseFloat(document.getElementById('number3').value);
    if (number3 <= 0) {
        var result = number1 + number2
    } else
        var result = (number1 + number2) * number3;
    if (result > 0) {
        document.getElementById('result').innerText = 'Umumiy Hisobi: ' + (result * 5000) + ' so\'m';

        if (clickCount < 1) {
            var originalButton = document.getElementById("result");
            var newButton = document.createElement("button");
            var buttonText = document.createTextNode("Buyurtma berish");
            newButton.appendChild(buttonText);

            var container = originalButton.parentNode;
            container.appendChild(newButton);
            newButton.classList.add("glow-on-hover");
            originalButton.disabled = true;
            clickCount++;

        }
    } else {
        document.getElementById('result').innerText = 'Iltimos Barcha maydonlarni to\'ldiring';

    }

}