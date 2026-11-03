from src.database import get_connection


with get_connection() as connection:
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            sales.id,
            customers.name AS customer,
            sales.total,
            products.name AS product,
            sale_items.quantity,
            sale_items.unit_price
        FROM sales
        JOIN customers ON sales.customer_id = customers.id
        JOIN sale_items ON sales.id = sale_items.sale_id
        JOIN products ON sale_items.product_id = products.id
        WHERE sales.id = 1
        """
    )

    results = cursor.fetchall()

    print("DETALHES DA VENDA")

    for item in results:
        print(dict(item))

    cursor.execute(
        """
        SELECT id, name, stock
        FROM products
        WHERE id IN (4, 5)
        """
    )

    products = cursor.fetchall()

    print("\nESTOQUE ATUALIZADO")

    for product in products:
        print(dict(product))