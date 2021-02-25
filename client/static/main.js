

var ws = new WebSocket("ws://127.0.0.1:8765/")

function newMessage() {
    var message = document.createElement("li");
    var messageValue = document.getElementById("message").value;
    var content = document.createTextNode(messageValue);
    message.appendChild(content);
    if (messageValue === '') {
        alert("You must write something!");
    } else {
        document.getElementById("chatUL").appendChild(message);
        ws.send(messageValue);
    }
    document.getElementById("message").value = "";
}

ws.onmessage = function (event) {
    var message = document.createElement("li");
    message.className = 'botLI'
    var content = document.createTextNode(event.data);
    message.appendChild(content);
    document.getElementById("chatUL").appendChild(message);
};
