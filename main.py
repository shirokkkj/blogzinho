from flask import Flask, redirect, render_template, url_for, request, flash
from forms.forms import RegistrationForm, LoginForm, PostsForm
from routes.navbar import navbar
from database.posts.posteds import POSTS
from routes.posts import posts_route
from database.registers_users.cadastred_users import db, Users


posts = [
    {'Author': 'Shiro', 'Content': 'Hello Everbody!'},
    {'Author': 'Shiro', 'Content': 'my list of top 10 musics of world!'},
]

app = Flask(__name__)

app.config['SECRET_KEY'] = '6c3aeec5aa9d96981e9bc7c79a49bfdc'

app.register_blueprint(navbar)
app.register_blueprint(posts_route)

@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

'''
[[
    Aqui, eu criei uma rota chamada "/register", que eu posso acessar ela dentro da minha página web. É através dessas rotas que eu consigo acessar as informações de uma página HTML, por exemplo. Nesse caso, essa função ficou responsável por renderizar o meu formulário HTML com o método HTTP - GET, pra pegar esses dados.
    
    O método HTTP - POST, eu te explico no decorrer dessa. Eu defini como variável "form" o meu formulário de registor, lembra dele? Depois, fiz uma verificação com uma requisição de método, porque eu preciso saber o que tá acontecendo no meu website pra fazer o validate
        - Antes de continuar, vou te mostrar esse "request.method" -
        - Viu? Ele me mostra o método de requisição que, quando eu clico no botão, vira um POST, porque tô inserindo dados.
        
    Verificando o método, eu fiz outra verificação do FlaskForm, que é o validate_on_submit(), que verifica se os dados do formulário foram preenchidos, se cumprem os requesitos, blablabla
    
    E então, eu fiz um "flash", que exibe uma pequena mensagem só pra notificar que eu loguei na página e o redireciono com um "redirect" e um url_for, pra acessar a minha página "home".
]]
'''
@app.route('/register', methods=['GET', 'POST'], )
def register():
    form = RegistrationForm()
    print(request.method)
    if request.method == 'POST':
        if form.validate_on_submit():
            flash(f'Welcome to blog, {form.username.data}!')
            
            Users.create(username=form.username.data, email=form.email.data, password=form.password.data)
            
            return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostsForm()
    postes = {
        'Title': form.title.data,
        'Content': form.content.data,
        'Image': form.img.data
    }
    
    pst = POSTS
    
    print(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            pst.append(postes) 
            print(pst)
            return redirect(url_for('home'))
        
    return render_template('formpost.html', form=form)
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print(request.form)
    print(request.method)
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.email.data == 'admin@gmail.com' and form.password.data == '1232':
                flash(f'Logged with Account: {'admin@gmail.com'}')
                return redirect(url_for('home'))
    return render_template('login.html', form=form)

app.run(debug=True)