import pyautogui
import time

pyautogui.PAUSE = 4

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# 1 entrar no sistema
pyautogui.press('win')
pyautogui.write('navegador opera gx')
pyautogui.press('enter')
time.sleep(9)
pyautogui.write(link)
pyautogui.press('enter')

# 2 fazer login
time.sleep(10)
pyautogui.click(3193, y=491)  # clicar no campo usuario
pyautogui.write('hromera761@gmail.com')
pyautogui.press('tab')
pyautogui.write('hugostoso')
pyautogui.press('tab')
pyautogui.press('enter')

# 3 abrir base de dados
import pandas
tabela = pandas.read_csv('Produtos.csv')

# 4 cadastrar produtos 
for linha in tabela.index:
    pyautogui.click(x=3388, y=353)  # clicar no campo de codigo
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(tabela.loc[linha, 'codigo'])
    pyautogui.press('tab')

    marca = tabela.loc[linha, 'marca']
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')

    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')

    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    
    obs = tabela.loc[linha, 'obs']
    pyautogui.write(str(tabela.loc[linha, 'obs']))
    
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)
    # if pandas.isna(obs):
    #     pyautogui.press('tab')
    # pyautogui.write(obs)
    # pyautogui.press('tab')
    # pyautogui.press('enter')
        # time.sleep(2)
        # pyautogui.scroll(5000)
   
# 5 repetir passo 4 até acabar lista de produtos
