from ctypes import c_char
from flask_wtf import FlaskForm
from sqlalchemy import CHAR
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blog.models import User
from flask_login import current_user


class RegistrationForm(FlaskForm):
	username = StringField('نام کاربری', validators=[DataRequired(), Length(min=4, max=25, message='نام کاربری حداقل باید چهار حرفی باشد')])
	password = PasswordField('پسورد', validators=[DataRequired()])
	confirm_password = PasswordField('تایید پسورد', validators=[DataRequired(), EqualTo('password', message='کلمه عبور یکسان نیست')])
	email = StringField('Email', validators=[DataRequired(), Email()])
	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('این نام کاربری وجود دارد')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('با این ایمیل ثبت نام انجام شده است')


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('پسورد', validators=[DataRequired()])
	remember = BooleanField('مرا به خاطر بسپار')


class UpdateProfileForm(FlaskForm):
	username = StringField('نام کاربری', validators=[DataRequired(), Length(min=4, max=25, message='username must be between 4 and 25 characters')])
	email = StringField('Email', validators=[DataRequired(), Email()])

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('این نام کاربری موجود است')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('با این ایمل ثبت نام انجام است')

class PostForm(FlaskForm):
	title = StringField('عنوان', validators=[DataRequired()])
	content = TextAreaField('محتوا', validators=[DataRequired()])

class WordForm(FlaskForm):
	word = StringField('WhgORD', validators=[DataRequired(),Length(min=5, max=5, message='word must be 5 characters')])










