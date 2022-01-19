from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.views import Response
from rest_framework import status
from .models import employees,nationality
from .serializers import employeesSerializer,nationalitySerializer
from rest_framework.pagination import PageNumberPagination

class nationalitylist(APIView):
    def get(self,request):
           countryoforigin=nationality.objects.all()
           serializer=nationalitySerializer(countryoforigin,many=True)
           return Response(serializer.data)

class employeeList(APIView):
    # pagination_class = PageNumberPagination
    # @property
    # def paginator(self):
    #     """
    #     The paginator instance associated with the view, or `None`.
    #     """
    #     if not hasattr(self, '_paginator'):
    #         if self.pagination_class is None:
    #             self._paginator = None
    #         else:
    #             self._paginator = self.pagination_class()
    #     return self._paginator
    #
    # def paginate_queryset(self, queryset):
    #     """
    #     Return a single page of results, or `None` if pagination is disabled.
    #     """
    #     if self.paginator is None:
    #         return None
    #     return self.paginator.paginate_queryset(queryset, self.request, view=self)
    #
    # def get_paginated_response(self, data):
    #     """
    #     Return a paginated style `Response` object for the given output data.
    #     """
    #     assert self.paginator is not None
    #     return self.paginator.get_paginated_response(data)
    def get(self,request):
           employees1=employees.objects.all()
           #page = self.paginate_queryset(employees1)
           # if page is not None:
           #     serializer = employeesSerializer(page, many=True)
           #     return self.get_paginated_response(serializer.data)
           serializer=employeesSerializer(employees1,many=True)
           return Response(serializer.data)

    def post(self,request):
           employee_data=request.data
           new_employee=employees.objects.create(firstname=employee_data["firstname"],lastname=employee_data["lastname"],id=employee_data["id"],Gender=employee_data["Gender"],Nationality=employee_data["Nationality"])
           new_employee.save()
           serializer=employeesSerializer(new_employee)
           return Response(serializer.data)

    def delete(self, request):
        employees.objects.all().delete()
        return Response(status=status.HTTP_200_OK)

class employeeUpdate(APIView):

    def get_post(self,pk):
        try:
            return employees.objects.get(pk=pk)
        except employees.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        employee_object =self.get_post(pk)
        serializer  = employeesSerializer(employee_object)
        return Response(serializer.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer  .errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk, format=None):
        employee_object =self.get_post(pk)



        data=request.data
        employee_object.firstname=data["firstname"]
        employee_object.lastname=data["lastname"]
        employee_object.Gender=data["Gender"]
        employee_object.Nationality=data["Nationality"]
        employee_object.id = pk
        #employee_object.save()
        serializer = employeesSerializer(employee_object,data)

        #serializer = employeesSerializer(employee_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
