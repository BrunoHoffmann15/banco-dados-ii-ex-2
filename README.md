# Atividade 2 - Banco de Dados 2

**Objetivo:** Implemente um programa na linguagem / framework de escolha de seu grupo que atenda a pelo menos um relacionamento do tipo 1:N.

## Integrantes:
- Bel Cogo
- Bruno Hoffmann
- João Accorsi
- Rafael Klauck

# Como Executar
Como pré-requisito é necessário ter instalado o python na máquina. Além disso, execute os seguintes comandos abaixo:

Inicialmente execute o comando abaixo para fazer a criação do `clientes.db`, e também a criação das tabelas.

```sh
python .\database_orm.py
```

Por fim, execute o comando abaixo para executar a aplicação. Esse executará a aplicação na porta 5000.

```sh
python .\app.py
```

Em seguida, você poderá executar alguns endpoints, conforme os mapeamentos expostos na seção abaixo.

## Mapeamentos

A aplicação possui um domínio composto por Clientes, que podem possuir cartões, tendo essa relação através de 1:N, onde um cliente pode ter 0 ou mais cartões e um cartão pode pertencer apenas a um cliente.

**1.1 - Criação de Cliente**

Realiza a criação de um novo cliente.

Mapeamento:
> POST /cliente

Executar em linha de comando (usando bash):

```sh
curl -X POST http://127.0.0.1:5000/cliente -H "Content-Type: application/json" -d "{\"nome\": \"Maria Fernandes\", \"idade\": 40, \"sexo\": \"M\"}"
```

**1.2 - Obter Cliente por Identificador**

Realiza a obtenção de um cliente pelo identificador.

Mapeamento:
> GET /cliente/:id-cliente


Executar em linha de comando (usando bash):

```sh
curl -X GET http://127.0.0.1:5000/cliente/1 -H "Content-Type: application/json"
```

**1.3 - Obter Cartões do Cliente**

Realiza a obtenção dos cartões do cliente, através do identificador do cliente.

Mapeamento:
> GET /cliente/:id-cliente/cartoes

Executar em linha de comando (usando bash):

```sh
curl -X GET http://127.0.0.1:5000/cliente/3/cartoes -H "Content-Type: application/json"
```

**1.4 - Criar Cartão**

Realiza a criação de um cartão.

Mapeamento:
> POST /cartao

Executar em linha de comando (usando bash):

```sh
curl -X POST http://127.0.0.1:5000/cartao -H "Content-Type: application/json" -d "{\"numero\":\"123456789\", \"cvv\": \"111\", \"validade\":\"02/24\", \"nome_no_cartao\": \"Maria F\", \"client_id\": 3}" 
```

**1.5 - Obter Cartão por Identificador**

Realiza a obtenção de um cartão pelo seu identificador.

Mapeamento:
> GET /cartao/:id-cartao

Executar em linha de comando (usando bash):
```sh
curl -X GET http://127.0.0.1:5000/cartao/5 -H "Content-Type: application/json"
```