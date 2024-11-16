from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Create the instance directory if it doesn't exist
instance_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance')
if not os.path.exists(instance_path):
    os.makedirs(instance_path)

# Configure the application to use SQLite for database storage
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(instance_path, "chocolate.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev' # Secret key

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Database Models
class Flavor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    is_seasonal = db.Column(db.Boolean, default=False)
    season = db.Column(db.String(20))  # Spring, Summer, Fall, Winter
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(20), nullable=False)

class CustomerSuggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flavor_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    allergens = db.Column(db.String(200))  
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Routes for Flavors
@app.route('/api/flavors', methods=['GET'])
def get_flavors():
    flavors = Flavor.query.all()
    return jsonify([{
        'id': f.id,
        'name': f.name,
        'is_seasonal': f.is_seasonal,
        'season': f.season
    } for f in flavors])

@app.route('/api/flavors', methods=['POST'])
def add_flavor():
    data = request.get_json()
    
    if not data or 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    
    flavor = Flavor(
        name=data['name'],
        is_seasonal=data.get('is_seasonal', False),
        season=data.get('season')
    )
    db.session.add(flavor)
    db.session.commit()
    return jsonify({'message': 'Flavor added successfully'}), 201

# Routes for Inventory
@app.route('/api/inventory', methods=['GET'])
def get_inventory():
    ingredients = Ingredient.query.all()
    return jsonify([{
        'id': i.id,
        'name': i.name,
        'quantity': i.quantity,
        'unit': i.unit
    } for i in ingredients])

@app.route('/api/inventory', methods=['POST'])
def add_ingredient():
    data = request.get_json()
    
    if not data or 'name' not in data or 'quantity' not in data:
        return jsonify({'error': 'Name and quantity are required'}), 400
    
    ingredient = Ingredient(
        name=data['name'],
        quantity=data['quantity'],
        unit=data.get('unit', 'grams')
    )
    db.session.add(ingredient)
    db.session.commit()
    return jsonify({'message': 'Ingredient added successfully'}), 201

@app.route('/api/inventory/<int:id>', methods=['PUT'])
def update_inventory(id):
    ingredient = Ingredient.query.get_or_404(id)
    data = request.get_json()
    
    if 'quantity' in data:
        ingredient.quantity = data['quantity']
    
    db.session.commit()
    return jsonify({'message': 'Inventory updated successfully'})

# Routes for Customer Suggestions
@app.route('/api/suggestions', methods=['POST'])
def add_suggestion():
    data = request.get_json()
    
    if not data or 'flavor_name' not in data:
        return jsonify({'error': 'Flavor name is required'}), 400
    
    suggestion = CustomerSuggestion(
        flavor_name=data['flavor_name'],
        description=data.get('description', ''),
        allergens=data.get('allergens', '')
    )
    db.session.add(suggestion)
    db.session.commit()
    return jsonify({'message': 'Suggestion received successfully'}), 201

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Ensure the instance directory exists before running the application
    if not os.path.exists('instance'):
        os.makedirs('instance')
    
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    
    # Start the Flask application
    app.run(debug=True)