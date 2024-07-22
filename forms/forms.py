from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Length, Email
from flask_wtf.file import FileField, FileRequired

'''
O que eu fiz aqui foi o seguinte:
[[
    Eu criei uma classe chamada RegistrationForm, responsável por criar o meu suposto formulário que vai carregar essas informações. Fiz isso usando o FlaskForm integrado com o wtforms, pra validar o formulário e até criar ele também
    Ali em baixo eu criei um LoginForm, que faz a mesma coisa, mas não importa muito, porque é a mesma coisa que o RegistrationForm
]]

'''


class RegistrationForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired(), Length(min=2, max=23)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()]) 
    
    submit = SubmitField('Submit!')
    
    
class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()]) 
    
    submitlogin = SubmitField('Submit!')
    
    
class PostsForm(FlaskForm):
    title = StringField('Title!', validators=[DataRequired(), Length(min=3, max=15)])
    content = StringField('Content!', validators=[DataRequired(), Length(min=10, max=1200)])
    img = FileField(validators=[FileRequired()])
    
    submitpost = SubmitField('Submit!')