#Automatizando um tarefa com o pyautogui:

#Passo 1 : Entrar no site
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui #Pacote de automação
import time #Pacote de espera.
pyautogui.PAUSE = 0.8 # Aonde a pausa do pyautogui vai ser de um pro outro
# pyautogui.click --> Clicar em algum lugar na tela
# pyautogui.write --> Escreve um texto
# Pyautogui.press --> Pressionar 1 tecla no teclado.
# pyautogui.hotkey('ctrl' + 'V') --> Comando duplo no teclado

pyautogui.press("win")#Abrindo o menu do not   
pyautogui.write("microsoft edge ")# Pesquisando o no (Chrome)
pyautogui.press("enter")# Pressionando enter para abrir a pagina
#Entrando no site

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press('enter')

#Dando uma pausa para que a pagina caregue por completo
time.sleep(4)#Margem de seguranca, para nao dar problema.


#Passo 2 : Fazer login:
pyautogui.click(x=317, y=357) 
pyautogui.write('luisgpa97@gmail.com')

#Digitando a senha 
#pyautogui.click(x=275, y=449)
pyautogui.press('tab')
pyautogui.write('Digite a senha do email aqui ')
#Clicando no botao de logar.
pyautogui.click(x=510, y=505)
time.sleep(3)#Pra garantir que a pagina vai carregar.

#Clicks = 2, button = 'Lefth' )#Podemos passar parametros para esse clique como, qual butao apertar , se vai dar 2 cliks 

#Passo 3 : Impostar a base de dados
import pandas as pd

tabela = pd.read_csv('produtos.csv')

#Passo 4: Cadastrar o produto
#Passo 5: Repetir o processo de cadastro ate acabar:
#Para cada linha da minha tabela: faça.... 
for linha in tabela.index:
    #Clicando no primeiro campo;
    pyautogui.click(x=300, y=263)
    #Cadastrando o codigo do produto;
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')
    #Marca do produto
    marca = tabela.loc[linha, 'marca']
    pyautogui.write( tabela.loc[linha, 'marca'])
    pyautogui.press('tab')
    #Tipo do produto
    pyautogui.write( tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    #Categoria do produtp;
    pyautogui.write(str( tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    #Preço
    pyautogui.write(str( tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    #Custo 
    pyautogui.write(str( tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    #Observaçao
    obs = tabela.loc[linha, 'obs' ]
    #Criando uma consdiçao;
    if not pd.isna(obs):    
        pyautogui.write(obs)
    pyautogui.press('tab')
    #Enviar
    pyautogui.press('enter')
    #Voltando pro inicio:
    pyautogui.scroll(500)


