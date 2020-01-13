from app import app
import view


from tickets.blueprint import tickets
app.register_blueprint(tickets, url_prefix='/tickets')
from users.blueprint import users
app.register_blueprint(users, url_prefix='/users')



if __name__ == '__main__':
    app.run()
