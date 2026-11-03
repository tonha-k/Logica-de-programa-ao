import pyautogui
import pandas as pd
import time  # VAI AJUDAR A DAR UMA PAUSA ENTRE CADA AÇÃO DO PYAUTOGUI

# 1° passo: abrir o navegador e acessar o link do sistema

pyautogui.PAUSE = 0.5  # TEMPO DE PAUSA ENTRE CADA AÇÃO DO PYAUTOGUI

link = "https://sistemapythonpwup.lovable.app/automacao-produtos"
email = "123abu@gmail.com"
senha = "12345678"

pyautogui.press("win")  # ABRE O MENU INICIAR DO WINDOWS
# FAZER UMA PAUSA PARA O SISTEMA CARREGAR
time.sleep(2)
pyautogui.write("edge")  # ESCREVE O NOME DO NAVEGADOR
pyautogui.press("enter")  # PRESSIONA A TECLA ENTER PARA ABRIR O NAVEGADOR
time.sleep(2)
pyautogui.write(link)  # ESCREVE O LINK DO SISTEMA
pyautogui.press("enter")  # PRESSIONA A TECLA ENTER PARA ABRIR O LINK DO SISTEMA
time.sleep(4)  # FAZ UMA PAUSA DE 4 SEGUNDOS PARA O SISTEMA CARREGAR

# 2° Passo: Logar no sistema

pyautogui.click(x=905, y=456)
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("enter")

# 3° Passo: Cadastrar os produtos da planilha (produtos.csv)

tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=596, y=253)

    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # Pega o valor da coluna correta "obs"
    obs = tabela.loc[linha, "obs"]

    # Verifica e escreve a observação se ela NÃO for nula
    if not pd.isna(obs):
        pyautogui.write(str(obs))

    # Passa para o botão de enviar e clica
    pyautogui.press("tab")
    pyautogui.press("enter")

    # Pausa de 1 segundo para dar tempo à página de processar o envio
    time.sleep(2)

    # Rola a página para cima para começar o próximo produto
    pyautogui.scroll(5000)