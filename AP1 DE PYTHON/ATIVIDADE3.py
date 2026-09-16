# Atividade 3: recibo de compra com entrada de dados do usuário

print("=== RECIBO DE COMPRA ===")

# Coleta as informações básicas da compra
cliente = input("Nome do cliente: ")
produto = input("Produto: ")
preco = float(input("Preço: R$ "))
quantidade = int(input("Quantidade: "))
desconto = float(input("Desconto: R$ "))

# Calcula o valor antes e depois do desconto
subtotal = preco * quantidade
total = subtotal - desconto

# Exibe o resumo da compra
print("\n--- RESUMO DA COMPRA ---")
print(f"Cliente: {cliente}")
print(f"Produto: {produto}")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total:.2f}")
print("Obrigado pela compra!")