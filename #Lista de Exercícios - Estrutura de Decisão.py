#Lista de exercicios 

# Exercício 01
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 > num2:
    print(num1)
else:
    print(num2)

# Exercício 02
valor = float(input("Digite um valor: "))
if valor >= 0:
    print("Positivo")
else:
    print("Negativo")

# Exercício 03
sexo = input("Digite F ou M: ").upper()
if sexo == 'F':
    print("F - Feminino")
elif sexo == 'M':
    print("M - Masculino")
else:
    print("Sexo Inválido")

# Exercício 04
letra = input("Digite uma letra: ").lower()
if letra in 'aeiou':
    print("Vogal")
else:
    print("Consoante")

# Exercício 05
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1 + n2) / 2
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

# Exercício 06
a = float(input("Num 1: "))
b = float(input("Num 2: "))
c = float(input("Num 3: "))
print(max(a, b, c))

# Exercício 07
a = float(input("Num 1: "))
b = float(input("Num 2: "))
c = float(input("Num 3: "))
print(f"Maior: {max(a, b, c)}")
print(f"Menor: {min(a, b, c)}")

# Exercício 08
p1 = float(input("Preço produto 1: "))
p2 = float(input("Preço produto 2: "))
p3 = float(input("Preço produto 3: "))
if p1 < p2 and p1 < p3:
    print("Compre o produto 1")
elif p2 < p1 and p2 < p3:
    print("Compre o produto 2")
else:
    print("Compre o produto 3")

# Exercício 09
nums = []
nums.append(float(input("Num 1: ")))
nums.append(float(input("Num 2: ")))
nums.append(float(input("Num 3: ")))
nums.sort(reverse=True)
print(nums)

# Exercício 10
turno = input("Turno (M/V/N): ").upper()
if turno == 'M':
    print("Bom Dia!")
elif turno == 'V':
    print("Boa Tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")

# Exercício 11
salario = float(input("Salário atual: "))
if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
else:
    percentual = 5

aumento = salario * (percentual / 100)
novo_salario = salario + aumento
print(f"Antes: R$ {salario:.2f}")
print(f"Percentual: {percentual}%")
print(f"Aumento: R$ {aumento:.2f}")
print(f"Novo: R$ {novo_salario:.2f}")

# Exercício 12
valor_hora = float(input("Valor da hora: "))
horas_trab = float(input("Horas trabalhadas: "))
bruto = valor_hora * horas_trab

if bruto <= 900:
    ir = 0
elif bruto <= 1500:
    ir = 5
elif bruto <= 2500:
    ir = 10
else:
    ir = 20

v_ir = bruto * (ir / 100)
v_inss = bruto * 0.10
v_fgts = bruto * 0.11
total_desc = v_ir + v_inss
liquido = bruto - total_desc

print(f"Salário Bruto: R$ {bruto:.2f}")
print(f"(-) IR ({ir}%): R$ {v_ir:.2f}")
print(f"(-) INSS (10%): R$ {v_inss:.2f}")
print(f"FGTS (11%): R$ {v_fgts:.2f}")
print(f"Total de descontos: R$ {total_desc:.2f}")
print(f"Salário Liquido: R$ {liquido:.2f}")

# Exercício 13
dia = input("Dia (1-7): ")
dias = {"1":"Domingo", "2":"Segunda", "3":"Terça", "4":"Quarta", "5":"Quinta", "6":"Sexta", "7":"Sábado"}
print(dias.get(dia, "Valor inválido"))

# Exercício 14
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1 + n2) / 2
if media >= 9: conc = "A"
elif media >= 7.5: conc = "B"
elif media >= 6: conc = "C"
elif media >= 4: conc = "D"
else: conc = "E"

status = "APROVADO" if conc in "ABC" else "REPROVADO"
print(f"Notas: {n1}, {n2} | Média: {media} | Conceito: {conc} | Status: {status}")

# Exercício 15
l1 = float(input("Lado 1: "))
l2 = float(input("Lado 2: "))
l3 = float(input("Lado 3: "))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 == l3: print("Equilátero")
    elif l1 == l2 or l1 == l3 or l2 == l3: print("Isósceles")
    else: print("Escaleno")
else:
    print("Não é um triângulo")

# Exercício 16
import math
a = float(input("Valor de A: "))
if a == 0:
    print("Encerrado (não é 2º grau)")
else:
    b = float(input("Valor de B: "))
    c = float(input("Valor de C: "))
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Não possui raízes reais")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"Uma raiz real: {raiz}")
    else:
        r1 = (-b + math.sqrt(delta)) / (2*a)
        r2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Duas raízes: {r1} e {r2}")

# Exercício 17
ano = int(input("Ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Bissexto")
else:
    print("Não é bissexto")

# Exercício 18
data = input("Data (dd/mm/aaaa): ")
try:
    dia, mes, ano = map(int, data.split('/'))
    import datetime
    datetime.datetime(ano, mes, dia)
    print("Data Válida")
except:
    print("Data Inválida")

# Exercício 19
num = int(input("Número (<1000): "))
c = num // 100
d = (num % 100) // 10
u = num % 10
saida = []
if c > 0: saida.append(f"{c} centena" + ("s" if c > 1 else ""))
if d > 0: saida.append(f"{d} dezena" + ("s" if d > 1 else ""))
if u > 0: saida.append(f"{u} unidade" + ("s" if u > 1 else ""))
print(", ".join(saida[:-1]) + (" e " if len(saida) > 1 else "") + saida[-1] if saida else "0")

# Exercício 20
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
media = (n1 + n2 + n3) / 3
if media == 10: print(f"Aprovado com Distinção ({media})")
elif media >= 7: print(f"Aprovado ({media})")
else: print(f"Reprovado ({media})")

# Exercício 21
saque = int(input("Valor (10-600): "))
if 10 <= saque <= 600:
    notas = [100, 50, 10, 5, 1]
    for n in notas:
        qtd = saque // n
        saque %= n
        if qtd > 0: print(f"{qtd} nota(s) de R$ {n}")
else:
    print("Valor fora do limite")

# Exercício 22
num = int(input("Número: "))
print("Par" if num % 2 == 0 else "Ímpar")

# Exercício 23
num = float(input("Número: "))
print("Inteiro" if num == round(num) else "Decimal")

# Exercício 24
n1 = float(input("Num 1: "))
n2 = float(input("Num 2: "))
op = input("Operação (+, -, *, /): ")
res = eval(f"{n1} {op} {n2}")
p_i = "Par" if res % 2 == 0 else "Ímpar"
p_n = "Positivo" if res >= 0 else "Negativo"
i_d = "Inteiro" if res == round(res) else "Decimal"
print(f"Resultado: {res} ({p_i}, {p_n}, {i_d})")

# Exercício 25
p1 = input("Telefonou para a vítima? ").lower()
p2 = input("Esteve no local do crime? ").lower()
p3 = input("Mora perto da vítima? ").lower()
p4 = input("Devia para a vítima? ").lower()
p5 = input("Já trabalhou com a vítima? ").lower()
resp = [p1, p2, p3, p4, p5].count("sim")
if resp == 5: print("Assassino")
elif resp >= 3: print("Cúmplice")
elif resp == 2: print("Suspeita")
else: print("Inocente")

# Exercício 26
litros = float(input("Litros: "))
tipo = input("Tipo (A/G): ").upper()
if tipo == 'A':
    preco = 1.90
    desc = 0.03 if litros <= 20 else 0.05
else:
    preco = 2.50
    desc = 0.04 if litros <= 20 else 0.06
total = litros * preco * (1 - desc)
print(f"Total: R$ {total:.2f}")

# Exercício 27
kg_mo = float(input("Kg Morango: "))
kg_ma = float(input("Kg Maçã: "))
p_mo = 2.50 if kg_mo <= 5 else 2.20
p_ma = 1.80 if kg_ma <= 5 else 1.50
total_kg = kg_mo + kg_ma
total_rs = (kg_mo * p_mo) + (kg_ma * p_ma)
if total_kg > 8 or total_rs > 25:
    total_rs *= 0.90
print(f"Valor a pagar: R$ {total_rs:.2f}")

# Exercício 28
print("1-File Duplo / 2-Alcatra / 3-Picanha")
tipo = input("Escolha o tipo: ")
qtd = float(input("Quantidade (Kg): "))
cartao = input("Cartão Tabajara? (S/N): ").upper()

precos = {"1": (4.90, 5.80), "2": (5.90, 6.80), "3": (6.90, 7.80)}
nomes = {"1": "File Duplo", "2": "Alcatra", "3": "Picanha"}

p_unit = precos[tipo][0] if qtd <= 5 else precos[tipo][1]
total = qtd * p_unit
desconto = total * 0.05 if cartao == 'S' else 0

print("\n--- CUPOM FISCAL ---")
print(f"Tipo: {nomes[tipo]}")
print(f"Qtd: {qtd}Kg")
print(f"Preço Total: R$ {total:.2f}")
print(f"Pagamento: {'Cartão Tabajara' if cartao == 'S' else 'Dinheiro'}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a Pagar: R$ {total - desconto:.2f}")

