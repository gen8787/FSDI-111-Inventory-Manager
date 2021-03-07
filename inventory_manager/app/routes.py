#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Routes"""

from inventory_manager.app import app
from inventory_manager.app.database import *
from flask import request, render_template


# ---- I N D E X
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# ---- A D D   P R O D U C T
@app.route("/product/add", methods=["POST"])
def add_product():
    data = request.json
    new_product = create(
        data.get("name"),
        data.get("price"),
        data.get("quantity"),
        data.get("description"),
        data.get("category")
    )

    return {"ok": True, "message": "Success", "product": new_product}


# ---- A L L   P R O D U C T S
@app.route("/products")
def all_products():
    out = get_all_products()
    return str(out)

# ---- O N E   P R O D U C T
@app.route("/product/<product_id>")
def one_product(product_id):
    out = get_one_product(product_id)
    return str(out)


# ---- E D I T   P R O D U C T
@app.route("/product/<product_id>/edit", methods=["PUT"])
def edit_product(product_id):
    data = request.json
    out = update_product(product_id, data)
    return {"ok": out, "message": "Updated"}


# ---- D E L E T E   P R O D U C T
@app.route("/product/<int:product_id>/remove", methods=["DELETE"])
def remove_user(product_id):
    out = delete_product(product_id)
    return str(out)