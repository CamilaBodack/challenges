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


# create
def create_data(name):
          models.execute_kw(db, uid, password,
                            'res.partner', 'create',
                            [{'name': name }])


# update
def update(id, name):
          models.execute_kw(db, uid, password, 'res.partner', 'write',
                            [[id], {'name': name}])


def check_update(id):
    models.execute_kw(db, uid, password, 'res.partner', 'name_get', [[id]])


# delete records http://localhost:8069
def delete_data(ids):
    list = []
    list.append(ids)

    models.execute_kw(db, uid, password,
                      'res.partner', 'unlink', list)


# lists records using method search_read
def list_data():
    user_data = models.execute_kw(db, uid, password,
                    'res.partner', 'search_read',
                    [[['customer', '=', True]]],
                    {'fields': ['display_name', 'id'], 'limit': 10})

    print(user_data)
    for i in user_data:
        print(i)

# create opportunity
def create_opportunity(opportunity, part_id, plan_revenue):
          models.execute_kw(db, uid, password,
                            'crm.lead', 'create',
                            [{'company_id': 1, 'priority': "3", 'name': opportunity, 'partner_id': part_id, 'planned_revenue': plan_revenue}])

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
            check_update(id)
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
