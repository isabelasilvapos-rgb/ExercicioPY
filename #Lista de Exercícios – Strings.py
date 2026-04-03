#Lista de Exercícios – Strings

# 1
s1 = input("String 1: ")
s2 = input("String 2: ")
print(f'"{s1}": {len(s1)} caracteres')
print(f'"{s2}": {len(s2)} caracteres')
print("Mesmo tamanho" if len(s1) == len(s2) else "Tamanhos diferentes")
print("Conteúdo igual" if s1 == s2 else "Conteúdo diferente")

# 2
nome = input("Digite seu nome: ")
print(nome[::-1].upper())

# 3
nome = input("Digite seu nome: ")
for letra in nome:
    print(letra)

# 4
nome = input("Digite seu nome: ")
for i in range(1, len(nome) + 1):
    print(nome[:i].upper())

# 5
nome = input("Digite seu nome: ")
for i in range(len(nome), 0, -1):
    print(nome[:i].upper())

# 6
data = input("Data (dd/mm/aaaa): ")
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
d, m, a = data.split('/')
print(f"{d} de {meses[int(m)-1]} de {a}")

# 7
frase = input("Digite uma frase: ")
espacos = frase.count(" ")
vogais = sum(frase.lower().count(v) for v in "aeiouáéíóúâêîôûãõ")
print(f"Espaços: {espacos}, Vogais: {vogais}")

# 8
texto = input("Digite a sequência: ").replace(" ", "").lower()
if texto == texto[::-1]:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")

# 9
cpf = input("CPF (xxx.xxx.xxx-xx): ").replace('.', '').replace('-', '')
if len(cpf) == 11 and cpf.isdigit():
    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(i))
        digito = (soma * 10 % 11) % 10
        if digito != int(cpf[i]):
            print("CPF Inválido")
            break
    else:
        print("CPF Válido")
else:
    print("Formato inválido")

# 10
nums_texto = {
    0: "zero", 1: "um", 2: "dois", 3: "três", 4: "quatro", 5: "cinco", 6: "seis", 7: "sete", 8: "oito", 9: "nove",
    10: "dez", 11: "onze", 12: "doze", 13: "treze", 14: "quatorze", 15: "quinze", 16: "dezesseis", 17: "dezessete", 18: "dezoito", 19: "dezenove",
    20: "vinte", 30: "trinta", 40: "quarenta", 50: "cinquenta", 60: "sessenta", 70: "setenta", 80: "oitenta", 90: "noventa"
}
n = int(input("Número até 99: "))
if n in nums_texto:
    print(nums_texto[n])
else:
    print(f"{nums_texto[(n//10)*10]} e {nums_texto[n%10]}")

# 11
palavra = "PYTHON"
digitadas = []
erros = 0
while True:
    exibicao = "".join([l if l in digitadas else "_" for l in palavra])
    print(f"Palavra: {exibicao} | Erros: {erros}/6")
    if "_" not in exibicao or erros == 6: break
    tentativa = input("Letra: ").upper()
    if tentativa in palavra: digitadas.append(tentativa)
    else: erros += 1
print("Ganhou!" if erros < 6 else f"Perdeu! A palavra era {palavra}")

# 12
tel = input("Telefone: ").replace("-", "")
if len(tel) == 7:
    tel = "3" + tel
    print(f"Telefone corrigido: 3{tel[1:4]}-{tel[4:]}")
elif len(tel) == 8:
    print(f"Telefone: {tel[:4]}-{tel[4:]}")

# 13
import random
p_original = "BANANA"
p_lista = list(p_original)
random.shuffle(p_lista)
print(f"Descubra a palavra: {''.join(p_lista)}")
chute = input("Seu chute: ").upper()
print("Acertou!" if chute == p_original else "Errou!")

# 14
leet_dict = {'a':'4', 'e':'3', 'i':'1', 'o':'0', 't':'7', 's':'5'}
texto_l = input("Texto: ").lower()
for k, v in leet_dict.items():
    texto_l = texto_l.replace(k, v)
print(texto_l)