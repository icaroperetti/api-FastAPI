from sqlalchemy import MetaData, Table, Column, Integer, String, select
from sqlalchemy.orm import registry, Session
from app.config.db import Database

# Configurar a reflexão para carregar a tabela existente
db_instance = Database()
engine = db_instance.engine
metadata = MetaData(schema="Person")
address_table = Table(
    "Address",
    metadata,
    Column("AddressID", Integer, primary_key=True),
    Column("AddressLine1", String),
    Column("City", String),
    autoload_with=engine,
    include_columns=["AddressID", "AddressLine1", "City"],
)


# Definir uma classe Python para representar o modelo SQLAlchemy
class PersonAddress:
    pass


mapper_registry = registry()
mapper_registry.map_imperatively(PersonAddress, address_table)


def get_all_persons_adresses(db_session: Session, offset: int = 0, limit: int = 10):
    query = (
        select(address_table.c.AddressLine1, address_table.c.City)
        .order_by(address_table.c.AddressID)
        .offset(offset)
        .limit(limit)
    )

    try:
        result = db_session.execute(query)
        adresses = result.fetchall()

        return [{"AddressLine1": a[0], "City": a[1]} for a in adresses]
    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")
        return []
