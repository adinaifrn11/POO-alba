from tkinter import *
janela = Tk()
janela.mainloop()
info = "Esse texto sera/nexibido no rotulo/nem varias linhas."

rotulo = Label(janela, text = info, justify="left")
rotulo.grid(row=0, column=0)

logo = PhotoImage(file="logo.png")
rotulo2 = Label(janela, image= logo)
rotulo2.grid(row=0,column=1)