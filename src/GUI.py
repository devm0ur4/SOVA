import eel
import sys
import os

##inicia o GUI

def startGUI():

    eel.init('src/ui')
    eel.start(
            'index.html',
            size=(700, 600),
            port=3636,
            cmdline_args=['--window-size=700,600', '--disable-resize']
            )

##encerra o código

def kill():
    eel.close()
    os._exit(0)

##pega as informações do frontend

@eel.expose
def setInputValue(value):
    global inputvalue
    inputvalue = value

def getInputValue():
    return inputvalue
