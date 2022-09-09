from tkinter.filedialog import Open
import pyautogui
from time import sleep

# 1- abrir programa
pyautogui.click(1914,1043,duration=1)
pyautogui.doubleClick(165,522,duration=4)
# 2 digitar usuário
pyautogui.click(948,542,duration=1)
pyautogui.write("jhonatan")
# Digitar senha
pyautogui.click(958,581,duration=1)
pyautogui.write("123456")
# 3 clicar em entrar
pyautogui.click(835,626,duration=1)
# 4 Extrair cada produto
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        # 	1 clicar e registrar produto
        pyautogui.click(532,522,duration=0.5)
        pyautogui.write(produto)
        # 	2 clicar e registrar quantidade
        pyautogui.click(527,567,duration=0.5)
        pyautogui.write(quantidade)
        # 	3 clicar e registrar preço
        pyautogui.click(540,595,duration=0.5)
        pyautogui.write(preco)    
        # 	4 clicar em registrar
        pyautogui.click(420,836,duration=0.5)    
        sleep(0.5)