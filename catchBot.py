import pyautogui as pag 
import time, math, random, sys #, pytesseract

#pytesseract.pytesseract.tesseract_cmd = '/usr/share/tesseract-ocr/4.00/tessdata'

def move(direction):
    pag.keyDown(direction)
    time.sleep(0.5)
    pag.keyUp(direction)

def checkPkmn(pokemon):
    pokemon = pag.screenshot(region = (300, 535, 125, 50))
    pokemon.save('pokemonName.png')
#    print(pytesseract.image_to_string('pokemonName.png'))

#    if pytesseract.image_to_string('pokemonName.png') == pokemon:
#        pag.click(347, 626)

def battleToDefeat():
    screen = pag.size()
    pag.click(347, 626)
    time.sleep(3)
    pag.scroll(-screen[1])
    pag.click(573, 567)
    time.sleep(3)
    for j in range(0, 5):
        pag.scroll(-screen[1])
        pag.click(441, 360)
        time.sleep(3)
        pag.scroll(-screen[1])
        y = 360
        for i in range(0, 10):
            pag.click(441, y)
            time.sleep(0.5)
            y += 21
        pag.click(432, 618)
    pag.click(500, 377)
    time.sleep(3)


while True:
    time.sleep(3)
    #checkPkmn('ekans')
    #print(pag.position())
    #battleToDefeat()
    #
    for i in range(0, 9999999):
        time.sleep(2)
        move('left')
        if random.randint(0, 2) == 0:
            battleToDefeat()
    #    checkPkmn()
        time.sleep(2)
        move('right')
        if random.randint(0, 2) == 0:
            battleToDefeat()
        print('Iteration: ', i)
    #    checkPkmn()
    break
