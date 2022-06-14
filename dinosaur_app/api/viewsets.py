from http.client import responses
from rest_framework.viewsets import ModelViewSet
from dinosaur_app.api.responses import success,error
from rest_framework.response import Response

class BaseDinosaurViewSet(ModelViewSet):

    def list(self, request, *args, **kwargs):
        pre = super().list(request, *args, **kwargs)
        return Response(data=success(pre.data,200,"List Successful!"),status=pre.status_code,headers=pre.headers)

    def create(self, request, *args, **kwargs):
        pre = super().create(request, *args, **kwargs)
        return Response(data=success(pre.data,201,"Create Successful!"),status=pre.status_code,headers=pre.headers)
    
    def retrieve(self, request, *args, **kwargs):
        pre = super().retrieve(request, *args, **kwargs)
        return Response(data=success(pre.data,200,"Retrieve Successful!"),status=pre.status_code,headers=pre.headers)

    def update(self, request, *args, **kwargs):
        pre = super().update(request, *args, **kwargs)
        return Response(data=success(pre.data,200,"Update Successful!"),status=pre.status_code,headers=pre.headers)

    def destroy(self, request, *args, **kwargs):
        pre = super().destroy(request, *args, **kwargs)
        return Response(data=success({},204,"Delete Successful!"),status=pre.status_code,headers=pre.headers)