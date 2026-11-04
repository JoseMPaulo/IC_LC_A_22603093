CAPACIDADE = 30
PESO_MAXIMO_ITEM = 20

itens = ["Espada", "Escudo", "Poção"]
pesos = [8, 10, 1]

print ("===== MOCHILA DO AVENTUREIRO =====")
print("1 - Ver mochila")
print("2 - Guardar item")
print("3 - sair")

menu = input("Qual a sua escolha: ")
captotal = pesos[0] + pesos[1] + pesos[2]
porcentagem = int((captotal / 30) * 100)
if (menu == "1"): 
 print(itens[0], " (", pesos[0], ")")
 print(itens[1], " (", pesos[1], ")")
 print(itens[2], " (", pesos[2], ")")
 print(captotal,"/30" )
 print( porcentagem, ("%"))
 if captotal >=  27:
     print("Quase cheio")
 elif captotal >= 15:
     print("A meio")
 else:
         print("Com espaço")
elif (menu == "2"):
    item = str(input("Qual o item a adicionar: "))
    peso = int(input("Qual o seu peso: "))
    while peso > 20:      
     if peso <= 20:
        print(item," guardado")
     else:
        print("Peso inválido. Tente novamente.")
    if peso + captotal > 30:
       print("Não Cabe!")
       print("Espaço livre: ", CAPACIDADE - captotal)     
elif (menu == "3"):
    print("Boa Aventura!")

else:
    print("Opção inválida")



