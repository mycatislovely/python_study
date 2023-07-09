from flask import Flask, request, abort, redirect
from markupsafe import escape

app = Flask(__name__)

users = {
    1: {"name": "Petya"},
    2: {"name": "Dasha"},
    3: {"name": "Vasya"},
    4: {"name": "Vova"},
}

def resolve_template(title, body):
    return """
        <html>
        <head><title>{}</title>
        </head>
        <body>
             {} 
        </body>
        </html>
    """.format(escape(title), body)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return resolve_template("Приветствие", f'<h1>Hello, {escape(name)}!</h1>')

@app.route('/ui/user/<id>')
def get_user(id):
    print("id =", id)
    if id is None or not id.isdigit():
        abort(412)
    id = int(id)
    user = users.get(id)
    if user is None:
        abort(404)
    else:
        return resolve_template("Профиль пользователя", 
            f'<p>id={id}</p><p>name={escape(user["name"])}</p>')


@app.route('/ui/user', methods=["POST"])
def add_user():
    id = request.values.get("id")
    # TODO сделать проверку
    id = int(id)
    name = request.values.get("name")
    # TODO сделать проверку    
    users[id] = {"name": name}
    return redirect(f"/ui/user/{id}")

@app.route('/ui/user')
def add_user_form():
    return resolve_template("Добавление пользователя", """
        <form action="/ui/user" method="POST">
            <p><label>ID:</label> <input type="text" name="id"/></p>
            <p><label>Имя:</label> <input type="text" name="name"/></p>
            <p><button type="submit">Добавить</button></p>
        </form>
    """)
    
if __name__ == '__main__':
    app.run()
