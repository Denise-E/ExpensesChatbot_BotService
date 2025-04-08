import os

from flask import Flask, render_template

from src.database.config import SessionLocal
from src.routes.expenses_routes import expenses
from src.routes.swagger_routes import swagger_json_blueprint, swaggerui_blueprint
from src.routes.users_routes import users

app = Flask(__name__)

# Global instance of the database session
session = SessionLocal()

# Register blueprints - routes files connection
app.register_blueprint(expenses, url_prefix="/api/expenses")
app.register_blueprint(users, url_prefix="/api/users")

# Swagger route
app.register_blueprint(swagger_json_blueprint)
app.register_blueprint(swaggerui_blueprint, url_prefix="/swagger")


@app.route("/")
def home():
    return render_template("index.html")


# Health route to check if the API is up
@app.route("/api/health", methods=['GET'])
def health():
    return {"msg": "OK"}, 200


if __name__ == '__main__':
    # Local URL: http://127.0.0.1:5000
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
