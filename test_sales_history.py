from src.sales import (
    get_sales,
    get_sale_by_id,
    get_sale_items,
    get_customer_sales
)

# Consulta todas as vendas
sales = get_sales()

print("HISTÓRICO DE VENDAS")

for sale in sales:
    print(dict(sale))


# Consulta uma venda específica
sale = get_sale_by_id(1)

print("\nVENDA ESPECÍFICA")

if sale:
    print(dict(sale))
else:
    print("Venda não encontrada.")
    
# Consulta os produtos de uma venda
items = get_sale_items(1)

print("\nPRODUTOS DA VENDA")

for item in items:
    print(dict(item))
    
# Consulta o histórico de compras de um cliente
customer_sales = get_customer_sales(3)

print("\nHISTÓRICO DO CLIENTE")

print("Quantidade de vendas encontradas:", len(customer_sales))
print("Resultado da consulta:", customer_sales)

for sale in customer_sales:
    print(dict(sale))