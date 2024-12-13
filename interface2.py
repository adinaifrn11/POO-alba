from tkinter import *
from tkinter import messagebox


def realizar_operacao(operacao):
    try:
        v1 = float(campo1.get())
        v2 = float(campo2.get())
        if operacao == "soma":
            resultado = v1 + v2
        elif operacao == "subtracao":
            resultado = v1 - v2
        elif operacao == "multiplicacao":
            resultado = v1 * v2
        elif operacao == "divisao":
            if v2 == 0:
                messagebox.showerror("Erro", "Divisão por zero não permitida.")
                return
            resultado = v1 / v2
        campo_total.config(state="normal") 
        campo_total.delete(0, END)  
        campo_total.insert(0, str(resultado))  
        campo_total.config(state="readonly")  
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")


def tela_login():
    def verificar_login():
        usuario = campo_usuario.get()
        senha = campo_senha.get()
        if usuario == "admin" and senha == "1234":
            messagebox.showinfo("Login", "Acesso permitido")
            janela_login.destroy()
        else:
            messagebox.showerror("Login", "Acesso negado")

    janela_login = Toplevel()
    janela_login.title("Login")
    janela_login.geometry("250x150")

    Label(janela_login, text="Usuário:").grid(row=0, column=0, padx=10, pady=5)
    campo_usuario = Entry(janela_login)
    campo_usuario.grid(row=0, column=1, padx=10, pady=5)

    Label(janela_login, text="Senha:").grid(row=1, column=0, padx=10, pady=5)
    campo_senha = Entry(janela_login, show="*")
    campo_senha.grid(row=1, column=1, padx=10, pady=5)

    botao_entrar = Button(janela_login, text="Entrar", command=verificar_login)
    botao_entrar.grid(row=2, column=0, columnspan=2, pady=10)


janela = Tk()
janela.title("Calculadora")
janela.geometry("300x200")


Label(janela, text="Valor 1:").grid(row=0, column=0, padx=10, pady=5)
campo1 = Entry(janela)
campo1.grid(row=0, column=1, padx=10, pady=5)

Label(janela, text="Valor 2:").grid(row=1, column=0, padx=10, pady=5)
campo2 = Entry(janela)
campo2.grid(row=1, column=1, padx=10, pady=5)


Label(janela, text="Total:").grid(row=2, column=0, padx=10, pady=5)
campo_total = Entry(janela, state="readonly")
campo_total.grid(row=2, column=1, padx=10, pady=5)


Button(janela, text="Somar", width=10, command=lambda: realizar_operacao("soma")).grid(row=3, column=0, pady=5)
Button(janela, text="Subtrair", width=10, command=lambda: realizar_operacao("subtracao")).grid(row=3, column=1, pady=5)
Button(janela, text="Multiplicar", width=10, command=lambda: realizar_operacao("multiplicacao")).grid(row=4, column=0, pady=5)
Button(janela, text="Dividir", width=10, command=lambda: realizar_operacao("divisao")).grid(row=4, column=1, pady=5)


Button(janela, text="Login", width=20, command=tela_login).grid(row=5, column=0, columnspan=2, pady=10)


janela.mainloop()