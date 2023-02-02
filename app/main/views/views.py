from app.main import blp 
from flask import abort, render_template, url_for, redirect, flash, request
from flask_login import current_user, login_required
from app.models import Recipe
from app import db
import os
from config import basedir
from app.main.forms import PasswordReset,ProfileUpdate, ProfilePhotoUpload


@blp.route('/')
def index():
    return render_template('index.html')

@blp.route('/myaccount', methods=['GET'])
@login_required
def my_account():
    recipes = Recipe.query.filter_by(created_by=current_user.id).all()
    return render_template('myaccount.html',user=current_user, recipes=recipes)

# @blp.route('/myaccount', methods=["POST"])
# @login_required
# def account_profile_upload():
#     uploaded_file = request.files['image_file']
#     if uploaded_file.filename != '':
#         sep_file = os.path.splitext(uploaded_file.filename)[1]
#         current_user.avatar = str(current_user.id)+sep_file
#         uploaded_file.save(basedir+'/app/static/avatars/'+current_user.avatar)
#         db.session.add(current_user)
#         db.session.commit()
#     return redirect(url_for('main.my_account'))


@blp.route('/updateaccount', methods=["POST","GET"])
@login_required
def update_account():
    pass_form = PasswordReset()
    profile_form = ProfileUpdate()
    if pass_form.validate_on_submit():
        current_user.password = pass_form.new_pwd.data
        db.session.add(current_user)
        db.session.commit()
        flash('Password successfully changed.', category='alert-success')
        return redirect(url_for('main.my_account'))
    elif 'profile_photo_form' in request.form:
        uploaded_file = request.files['image_file']
        if uploaded_file.filename != '':
            sep_file = os.path.splitext(uploaded_file.filename)[1]
            current_user.avatar = str(current_user.id)+sep_file
            uploaded_file.save(basedir+'/app/static/avatars/'+current_user.avatar)
            db.session.add(current_user)
            db.session.commit()
    elif profile_form.validate_on_submit():
        pwd_change = False
        if current_user.email != profile_form.email.data:
            current_user.email = profile_form.email.data
            current_user.confirmed = False
            pwd_change = True
        elif current_user.username != profile_form.username.data:
            current_user.username = profile_form.username.data
        db.session.add(current_user)
        db.session.commit()
        flash(('Profile successfully updated. A new confirmation email was sent to your updated email.' if pwd_change else 'Profile successfully updated.'), category='alert-success')
        if pwd_change:
            return redirect(url_for('auth.resend_confirmation'))
        else:
            return redirect(url_for('main.my_account'))


    return render_template('updateaccount.html', pass_form=pass_form,profile_form=profile_form, user=current_user)