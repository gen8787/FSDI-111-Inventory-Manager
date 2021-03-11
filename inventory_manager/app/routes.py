#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Routes"""

from inventory_manager.app import app
from inventory_manager.app.database import *
from flask import request, render_template, redirect


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
    return render_template("all_products.html", products = out)

# ---- O N E   P R O D U C T
@app.route("/product/<product_id>")
def one_product(product_id):
    one_product = get_one_product(product_id)
    return render_template("one_product.html", one_product = one_product)


# ---- E D I T   P R O D U C T
@app.route("/product/<product_id>/edit", methods=["PUT"])
def edit_product(product_id):
    data = request.json
    out = update_product(product_id, data)
    return {"ok": out, "message": "Updated"}


# ---- D E L E T E   P R O D U C T
@app.route("/product/<product_id>/remove", methods=["GET"])
def remove_product(product_id):
    out = delete_product(product_id)
    return redirect("/products")


# ---- I N A C T I V E   P R O D U C T S
@app.route("/products/inactive")
def inactive_products():
    out = get_inactive_products()
    return render_template("inactive.html", products = out)


# ---- A C T I V A T E  P R O D U C T
@app.route("/product/<product_id>/activate")
def activate_product(product_id):
    out = set_is_active(product_id)
    return redirect("/products/inactive")

# ---- P A G E   N O T   F O U N D
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404