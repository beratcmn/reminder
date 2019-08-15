import time
import ctypes
import sys
import os
import winsound

ctypes.windll.kernel32.SetConsoleTitleW("Reminder by Berat Çimen")
os.system('mode con: cols=70 lines=20')
remind = input("Neyin hatırlatılmasını istersiniz? ")

while True:
    x = input("Kaç dakika sonra hatırlatılsın? ")
    try:
        x = int(x)
        break
    except ValueError:
        print("Geçersiz bir sayı değeri girdiniz. Lütfen tekrar deneyiniz.")
        continue


sure = x * 60 
while  sure > 0:
    dakika = int(sure / 60)
    saniye = int(sure % 60)
    #print(dakika,saniye)
    baslik = str(dakika) + " : " + str(saniye)
    ctypes.windll.kernel32.SetConsoleTitleW(str(baslik))
    time.sleep(1)
    sure = sure - 1

ctypes.windll.user32.MessageBoxW(0, "'" + remind + "'" + " adlı hatırlatıcının süresi sona erdi.", "Reminder", 0)
winsound.PlaySound("*", winsound.SND_ALIAS)
sys.exit()
