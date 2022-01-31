# Bibliotecas a serem usadas
import pyautogui
import time

# pyautogui.click(x=713, y=700)

# Solicita entrada do usuário em relação ao número de atividades entregues.
# var = int(input("Insira o número de alunos que entregaram as atividades: "))


# Funções para otimizar o código
def alttab():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')

def controlc():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('c')
    pyautogui.keyUp('c')
    pyautogui.keyUp('ctrl')

def alttab2():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')

def f2():
    pyautogui.press('f2')

def controlv():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('v')
    pyautogui.keyUp('ctrl')

def enter():
    pyautogui.press('enter')

def down():
    pyautogui.press("down")

def up():
    pyautogui.press("up")

def right():
    pyautogui.press("right")

def left():
    pyautogui.press('left')


# -------------Código começa------------------------

# -------------Ajuste das janelas-------------------
alttab()
time.sleep(0.5)
alttab2()
time.sleep(0.5)
alttab()
time.sleep(0.5)
down()
up()


#-----------------------6°ano A----------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------

for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()


#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(5):
    up()
for i in range(5):
    down()
pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------


#-----------------------6°ano B----------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------

for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()

#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(6):
    up()
for i in range(6):
    down()
pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------

#-----------------------6°ano C----------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------

for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()

#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(7):
    up()
for i in range(7):
    down()
pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------


#-----------------------6°ano D----------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------

for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()


#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(8):
    up()
for i in range(8):
    down()

pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------

#-----------------------6°ano E----------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------

for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()

#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(10):
    up()
for i in range(10):
    down()

pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------


#-----------------------7°ano A----------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------
for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()

#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(23):
    up()
for i in range(23):
    down()

pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------





#-----------------------9°ano A----------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------
for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()

#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(24):
    up()
for i in range(24):
    down()

pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------




#-----------------------9°ano B----------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------

for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()

#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(25):
    up()
for i in range(25):
    down()

pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------



#-----------------------9°ano C---------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------
for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()

#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(26):
    up()
for i in range(26):
    down()

pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------


#-----------------------9°ano D---------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------
for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()

#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(27):
    up()
for i in range(27):
    down()

pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------

#-----------------------9°ano E---------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------
for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()

#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(28):
    up()
for i in range(28):
    down()

pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------



#-----------------------9°ano F---------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------
for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
#---------------------------Virada para o perído Vespertino---------------------------------
right()
right()
right()
#---------------------------Virada para o perído Vespertino---------------------------------

alttab()

#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(29):
    up()
for i in range(9):
    down()

pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------





















#---------------------------Virada para o perído Vespertino---------------------------------

#--------------------------Selecionando a primeira aula da tarde---------------------------
up()
up()
up()
up()
up()
up()
up()
up()

down()
down()
down()
down()
down()
down()
down()
down()
#--------------------------Selecionando a primeira aula da tarde---------------------------

#---------------------------Virada para o perído Vespertino---------------------------------

#-----------------------6°ano F---------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------
for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()

#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(11):
    up()
for i in range(11):
    down()

pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------








#--------------------------Selecionando a primeira aula da tarde---------------------------
up()
up()
up()
up()
up()
up()
up()
up()

down()
down()
down()
down()
down()
down()
down()
down()
#--------------------------Selecionando a primeira aula da tarde---------------------------

#---------------------------Virada para o perído Vespertino---------------------------------

#-----------------------7°ano B---------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------
for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()

#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(12):
    up()
for i in range(12):
    down()

pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------




#--------------------------Selecionando a primeira aula da tarde---------------------------
up()
up()
up()
up()
up()
up()
up()
up()

down()
down()
down()
down()
down()
down()
down()
down()
#--------------------------Selecionando a primeira aula da tarde---------------------------

#---------------------------Virada para o perído Vespertino---------------------------------

#-----------------------7°ano C---------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------
for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()

#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(13):
    up()
for i in range(13):
    down()

pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------








#--------------------------Selecionando a primeira aula da tarde---------------------------
up()
up()
up()
up()
up()
up()
up()
up()

down()
down()
down()
down()
down()
down()
down()
down()
#--------------------------Selecionando a primeira aula da tarde---------------------------

#---------------------------Virada para o perído Vespertino---------------------------------

#-----------------------7°ano D---------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------
for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()

#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(14):
    up()
for i in range(14):
    down()

pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------










#--------------------------Selecionando a primeira aula da tarde---------------------------
up()
up()
up()
up()
up()
up()
up()
up()

down()
down()
down()
down()
down()
down()
down()
down()
#--------------------------Selecionando a primeira aula da tarde---------------------------

#---------------------------Virada para o perído Vespertino---------------------------------

#-----------------------7°ano E---------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------
for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()

#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(15):
    up()
for i in range(15):
    down()

pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------










#--------------------------Selecionando a primeira aula da tarde---------------------------
up()
up()
up()
up()
up()
up()
up()
up()

down()
down()
down()
down()
down()
down()
down()
down()
#--------------------------Selecionando a primeira aula da tarde---------------------------

#---------------------------Virada para o perído Vespertino---------------------------------

#-----------------------7°ano F---------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------
for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()

#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(16):
    up()
for i in range(16):
    down()

pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------











#--------------------------Selecionando a primeira aula da tarde---------------------------
up()
up()
up()
up()
up()
up()
up()
up()

down()
down()
down()
down()
down()
down()
down()
down()
#--------------------------Selecionando a primeira aula da tarde---------------------------

#---------------------------Virada para o perído Vespertino---------------------------------

#-----------------------7°ano G---------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------
for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()

#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(17):
    up()
for i in range(17):
    down()

pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------










#--------------------------Selecionando a primeira aula da tarde---------------------------
up()
up()
up()
up()
up()
up()
up()
up()

down()
down()
down()
down()
down()
down()
down()
down()
#--------------------------Selecionando a primeira aula da tarde---------------------------

#---------------------------Virada para o perído Vespertino---------------------------------

#-----------------------8°ano A---------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------
for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()

#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(18):
    up()
for i in range(18):
    down()

pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------






#--------------------------Selecionando a primeira aula da tarde---------------------------
up()
up()
up()
up()
up()
up()
up()
up()

down()
down()
down()
down()
down()
down()
down()
down()
#--------------------------Selecionando a primeira aula da tarde---------------------------

#---------------------------Virada para o perído Vespertino---------------------------------

#-----------------------8°ano B---------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------
for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()

#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(19):
    up()
for i in range(19):
    down()

pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------










#--------------------------Selecionando a primeira aula da tarde---------------------------
up()
up()
up()
up()
up()
up()
up()
up()

down()
down()
down()
down()
down()
down()
down()
down()
#--------------------------Selecionando a primeira aula da tarde---------------------------

#---------------------------Virada para o perído Vespertino---------------------------------

#-----------------------8°ano C---------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------
for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()

#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(20):
    up()
for i in range(20):
    down()

pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------














#--------------------------Selecionando a primeira aula da tarde---------------------------
up()
up()
up()
up()
up()
up()
up()
up()

down()
down()
down()
down()
down()
down()
down()
down()
#--------------------------Selecionando a primeira aula da tarde---------------------------

#---------------------------Virada para o perído Vespertino---------------------------------

#-----------------------8°ano D---------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------
for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()

#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(21):
    up()
for i in range(21):
    down()

pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------











#--------------------------Selecionando a primeira aula da tarde---------------------------
up()
up()
up()
up()
up()
up()
up()
up()

down()
down()
down()
down()
down()
down()
down()
down()
#--------------------------Selecionando a primeira aula da tarde---------------------------

#---------------------------Virada para o perído Vespertino---------------------------------

#-----------------------8°ano E---------------------
# --------Inicia a transferência-----------
for i in range (5):

    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------
for i in range(5):
    left()
alttab()
for i in range (45):
        up()
right()
alttab()

#------------------------------Tentativa de continuação do código---------------------------
pyautogui.click(x=100, y=70)
for i in range(22):
    up()
for i in range(22):
    down()

pyautogui.click(x=200, y=350)
#--------------------------------------------------------------------------------------------













