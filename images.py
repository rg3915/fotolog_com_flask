from flask_wtf import Form
from wtforms import StringField, FileField, TextAreaField
from wtforms.validators import DataRequired, regexp
from photolog import db
<<<<<<< HEAD

=======
>>>>>>> c67622bc5d4dc5a061b4692f2af7251843b1b733

class ImageForm(Form):
    name = StringField("Nome", validators=[DataRequired()])
    description = TextAreaField("Descrição")
    image = FileField("Imagem", validators=[DataRequired()])
    tags = StringField("Tags")


class ImageModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(2048))
    filename = db.Column(db.String(200), unique=True)
    tags = db.Column(db.String(1024))

<<<<<<< HEAD
=======
class ImageModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(2048))
    filename = db.Column(db.String(200), unique=True)
    tags = db.Column(db.String(1024))

>>>>>>> c67622bc5d4dc5a061b4692f2af7251843b1b733
    def __init__(self, name, description, filename, tags):
        self.name = name
        self.description = description
        self.filename = filename
        self.tags = tags

<<<<<<< HEAD
    def get_mime(self):
        ''' [-1] último elemento '''
        return "image/{}".format(self.filename.split(".")[-1].lower())

    def __repr__(self):
        return '<Image %r>' % self.name
=======
    def __repr__(self):
        return '<Image %r>' % self.name
>>>>>>> c67622bc5d4dc5a061b4692f2af7251843b1b733
