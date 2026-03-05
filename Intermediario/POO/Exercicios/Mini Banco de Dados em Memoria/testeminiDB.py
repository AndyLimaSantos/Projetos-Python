from MiniDB import miniDB

db = miniDB()
db.create_table("clientes", ["id", "nome", "idade"])
print(db.bancoDedados)
print(db.colunas_dados)
db.insert("clientes", {"id": 1, "nome": "Ana", "idade": 25})
print(db.bancoDedados)
print(db.colunas_dados)