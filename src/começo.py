


#exercicio 1

faturamento_total = 50000
bonus = 0.1 
bonus_final = faturamento_total * bonus
faturamento_final = faturamento_total - bonus_final 

print("faturamento_final", faturamento_final)
print("bonus_final", bonus_final)

#exercicio 2 

unidades_cel = 250 
ventas_do_dia = 78

estoque = unidades_cel - ventas_do_dia 
mercaderia_nova = 100

estoque_final = estoque + mercaderia_nova 

print("estoque_final", estoque_final)

#exercicio 3 

total_caixas = 1250
caminhões_cap = 12

caminhões_cheios = total_caixas // caminhões_cap 
sobra_caixas = total_caixas % caminhões_cap
print("Los caminhões que vão cheios são", caminhões_cheios)
print("A cantidade de caixas que sobram são", sobra_caixas)


#exercicio 3.1 

print("Olá senhor temos caixas pra levar sua mercancia, cada caminhõe pode levar até 12 caixas")
caixas = int(input("Quantas caixas voce vai transportar? "))
capacidade = 12 

T = caixas // capacidade 
sobra = caixas % capacidade 

print("Voce pode levar:", T)
print("O que sobra é:", sobra ) 

# exercicio 4 

faturamento1 = 15000
custos = 5000

imposto = faturamento1 * 0.15 
lucro = faturamento1 - custos - imposto

print("O imposto é de:", imposto)
print("O lucro foi de:", lucro) 

margem_lucro = lucro / faturamento1 
print("A margem de lucro é:", margem_lucro)

meta_atingida = margem_lucro > 0.30 
print("Meta atingida?", meta_atingida)



# exercicio 5


duração = 40
anos = duração // 12 
meses = duração % 12

print(anos)
print(meses)