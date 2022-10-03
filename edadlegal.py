edad = int(input("cual es tu edad "))

if (edad <= 0 or edad >= 500 ):
    print("usted no existe ")

elif(edad >=0 and edad <= 14):
    print("usted es un joven")

elif(edad > 14 and edad <= 28):
    print("eres un adulto")    

elif(edad > 28 and edad <= 60):
    print("ya pagas impuesto ")

elif(edad > 60 ):
    print("eres adulto mayor")            