# routes.py

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from models import User, Appointment, Barber
from forms import LoginForm, RegistrationForm
from datetime import datetime

auth = Blueprint("auth", __name__)
scheduling = Blueprint("scheduling", __name__)
main = Blueprint("main", __name__)
admin = Blueprint("admin", __name__)


@main.route("/")
def home():
    return render_template(
        "index.html"
    )  # Ensure that index.html exists in your templates folder


# Authentication routes
@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("auth.login"))
        login_user(user)
        return redirect(url_for("scheduling.dashboard"))
    return render_template("login.html", form=form)


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data, email=form.email.data, role=form.role.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful!")
        return redirect(url_for("auth.login"))
    return render_template("register.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


scheduling = Blueprint("scheduling", __name__)


@scheduling.route("/dashboard")
@login_required
def dashboard():
    if current_user.role == "barber":
        # Barber's view of the dashboard
        appointments = Appointment.query.filter_by(barber_id=current_user.id).all()
        return render_template("dashboard.html", appointments=appointments)

    elif current_user.role == "customer":
        # Customer's view of the dashboard
        barbers = Barber.query.all()
        return render_template("dashboard.html", barbers=barbers)

    elif current_user.role == "admin":
        # Redirect admin to the admin dashboard or give a message
        return redirect(url_for("admin.admin_dashboard"))

    else:
        # Handle other cases, if any (or raise an error)
        return "Role not recognized", 403


@scheduling.route("/book/<int:barber_id>", methods=["POST"])
@login_required
def book(barber_id):
    # Get the datetime from the form (as a string)
    date_time_str = request.form["date_time"]

    # Convert the string to a Python datetime object
    try:
        date_time = datetime.strptime(date_time_str, "%Y-%m-%dT%H:%M")
    except ValueError:
        flash("Invalid date or time format. Please try again.", "danger")
        return redirect(url_for("scheduling.dashboard"))

    # Create a new appointment
    appointment = Appointment(
        barber_id=barber_id, customer_id=current_user.id, date_time=date_time
    )

    # Save the appointment to the database
    db.session.add(appointment)
    db.session.commit()

    flash("Appointment booked successfully!", "success")
    return redirect(url_for("scheduling.dashboard"))


@admin.route("/admin")
@login_required
def admin_dashboard():
    if current_user.role != "admin":
        return "Access Denied", 403  # Only allow admins

    users = User.query.all()
    barbers = Barber.query.all()
    appointments = Appointment.query.all()

    return render_template(
        "admin_dashboard.html", users=users, barbers=barbers, appointments=appointments
    )
