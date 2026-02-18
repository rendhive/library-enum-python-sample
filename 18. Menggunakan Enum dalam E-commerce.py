from enum import Enum

class OrderStatus(Enum):
    PENDING = "Pending"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    RETURNED = "Returned"

status = OrderStatus.SHIPPED
print(f"Order status: {status.value}")
# Fungsi: Mengelola status pesanan dalam aplikasi e-commerce.
# Kondisi: Ketika Anda perlu mendokumentasikan dan mengelola status kompleks dalam aplikasi.