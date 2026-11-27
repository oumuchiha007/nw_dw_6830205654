# ตารางใน schema raw → ไฟล์ต้นทาง (มาจาก 2 ระบบ)
SOURCES = {
    # แหล่ง A: ระบบขายปัจจุบัน
    "customer": "raw/customer.csv",
    "employees": "raw/employees.csv",
    "suppliers": "raw/suppliers.csv",
    "shippers": "raw/shippers.csv",
    "products": "raw/products.csv",
    "orders": "raw/orders.csv",
    "order_details": "raw/order_details.csv",

    # แหล่ง B: ระบบขายเดิม (มีเฉพาะใบสั่งซื้อและรายการสินค้า)
    "legacy_orders": "legacy/orders.csv",
    "legacy_order_details": "legacy/order_details.csv",
}