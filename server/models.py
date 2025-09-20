# server/models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)           # ✅ body text
    username = db.Column(db.String, nullable=False)       # ✅ username
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # ✅ default now
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Optional: automatically serialize these fields
    serialize_rules = ('-updated_at',)  # can exclude updated_at if you want
