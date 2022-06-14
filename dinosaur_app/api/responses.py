from os import stat
from rest_framework.response import Response
from rest_framework import status

def success(data, code, message):
    data = {
        "success" : True,
        "code" : code,
        "message" : message,
        "data" : data
    }
    return data

def error(code, message):
    data = {
        "success" : False,
        "code" : code,
        "message" : message
    }
    return data
