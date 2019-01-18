from wtforms import Form, StringField, TextField, validators, HiddenField
from wtforms.fields.html5 import EmailField

def length_honeypot(form, field):
    #Si nos atacan, llenarán el campo oculto del formulario
    #Si es así, se devolverá un error.
    if len(field.data) >0:
        raise validators.ValidationError('El campo debe estar vacio.')

class CommentForm(Form):
    username = StringField('username', [validators.length(min=4,max=25, message='Ingresa un Username válido')])
    email = EmailField('Correo electronico',
            [validators.Required(message='El campo email no puede estar vacio'),
            validators.Email(message='Introduce un email válido')])
    comment = TextField('Comentario')
    # Honeypot es un "señuelo" para futuros ataques de spam,
    # el campo no va a estar visible para un usuario normal
    honeypot = HiddenField('', [length_honeypot])
