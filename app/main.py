from app import app
from tickets.blueprint import tickets
import view

app.register_blueprint(tickets, url_prefix='/tickets')

if __name__ == '__main__':
    app.run()