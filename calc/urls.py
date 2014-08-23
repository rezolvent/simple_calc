from django.conf.urls import patterns

urlpatterns = patterns('',
                       (r'^$', 'calc.views.calc'),
                       (r'^do-calc$', 'calc.views.do_calculate'),
                       )
