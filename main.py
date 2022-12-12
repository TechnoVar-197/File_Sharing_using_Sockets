from tkinter import *
import socket
from tkinter import filedialog
import pathlib
import os

root = Tk()
root. title("FILE TRANSFER USING SOCKETS")
root. geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root. resizable(False, False)


def Send():
    window = Toplevel(root)
    window.title("Send",)
    window.geometry('450x560+500+200')
    window. configure(bg="#f4fdfe")
    window. resizable(False, False)

    def select_files():
        global filename
        global text
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text file', '*.txt'),('all files', '*.*')))
        file_extension = pathlib.Path(filename).suffix
        text = 'received' + file_extension
    def sender():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("localhost", 9999))
        file = open(filename, "rb")
        file_size = os.path.getsize(filename)
        client.send(text.encode())
        client.send(str(file_size).encode())
        data = file.read()
        client.sendall(data)
        client.send(b"<END>")
    # icon
    image_icon1 = PhotoImage(file="Image/send.png")
    window.iconphoto(False, image_icon1)
    Sbackground = PhotoImage(file="Image/sender.png")
    Label(window, image=Sbackground).place(x=-2, y=0)
    Mbackground = PhotoImage(file="Image/id.png")
    Label(window, image=Mbackground, bg="#f4fdfe").place(x=100, y=260)

    host = socket.gethostname()
    Label(window, text=f'ID:{host}', bg='white',fg='black').place(x=140, y=290)

    Button(window, text="+ Select File", width=10, height=1, font='arial 14 bold',bg="#fff", fg="#000", command=select_files).place(x=160, y=150)
    Button(window, text="Send", width=8, height=1, font='arial 14 bold',bg="#fff", fg="#000",command=sender).place(x=300, y=150)

    window.mainloop()





def Receive():
    main = Toplevel(root)
    main.title("Receive",)
    main.geometry('450x560+500+200')
    main.configure(bg="#f4fdfe")
    main.resizable(False, False)
    
    def receiver():
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("localhost", 9999))
        server.listen()

        client, addr = server.accept()
        file_name = client.recv(1024).decode()
        # print(file_name)
        file_size = client.recv(1024).decode()
        # print(file_size)
        file = open(file_name, "wb")
        file_bytes = b""
        done = False
        while not done:
            data = client.recv(1024)
            if file_bytes[-5:] == b"<END>":
                done = True
            else:
                file_bytes += data

    
    # icon
    image_icon1 = PhotoImage(file="Image/receive.png")
    main.iconphoto(False,image_icon1)
    
    Hbackground = PhotoImage(file="Image/receiver.png")
    Label(main,image=Hbackground).place(x=-2, y=0)
    logo = PhotoImage(file="Image/profile.png")
    Label(main,image=logo,bg="#f4fdfe").place(x=10,y=280) 
    
    Label(main,text="Receive",font=('arial',20),bg="#f4fdfe").place(x=100,y=280)
    
    #Label(main,text="Input sender id",font=('arial',10),bg="#f4fdfe").place(x=20,y=340)
    #SenderId=Entry(main,width=25,fg='black',border=2,bg='white',font=('arial',15))
    #SenderId.place(x=20,y=370)
    #SenderId.focus()
    #Label(main,text="Filename for the incoming file: ",font=('arial',10),bg="#f4fdfe").place(x=20,y=340)
    #incoming_file=Entry(main,width=25,fg='black',border=2,bg='white',font=('arial',15))
    #incoming_file.place(x=20,y=450)
    
    imageicon=PhotoImage(file="Image/arrow.png")
    r=Button(main,text="Receive",compound=LEFT,image=imageicon,width=130,bg="#39c790",font='arial 14 bold',command=receiver)
    r.place(x=20,y=500)
    
    main.mainloop()



# icon
image_icon = PhotoImage(file="Image/icon.png")
root.iconphoto(False, image_icon)
Label(root, text="File Transfer", font=('Acumin Variable Concept', 20, 'bold'), bg="#f4fdfe").place(x=20, y=31)
Frame(root, width=400, height=2, bg="#f3f5f6").place(x=25, y=80)
send_image = PhotoImage(file="Image/send.png")
send = Button(root, image=send_image, bg="#f4fdfe", bd=0, command=Send)
send.place(x=50, y=100)
receive_image = PhotoImage(file="Image/receive.png")
receive = Button(root, image=receive_image,bg="#f4fdfe", bd=0, command=Receive)
receive.place(x=300, y=100)
# label
Label(root, text="Send", font=('Acumin Variable Concept',17, 'bold'), bg="#f4fdfe") .place(x=65, y=200)
Label(root, text="Receive", font=('Acumin Variable Concept',17, 'bold'), bg="#f4fdfe") .place(x=300, y=200)
background = PhotoImage(file="Image/background.png")
Label(root, image=background).place(x=-2, y=323)

root. mainloop()