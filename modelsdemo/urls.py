from django.urls import path
from .views import DepartmentView, SpecificDepartmentView

urlpatterns = [
    path('', DepartmentView.as_view(), name='departments'),
    path('<int:department_id>/', SpecificDepartmentView.as_view(), name='department_by_id')
]


