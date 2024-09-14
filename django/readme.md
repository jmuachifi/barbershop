
# Barbershop Scheduling App (Django Version)

A scheduling platform for barbershops where customers can book appointments with barbers, and barbers can view their upcoming appointments.

## Features

- **Customer Dashboard**: View available barbers and book appointments.
- **Barber Dashboard**: View upcoming appointments with customers.
- **Admin Dashboard** (Optional): Manage barbers and customers.
- **Role-Based Access**: Supports customer, barber, and admin roles.

---

## Setup and Installation

### Prerequisites

Make sure you have the following installed:

- **Python 3.x** (Latest version recommended)
- **Pip** (Python's package manager)
- **Virtualenv** (Optional but recommended)
- **Django** and **Django dependencies** (listed in `requirements.txt`)

### Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/jmuachifi/barbershop-app.git
cd barbershop-app/django
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

1. **Set up the environment variables**:
   You can do this by creating a `.env` file with the following content:

   ```bash
   SECRET_KEY=your_secret_key
   DEBUG=True
   ```

2. **Set Up the Database**:
   - Apply the initial database migrations:
   
   ```bash
   python manage.py migrate
   ```

   - This will create the necessary tables for your application.

3. **Create a Superuser**:
   Create an admin user to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

---

## Running the Application

Run the Django development server:

```bash
python manage.py runserver
```

The application will be accessible at `http://127.0.0.1:8000/`.

---

## Testing the Application

To run tests, follow these steps:

1. **Unit Testing**: Make sure to have `pytest` installed for testing.
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
   heroku config:set SECRET_KEY=your_secret_key
   heroku config:set DEBUG=False
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
   heroku run python manage.py migrate
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
