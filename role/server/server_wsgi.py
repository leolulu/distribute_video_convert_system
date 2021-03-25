import json

from constants.argument import ArgConstants
from flask import Flask
from flask_restful import Api, Resource, reqparse

from role.server.client_manager import ClientManager

app = Flask(__name__)
api = Api(app)


class ClientManage(Resource):
    def __init__(self) -> None:
        self.clientmanager = ClientManager()
        parser = reqparse.RequestParser(strict=False)
        parser.add_argument(ArgConstants.NAME, type=str, help='client name')
        self.args = parser.parse_args(bundle_errors=True)

    def post(self):
        self.clientmanager.add_client(self.args[ArgConstants.NAME])

    def get(self):
        return json.dumps(self.clientmanager.get_all_client_name())


api.add_resource(ClientManage, '/client-manage')

if __name__ == '__main__':
    app.run(debug=True)
