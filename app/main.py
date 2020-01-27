from app import app
from tickets.blueprint import tickets
from users.blueprint import users
from auth.blueprint import auth
import view


app.register_blueprint(tickets, url_prefix='/tickets')
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(auth, url_prefix='/auth')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
