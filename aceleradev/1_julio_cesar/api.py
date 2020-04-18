import requests, json, hashlib, string

# requests and response

codenation_url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token="

request_to_codenation = requests.get(codenation_url)

response = request_to_codenation.json()

# create file and write data from json

with open("answear.json", "w") as json_file:
    json.dump(response, json_file)

# get key 'numero_casas' value

get_file = open("answear.json")
data = json.load(get_file)
numero_casas = data["numero_casas"]

# generating chars
phrase = data["cifrado"]

def split(phrase): 
    return list(phrase) 
      
# create alphabet range
alphabet = list(string.ascii_lowercase)
new_phrase = ""

for letter in split(phrase):
    posicao = string.ascii_lowercase.index(letter)
    posicao = posicao - numero_casas
    #new_phrase += alphabet[:posicao]
    print('-----> nc', alphabet[:posicao])




# resumo = hashlib.sha1(data['cifrado'].decode(encoding)).hexdigest()
# data['resumo_criptografico'] = resumo
# print('---------------->', resumo)

# with open('answear.json', 'w') as json_file:
# json.dump(data, json_file)
