import sqlite3, time

# Conectar database.
with sqlite3.connect('first_bank.db') as conn:
    cursor = conn.cursor()
    
# Criar colunas no banco de dados.
#=========================================================================================================================    
# cursor.execute('CREATE TABLE pessoas (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, rg TEXT UNIQUE, idade INTEGER) ')
# conn.commit()
#=========================================================================================================================
    
# Registrar um usuário.
def register_users():
    nome = input('Digite o seu nome: ')
    rg = input('Digite seu RG: ')
    idade = int(input('Digite sua idade: '))
    try:
        cursor.execute('INSERT INTO pessoas (nome, rg, idade) VALUES( ?, ?, ?)', (nome, rg, idade))
        conn.commit()
        print(f'Obrigado {nome}, cadastrado(a) com sucesso!')
    except sqlite3.IntegrityError:
        print(f'Erro. {rg} já cadastrado no sistema.')

# Deletar um usuário.
def delete_users():
    nome = input('Digite o nome da pessoa que deseja remover: ')
    cursor.execute('DELETE FROM pessoas WHERE nome = ?', (nome,))
    if cursor.rowcount > 0:
        conn.commit()
        print(f'{nome} Removido(a) do sistema.')
    else:
        print(f'Erro. {nome} não encontrado no sistema. ')

# Listar um usuário.
def list_users():
    cursor.execute('SELECT * FROM pessoas')
    users = cursor.fetchall()
    if users:
        for user in users:
            print(f'ID:{user[0]}, Nome: {user[1]}, RG: {user[2]}, Idade: {user[3]}')
        else:
            print('Nenhua pessoa cadastrada.')

# Editar um usuário.
def edit_users():
    id_user = int(input('Digite o ID da pessoa que deseja editar: '))
    
    # Verificar se o ID fornecido existe.
    cursor.execute('SELECT * FROM pessoas WHERE id = ?', (id_user,))
    user = cursor.fetchall()
    
    if not user:
        print(f'Erro. Nenhum ID encontrado para {id_user}.')
        return

    new_nome = input('Digite seu novo nome: ')
    new_rg = input('Digite seu novo RG: ')
    new_idade = int(input('Digite sua nova idade: '))
    
    try:
        cursor.execute('UPDATE pessoas SET nome=?, rg=?, idade=? WHERE id=?', (new_nome, new_rg, new_idade, id_user,))
        conn.commit()
        print(f'Os dados do ID:{id_user} foram atualizados com sucesso.')
    except sqlite3.IntegrityError:
        print('Erro ao atualizar dados.')

# Procurar um usuário.
def find_users():
    criterios_validos = ['nome', 'rg', 'idade']
    criterio = input('Digite qual CRITÉRIO de pesquisa.(nome, rg ou idade): ')

     # Verificar se o critério de pesquisa é válido.
        
    if criterio not in criterios_validos:
        print(f'Erro. Critério de pesquisa inválido. Escolha entre {", ".join(criterios_validos)} ')
        return
    valor = input(f'Digite o VALOR para o crtitério.(nome, rg ou idade): {criterio}')

    # Executar a consulta com base no critério e valor fornecidos.
    
    cursor.execute(f'SELECT * FROM pessoas WHERE {criterio} = ?', (valor,))
    pessoas = cursor.fetchall()
    
    # Verificar se alguma pessoa foi encontrada.
    if pessoas:
        for pessoa in pessoas:
         print(f'ID: {pessoa[0]}, Nome: {pessoa[1]}, RG: {pessoa[2]}, Idade: {pessoa[3]}')
    else: 
        print(f'Nenhuma pessoas com critério {criterio} igual a {valor}')

#=== MENU RPINCIPAL ===
while True:
    print('------- Menu -------')
    print('1. Register User')
    print('2. Delete User')
    print('3. List User')
    print('4. Edit User')
    print('5. Find User')
    print('0. Exit')

    opcao = int(input('Escolha uma das opções acima: '))
    if opcao == 1:
        register_users()
    elif opcao == 2:
        delete_users()
    elif opcao == 3:
        list_users()
    elif opcao == 4:
        edit_users()
    elif opcao == 5:
        find_users()
    elif opcao == 0:
        break
    else:
        print('Opção inválida. Tente Novamente. ')

    time.sleep(2)

conn.close()
