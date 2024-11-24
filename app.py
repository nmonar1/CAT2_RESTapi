from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database for perfumes
perfumes = []

# POST /products: Create a new perfume
@app.route('/products', methods=['POST'])
def create_perfume():
    data = request.get_json()

    # Validate input
    if not data or not 'name' in data or not 'description' in data or not 'price' in data:
        return jsonify({"error": "Invalid data"}), 400

    # Add the perfume
    perfume = {
        "name": data['name'],
        "description": data['description'],
        "price": data['price']
    }
    perfumes.append(perfume)
    return jsonify(perfume), 201

# GET /products: Retrieve all perfumes
@app.route('/products', methods=['GET'])
def get_perfumes():
    return jsonify(perfumes), 200

if __name__ == '__main__':
    app.run(debug=True)
