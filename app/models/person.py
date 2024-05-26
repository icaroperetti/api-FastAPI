from sqlalchemy import MetaData, Table, text
from sqlalchemy.orm import registry, Session
from app.config.db import Database

# Configurar a reflexão para carregar a tabela existente
db_instance = Database()
engine = db_instance.engine
metadata = MetaData(schema="Person")
person_table = Table("Person", metadata, autoload_with=engine)


# Definir uma classe Python para representar o modelo SQLAlchemy
class Person:
    pass


mapper_registry = registry()
mapper_registry.map_imperatively(Person, person_table)


def get_all_persons(db_session: Session, offset: int = 0, limit: int = 10):
    query = text(
        "SELECT FirstName, LastName, BusinessEntityID FROM Person.Person "
        "ORDER BY BusinessEntityID OFFSET :offset ROWS FETCH NEXT :limit ROWS ONLY"
    )

    try:
        result = db_session.execute(query, {"offset": offset, "limit": limit})
        persons = result.fetchall()

        return [
            {"FirstName": p[0], "LastName": p[1], "BusinessEntityID": p[2]}
            for p in persons
        ]
    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")
        return []
