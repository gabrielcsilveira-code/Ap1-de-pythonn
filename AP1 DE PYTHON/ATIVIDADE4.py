# Atividade 4: classificador de acesso para evento

print("=== CLASSIFICADOR DE ACESSO ===")

# Lê a idade e verifica se o usuário possui ingresso
idade = int(input("Digite sua idade: "))
ingresso = input("Você possui ingresso? (sim/nao): ").lower()

# Regra de acesso: menor de 16 anos é bloqueado
if idade < 16:
    print("Acesso negado. Idade mínima: 16 anos.")
# Se tiver 16 ou mais e ingresso confirmado, libera a entrada
elif idade >= 16 and ingresso == "sim":
    print("Entrada liberada!")
# Caso não tenha ingresso, pede para comprar
else:
    print("É necessário comprar um ingresso.")
