from colorama import Fore, Style
from time import sleep
from os import system
from requests import get
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
r = get("https://raw.githubusercontent.com/latews1/latewste/main/sms.py").text
with open("sms.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == r:
    pass
else:
    print(Fore.RED + "Güncelleme yapılıyor...")
    with open("sms.py", "w", encoding="utf-8") as f:
        f.write(r)
from sms import SendSms
servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)    
while 1:
    system("cls||clear")
    print("""{}
  
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
▀                ▀
▀ LATEWS BOOMBER ▀
▀                ▀
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

    SMS API: {}                                      
    """.format(Fore.LIGHTRED_EX, len(servisler_sms), Style.RESET_ALL, Fore.CYAN))
    print(Fore.LIGHTGREEN_EX+"{/} "+Style.RESET_ALL+"LATEWS B00MBER "+Fore.LIGHTGREEN_EX+Style.BRIGHT+"latews#1000\n"+Style.RESET_ALL)
    try:
        menu = int(input(Fore.LIGHTMAGENTA_EX + " 1- SMS Gönder\n 2- Çıkış\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: "))
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Tekrar deneyiniz.")
        sleep(3)
        continue
    if menu == 1:
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Telefon numarasini basinda '+90' olmadan yaz: "+ Fore.LIGHTGREEN_EX, end="")
            tel_no = input()
            if tel_no != "" and len(str(tel_no)) == 10:
                tel_no2 = "bos"
                tel_no3 = "bos"
                tel_no4 = "bos"
                tel_no5 = "bos"
            if tel_no == "":
                system("cls||clear")
                print( Fore.LIGHTGREEN_EX+"[+] "+Fore.CYAN+"TXT dosya formati:\n"
                      +Fore.LIGHTGREEN_EX+"[+] "+Fore.CYAN+"En fazla 5 numara olacak şekilde basinda '+90' olmadan alt alta numaralari yaz .")
                print("")
                print("")
                print(Fore.LIGHTYELLOW_EX + "TXT dosyasının yolunu giriniz: "+ Fore.LIGHTGREEN_EX, end="")
                dosya_yolu = input()
                try:
                    with open(dosya_yolu, 'r') as file:
                        tel_list = file.readlines()
                        for i, number in enumerate(tel_list):
                            if i == 0:
                                tel_no = number.strip()
                            elif i == 1:
                                tel_no2 = number.strip()
                            elif i == 2:
                                tel_no3 = number.strip()
                            elif i == 3:
                                tel_no4 = number.strip()
                            elif i == 4:
                                tel_no5 = number.strip()
                            if len(number.strip()) != 10:
                                raise ValueError
                        if i<4:
                            for j in range(i+1,5):
                                if j==1:
                                    tel_no2 = "bos"
                                elif j==2:
                                    tel_no3 = "bos"
                                elif j==3:
                                    tel_no4 = "bos"
                                elif j==4:
                                    tel_no5 = "bos"
                except FileNotFoundError:
                    system("cls||clear")
                    print(Fore.LIGHTRED_EX + "Dosya bulunamadi. Tekrar deneyiniz.")
                    sleep(3)
                    continue
                except ValueError:
                    system("cls||clear")
                    print(Fore.LIGHTRED_EX + "Hatali telefon numarasi. Tekrar deneyiniz.")
                    sleep(3)
                    continue
            else:
                if len(tel_no) != 10:
                  raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatali telefon numarasi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsan 'enter' bas): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatali mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTGREEN_EX+"[+] "+Fore.CYAN+"Birden cok numara varsa her bir numara icin.")
            print(Fore.LIGHTYELLOW_EX + "Gonderilecek sms adeti (sonsuz ise 'enter' bas): "+ Fore.LIGHTGREEN_EX, end="")  
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatali giris yaptiniz. Tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Kac saniye araliklarla gonderilecek? : "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatali giris yaptiniz. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        if kere is not None:
             tel_numbers = [tel_no, tel_no2, tel_no3, tel_no4, tel_no5]
             bos_olmayan = len([x for x in tel_numbers if x != "bos"])
             keree = kere * bos_olmayan
        sms = SendSms(tel_no, tel_no2, tel_no3, tel_no4, tel_no5, mail)
        if isinstance(kere, int):
                  while sms.adet < kere:
                      for attribute in dir(SendSms):
                          attribute_value = getattr(SendSms, attribute)
                          if callable(attribute_value):
                              if attribute.startswith('__') == False:
                                  if sms.adet == keree or sms.adet > keree:
                                      break
                                  exec("sms."+attribute+"()")
                                  sleep(aralik)
                  print(Fore.LIGHTRED_EX + "\nMenuye donmek icin 'enter' tuşuna bas..")
                  input()
        elif kere is None: 
                  while True:
                      for attribute in dir(SendSms):
                          attribute_value = getattr(SendSms, attribute)
                          if callable(attribute_value):
                              if attribute.startswith('__') == False:
                               exec("sms."+attribute+"()")
                               sleep(aralik)
    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Cikis yapiliyor...")
        break
