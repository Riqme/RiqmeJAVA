import sqlite3

bank = sqlite3.connect('first_bank.db')
cursor = bank.cursor()
#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")
#cursor.execute("INSERT INTO pessoas VALUES('Joao', 32,'joao@gmail.com')")

for i in range(1):
    print('\033[1;30;41mBem vindo ao nosso site!\033[m')
    print('\033[4;30;47mPara realizar o cadastro complete as seguintes informações abaixo.\033[m')

    nome = str(input('Qual seu nome?'))
    idade = int(input('Qual sua idade?'))
    email = str(input('Qual seu email?'))
    cursor.execute("INSERT INTO pessoas VALUES('{}', '{}', '{}')".format(nome, idade, email))
    
    print('\033[0;30;42mCadastro realizado com sucesso!\033[m')
    print('Seja bem vindo ao nosso site, {}. Para ganhar um ótimo desconto, veja seu email {}'.format(nome, email))
   
    cursor.execute("SELECT * FROM pessoas")
    print(cursor.fetchall())

try:
    remove_ida = str(input('Deseja remover sua idade?( Sim/Não )').upper())
    if remove_ida == 'SIM':
        cursor.execute("UPDATE pessoas SET idade = NULL WHERE idade == 16")
        print('Sua idade foi removida com sucesso! Tenha um bom dia.')
    else:
      print('Agrademos sua compreenção!')
       
    cursor.execute("SELECT * FROM pessoas")
    print(cursor.fetchall())

except sqlite3.Error as erro_remocao:
    print('Não conseguimos concluir a exclusão.')

bank.commit()
bank.close()
