# rioDoceStardogAPI

## Dependências
Desenvolvida em python3.
Os seguintes módulos são necessários para a execução da API:  
* requests
* requests-toolbelt
* urllib3
* pystardog
* Flask-RESTful

## Configurações iniciais
Para a execução da API, é necessário modificar o dicionário _connectionPool_ presente no arquivo _setup.py_ dentro da pasta _dao_ com as respectivas informações: endereço do banco, login e senha. Também é necessário alterar a variável databaseName para o nome correto do banco.

Exemplo:

Dado que o banco esteja rodando numa máquina virtual dentro da máquina local. Esta vm pode ser acessada via ipv4 192.168.56.104. A porta _default_ em que o banco fica acessível é a 5820, logo o endereço do banco nesse dicionário será http://192.168.56.104:5820

Os valores de usuário e senha podem ser modificados conforme o ambiente e necessidade.
## Setup de testes
Os testes da API foram feitos utilizando uma máquina virtual linux onde o banco estava rodando e as requisições eram testadas utilizando o Postman. As requisições devem ser feitas utilizando o endereço definido no flask que, por padrão, é http://localhost:5000

## Iniciando a API

Com as depêndencias instaladas e configurações de endereço realizadas, basta rodar o arquivo _main.py_. Ele iniciará um servidor de endereço padrão http://localhost:5000, por onde devem ser feitas as requisições. Na única linha da função principal temos o parâmetro _debug=true_. Sendo ele verdadeiro, todas as informações passadas via requisições e até possíveis erros aparecerão no terminal onde o arquivo foi executado.

Para conferir se está tudo Ok, basta utilizar o Postman, com o método GET o seguinte endereço: http://localhost:5000/list/property A api deve retornar em formato JSON todas as propriedades do banco.

## _Endpoints_ Disponíveis

Atualmente os seguinte endpoints estão disponíveis para consulta:
* /list/property
* /list/party
* /list/river
* /filter/measurement
  
Este último permite a passagem de parâmetros de consulta, por exemplo http://localhost:5000/filter/measurement?property=Solidos_suspensos_totais

O _endpoint_ /measurement por sua vez ainda não está completo. Com ele será possível a realização de consultas desmembrando cada propriedade, por exemplo, http://localhost:5000/measurement?locale.lat=27,86
