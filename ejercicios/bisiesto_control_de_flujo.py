while True:
    try:
        a= int(input("Dame un numero entero:  "))
        if a ==1:
            print("es bisiesto")
        else:
            print("no es bisiesto")
        b= input("Quieres finalizar?")
        if b == "SI":
            break
        else:
            continue
    except:
        print("chingas a tu madre")