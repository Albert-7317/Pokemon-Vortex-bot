import pyautogui as pag 
import time, math, random, sys, pytesseract

pytesseract.pytesseract.tesseract_cmd = '/usr/share/tesseract-ocr/4.00/tessdata'

def move(direction):
    pag.keyDown(direction)
    time.sleep(0.5)
    pag.keyUp(direction)

def checkPkmn(pokemon):
    pokemon = pag.screenshot(region = (300, 535, 125, 50))
    pokemon.save('pokemonName.png')
    print(pytesseract.image_to_string('pokemonName.png'))

    if pytesseract.image_to_string('pokemonName.png') == pokemon:
        pag.click(347, 626)

while True:
    time.sleep(3)
    #checkPkmn('ekans')
    print(pag.position())
    for i in range(0, 3):
        time.sleep(2)
        move('left')
    #   checkPkmn()
        time.sleep(2)
        move('right')
    #    checkPkmn()
    break