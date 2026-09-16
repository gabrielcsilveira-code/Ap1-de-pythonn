# Atividade 2: cálculo do subtotal e do total com desconto

print("=== CARRINHO DE COMPRAS ===")

# Dados do produto
preco = 35.00
quantidade = 2
desconto = 10.00

# Cálculo do valor antes e depois do desconto
subtotal = preco * quantidade
total = subtotal - desconto

# Exibe os dados do carrinho
print(f"Preço: R$ {preco:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total: R$ {total:.2f}")