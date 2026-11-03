
from src.database import get_connection


def create_sale(customer_id, items):
    """Registra uma venda e atualiza o estoque dos produtos."""

    if not isinstance(customer_id, int) or isinstance(customer_id, bool) or customer_id <= 0:
        raise ValueError("O ID do cliente deve ser um número inteiro positivo.")

    if not isinstance(items, list) or not items:
        raise ValueError("A venda precisa conter pelo menos um produto.")

    for item in items:
        if not isinstance(item, dict):
            raise ValueError("Cada item da venda deve ser um dicionário.")

        if "product_id" not in item or "quantity" not in item:
            raise ValueError("Cada item precisa ter product_id e quantity.")

        product_id = item["product_id"]
        quantity = item["quantity"]

        if not isinstance(product_id, int) or isinstance(product_id, bool) or product_id <= 0:
            raise ValueError("O ID do produto deve ser um número inteiro positivo.")

        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            raise ValueError("A quantidade deve ser um número inteiro positivo.")

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id FROM customers
            WHERE id = ?
            """,
            (customer_id,)
        )

        customer = cursor.fetchone()

        if customer is None:
            raise ValueError("Cliente não encontrado.")

        products_data = []

        for item in items:
            product_id = item["product_id"]
            quantity = item["quantity"]

            cursor.execute(
                """
                SELECT id, name, price, stock
                FROM products
                WHERE id = ?
                """,
                (product_id,)
            )

            product = cursor.fetchone()

            if product is None:
                raise ValueError(
                    f"Produto com ID {product_id} não encontrado."
                )

            if product["stock"] < quantity:
                raise ValueError(
                    f"Estoque insuficiente para o produto {product['name']}."
                )

            products_data.append({
                "product_id": product["id"],
                "quantity": quantity,
                "unit_price": product["price"]
            })

        # Calcula o valor total da venda
        total = 0

        for product in products_data:
            subtotal = product["unit_price"] * product["quantity"]
            total += subtotal

        # Registra a venda
        cursor.execute(
            """
            INSERT INTO sales (customer_id, total)
            VALUES (?, ?)
            """,
            (customer_id, total)
        )

        sale_id = cursor.lastrowid

        # Registra os produtos da venda
        for product in products_data:
            cursor.execute(
                """
                INSERT INTO sale_items (
                    sale_id,
                    product_id,
                    quantity,
                    unit_price
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    sale_id,
                    product["product_id"],
                    product["quantity"],
                    product["unit_price"]
                )
            )

        # Atualiza o estoque
        for product in products_data:
            cursor.execute(
                """
                UPDATE products
                SET stock = stock - ?
                WHERE id = ? AND stock >= ?
                """,
                (
                    product["quantity"],
                    product["product_id"],
                    product["quantity"]
                )
            )

            if cursor.rowcount == 0:
                raise ValueError(
                    f"Não foi possível atualizar o estoque do produto "
                    f"ID {product['product_id']}."
                )

        return sale_id
    
    
def get_sales():
    """Consulta todas as vendas registradas no sistema."""

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT * FROM sales
            """
        )

        sales = cursor.fetchall()

        return sales
    
def get_sale_by_id(sale_id):
    """Consulta uma venda específica pelo seu ID."""
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT * FROM sales
            WHERE id = ?
            """,
            (sale_id,)
        )

        sale = cursor.fetchone()

        return sale
    
def get_sale_items(sale_id):
    """Consulta os produtos e detalhes de uma venda."""
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                sale_items.product_id,
                products.name,
                sale_items.quantity,
                sale_items.unit_price
            FROM sale_items
            INNER JOIN products
                ON sale_items.product_id = products.id
            WHERE sale_items.sale_id = ?
            """,
            (sale_id,)
        )
        
        items = cursor.fetchall()

        return items
    
def get_customer_sales(customer_id):
    """Consulta o histórico de compras de um cliente."""

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                sales.id,
                sales.customer_id,
                customers.name AS customer_name,
                sales.total,
                sales.sale_date
            FROM sales
            INNER JOIN customers
                ON sales.customer_id = customers.id
            WHERE sales.customer_id = ?
            ORDER BY sales.sale_date DESC
            """,
            (customer_id,)
        )

        sales = cursor.fetchall()

        return sales
