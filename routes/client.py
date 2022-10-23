from flask import Blueprint, request
import json

client_page = Blueprint('client_page', __name__, url_prefix='/client')

@client_page.route('/', methods=['GET', 'POST'])
def client():
    if request.method == 'POST':
        data = json.loads(request.data)

        # database["cliente"].insert_one(data)
        return data
