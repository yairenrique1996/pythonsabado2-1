mes = input("ingrese el mes ")

if(mes == "enero" or mes == "febrero" or mes == "marzo"):
    print(f"el mes {mes} es de invierno") 

elif(mes == "abril" or mes == "mayo" or mes == "junio"):
    print(f"el mes {mes} es de primavera")     


elif(mes == "julio" or mes == "agosto" or mes == "septiembre"):
    print(f"el mes {mes} es de verano")         

elif(mes == "octubre" or mes == "noviembre" or mes == "diciembre"):
    print(f"el mes {mes} es otoño")    

else: 
    print("el dato es invalido")       