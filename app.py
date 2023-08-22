from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Cliente  # Importe a classe Cliente do seu módulo models
from models import Cartao  # Importe a classe Cartao do seu módulo models

app = Flask(__name__)

# Configuração da conexão com o banco de dados (SQLite no exemplo)
engine = create_engine('sqlite:///clientes.db')

Session = sessionmaker(bind=engine)
session = Session()

@app.route('/cliente', methods=['POST'])
def create_cliente():
    data = request.get_json()
    novo_cliente = Cliente(nome=data['nome'], idade=data['idade'], sexo=data['sexo'])
    session.add(novo_cliente)
    session.commit()
    return jsonify({'message': 'Cliente criado com sucesso!'})

@app.route('/cliente/<int:cliente_id>', methods=['GET'])
def get_cliente(cliente_id):
    cliente = session.query(Cliente).filter_by(id=cliente_id).first()
    if cliente:
        return jsonify({
            'id': cliente.id,
            'nome': cliente.nome,
            'idade': cliente.idade,
            'sexo': cliente.sexo
        })
    else:
        return jsonify({'message': 'Cliente não encontrado'}), 404

@app.route('/cartao', methods=['POST'])
def create_card():
    data = request.get_json()
    novo_cartao = Cartao(
        numero = data['numero'],
        cvv = data['cvv'],
        validade = data['validade'],
        nome_no_cartao = data['nome_no_cartao'],
        client_id = data['client_id'],
    )
    session.add(novo_cartao)
    session.commit()
    return jsonify({'message': 'Cartao criado com sucesso!'})

@app.route('/cartao/<int:client_id>', methods=['GET'])
def get_cartao(client_id):
    cartoes = session.query(Cartao).filter_by(client_id=client_id).all()
    if cartoes:
        card_list = []
        for cartao in cartoes:
            card_list.append({
                'id': cartao.id,
                'numero': cartao.numero,
                'cvv': cartao.cvv,
                'validade': cartao.validade,
                'nome_no_cartao': cartao.nome_no_cartao,
                'client_id': cartao.client_id,
            })
        return jsonify(card_list)
    else:
        return jsonify({'message': 'Cartão não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
