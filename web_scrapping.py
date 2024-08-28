import webbrowser as wb
import pyperclip
import sys

#checa se o enderço foi passado na linha de comando
if (len(sys.argv)>1):
    address = ''.join(sys.argv)
#se não, pega dos copiados
else:
    address = pyperclip.paste()

wb.open('https://www.google.com/maps/place/' + address)



