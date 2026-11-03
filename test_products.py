from src.products import delete_product, get_product_by_id


# Excluindo o produto de ID 1
result = delete_product(1)

if result == 1:
    print("Produto excluído com sucesso!")
else:
    print("Produto não encontrado.")


# Verificando se o produto realmente foi excluído
product = get_product_by_id(1)

if product is None:
    print("Confirmação: o produto não existe mais no banco.")
else:
    print("O produto ainda está cadastrado.")