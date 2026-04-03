#Lista de Exercícios – Estrutura Sequencial

# 1
print('Alô mundo')

# 2
numero = input('Digite um número: ')
print(f'O número informado foi {numero}')

# 3
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
print(f'A soma é: {n1 + n2}')

# 4
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
nota4 = float(input('Nota 4: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A média é: {media}')

# 5
metros = float(input('Digite o valor em metros: '))
centimetros = metros * 100
print(f'{metros}m equivale a {centimetros}cm')

# 6
raio = float(input('Raio do círculo: '))
area = 3.14159 * (raio ** 2)
print(f'A área é: {area:.2f}')

# 7
lado = float(input('Lado do quadrado: '))
area_quad = lado ** 2
print(f'O dobro da área é: {area_quad * 2}')

# 8
valor_hora = float(input('Quanto ganha por hora? '))
horas_mes = float(input('Horas trabalhadas no mês? '))
print(f'Salário total: R$ {valor_hora * horas_mes:.2f}')

# 9
f = float(input('Temperatura em Fahrenheit: '))
c = 5 * ((f - 32) / 9)
print(f'Celsius: {c:.2f}°C')

# 10
celsius = float(input('Temperatura em Celsius: '))
fahrenheit = (celsius * 9/5) + 32
print(f'Fahrenheit: {fahrenheit:.2f}°F')

# 11
i1 = int(input('Inteiro 1: '))
i2 = int(input('Inteiro 2: '))
r1 = float(input('Real: '))
res_a = (i1 * 2) * (i2 / 2)
res_b = (i1 * 3) + r1
res_c = r1 ** 3
print(f'A: {res_a}\nB: {res_b}\nC: {res_c}')

# 12
gb = float(input('Valor em GB: '))
mb = gb * 1024
print(f'{gb} GB = {mb} MB')

# 13
gb_ent = float(input('Valor em GB: '))
mb_conv = gb_ent * 1024
kb_conv = mb_conv * 1024
print(f'{gb_ent} GB = {mb_conv} MB e {kb_conv} KB')

# 14
peso = float(input('Peso de peixes (kg): '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    excesso = 0
    multa = 0
print(f'Excesso: {excesso}kg | Multa: R$ {multa:.2f}')

# 15
valor_h = float(input('Ganha por hora: '))
horas_m = float(input('Horas no mês: '))
bruto = valor_h * horas_m
ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
liquido = bruto - ir - inss - sindicato
print(f'Bruto: R$ {bruto:.2f}\nIR: R$ {ir:.2f}\nINSS: R$ {inss:.2f}\nSindicato: R$ {sindicato:.2f}\nLíquido: R$ {liquido:.2f}')

# 16
import math
area_pintar = float(input('Área em m²: '))
litros_nec = area_pintar / 3
latas = math.ceil(litros_nec / 18)
print(f'Comprar {latas} latas. Total: R$ {latas * 80:.2f}')

# 17
import math
area_m2 = float(input('Área em m²: '))
litros_folga = (area_m2 / 6) * 1.1

latas_apenas = math.ceil(litros_folga / 18)
galoes_apenas = math.ceil(litros_folga / 3.6)

mix_latas = int(litros_folga // 18)
resto = litros_folga % 18
mix_galoes = math.ceil(resto / 3.6)

print(f'Opção 1 (Só latas): {latas_apenas} unidades - R$ {latas_apenas * 80}')
print(f'Opção 2 (Só galões): {galoes_apenas} unidades - R$ {galoes_apenas * 25}')
print(f'Opção 3 (Misto): {mix_latas} latas e {mix_galoes} galões - R$ {(mix_latas * 80) + (mix_galoes * 25)}')

# 18
tamanho_mb = float(input('Tamanho do arquivo (MB): '))
vel_internet = float(input('Velocidade (Mbps): '))
tempo_segundos = tamanho_mb / (vel_internet / 8)
tempo_minutos = tempo_segundos / 60
print(f'Tempo aproximado: {tempo_minutos:.2f} minutos')