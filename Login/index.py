from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import DataBaser

# Função para verificar se o arquivo existe e carregar a imagem
def carregar_imagem(caminho):
    if os.path.exists(caminho):
        return PhotoImage(file=caminho)
    else:
        messagebox.showerror("Erro", f"Não foi possível encontrar o arquivo: {caminho}")
        return None

# Criar Nossa Janela
jan = Tk()
jan.title("ACERVO DE PALAVRAS")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="icons/livroicon.png")


# =======Criando Imagens====
caminho_logo = os.path.join(os.path.dirname(__file__), "icons", "logo.png")
logo = carregar_imagem(caminho_logo)
# =========Widgets=============
LeftFrame = Frame(jan, width=200, height=300, bg="purple", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="purple", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="purple")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Usuário: ", font=("Century Gothic", 20), bg="purple", fg="yellow")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)  # Alterado para Entry
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text="Senha: ", font=("Century Gothic", 20), bg="purple", fg="yellow")
PassLabel.place(x=5, y=150)

PassEntry= ttk.Entry(RightFrame, width=30, show=".")
PassEntry.place(x=150, y=160)

#Botões
LoginButton = ttk.Button(RightFrame, text="Login", width=30)
LoginButton.place(x=100, y=225)

def Register():
   #removendo Widgets de Login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    #Inserindo Widgets de Cadastro
    NomeLabel = Label(RightFrame,text="Nome:", font=("Century Gothic",20), bg="purple", fg="yellow")
    NomeLabel.place(x=5, y=5)

    NomeEntry = Entry(RightFrame, width=39)
    NomeEntry.place(x=100,y=16)

    EmailLabel = Label(RightFrame,text="Email:", font=("Century Gothic",20), bg="purple", fg="yellow")
    EmailLabel.place(x=5, y=55)

    EmailEntry = Entry(RightFrame, width=39)
    EmailEntry.place(x=100,y=66)

    def RegisterToDataBaser():
        Name = NomeEntry.get()
        Email = EmailEntry.get() 
        User = UserEntry.get() 
        Pass = PassEntry.get()  
        DataBaser.cursor.execute("""
        INSERT INTO Users(Nome, Email, Usuário, Senha) VALUES(?, ?, ?, ?)
        """, (Name, Email, User, Pass ))
        DataBaser.conn.commit()
        messagebox.showinfo(title="Register Info", message="Conta Criada Com Sucesso")

    Register = ttk.Button(RightFrame, text="Register", width=30, command=RegisterToDataBaser)
    Register.place(x=100, y=225)

    def BackToLogin():
        #Removendo Widgets de Cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)

    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=125, y=260)



RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=125, y=260)


jan.mainloop()