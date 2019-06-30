# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):
    kind = StringField(u'вид питомца',
                        validators=[DataRequired(), Length(min=2, max=10)])
    nickname = StringField(u'кличка',
                        validators=[DataRequired(), Length(min=1, max=10)])
    age = StringField(u'возраст',
                        validators=[DataRequired()])
    submit = SubmitField(u'Записать в базу')



