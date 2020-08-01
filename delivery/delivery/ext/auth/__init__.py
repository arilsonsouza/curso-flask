from delivery.ext.admin import admin as base_admin
from delivery.ext.auth import models  # noqa
from delivery.ext.auth.admin import UserAdmin
from delivery.ext.auth.models import User
from delivery.ext.db import db

def init_app(app):
	"""TODO: inicializar Flask simple login + JWT"""
	base_admin.add_view(UserAdmin(User, db.session))