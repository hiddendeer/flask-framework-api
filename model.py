# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Area(db.Model):
    __tablename__ = 'area'

    id = db.Column(db.BigInteger, primary_key=True)
    description = db.Column(db.String(255, 'utf8mb4_general_ci'))
    modifier = db.Column(db.String(255, 'utf8mb4_general_ci'))
    dept_belong_id = db.Column(db.String(255, 'utf8mb4_general_ci'))
    update_datetime = db.Column(db.DateTime)
    create_datetime = db.Column(db.DateTime)
    name = db.Column(db.String(100, 'utf8mb4_general_ci'), nullable=False)
    code = db.Column(db.String(20, 'utf8mb4_general_ci'), nullable=False, unique=True)
    level = db.Column(db.BigInteger, nullable=False)
    pinyin = db.Column(db.String(255, 'utf8mb4_general_ci'), nullable=False)
    initials = db.Column(db.String(20, 'utf8mb4_general_ci'), nullable=False)
    enable = db.Column(db.Integer, nullable=False)
    creator_id = db.Column(db.BigInteger, index=True)
    pcode_id = db.Column(db.String(20, 'utf8mb4_general_ci'), index=True)
