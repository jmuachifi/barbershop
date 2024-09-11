# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object("config.Config")

csrf = CSRFProtect(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"  # Redirect to login page if not authenticated

# User loader function for Flask-Login
from models import User  # Import the User model here


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Load the user by ID from the database


# Import models (Make sure models.py exists and contains User, Barber, Appointment)
from models import User, Barber, Appointment

# Import blueprints (Ensure routes.py exists and defines auth and scheduling blueprints)
from routes import auth, scheduling, main, admin

# Register blueprints
app.register_blueprint(
    auth, url_prefix="/auth"
)  # Prefix /auth for authentication routes
app.register_blueprint(scheduling)  # Scheduling routes, no prefix
app.register_blueprint(main)  # Main routes, no prefix
app.register_blueprint(admin)  # Admin blueprint

if __name__ == "__main__":
    app.run(debug=True)
