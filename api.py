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
from base_model.test import Num
from api_model.test import Test
from controlers.test import deal_test


class QueryTest(graphene.ObjectType):
    class Meta:
        description = '查询类接口'
        name = "SearchApi"
    name = graphene.Field(Name, name=graphene.String())
    num = graphene.List(Num, num=graphene.Int())
    test = graphene.List(Test)

    def resolve_name(self, info, name):
        return {"name": name}

    def resolve_num(self, info, num):
        result = []
        for i in range(10):
            if i < num:
                result.append({"num": i})
        return result

    def resolve_test(self, info):
        result = deal_test()
        return result
    
    
class MutateTest(graphene.ObjectType):
    class Meta:
        description = '修改操作类接口'
        name = "OperateApi"

    name = graphene.Field(Name, name=graphene.String())
    num = graphene.List(Num, num=graphene.Int())

    def resolve_name(self, info, name):
        return {"name": name}

    def resolve_num(self, info, num):
        result = []
        for i in range(10):
            if i < num:
                result.append({"num": i})
        return result

    def resolve_test(self, info):
        result = deal_test()
        return result

schema = graphene.Schema(QueryTest,mutation=MutateTest)
