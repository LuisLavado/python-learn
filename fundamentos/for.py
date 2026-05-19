# palabra = "Python"
# for letra in palabra:
#     print(letra)

# frutas = ["Manzana", "Pera", "Naranja"]
# for fruta in frutas:
#     print(fruta)

# frutas = ["Manzana", "Pera", "Naranja"]
# for fruta in frutas:
#     if fruta == "Pera":
#         break
#     print(fruta)

# frutas = ["Manzana", "Pera", "Naranja"]
# for fruta in frutas:
#     if fruta == "Pera":
#         continue
#     print(fruta)
# else:
#     print("No quedan más frutas")

print("-------------------------------")
# for i in range(5):
#     print(i)

# for i in range(1, 11):
#     print(i)

# for i in range(0, 11, 2):
#     print(i)


adjetivos = ["Rica", "Saludable"]
frutas = ["Manzana", "Naranja", "Kiwi"]
for fruta in frutas:
    for adjetivo in adjetivos:
        print(f"{fruta} {adjetivo}")

for adjetivo in adjetivos:
    for fruta in frutas:
        print(fruta, adjetivo)