from django.urls import path
from .views import home_page1, MyView, FormView,FormView1,get_post_form, my_form_new,dev_dims

urlpatterns = [

    path('home/', home_page1, name='home_page1'),
    path('api/', MyView.as_view(),name='class_view') ,
    path('', FormView.as_view(),name='class_view'),
    path('form/', FormView1.as_view(),name='class_view1') ,
    path('dev_dim/<int:id>/', dev_dims,name='dev_dim') ,
    # path('formnew/', MyFormNew.as_view(),name='class_view1') ,
    path('formnew/<int:id>/', my_form_new,name='my_form') ,
    path('getpost/', get_post_form,name='class_view2') ,
]
