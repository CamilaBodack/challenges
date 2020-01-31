# Conversão de números para palavras


## Desafio

Na linguagem de sua preferência, crie um servidor HTTP que, para cada requisição GET, retorne um JSON cuja chave extenso seja a versão por extenso do número inteiro enviado no path. Os números podem estar no intervalo [-99999, 99999].

Exemplos:
λ curl http://localhost:3000/1
{ "extenso": "um" }
λ curl http://localhost:3000/-1042
{ "extenso": "menos mil e quarenta e dois" }
λ curl http://localhost:3000/94587
{ "extenso": "noventa e quatro mil e quinhentos e oitenta e sete" }
Nos mande o link do repositório no GitHub com o código em até sete dias.
Se você abrir um Pull Request (p.ex. do seu branch de desenvolvimento para o master) nós faremos o review e você terá a chance de corrigir os erros para uma segunda avaliação.
Não esqueça do README.md com as instruções para rodar o servidor!
Não esqueça dos "e"s separando milhares, centenas e dezenas (vide exemplo): "noventa e quatro mil e quinhentos e oitenta e sete". Esse não é o padrão da norma culta da língua portuguesa, e isso é intencional.
É esperado que você implemente o algoritmo de tradução.
Mesmo que não esteja com a lógica completa, nos envie o que conseguiu fazer até o momento.


## Requerimentos

- Ambiente Linux
Para que esse projeto funcione é necessário instalar o [Flask], a biblioteca [Jsonify] e a [num2words].
Via PIP:

```console
pip install Flask
pip install jsonify
pip install num2words
```

## Setup

Abra a pasta do Projeto, abra o terminal de comando e digite:

```console
python3 1_number_to_text.py
```

Clique no endereço informado, p ex. http://127.0.0.1:5000/
e passe o valor desejado pela url.
