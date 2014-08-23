# -*- coding: utf-8 -*-
from django.db import models
from django.core.mail import send_mail, get_connection
from calc_lib import NumericStringParser
from datetime import datetime

import threading
import json


class CalcResult(models.Model):
    result = models.FloatField(verbose_name=u'Результат', editable=False)
    message = models.CharField(max_length=256, verbose_name=u'Сообщение с результатом', editable=False)
    time = models.DateTimeField(verbose_name=u'Время', editable=False, blank=True)

    @classmethod
    def send_msg(cls, e_data, e_message):
        connection = get_connection(username=e_data['email_from'],
                                    password=e_data['password'],
                                    fail_silently=False
                                    )

        smt = threading.Thread(target=send_mail,
                               args=(u'Результат вычисления',
                                     e_message,
                                     e_data['email_from'],
                                     [e_data['email_to']],),
                               kwargs=dict(connection=connection)
                               )
        smt.start()

    @classmethod
    def get_result(cls, expression, e_data):
        """side effect!"""
        ans = -1
        error_msg = ""
        if not expression is None:
            try:
                ans = round(NumericStringParser().eval(expression), 10)
            except:
                ans = expression
                error_msg = u"Ошибка! Не верное выражение."
        time_of_result = datetime.now()

        if error_msg == "":
            e_message = u'Операция "{0}" выполнена успешно (Результат: {1})\n'
            e_message = e_message.format(expression, ans)
            cls.objects.create(result=ans,
                               message=e_message,
                               time=time_of_result)
        else:
            e_message = u'{0}\n Выражение: "{1}"\n'.format(error_msg, expression)

        e_message += u'Время: {0}'.format(time_of_result)
        cls.send_msg(e_data, e_message)
        json_data = json.dumps({"value": ans, "errorMsg": error_msg})

        return json_data

    def __unicode__(self):
        return u"%s (%s)" % (self.result, self.time)

    class Meta:
        ordering = ['time']
