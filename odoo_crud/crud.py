import xmlrpc.client

url = 'http://localhost:8069'
db = 'teste'
username = 'admin'
password = '123'


# log in - endpoint: 1
basic_login = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

# return the user id (uid) to next requests
uid = basic_login.authenticate(db, username, password, {})


# calling methods - endpoint: 2
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))


'''create user. Function that orchestrate execution is 'execute_kw' with default parameters: db, uid, password
model name in this case is 'res.partner', method name: 'create', and list with parameters
'''
def create_data(name):
    models.execute_kw(db, uid, password,
                     'res.partner', 'create',
                     [{'name': name }])


'''update user. Function to orchestrate execution is 'execute_kw' with default parameters: db, uid, password
model name in this case is 'res.partner', method name: 'write' (records in odoo are made by this method), and list with parameters
'''
def update(id, name):
    models.execute_kw(db, uid, password, 'res.partner', 'write',
                      [[id], {'name': name}])


'''delete user. Function to orchestrate execution is 'execute_kw' with default parameters: db, uid, password
model name in this case is 'res.partner', method name: 'unlink' (delete in odoo are made by this method), and list with parameters
'''
def delete_data(ids):
    list = []
    list.append(ids)
    models.execute_kw(db, uid, password,
                      'res.partner', 'unlink', list)


'''list users. Function to orchestrate execution is 'execute_kw' with default parameters: db, uid, password
model name in this case is 'res.partner', method name: 'search_read' (search and read methods united), and list with parameters
'''
def list_data():
    user_data = models.execute_kw(db, uid, password,
                                 'res.partner', 'search_read',
                                 [[['customer', '=', True]]],
                                 {'fields': ['display_name', 'id'], 'limit': 10})

    print(user_data)
    for i in user_data:
        print(i)


'''create opportunity in crm. Function to orchestrate execution is 'execute_kw' with default parameters: db, uid, password
model name in this case is 'crm.lead', method name: 'create', and list with parameters
'''

def create_opportunity(opportunity, part_id, plan_revenue):
    models.execute_kw(db, uid, password,
                     'crm.lead', 'create',
                     [{'company_id': 1, 'priority': "3", 'name': opportunity, 'partner_id': part_id, 'planned_revenue': plan_revenue}])



# show options to users interactions

def options():
    options = 0
    while True:
        print("1 - Criar usuário")
        print("2 - Atualizar dados usuário")
        print("3 - Deletar usuário ")
        print("4 - Listar informações inseridas")
        print("5 - Criar oportunidade")
        print("0 - Sair")
        options = int(input("Insira uma opção:"))
        if options == 1:
            name = input("Insira o nome do contato:")
            create_data(name)
        elif options == 2:
            id = int(input("Informe o id"))
            name = input("Insira o novo nome:")
            update(id, name)
        elif options == 3:
            ids = int(input("Insira o(s) id(s):"))
            delete_data(ids)
        elif options == 4:
            list_data()
        elif options == 5:
            opportunity = input("Insira o nome da oportunidade:")
            part_id = int(input("Insira o ID do usuário responsável:"))
            plan_revenue = float(input("Insira o valor da oportunidade:"))
            create_opportunity(opportunity, part_id, plan_revenue)
        elif options == 0:
            print("Finalizando...")
            break
        else:
            print("Insira uma opção válida")

            
options()
