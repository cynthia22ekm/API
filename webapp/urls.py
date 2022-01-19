from django.urls import path
from .views import employeeList,nationalitylist
from .views import employeeUpdate

urlpatterns=[

    path("api/employees/<int:pk>/",employeeUpdate.as_view()),
    path('api/employees/',employeeList.as_view()),
    path('api/nationality/',nationalitylist.as_view())
]