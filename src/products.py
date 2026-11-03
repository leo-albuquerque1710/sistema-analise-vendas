
from src.database import get_connection


def create_product(name, price, stock):
    """Cadastra um novo produto no banco de dados."""

    if not name or not name.strip():
        raise ValueError("O nome do produto é obrigatório.")

    if price < 0:
        raise ValueError("O preço não pode ser negativo.")

    if stock < 0:
        raise ValueError("O estoque não pode ser negativo.")

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO products (name, price, stock)
            VALUES (?, ?, ?)
            """,
            (name.strip(), price, stock)
        )

        product_id = cursor.lastrowid

        return product_id


def get_products():
    """Consulta todos os produtos cadastrados."""

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT * FROM products
            """
        )

        products = cursor.fetchall()

        return products


def get_product_by_id(product_id):
    """Consulta um produto específico pelo seu ID."""

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT * FROM products
            WHERE id = ?
            """,
            (product_id,)
        )

        product = cursor.fetchone()

        return product
    
def update_product(product_id, name, price, stock):
    """Atualiza as informações de um produto."""

    if not name or not name.strip():
        raise ValueError("O nome do produto é obrigatório.")

    if price < 0:
        raise ValueError("O preço não pode ser negativo.")

    if stock < 0:
        raise ValueError("O estoque não pode ser negativo.")

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE products
            SET name = ?, price = ?, stock = ?
            WHERE id = ?
            """,
            (name.strip(), price, stock, product_id)
        )

        return cursor.rowcount
def delete_product(product_id):
    """Exclui um produto do banco de dados pelo ID."""

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM products
            WHERE id = ?
            """,
            (product_id,)
        )

        return cursor.rowcount

