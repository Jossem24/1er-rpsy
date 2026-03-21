

faturamento = 50000
bonus = 0.10    

r_bonus = faturamento * bonus 
print("O valor do bonus é:", r_bonus )

r_faturamento = faturamento - r_bonus
print("O faturamento final é:", r_faturamento)





cels = 250
ventas = 78
ingressos = 100

estoque = cels - ventas
print("O estoque é:", estoque)

estoque_final = estoque + ingressos
print("O estoque final é:", estoque_final)







caixas = 1250
sup_caminhões = 12

caminhões = caixas // sup_caminhões
sobra_caixas = caixas % sup_caminhões

print(caminhões, "Irão totalmente cheios")
print(sobra_caixas, "caixas sobram" )