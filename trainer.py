import pymem
import time
import threading
import tkinter as tk

# Endereços encontrados com cheat engine 
ENDERECO_BALAS = 0x006C3130
ENDERECO_VIDA = 0x006C30DC

PROCESSO_NOME = "ac_client.exe"

LIMITE_BALAS = 5
VALOR_BALAS = 20

LIMITE_VIDA = 60
VALOR_VIDA = 100

# Flags de controle
repor_balas = False
repor_vida = False

# Conectar ao processo
try:
    pm = pymem.Pymem(PROCESSO_NOME)
except Exception as e:
    print("Erro ao conectar ao processo:", e)
    exit()

# Função que faz o loop de monitoramento
def monitorar():
    global repor_balas, repor_vida
    while True:
        if repor_balas:
            try:
                balas = pm.read_int(ENDERECO_BALAS)
                if balas < LIMITE_BALAS:
                    pm.write_int(ENDERECO_BALAS, VALOR_BALAS)
            except:
                pass

        if repor_vida:
            try:
                vida = pm.read_int(ENDERECO_VIDA)
                if vida < LIMITE_VIDA:
                    pm.write_int(ENDERECO_VIDA, VALOR_VIDA)
            except:
                pass

        time.sleep(0.1)


def toggle_balas():
    global repor_balas
    repor_balas = not repor_balas
    botao_balas.config(text=f"{'Desativar' if repor_balas else 'Ativar'} Reposição de Balas")

def toggle_vida():
    global repor_vida
    repor_vida = not repor_vida
    botao_vida.config(text=f"{'Desativar' if repor_vida else 'Ativar'} Reposição de Vida")

# Thread do monitoramento
threading.Thread(target=monitorar, daemon=True).start()


janela = tk.Tk()
janela.title("Trainer - Assault Cube")
janela.geometry("300x100")

botao_balas = tk.Button(janela, text="Ativar Reposição de Balas", command=toggle_balas, width=30)
botao_balas.pack(pady=10)

botao_vida = tk.Button(janela, text="Ativar Reposição de Vida", command=toggle_vida, width=30)
botao_vida.pack(pady=10)

janela.mainloop()
