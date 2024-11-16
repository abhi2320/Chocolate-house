**Chocolate House Management System**

__The Chocolate House Management System is a Python-based web application designed to manage:__

1. Seasonal Flavor Offerings
2. Ingredient Inventory
3. Customer Flavor Suggestions and Allergy Concerns
This application leverages Flask for the backend, SQLite for data storage, and HTML for frontend. It is simple to use and helps streamline chocolate house operations.

###Features
#Seasonal Flavors
1.Add and view seasonal flavors.
2.Specify the season for seasonal flavors or mark them as year-round.
#Ingredient Inventory
1.Add ingredients with details like name, quantity, and unit.
2.Update ingredient quantities easily.
#Customer Suggestions
1.Collect customer feedback and flavor suggestions.
2.Log potential allergens and additional notes provided by customers

###Installation of Dependencies
pip install -r requirements.txt

###Run the Application
##1. Clone the Repository:
  git clone <repository-url>
  cd <repository-directory>
##2. Set up the Database:
  python app.py
##3. Start the Application:
  python app.py
#Application will run at http://127.0.0.1:5000


##API Endpoints
Endpoint	Method	Description
/api/flavors	GET	Retrieve all seasonal flavors.
/api/flavors	POST	Add a new seasonal flavor.
/api/inventory	GET	Retrieve inventory details.
/api/inventory	POST	Add a new ingredient.
/api/inventory/<id>	PUT	Update inventory details.
/api/suggestions	POST	Submit a customer suggestion.


##Project Structure
.
├── app.py               # Main application code
├── instance/            # Contains SQLite database file
├── templates/
│   └── index.html       # Frontend HTML template
├── Dockerfile           # Docker configuration file
├── requirements.txt     # Python dependencies
└── README.md            # Documentation


##Docker Setup
#Build and Run the Application with Docker
Build the Docker Image:
docker build -t chocolate-house .

#Run the Docker Container:
docker run -p 5000:5000 chocolate-house

Access the Application: Open your browser and visit http://localhost:5000

##Testing Instructions
Endpoints can be checked with tools like POSTMAN.

