from src.database import get_connection


def create_customer(name, email):
    """Cadastra um novo cliente no banco de dados."""

    if not name or not name.strip():
        raise ValueError("O nome do cliente é obrigatório.")

    if email:
        email = email.strip()

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO customers (name, email)
            VALUES (?, ?)
            """,
            (name.strip(), email)
        )

        customer_id = cursor.lastrowid

        return customer_id
def get_customers():
    """Consulta todos os clientes cadastrados."""

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT * FROM customers
            """
        )

        customers = cursor.fetchall()

        return customers
def get_customer_by_id(customer_id):
    """Consulta um cliente específico pelo seu ID."""

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT * FROM customers
            WHERE id = ?
            """,
            (customer_id,)
        )

        customer = cursor.fetchone()

        return customer
def update_customer(customer_id, name, email):
    """Atualiza as informações de um cliente."""

    if not name or not name.strip():
        raise ValueError("O nome do cliente é obrigatório.")

    if email:
        email = email.strip()

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE customers
            SET name = ?, email = ?
            WHERE id = ?
            """,
            (name.strip(), email, customer_id)
        )

        return cursor.rowcount
def delete_customer(customer_id):
    """Exclui um cliente do banco de dados pelo ID."""

    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM customers
            WHERE id = ?
            """,
            (customer_id,)
        )

        return cursor.rowcount