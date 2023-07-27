import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import textwrap

Estado_Imagem_Selec_Arq = 1
Estado_Imagem_Selec_Sai = 1

def intro ():
    def close_intro():
        intro_window.destroy()
    
    # Carregar a imagem com transparência usando o PIL
    image = Image.open(r"C:\Users\Pedro\Desktop\VCT\Interface\intro.png")
    image_width, image_height = image.size

    # Criar a janela de introdução com base no tamanho da imagem
    intro_window = tk.Tk()
    intro_window.title("Introdução")
    intro_window.geometry(f"{image_width}x{image_height}")

    # Remover a borda e a barra de título da janela
    intro_window.overrideredirect(True)

    # Converter a imagem para o formato Tkinter
    photo = ImageTk.PhotoImage(image)

    # Criar um rótulo para exibir a imagem
    label = tk.Label(intro_window, image=photo)
    label.pack()

    # Obter a largura e altura da tela
    screen_width = intro_window.winfo_screenwidth()
    screen_height = intro_window.winfo_screenheight()

    # Calcular a posição x e y para centralizar a janela
    x_pos = (screen_width - image_width) // 2
    y_pos = (screen_height - image_height) // 2

    # Definir a posição da janela no centro da tela
    intro_window.geometry(f"{image_width}x{image_height}+{x_pos}+{y_pos}")

    # Fechar a janela de introdução após alguns segundos (opcional)
    intro_window.after(2500, close_intro)  # Fecha após 5 segundos (5000 ms)

    # Iniciar o loop principal do tkinter
    intro_window.mainloop()

def interface ():

    # Variável de controle do estado da imagem


    ######### COMANDOS #########
    def on_select(event):
        selected_option = var_selecionada.get()
        print("Opção selecionada:", selected_option)

    ### SELECIONADOR DE ARQUIVO ###
    def Mouse_Entra_Selec_Arq(event):
        global Estado_Imagem_Selec_Arq
        # Exibe a imagem 2 quando o mouse entra
        if Estado_Imagem_Selec_Arq == 1:
            Label_Selec_Arq.config(image=photo_selec_arq_2)
    def Mouse_Sai_Selec_Arq(event):
        global Estado_Imagem_Selec_Arq
        # Volta para a imagem 1 quando o mouse sai
        if Estado_Imagem_Selec_Arq == 1:
            Label_Selec_Arq.config(image=photo_selec_arq)
    def Click_Abre_Selec_Arq(event):
        global Estado_Imagem_Selec_Arq
        global Nome_Arq
        if Estado_Imagem_Selec_Arq == 1:
            Arquivo_Selecionado = filedialog.askopenfilename()
            if Arquivo_Selecionado:
                print("Arquivo selecionado:", Arquivo_Selecionado)
                #Label com nome do arquivo
                indice_ultima_barra_Arq = Arquivo_Selecionado.rfind("/")# Encontre a posição da última ocorrência da barra
                # Extraia o texto que está à frente da última barra
                texto_final_Arq = Arquivo_Selecionado[indice_ultima_barra_Arq + 1:]
                # Verifique o comprimento do texto final
                if len(texto_final_Arq) > 11:
                    texto_quebrado = textwrap.fill(texto_final_Arq, width=11)
                    Nome_Arq = tk.Label(janela, text=texto_quebrado, bg="#a7a7a7",font=("Arial", 9), justify="left")
                else:
                    Nome_Arq = tk.Label(janela, text=texto_final_Arq, bg="#a7a7a7",font=("Arial", 9))
                Nome_Arq.place(x=165,y=215)
                # Exibe a imagem 3 somente se o estado atual for 1
                Label_Selec_Arq.config(image=photo_selec_arq_3)
                Estado_Imagem_Selec_Arq = 3


    ### SELECIONADOR DE SAIDA ###
    def Mouse_Entra_Selec_Sai(event):
        global Estado_Imagem_Selec_Sai
        # Exibe a imagem 2 quando o mouse entra
        if Estado_Imagem_Selec_Sai == 1:
            Label_Selec_Sai.config(image=photo_selec_Sai_2, bg="#f3f3f3")
    def Mouse_Sai_Selec_Sai(event):
        global Estado_Imagem_Selec_Sai
        # Exibe a imagem 1 quando o mouse entra
        if Estado_Imagem_Selec_Sai == 1:
            Label_Selec_Sai.config(image=photo_selec_Sai, bg="#f3f3f3")
    def Click_Selec_Sai(event):
        global Estado_Imagem_Selec_Sai
        global Nome_Sai
        if Estado_Imagem_Selec_Sai == 1:
            Local_Saida = filedialog.askdirectory()
            if Local_Saida:
                indice_ultima_barra_Sai = Local_Saida.rfind("/") # Encontre a posição da última ocorrência da barra
                # Extraia o texto que está à frente da última barra
                texto_final_Sai = Local_Saida[indice_ultima_barra_Sai + 1:]
                # Verifique o comprimento do texto final
                if len(texto_final_Sai) > 15:
                    texto_quebrado_Sai = textwrap.fill(texto_final_Sai, width=15)
                    Nome_Sai = tk.Label(janela, text=f"Local de saida:\n{texto_quebrado_Sai}", bg="#f3f3f3",font=("Arial", 9), justify="left")
                else:
                    Nome_Sai = tk.Label(janela, text=f"Local de saida:\n{texto_final_Sai}", bg="#f3f3f3",font=("Arial", 9),justify="left")
                Nome_Sai.place(x=432,y=210)
                print("Local de saida:", Local_Saida)
                # Exibe a imagem 2 quando o botão esquerdo é clicado
                Label_Selec_Sai.config(image=photo_selec_Sai_2)
                Estado_Imagem_Selec_Sai = 2

        
                



    ### BOTAO INICIAR ###
    def Mouse_Entra_Bt_Ini(event):
        Label_Bt_Ini.config(image=photo_Bt_Ini_2)
    def Mouse_Sai_Bt_Ini(event):
        Label_Bt_Ini.config(image=photo_Bt_Ini)
    def Click_Bt_Ini(event):
        global Estado_Imagem_Selec_Arq
        global Estado_Imagem_Selec_Sai
        print("Botao clicado")
        # Muda para a imagem 1 quando a função é chamada
        Label_Selec_Arq.config(image=photo_selec_arq)
        Label_Selec_Sai.config(image=photo_selec_Sai)
        Estado_Imagem_Selec_Arq = 1
        Estado_Imagem_Selec_Sai = 1
        Nome_Arq.place_forget()
        Nome_Sai.place_forget()




    ######### CRIACAO DA JANELA #########
    # Carregar a imagem com transparência usando o PIL
    Bg = Image.open(r"c:\Users\Pedro\Desktop\VCT\Interface\Janela_V1.png")
    image_width, image_height = Bg.size

    # Cria a janela principal
    janela = tk.Tk()
    janela.title("AICA | Processador de Dados - VCT Brasil")
    janela.geometry(f"{image_width}x{image_height}")
    janela.resizable(False, False) #Bloqueia o redimensionamento da janela
    photo = ImageTk.PhotoImage(Bg) # Converter a imagem para o formato Tkinter
    Label_Bg = tk.Label(janela, image=photo) # Criar um rótulo para exibir a imagem
    Label_Bg.place(x=0,y=0) # Colocando a imagem na janela

    # Obter a largura e altura da tela
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()

    # Calcular a posição x e y para centralizar a janela
    x_pos = (screen_width - image_width) // 2
    y_pos = (screen_height - image_height) // 2

    # Definir a posição da janela no centro da tela
    janela.geometry(f"{image_width}x{image_height}+{x_pos}+{y_pos}")





    ######### OUTROS #########
    # Lista de opções para o Combobox
    opcoes = ['Opção 1', 'Opção 2', 'Opção 3', 'Opção 4']

    # Variável para armazenar a opção selecionada (Selecionador de Padrao)
    var_selecionada = tk.StringVar()


    ######### CRIACAO DE OBJETOS #########
    # ComboBox
    combobox = ttk.Combobox(janela, values=opcoes, textvariable=var_selecionada) 

    # Selecionador de Arquivo
    Selec_Arq = Image.open(r"C:\Users\Pedro\Desktop\VCT\Interface\Selec_Folder\Selec_Folder_1.png")
    photo_selec_arq = ImageTk.PhotoImage(Selec_Arq) # Converter a imagem para o formato Tkinter
    Selec_Arq_2 = Image.open(r"C:\Users\Pedro\Desktop\VCT\Interface\Selec_Folder\Selec_Folder_2.png")
    photo_selec_arq_2 = ImageTk.PhotoImage(Selec_Arq_2) # Converter a imagem para o formato Tkinter
    Selec_Arq_3 = Image.open(r"C:\Users\Pedro\Desktop\VCT\Interface\Selec_Folder\Selec_Folder_3.png")
    photo_selec_arq_3 = ImageTk.PhotoImage(Selec_Arq_3) # Converter a imagem para o formato Tkinter

    # Criar um rótulo para exibir a imagem
    Label_Selec_Arq = tk.Label(janela, image=photo_selec_arq)
 
    # Selecionador de Saida
    Selec_Sai = Image.open(r"C:\Users\Pedro\Desktop\VCT\Interface\Folder\Folder_1.png")
    photo_selec_Sai = ImageTk.PhotoImage(Selec_Sai) # Converter a imagem para o formato Tkinter
    Selec_Sai_2 = Image.open(r"C:\Users\Pedro\Desktop\VCT\Interface\Folder\Folder_2.png")
    photo_selec_Sai_2 = ImageTk.PhotoImage(Selec_Sai_2) # Converter a imagem para o formato Tkinter
    # Criar um rótulo para exibir a imagem
    Label_Selec_Sai = tk.Label(janela, image=photo_selec_Sai)

    # Botao Iniciar
    Bt_Ini = Image.open(r"C:\Users\Pedro\Desktop\VCT\Interface\BT_Iniciar\Bt_Iniciar_1.png")
    photo_Bt_Ini = ImageTk.PhotoImage(Bt_Ini) # Converter a imagem para o formato Tkinter
    Bt_Ini_2 = Image.open(r"C:\Users\Pedro\Desktop\VCT\Interface\BT_Iniciar\Bt_Iniciar_2.png")
    photo_Bt_Ini_2 = ImageTk.PhotoImage(Bt_Ini_2) # Converter a imagem para o formato Tkinter
    # Criar um rótulo para exibir a imagem
    Label_Bt_Ini = tk.Label(janela, image=photo_Bt_Ini)

 






    ######### ADICIONANDO OBJETOS A JANELA #########
    combobox.place(x=60, y=150)
    Label_Selec_Arq.place(x=58, y=182)
    Label_Selec_Sai.place(x=327, y=198)#393
    Label_Bt_Ini.place(x=225, y=311)





    ######### ASSOCIANDO EVENTOS A OBJETOS #########
    # Associando a função on_select ao evento de seleção do Combobox
    combobox.bind("<<ComboboxSelected>>", on_select)

    # Associando as funções do Selec_Arq
    Label_Selec_Arq.bind("<Enter>", Mouse_Entra_Selec_Arq)
    Label_Selec_Arq.bind("<Leave>", Mouse_Sai_Selec_Arq)
    Label_Selec_Arq.bind("<Button-1>", Click_Abre_Selec_Arq)
    # Associando as funções do Selec_Sai
    Label_Selec_Sai.bind("<Enter>", Mouse_Entra_Selec_Sai)
    Label_Selec_Sai.bind("<Leave>", Mouse_Sai_Selec_Sai)
    Label_Selec_Sai.bind("<Button-1>", Click_Selec_Sai)
    # Associando as funções do BT_Ini
    Label_Bt_Ini.bind("<Enter>", Mouse_Entra_Bt_Ini)
    Label_Bt_Ini.bind("<Leave>", Mouse_Sai_Bt_Ini)
    Label_Bt_Ini.bind("<Button-1>", Click_Bt_Ini)


    

    janela.mainloop()

intro ()
interface()


