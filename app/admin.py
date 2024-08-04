from app import app, mongo

from flask import render_template, request, url_for, redirect, flash, session

import os, re

from functools import wraps

# from flask_login import current_user

app.config["SECRET_KEY"] = "b'n\x1d\xb1\x8a\xc0Jg\x1d\x08|!F3\x04P\xbf'"

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'login' in session:
            return f(*args, **kwargs)
        else:
            flash("Unauthorized, Please login", 'danger')
            return redirect(url_for("index"))
    return wrap

@app.route("/admin")
@login_required
def admin():
    return render_template("admin/login.html")

@app.route("/admin/dashboard")
@login_required
def admin_dashboard():
    
    users = mongo.db.signup.find({}, {"_id": 0, "username": 1, "email": 1, "registeredDate": 1})
    
    return render_template("admin/admin_dashboard.html", users=users)

@app.route("/admin/admin-profile")
@login_required
def admin_profile():
    return render_template("admin/admin_profile.html")

@app.route("/add-student", methods=["GET", "POST"])
def add_student():
    if request.method == 'POST':
        req = request.form
        
        name = req["name"]
        mat_number = req["mat_no"]
        email = req["email"]
        reg_date = req["reg_date"]
        address = req["home_addr"]
        marital_status = req["marital_status"]
        level = req["level"]
        gender = req["gender"]
        phone_number = req["phone_number"]
        dob = req["dob"]
        next_of_kin = req["next_of_kin"]
        state = req["state"]
        city = req["city"]
        image = req["image"]
        
        mongo.db.students.insert_one({"full_name": name, "mat_number": mat_number, "email": email, "reg_date": reg_date, "home_address": address, "marital_status": marital_status, "level": level, "gender": gender, "phone_number": phone_number, "date_of_birth": dob, "next_of_kin": next_of_kin, "state": state, "city": city, "image": image})
        
        return redirect(url_for("admin_dashboard"))
                
    return render_template("admin/add_student.html")

@app.route("/add-lecturer", methods=["GET", "POST"])
def add_lecturer():
    if request.method == 'POST':
        req = request.form
        
        staff_no = req["staff_no"]
        title = req["title"]
        f_name = req["f_name"]
        m_name = req["m_name"]
        l_name = req["l_name"]
        email = req["email"]
        position = req["position"]
        dob = req["birthday"]
        state = req["state"]
        res_addr = req["res_addr"]
        gender = req["gender"]
        phone_no = req["phone_no"]
        qual = req["qual"]
        image = req["image"]
        
        mongo.db.staff.insert_one({"staff_number": staff_no, "title": title, "first_name": f_name, "middle_name": m_name, "last_name": l_name, "email": email, "position": position, "date_of_birth": dob, "state": state, "res_addr": res_addr, "gender": gender, "phone_number": phone_no, "qualification": qual, "image": image})
        
        return redirect(url_for("admin_dashboardd"))
        
    return render_template("admin/add_lecturer.html")

@app.route("/add-found-pet", methods=["GET", "POST"])
@login_required
def add_found_pet():
    if request.method == 'POST':
        req = request.form
        
        petid = req["petId"]
        ownersname = req["ownersName"]
        ownersemail = req["ownersEmail"]
        ownersphoneno = req["ownersPhoneNumber"]
        petname = req["petName"]
        petcolor = req["petColor"]
        pettype = req["petType"]
        gender = req["gender"]
        petage = req["petAge"]
        
        mongo.db.foundPet.insert_one({"Pet Id": petid, "Owner's Name": ownersname, "Owner's Email": ownersemail, "Owner's Phone Number": ownersphoneno, "Pet Name": petname, "Pet Color": petcolor, "Pet Type": pettype, "Gender": gender, "Pet Age": petage})
        
        flash("Record Added Successfully!", "success")
        return redirect(url_for("add_found_pet"))
        
    return render_template("admin/add_found_pet.html")

@app.route("/edit-student")
def edit_student():
    return render_template("admin/edit_student.html")

@app.route("/edit-pets")
@login_required
def edit_pets():
    return render_template("admin/edit_pets.html")

@app.route("/edit-lecturer")
def edit_lecturer():
    return render_template("admin/edit_lecturer.html")

@app.route("/all-added-students")
def all_added_students():
    return render_template("admin/all_added_students.html")

@app.route("/edit-found-pets")
@login_required
def edit_found_pets():
    return render_template("admin/edit_found_pets.html")

@app.route("/all-added-staff")
def all_added_staff():
    return render_template("admin/all_added_staff.html")

@app.route("/all-pets-found")
@login_required
def all_pets_found():
    return render_template("admin/all_pets_found.html")

@app.route("/all-lecturer-view")
def all_lecturer_view():
    return render_template("admin/all_lecturer_view.html")

@app.route("/all-missing-pets")
@login_required
def all_missing_pets():
    return render_template("admin/all_missing_pets.html")