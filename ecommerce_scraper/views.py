from django.shortcuts import render
from rest_framework.views import APIView

from ecommerce_scraper_website.services.view_services import ViewServices


class Home(APIView):
    def get(self, request, *args, **kwargs):
        kwargs.update({
            "request": request
        })
        service_obj = ViewServices(service_name="home")
        status_code, data = service_obj.execute_service(*args, **kwargs)
        return render(request=request, template_name='index.html', context={
            "status_code": status_code,
            "data": data
        })

    def post(self, request, *args, **kwargs):
        kwargs.update({
            "request": request
        })
        service_obj = ViewServices(service_name="home")
        status_code, data = service_obj.execute_service(*args, **kwargs)
        return render(request=request, template_name='index.html', context={
            "status_code": status_code,
            "data": data
        })
