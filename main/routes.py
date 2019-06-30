# -*- coding: utf-8 -*-
from main.models import Pet
from main.forms import RegistrationForm
from flask import render_template, flash, redirect, url_for, request
from main import app, db

@app.route("/", methods=['GET', 'POST'])
@app.route("/1", methods=['GET', 'POST'])
def first():
    db.create_all()
    form = RegistrationForm()
    if form.validate_on_submit():
        print('true')
        pett = Pet(kind=form.kind.data, nickname=form.nickname.data, age=form.age.data)
        db.session.add(pett)
        db.session.commit()
        # print(form.kind.data)
        # print(form.nickname.data)
        # print(form.age.data)
        print(db.session.query(Pet).count())
        flash(u'Питомец {} записан!'.format(form.nickname.data))
        return redirect(url_for('second'))
    print(db.session.query(Pet).count())
    return render_template('first.html', form=form)

@app.route("/2", methods=['GET', 'POST'])
def second():
    id = request.form.get("id")
    Pet.query.filter(Pet.id == id).delete()
    db.session.commit()
    pets = Pet.query.all()
    return render_template('second.html', a = pets)