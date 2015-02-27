from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    html = """\
<!DOCTYPE html>
<html>
    <body>
        <ul>
            <li>Cadastre-se</li>
            <li>Entre</li>
            <li>Subir fotos</li>
            <li>Navegar</li>
            <li>Sair</li>
        </ul>

        <h1>Bem-vindo ao Fotolog</h1>


        <footer>
            <p>Copyright 2015 - João S. O. Bueno</p>
            <p>Feito com <a href="http://flask.pocoo.org/">Flask</a></p>
        </footer>
    </body>
</html>\
"""
    return html

if __name__ == "__main__":
    app.run()