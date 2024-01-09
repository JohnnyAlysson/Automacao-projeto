#Projeto de automação
# 1. Acessar o sistema da empresa
import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)
# 2. Fazer login
pyautogui.click(x=821,y=487)
pyautogui.write("login example")
pyautogui.press("tab")
pyautogui.write("password")
pyautogui.press("enter")
time.sleep(3)
# 3. importar a base da dados
products_table = pd.read_csv("produtos.csv")
# 4. Cadastrar um produto
# 5. Repetir até acabar a base de dados 
for line in products_table.index:
    pyautogui.press("home")
    pyautogui.click(x=900, y=335)
    
    pyautogui.write(str(products_table.loc[line,"codigo"]))
    pyautogui.press("tab")

    pyautogui.write(products_table.loc[line,"marca"])
    pyautogui.press("tab")

    pyautogui.write(products_table.loc[line,"tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(products_table.loc[line,"categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(products_table.loc[line,"preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(products_table.loc[line,"custo"]))
    pyautogui.press("tab")

    obs= products_table.loc[line,"obs"]
    if not pd.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")