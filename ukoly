ukoly = []

def hlavi_nemu():
    print("\nSprávce úkolů - Hlavní menu")
    print("1. Přidat nový úkol") 
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol ")
    print("4. Konec programu ")
    return int(input("Vyberte možnost (1 - 4): "))

def pridat_ukol(nazev, popis):
    if not nazev.strip() or not popis.strip():
        print("Zadal prázdný vstup. Zkus to znovu!")
        return
    
    i = len(ukoly) + 1  
    ukoly.append({'cislo_ukolu': i, 'ukol': nazev, 'popis': popis})
    print(f"{i}. Úkol '{nazev}' byl přidán.") 

def zobrazit_ukoly():
    if not ukoly:
        print("Žádné úkoly nejsou k dispozici.")
        return
    
    print("\nSeznam úkolů:")
    for u in ukoly:
        print(f"{u['cislo_ukolu']}: {u['ukol']} - {u['popis']}")

def odstranit_ukol():
    
    if not ukoly:
        print("Seznam úkolů je prázdný.")
        return
    
    cislo_ukolu = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
    
    if 1 <= cislo_ukolu <= len(ukoly):
        del ukoly[cislo_ukolu - 1]
        
        for i, u in enumerate(ukoly, start=1):
            u['cislo_ukolu'] = i
        
        print(f"Úkol {cislo_ukolu} byl odstraněn.")
    else:
        print("Vybrali jste špatný úkol.")

loop = True
while loop:
    ukol = hlavi_nemu()
    
    if ukol == 1:
        pridat_ukol(input("Zadejte název úkolu: "), input("Zadejte popis úkolu: "))
    
    elif ukol == 2:
        zobrazit_ukoly()
        
    elif ukol == 3:
        odstranit_ukol()
    
    elif ukol == 4:
        print("Konec programu")
        loop = False

    else:
        print("To není správná možnost. Zkus to znovu!")
