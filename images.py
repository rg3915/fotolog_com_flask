from flask_wtf import Form
from wtforms import StringField, FileField, TextAreaField
from wtforms.validators import DataRequired, regexp


class ImageForm(Form):
    name = StringField("Nome", validators=[DataRequired()])
    description = TextAreaField("Descrição")
    image = FileField("Imagem", validators=[DataRequired() ])
    tags = StringField("Tags")



