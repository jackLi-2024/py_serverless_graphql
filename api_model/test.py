#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:Lijiacai
Email:1050518702@qq.com
===========================================
CopyRight@JackLee.com
===========================================
"""

import os
import sys
import json

try:
    reload(sys)
    sys.setdefaultencoding("utf8")
except:
    pass
import graphene
from base_model.test import Name


class Test(graphene.ObjectType):
    name = graphene.String()
    test2 = graphene.List(Name)
