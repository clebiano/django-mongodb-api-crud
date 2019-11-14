from rest_framework.serializers import ModelSerializer, SerializerMethodField
from payments.models import Payment


class PaymentSerializer(ModelSerializer):
    change = SerializerMethodField(method_name='calculate_change')
    best_change = SerializerMethodField(method_name='calculate_best_change')

    class Meta:
        model = Payment
        fields = ['id', 'amount', 'amount_paid', 'change', 'best_change', 'create_date', 'update_date']

    @staticmethod
    def calculate_change(instance):
        amount = float(instance.amount)
        amount_paid = float(instance.amount_paid)
        change = round(amount_paid - amount, 2)
        return change

    @staticmethod
    def calculate_best_change(instance):
        amount = float(instance.amount)
        amount_paid = float(instance.amount_paid)
        change = round(amount_paid - amount, 2)
        best_change = []
        values = (100, 50, 10, 5, 1, 0.5, 0.1, 0.05, 0.01)
        for i in values:

            print(i)
        return change
