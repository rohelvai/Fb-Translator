#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: app.py
# Created: Wednesday, 25th March 2020 3:57:22 pm
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Thursday, 26th March 2020 7:42:50 pm
# Modified By: Mohammad Rohel Ahmed (mail2rohel@gmail.com)
# -----https://github.com/dreygur/TranslatorBot.git
# Copyright (c) 2020 Slishee
###

import os
import sys
from flask import Flask

# Stop writing bytecodes
sys.dont_write_bytecode = True

# Internal Importing
import views

app = Flask(__name__)

app.add_url_rule('/', view_func=views.index, methods=["GET", "POST"])

if __name__ == "__main__":
    app.port = int(os.environ.get("PORT", 5000))
    app.host = '0.0.0.0'
    app.debug = True
    app.run()
