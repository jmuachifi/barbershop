
# Barbershop Scheduling App

A simple scheduling platform for barbershops where customers can book appointments with barbers, and barbers can view their upcoming appointments.

## Features

- **Customer Dashboard**: View available barbers and book appointments.
- **Barber Dashboard**: View upcoming appointments with customers.
- **Admin Dashboard** (Optional): Manage barbers and customers.
- **Role-Based Access**: Supports customer, barber, and admin roles.

---

## Setup and Installation

### Prerequisites

Make sure you have the following installed:

- **Python 3.x** (Make sure to have the latest version)
- **Pip** (Python's package manager)
- **Virtualenv** (Optional, but recommended)
- **Flask** and **Flask dependencies** (listed in `requirements.txt`)

### Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/jmuachifi/barbershop-app.git
cd barbershop-app/flask
```

### Set Up the Virtual Environment (Optional but Recommended)

Create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies

Install the required packages using `pip`:

```bash
pip install -r requirements.txt
```

### Configuration

1. **Set the Flask environment variables**:
   You can do this by setting environment variables or by creating a `.env` file with the following content:

   ```bash
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   ```

2. **Set Up the Database**:
   - Initialize the SQLite database (or any other configured database):
   
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

   - This will create the necessary tables for your application.

3. **Create an Admin User (Optional)**:
   You can create an admin user manually by opening a Flask shell:

   ```bash
   flask shell
   ```

   Inside the shell, create the admin user:

   ```python
   from app import db
   from models import User

   admin = User(username="admin", email="admin@example.com", role="admin")
   admin.set_password("adminpassword")
   db.session.add(admin)
   db.session.commit()
   ```

---

## Running the Application

Run the Flask development server:

```bash
flask run
```

The application will be accessible at `http://127.0.0.1:5000/`.

---

## Testing the Application

To run tests, follow these steps:

1. **Unit Testing**: Make sure to have a testing framework like `pytest` installed.
2. **Run Tests**:
   
   ```bash
   pytest
   ```

   This will run all the tests defined in the `tests/` directory.

---

## Deployment

### Deploying to Heroku

1. **Create a Heroku account**: [Heroku Signup](https://signup.heroku.com/)

2. **Install Heroku CLI**: Follow the instructions [here](https://devcenter.heroku.com/articles/heroku-cli).

3. **Create a Heroku app**:

   ```bash
   heroku create your-app-name
   ```

4. **Set up the environment variables**:
   
   ```bash
   heroku config:set FLASK_APP=app.py
   heroku config:set SECRET_KEY=your_secret_key
   ```

5. **Add PostgreSQL database** (optional for production):

   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

6. **Deploy to Heroku**:

   ```bash
   git push heroku main
   ```

7. **Run Database Migrations on Heroku**:

   ```bash
   heroku run flask db upgrade
   ```

8. **Open the Application**:

   ```bash
   heroku open
   ```

### Other Deployment Options

You can also deploy the app using other platforms like AWS, Google Cloud, or a traditional VPS. Just ensure that you have the correct Python version, database setup, and environment variables configured.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
