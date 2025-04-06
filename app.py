from src.database.config import SessionLocal
from src.routes.expenses_routes import expenses
from src.routes.users_routes import users
from flask import Flask

app = Flask(__name__)

# Global instance of the database session
session = SessionLocal()

# Register blueprints
app.register_blueprint(expenses, url_prefix="/api/expenses")
app.register_blueprint(users, url_prefix="/api/users")


@app.route("/api/health", methods=['GET'])
def health():
    return {"msg": "OK"}, 200


if __name__ == '__main__':
    app.run(port=5000)
