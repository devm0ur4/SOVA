import eel
import sys
import os
from time import sleep

##inicia o GUI
def startGUI():
    eel.init('src/ui')
    eel.start(
            'index.html',
            size=(800, 800),
            port=8000,
            cmdline_args=['--window-size=800,800', '--disable-resize']
            )
    

##encerra o código
@eel.expose
def kill(message=None):
    if message is not None:
        updateStatus(message)
        sleep(3)
    else:
        updateStatus("ENCERRANDO O SISTEMA...")
        sleep(3)

        
    try:
        print("Encerrando o programa...")
        eel.closeWindow()
        sys.exit(0) 
    except SystemExit:
        os._exit(0) 
    except Exception as e:
        print(f"Error in sys.exit or os._exit: {e}")

##pega as informações do frontend

@eel.expose
def setInputValue(value):
    global inputvalue
    inputvalue = value

@eel.expose
def updateStatus(text):
    eel._updateStatus(text)

@eel.expose
def updateOrder(text):
    eel._updateOrder(text)

@eel.expose
def waitForUserInput():
    global inputvalue
    inputvalue = None
    eel.sendText()
    updateStatus("Aguardando input do usuario...")
    while inputvalue is None:
        sleep(1)
    updateStatus(f"Input do usuario recebido: {inputvalue}")
    return inputvalue

@eel.expose
def waitForOkButton(message=None):
    if message is None:
        updateOrder("Aguardando o usuário apertar o botão OK.")
    else:
        updateOrder(message)

    global ok_pressed
    ok_pressed = False
    eel.waitForOk()  
    while not ok_pressed:
        sleep(1)

    updateOrder("Aguarde mais instruções...")
    updateStatus("Botão OK pressionado. Continuando...")

@eel.expose
def setOkPressed():
    global ok_pressed
    ok_pressed = True
