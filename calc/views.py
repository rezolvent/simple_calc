# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from calc_lib import NumericStringParser
from calc.models import CalcResult
from django.http import HttpResponse
from datetime import datetime
from django.core.mail import send_mail

import threading
import json


def calc(request):
    calc_struct = [
        [
            pd("(", None, "symbol"),
            pd(")", None, "symbol"),
            pd("←", None, "symbol"),
            pd("c", None, "symbol")
        ],
        map(pd, [7,8,9])+[pd("/", None, "symbol")],
        map(pd, [4,5,6])+[pd("*", None, "symbol")],
        map(pd, [1,2,3])+[pd("-", None, "symbol")],
        [pd(0), pd(".", None, "symbol"),
                pd("=", None, "symbol"),
                pd("+", None, "symbol")],
    ]
    return render_to_response('calc.html',
        {'calc_struct':calc_struct,
        'sheet_title':'Calculator'})

def pd(_key, _value=None, _type="number"):
    """ a,b,c -> {type:a, key:b, value:c}"""
    
    symbol_templates = {
        '-': 'minus.html',
        '/': 'divide.html',
        '+': 'plus.html',
        '=': 'equal.html',
        '←': 'arrow-left.html',
        '*': 'multiply.html',
        'c': 'clear.html',
        '.': 'dot.html',
        ')': 'rpar.html',
        '(': 'lpar.html',
    }

    _key = str(_key)

    if _type == "symbol":
        _value = symbol_templates[_key]
    else:
        _value = _value if not (_value is None) else _key

    _type = _type if _key!="" else ""
    d = dict(type=_type, key=_key, value=_value)
    return d

def send_mail_wrap(*args):
    send_mail(*args,
              fail_silently=False)

def do_calculate(request):
    field = request.GET.get('field', None)
    ans = -1
    errorMsg = ""
    if not field is None:
        try:
            ans = round(NumericStringParser().eval(field), 10)
        except:
            ans = field
            errorMsg = u"Ошибка! Не верное выражение."
    time_of_result = datetime.now()
    if errorMsg=="":
        em_message = u"Операция {0} выполнена успешно\n"
        em_message = em_message.format(field, time_of_result)
        CalcResult.objects.create(result=ans, message=em_message, time=time_of_result)
    else:
        em_message = u'{0}\n Выражение: "{1}"\n'.format(errorMsg, field)
    em_message += u'Время: {0}'.format(time_of_result)
    json_data = json.dumps({"value":ans, "errorMsg":errorMsg})

    smt = threading.Thread(target=send_mail_wrap,
        args=(u'Результат вычисления',
              em_message,
              'from@example.com',
              ['to@example.com']))
    smt.start()

    return HttpResponse(json_data, mimetype="application/json")
