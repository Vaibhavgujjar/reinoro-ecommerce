from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Order
import razorpay

# Razorpay client
client = razorpay.Client(auth=("YOUR_KEY", "YOUR_SECRET"))

@api_view(['GET'])
def home(request):
    return Response({"message": "Rein Oro Backend Live 🚀"})

# ---------------- PRODUCTS ----------------
@api_view(['GET'])
def get_products(request):
    products = Product.objects.all().values()
    return Response(products)


# ---------------- PAYMENT ----------------
@api_view(['POST'])
def create_order(request):
    try:
        amount = request.data.get('amount')

        if not amount:
            return Response({"error": "Amount required"}, status=400)

        order = client.order.create({
            "amount": int(float(amount) * 100),
            "currency": "INR",
            "payment_capture": 1
        })

        return Response({
            "id": order["id"],
            "amount": order["amount"],
            "currency": order["currency"]
        })

    except Exception as e:
        return Response({"error": str(e)}, status=500)


# ---------------- SAVE ORDER ----------------
@api_view(['POST'])
def save_order(request):
    user = request.user
    total = request.data.get('total')

    order = Order.objects.create(
        user=user,
        total=total,
        paid=True
    )

    return Response({"message": "Order saved"})