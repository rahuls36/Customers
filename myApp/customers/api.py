from .models import Customer
from rest_framework import viewsets,permissions
from rest_framework.decorators import action
from .serializers import CustomerSerializer
from rest_framework.response import Response




class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail= False)
    def get_youngest_customer(self,request):
        n = int(self.request.query_params.get('n'))
        customers = Customer.objects.all()
        young_customers = customers.order_by('-dob')[:n]
        serializer = CustomerSerializer(young_customers, many = True)
        return Response(serializer.data)