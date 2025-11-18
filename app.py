from flask import Flask, render_template, request, flash, redirect, url_for
app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'
@app.route('/')
def index():
 return redirect(url_for('registrarUsuario'))
@app.route('/registrarUsuario', methods=['GET', 'POST'])
def registrarUsuario():
 if request.method == 'POST':
 username = request.form['username']
 email = request.form['email']
 password = request.form['password']
 # Validação simples do lado do servidor
 if not username or not email or not password:
 flash('Todos os campos são obrigatórios!', 'danger')
 else:
 flash(f'Usuário {username} cadastrado com sucesso!', 'success')
 return redirect(url_for('register'))
# flash(): Armazena uma mensagem que será exibida na próxima requisição. Isso
# é útil para fornecer mensagens ao usuário.
 return render_template(“base.html')
if __name__ == '__main__':
 app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from models import db, User, Game, Auction, Bid
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

# Inicializa extensões
db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)

# =====================
# ROTAS PRINCIPAIS
# =====================

@app.route('/')
def index():
    auctions = Auction.query.filter_by(status='active').all()
    return render_template('index.html', auctions=auctions)

@app.route('/auction/<int:auction_id>')
def auction_detail(auction_id):
    auction = Auction.query.get_or_404(auction_id)
    bids = Bid.query.filter_by(auction_id=auction_id).order_by(Bid.amount.desc()).all()
    return render_template('auction.html', auction=auction, bids=bids)

@app.route('/bid', methods=['POST'])
def place_bid():
    if 'user_id' not in session:
        flash('Você deve estar logado para dar lances.')
        return redirect(url_for('login'))

    auction_id = int(request.form['auction_id'])
    amount = float(request.form['amount'])
    auction = Auction.query.get_or_404(auction_id)

    # Validação simples
    if amount <= auction.current_price:
        flash('O lance deve ser maior que o preço atual.')
        return redirect(url_for('auction_detail', auction_id=auction_id))

    bid = Bid(auction_id=auction_id, bidder_id=session['user_id'], amount=amount)
    auction.current_price = amount
    db.session.add(bid)
    db.session.commit()

    flash('Lance registrado com sucesso!')
    return redirect(url_for('auction_detail', auction_id=auction_id))


# =====================
# AUTENTICAÇÃO
# =====================

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Verifica duplicatas
        if User.query.filter_by(email=email).first():
            flash('Email já cadastrado!')
            return redirect(url_for('register'))

        user = User(username=username, email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash('Cadastro realizado com sucesso! Faça login.')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login realizado com sucesso!')
            return redirect(url_for('index'))
        else:
            flash('Credenciais inválidas. Tente novamente.')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    flash('Você saiu da conta.')
    return redirect(url_for('index'))


# =====================
# ADMIN / DASHBOARD
# =====================

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Faça login para acessar o painel.')
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    if user.role == 'admin':
        auctions = Auction.query.all()
        return render_template('dashboard_admin.html', auctions=auctions)
    else:
        auctions = Auction.query.filter_by(seller_id=user.id).all()
        return render_template('dashboard_user.html', auctions=auctions)


# =====================
# EXECUÇÃO
# =====================

if __name__ == '__main__':
    app.run(debug=True)
