from flask import Flask, jsonify
import os

app = Flask(__name__)


users = [
    {
        "id": "8a169ade-2d06-4508-b5ba-57e730bef4af",
        "name": "John",
        "age": 20,
        "phone": "123-456-7890",
        "street": "123 Main St",
        "city": "Miami",
    },
    {
        "id": "ef3347db-d6f3-46ac-84aa-36f4c6076cc3",
        "name": "Jane",
        "age": 22,
        "phone": "334-159-2123",
        "street": "123 Hook St",
        "city": "New York",
    },
]

datos = {
            "author": os.environ['AUTHOR_NAME'],
            "email": os.environ['AUTHOR_EMAIL'],
            "version": 1
            }

@app.route('/')
def hello_world():
    return jsonify(author=os.environ['AUTHOR_NAME'], email=os.environ['AUTHOR_EMAIL'])

@app.route('/author')
def hello_world2():
    return jsonify(datos)


@app.route('/users')
def hello_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

    """
    Esto es un comentario de prueba
    """
