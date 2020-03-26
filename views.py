#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: views.py
# Created: Wednesday, 25th March 2020 4:03:25 pm
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Thursday, 26th March 2020 6:53:02 pm
# Modified By: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Copyright (c) 2020 Slishee
###

import json
from flask import request
from controller import *

def index():
    """
    Recieves Post Data
    """

    """
    Short forms of what Chafuel provides
        lcbn : last clicked button name
        lufi : last user freeform input
        mui : messenger user id
        fn : first name
        ln : last name
    """
    # data = request.args.to_dict()
    data = request.get_json()
    if request.args.get('lcbn') == 'Get Started' and request.args.get('lufi') == '':
        message = '/start'
    else:
        message = request.args.get('lufi')
    uid = request.args.get('mui')
    fname = request.args.get('fn')
    lname = request.args.get('ln')
    name = fname+' '+lname if fname != lname else lname
    return json.dumps({"messages": [{"text": controller(message, uid, name)}]})
