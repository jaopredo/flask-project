from flask import Flask
from routes.client import client_page


class Application:
    def __init__(self):
        self.server = Flask(__name__)

    def add_controller(self, controller):
        self.server.register_blueprint(controller)

    def run(self, debug):
        self.server.run(debug=debug)


if __name__ == "__main__":
    app = Application()
    app.add_controller(client_page)
    app.run(debug=True)
