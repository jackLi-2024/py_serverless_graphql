#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:Lijiacai
Email:1050518702@qq.com
===========================================
CopyRight@JackLee.com
===========================================
"""

import json
import graphene
import logging
from api import schema
from flask import Flask
from flask_graphql import GraphQLView


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def python_grapgql(event, context):
    operationName = event.get("operationName")
    query = event.get("query")
    variables = event.get("variables")
    result = schema.execute(query, variables=variables)
    if result.errors:
        logging.exception(str(result.errors))
        body = {
            "code": False,
            "data": None,
            "msg": result.errors[0]
        }
    else:
        body = {
            "code": True,
            "data": result.data,
            "msg": None
        }

#     response = {
#         "statusCode": 200,
#         "body": json.dumps(body)
#     }
    return body


def test_python_grapgql():
    event = {"query": """
        query something ($name: String, $num: Int){
            name (name:$name){
                name
            },
            num(num:$num){
                num
            },
            test{
                name
            }
        }
        """, "variables": {'name': "lijiacai", "num": 4}}
    response = python_grapgql(event, context=None)
    print(response)


if __name__ == '__main__':
    # test_python_grapgql()
    app = Flask(__name__)
    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql',
                                                               schema=schema, graphiql=True))
    app.run(port=4901, debug=True, host="0.0.0.0")
