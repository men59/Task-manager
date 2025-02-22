



úkoly = []

def hlavi_nemu():
    print("")
    print("Správce úkolů - Hlavní menu")
    print("1. Přidat nový úkol") 
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol ")
    print("4. Konec programu ")
    print("")
    return int(input( "Vyberte možnost (1 - 4):"))

def pridat_ukol(nazev,popis):
    
    if not nazev.strip() or not popis.strip():
        print("Zadal prázdný vstup. Zkus to znovu!")
    else:                        
        úkoly.append(nazev + "-" + popis)
        print(f"Úkol '{nazev}' byl přidán.")
        
    return 
    


def zobrazit_ukoly():
    if úkol in úkoly:
        print()
    return len(úkoly)


def odstranit_ukol (čislo_úkolu):
    print(úkoly)
    čislo_úkolu= int(input("Zadejte čislo úkolu,který chcete odstranit:"))
    if len(úkoly) >= čislo_úkolu > 0:
    
        del(úkoly[čislo_úkolu - 1])
        print("Úkol", čislo_úkolu , "byl odstraněn.")
    elif čislo_úkolu <= 0:
        print("Vybraly špatný úkol")
    else:    
        print("Vybraly špatný úkol")
    return 
         
   
    
loop = 1
úkol = 0
while loop == 1:
    úkol = hlavi_nemu()
    if úkol == 1:
        print("1. Přidat nový úkol")
        pridat_ukol(input("Zadejte název úkolu:"),input("Zadejte popis úkolu:"))
    
    elif úkol == 2:
        print("2. Zobrazit všechny úkoly")
        print("Seznam úloh:")
        print(úkoly)
    elif úkol == 3:
        print("3. Odstranit úkol ")
        odstranit_ukol(čislo_úkolu=int)

    elif úkol == 4:
        print(" Konec programu ")
        loop = 0

    else :
        print("To neni spravna možnost. Zkus to znovu! ")
        