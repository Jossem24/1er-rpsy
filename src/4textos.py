#Textos





faturamento = 1000
custo = 200

lucro = faturamento - custo

texto = f"O lucro foi de {lucro} e o faturamento foi de {faturamento}"
print(texto)



email = "PAPArilo@GMAIL.COM"

email = email.upper()
print(email)



gano = 45000
gasto = 23500

gano_final = gano - gasto
margem = gano_final / gano

texto = f"O lucro foi de {gano_final:.2f} e a margem foi de {margem:.0%}"
print(texto)




foco = email.find("@")
print(foco)

lugar = email[:foco]
print(lugar)


email = email.replace("@GMAIL.COM", "@yahoo.com")
print(email)