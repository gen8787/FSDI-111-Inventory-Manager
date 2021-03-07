#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Database functions"""

from flask import g
from inventory_manager.app import app
import sqlite3

DATABASE = "inventory_manager.db"

# ---- C O N N E C T   D B
def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# ---- C R E A T E   P R O D U C T
def create(name, price, quantity, description, category):
    values = (name, price, quantity, description, category)
    query = """INSERT INTO product(name, price, quantity, description, category) VALUES(?, ?, ?, ?, ?)"""
    cursor = get_db()
    last_row_id = cursor.execute(query, values).lastrowid
    cursor.commit()
    return last_row_id


# ---- G E T   A L L   P R O D U C T S
def get_all_products():
    cursor = get_db().execute("SELECT * FROM product", ())
    results = cursor.fetchall()
    cursor.close()
    return results


# ---- G E T   O N E   P R O D U C T
def get_one_product(product_id):
    cursor = get_db().execute("SELECT * FROM product WHERE id=%s" % product_id, ())
    results = cursor.fetchall()
    cursor.close()
    return results


# ---- U P D A T E   U S E R
def update_product(product_id, values: dict):
    value_string = ",".join("%s=\"%s\"" % (key, val) for key, val in values.items())
    query = """UPDATE product SET %s WHERE id=?""" % value_string
    cursor = get_db()
    cursor.execute(query, (product_id))
    cursor.commit()
    return True


# ---- D E L E T E   P R O D U C T
def delete_product(product_id):
    query = "UPDATE product SET is_active=False WHERE id=%s" % product_id
    cursor = get_db()
    print(query)
    cursor.execute(query, ())
    cursor.commit()
    return True


# ---- G E T   I N A C T I V E  P R O D U C T S
def get_inactive_products():
    cursor = get_db().execute("SELECT * FROM product WHERE is_active=0")
    results = cursor.fetchall()
    cursor.close()
    return results