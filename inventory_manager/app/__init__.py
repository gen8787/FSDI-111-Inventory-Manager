#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Inventory Manager App"""

from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

from inventory_manager.app import routes  # must go last