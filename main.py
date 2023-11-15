import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='H@pp!n3$',
    database='bdcrud',
)

cursor = conexao.cursor()

#CRUD
# CREATE
# nome_produto = "Redmi"
# valor = 1500
# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
# cursor.execute(comando)
# conexao.commit() #edita o banco de dados
# resultado = cursor.fetchall() #lê o banco de dados



# READ
# comando = f'SELECT * FROM vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall() #lê o banco de dados
# print(resultado)



# UPDATE
# nome_produto = "iphone"
# valor = 6000
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit()


# DELETE
# nome_produto = "iphone"
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit()

cursor.close()
conexao.close()