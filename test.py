import os
import pathlib
import socket
from tkinter import filedialog

global text
filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text file', '*.txt'),('all files', '*.*')))
file_extension = pathlib.Path(filename).suffix
text = 'received' + file_extension

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))
file = open(filename, "rb")
file_size = os.path.getsize(filename)
client.send(text.encode())
client.send(str(file_size).encode())
data = file.read()
client.sendall(data)
client.send(b"<END>")
