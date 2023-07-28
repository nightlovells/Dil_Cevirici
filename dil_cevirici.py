from googletrans import Translator
import pyautogui
import keyboard
import pyperclip
import colorama
from colorama import Fore
import os

os.system("cls")
print(Fore.RED+"Dil ceviriciye hos geldiniz!")
print("Bu program Turkce yazdiginiz metinleri otomatik olarak istediginiz dilde cevirir")

print(Fore.BLUE+"Yaziyi yazdiktan sonra CTRL tuşuna basarsaniz istediginiz dile cevirir ESC tusuna basarsaniz programi kapatir")

print(Fore.YELLOW + """Lütfen cevirmek istediginiz dili seciniz: 
      
      1- Ingilizce
      2- Fransizca
      3- Rusca
      4- Ispanyolca
      5- Almanca

      """)
secim=input("Secimi giriniz: ")

if secim == '1':
    deest = 'en'
elif secim == '2':
    deest = 'fr'
elif secim == '3':
    deest = 'ru'
elif secim == '4':
    deest = 'es'
elif secim == '5':
    deest = 'de'
elif secim == '0':
    deest=input("Dil kodu giriniz ORN(en,fr,ru): ")
else:
    print("Hatalı Islem")
    quit()

print("İslem baslamistir lütfen metni girdiginiz yere gidin ve istediginizi yazin yazdiktan sonra CTRL basmayi unutmayin")
def esc_kontrol():
    while True:
        if keyboard.is_pressed('esc'):
            break

        if keyboard.is_pressed('ctrl'):
            pyautogui.hotkey('ctrl','a')
            pyautogui.hotkey('ctrl','c')
            metin = pyperclip.paste()
            pyautogui.press('delete')
            translator = Translator()
            ceviri = translator.translate(metin, src='tr', dest=deest)
            fransizca = ceviri.text
            pyperclip.copy(fransizca)
            pyautogui.hotkey('ctrl','v')

esc_kontrol()
