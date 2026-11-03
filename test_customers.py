from src.customers import delete_customer, get_customer_by_id


result = delete_customer(1)

if result == 1:
    print("Cliente excluído com sucesso!")
else:
    print("Cliente não encontrado.")


customer = get_customer_by_id(1)

if customer is None:
    print("Confirmação: o cliente não existe mais no banco.")
else:
    print("O cliente ainda está cadastrado.")