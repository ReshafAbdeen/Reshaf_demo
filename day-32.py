# Humne ek single function banaya jo dono ko accept karega
def shadi_ka_function(*args, **kwargs):
    
    print("============ 🟢 *ARGS KA KHEL (Bina Naam Wale Mehman) ============")
    print(f"Raw args dabba: {args}") # Yeh background me Tuple dikhayega
    
    # Ab jitne bhi mehman aaye hain unka naam ek-ek karke pukarenge
    print("Mehmano ki entry ho rahi hai:")
    for mehman in args:
        print(f"-> Khushamdeed, {mehman} bhai!")
        
    print(f"\nTotal kitne log aaye bina bataye? Total: {len(args)}\n")


    print("============ 🟠 **KWARGS KA KHEL (Naam + Gift Wale VIPs) ============")
    print(f"Raw kwargs dabba: {kwargs}") # Yeh background me Dictionary dikhayega
    
    # Dictionary hai toh .items() lagakar Key (Naam) aur Value (Gift) nikalenge
    for naam, gift in kwargs.items():
        print(f"-> {naam} ne toh bada mast gift diya: {gift}")

# --- 🚀 AB FUNCTION KO CALL KARTE HAIN ---

# Shuruat me humne sirf 3 dosto ke naam diye (Yeh jayenge *args me)
# Baad me humne 'Naam=Gift' ka joda diya (Yeh jayenge **kwargs me)
shadi_ka_function("Rahul", "Amit", "Salman", Imran="iPhone 15", Sonu="Silver Ring")