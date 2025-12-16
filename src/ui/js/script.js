eel.expose(sendText);
function sendText(){
    let text = document.getElementById("input");
    let button = document.getElementById("send");

    text.disable = false;
    button.disable = false;

    text.focus();

    button.addEventListener("click", () => {
         if (text.value.trim() !== ""){
            eel.setInputValue(text.value);
         } else {
            alert("Por favor, insira um valor válido.");
         }
    });

    text.value = "";
    text.disable = true;
    button.disable = true;
}

eel.expose(closeWindow);
function closeWindow(){
    window.close();
}

function kill(){ 
    eel.kill(); 
}

eel.expose(_updateStatus);
function _updateStatus(text){
    let status = document.getElementById("status");
    status.innerHTML += '<br><p><a class="_SOVA">SOVA</a> <i class="bi bi-chevron-right"></i> ' + text + '</p>';
    status.scrollTop = status.scrollHeight;
}

eel.expose(_updateOrder);
function _updateOrder(text){
    let order = document.getElementById("order-text");
    order.innerText = text;
}

eel.expose(waitForOk);
function waitForOk() {
    let button = document.getElementById("ok"); 
    button.disabled = false;
    button.addEventListener("click", () => {
        eel.setOkPressed();
        button.disabled = true;
    });
}

