from src.products import create_product, get_products
from src.customers import create_customer, get_customers


# Cadastra um cliente de teste
customer_id = create_customer(
    "Cliente Teste",
    "cliente.teste2@email.com"
)

# Cadastra dois produtos de teste
product_id_1 = create_product("Teclado", 150.00, 20)
product_id_2 = create_product("Mouse", 80.00, 15)

print("Cliente cadastrado:", customer_id)
print("Produtos cadastrados:", product_id_1, product_id_2)

print("\nClientes:")
for customer in get_customers():
    print(dict(customer))

print("\nProdutos:")
for product in get_products():
    print(dict(product))
    
from src.sales import create_sale


# Produtos que serão vendidos
items = [
    {"product_id": product_id_1, "quantity": 2},
    {"product_id": product_id_2, "quantity": 3}
]

# Registra a venda
sale_id = create_sale(customer_id, items)

print("\nVenda registrada com sucesso!")
print("ID da venda:", sale_id)