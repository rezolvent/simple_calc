# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from calc.forms import ContactForm
from calc.models import CalcResult
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf


def calc(request):
    enabled = False
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            enabled = True
            print u'valid!'
    calc_struct = [
        [
            pd("(", None, "symbol"),
            pd(")", None, "symbol"),
            pd("←", None, "symbol"),
            pd("c", None, "symbol")
        ],
        map(pd, [7, 8, 9])+[pd("/", None, "symbol")],
        map(pd, [4, 5, 6])+[pd("*", None, "symbol")],
        map(pd, [1, 2, 3])+[pd("-", None, "symbol")],
        [pd(0), pd(".", None, "symbol"),
            pd("=", None, "symbol"),
            pd("+", None, "symbol")],
    ]
    context = {'calc_struct': calc_struct,
               'sheet_title': 'Calculator',
               'menu_title': u"Ввести Email'ы",
               'csrf_protect': csrf_protect,
               'calc_enabled': enabled,
               'form': form}
    request.session['email_data'] = form.data
    context.update(csrf(request))
    return render_to_response('calc.html', context)


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

    _type = _type if _key != "" else ""
    d = dict(type=_type, key=_key, value=_value)
    return d


def do_calculate(request):
    field = request.GET.get('field', None)
    email_data = request.session['email_data']
    json_data = CalcResult.get_result(field, email_data)
    return HttpResponse(json_data, mimetype="application/json")
