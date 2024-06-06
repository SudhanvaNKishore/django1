from django.urls import path
from . import views
urlpatterns=[
        path('fact/<int:num>/',views.cal_fact,name='cal_fact'),
        path('number/',views.number,name='number'),
        path('check/',views.number_list,name='Check odd or even'),
        path('multiplication_table/',views.multiplication_table,name="multiplication_table"),

    ]
