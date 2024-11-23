from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Inicializando o app Flask
app = Flask(__name__)

# Configurando o banco de dados SQLite no Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desabilitar o tracking de modificações (opcional)
db = SQLAlchemy(app)

# Definindo a tabela "user" com SQLAlchemy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    pwd = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'
'''
# Criar todas as tabelas (se não existirem)
with app.app_context():
    db.create_all()

    # Verificar se a tabela "user" está vazia e inserir um usuário de teste
    if not User.query.first():
        test_user = User(name="Teste", email="teste@teste.com", pwd="teste")
        db.session.add(test_user)
        db.session.commit()
        print("Usuário de teste criado!")
'''
# Rota inicial
@app.route('/')
def home():
    return "Hello, World!"

# Rota para retornar dados da tabela 'user'
@app.route('/data')
def data():
    # Consultando todos os registros da tabela "user"
    users = User.query.all()
    # Convertendo os resultados para um formato JSON
    data = [{"id": user.id, "name": user.name, "email": user.email, "pwd": user.pwd} for user in users]
    return jsonify(data)

if __name__ == "__main__":
      app.run(port=5000)
