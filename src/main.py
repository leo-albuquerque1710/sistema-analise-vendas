
from database import create_tables
from products import create_product


def main():
    create_tables()

    product_id = create_product(
        name="Teclado Mecânico",
        price=199.90,
        stock=15
    )

    print(f"Produto cadastrado com sucesso! ID: {product_id}")


if __name__ == "__main__":
    main()
