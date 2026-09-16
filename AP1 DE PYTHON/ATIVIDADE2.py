print("=== CARRINHO DE COMPRAS ===")

preco = 35.00
quantidade = 2
desconto = 10.00

subtotal = preco * quantidade
total = subtotal - desconto

print(f"Preço: R$ {preco:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total: R$ {total:.2f}")