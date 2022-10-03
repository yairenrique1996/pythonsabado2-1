#entrada del problema 
nivelAgua=int(input("digite el nivel de agua de la presa: "))

#proceso del problema 
if(nivelAgua >=0 and nivelAgua < 20):
    print(f"el nivel del agua {nivelAgua} es muy bajo") 

elif(nivelAgua >= 20 and nivelAgua < 400):
    print(f"el nivel de agua es {nivelAgua} es optimo")   

elif(nivelAgua >= 400):
    print(f"el nivel del agua {nivelAgua} es muy alto")

else:
    print("digite una opcion valida")           
