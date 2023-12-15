from googletrans import Translator
from colorama import init, Fore
import os
init(autoreset=True)
translator = Translator()

languages = {
    "English" : "en",
    "Russian" : "ru", 
    "Arabic" : "ar",
    "Spanish" : "es",
    "French" : "fr",
    "Japanese" : "ja",
    "Uzbek" : "uz",
    "German" : "de",
    "Turkish" : "tr"
    }

languages_name = sorted(languages)

# display
while True:
    print("------------------------------")
    print(Fore.GREEN+"[         Translator         ]")
    print("------------------------------")
    count = 1
    for i in languages_name:
        print(Fore.GREEN+f"[{count}] {i}")
        print("------------------------------")
        count+=1
    
    print(Fore.MAGENTA+"[10] Exit")
    print("------------------------------")
    
    try:
        lang = int(input(Fore.BLUE+">>> Select language: "))
        if lang == 10 or lang > 10:
            print(Fore.RED+"Leaved translator!")
            exit(0)

        text = input(Fore.BLUE+">>> Text: ")
    
    except ValueError:
        print(Fore.RED+"Please enter a number!")
        exit(1)
    
    if lang == 1:
        selection = languages.get("Arabic")
    elif lang == 2:
        selection = languages.get("English")
    elif lang == 3:
        selection = languages.get("French")
    elif lang == 4:
        selection = languages.get("German")
    elif lang == 5:
        selection = languages.get("Japanese")
    elif lang == 6:
        selection = languages.get("Russian")
    elif lang == 7:
        selection = languages.get("Spanish")
    elif lang == 8:
        selection = languages.get("Turkish")
    elif lang == 9:
        selection = languages.get("Uzbek")
    else:
        print(Fore.RED+"Wrong value")
        exit(1)
    
    translation = translator.translate(text, dest=selection)
    
    lang_to = str(translation.src)
    lang_from = str(translation.dest)
    lang_to = lang_to.upper()
    lang_from = lang_from.upper()
    
    res = translation.text
    
    # result
    print(Fore.CYAN+f'\n🟢 {lang_to} >>> {lang_from}')
    print(f'👉 {res}')
    req = input(Fore.YELLOW+"\nNew translate yes[y] no[n]: ")

    if req == "y":
        os.system("clear")
    elif req == "n":
        print(Fore.RED+"Leaved translator!")
        exit(0)
    else:
        print(Fore.RED+"Value was wrong!")
        exit(0)
        
