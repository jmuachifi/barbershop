from app import db
from models import User, Barber

# Find an existing user or create a new one for the barber
user = User.query.filter_by(username='barber1').first()
if not user:
    user = User(username='barber1', email='barber1@ua.pt', role='barber')
    user.set_password('Barberpassword2024')
    db.session.add(user)
    db.session.commit()

# Create the barber associated with the user
barber = Barber(user_id=user.id)
db.session.add(barber)
db.session.commit()
