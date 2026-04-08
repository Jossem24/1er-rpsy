faturamento = 50000
porcetagem_bonus = 0.10

bonus = (faturamento*porcetagem_bonus)
faturamento_final = faturamento - bonus

print("O faturamento final é", faturamento_final)
print("O bonus é", bonus)


estoque = 250 
ventas = 78 
ingreso = 100

estoque_final = estoque - ventas + ingreso
estoque = estoque_final

print("O estoque final é:", estoque) 

caixas = 1250
suport_caminhoes = 12

total_caminhoes = caixas // suport_caminhoes
sob_caixas = caixas % suport_caminhoes

print("Poderão ir", total_caminhoes, "totalmente cheios")
print("As caixas que sobraram são", sob_caixas)


fatur = 15000
gasto = 5000
imposto = 0.15 

total_imposto = imposto * fatur
lucro = fatur - gasto - total_imposto
margem = (lucro / fatur) * 100
meta = margem > 0.3 


print(total_imposto)
print(lucro)
print(margem)
print("Meta atingida?", meta )


contrato = 40 

anos = contrato // 12
meses = contrato % 12

print(anos)
print(meses)