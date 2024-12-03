from tkinter import *
janela = Tk()
janela.mainloop()
info = "Esse texto sera/nexibido no rotulo/nem varias linhas."

rotulo = Label(janela, text = info, justify="left")
rotulo.grid(row=0, column=0)

info2 = """"asssim tambem é possivel ter varias linhas"""

rotulo2 = Label(janela,text= info2,justify= "right")
rotulo2.grid(row=2,column=0)

