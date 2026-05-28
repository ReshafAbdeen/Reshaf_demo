import random

def play_kbc():
    print("====================================================")
    print("\n\033[1mWelcome to koun banega crorepate(KBC)!\033[0m\n")
    print("====================================================")

    sawaal_bank = [{
        'sawaal': "India ka sabse bada individual Youtuber kon hai ?",
        'options':"A)MrBeast   B)Techinical Guruji\nC) Elvish Yadav   D) Carryminati",
        'sahi': 'D'

    },
    {
         'sawaal': "Python me datafrmae banae ke liye konsi library use hoti hai ? ?",
        'options':"A)Pandas   B)Tabulate\nC) Matplotlib  D) Turtle",
        'sahi': 'A'

    },
   {
        "sawaal": "NumPy ka asly kaam kis cheez par hota hai?",
        "options": "A) Arrays/Matrix  B) Web Scraping  C) UI Design  D) Game Development",
        "sahi": "A"  
    }]  
    
    suruat = 1
    paise = 0

    for q in sawaal_bank:
        print(f"\nSawaal number {suruat}: {q['sawaal']}" )
        print(q['options'])
        jawab = input("Apka jawab kiya hai (A/B/C/D) YA Quite likho : ").upper()
        if jawab == 'QUIT':
            print(f"Aapne game quite kar diya hai. Rs{paise} lekar gahr ja rhe hai.")
            break
        elif jawab == q['sahi']:
            paise += 1000
            print("Aapka jawab sahi hai! aap 1000 rupees jeet gye .")
            suruat += 1
        else:
            print(f"Soory glat jawab! sahi option {q['sahi']} tah.\nAap rs{paise} lekar ghar ja rhe hai.")
            paise = 0
            break
    print(f"Aap itne paise lekar ghar ja rhe hai: Rs{paise}")
    print("===============================")
    print("\n\033[1mGame over!\033[0m\n")
    print("=================================")

play_kbc()