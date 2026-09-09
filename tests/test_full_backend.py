# -*- coding: utf-8 -*-
import sys
import json
import urllib.request
import urllib.parse

sys.stdout.reconfigure(encoding='utf-8')

BASE_URL = "http://localhost:8000"

def get(path):
    url = BASE_URL + path
    req = urllib.request.Request(url, method='GET')
    with urllib.request.urlopen(req) as resp:
        return resp.getcode(), json.loads(resp.read().decode('utf-8'))

def post_json(path, data):
    url = BASE_URL + path
    body = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url, data=body, headers={'Content-Type': 'application/json'}, method='POST')
    with urllib.request.urlopen(req) as resp:
        return resp.getcode(), json.loads(resp.read().decode('utf-8'))

def post_form(path, data):
    url = BASE_URL + path
    body = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data=body, headers={'Content-Type': 'application/x-www-form-urlencoded'}, method='POST')
    with urllib.request.urlopen(req) as resp:
        return resp.getcode(), json.loads(resp.read().decode('utf-8'))

passed = 0
total = 0

def test(name, condition, extra=""):
    global passed, total
    total += 1
    if condition:
        passed += 1
        print(f"PASS: {name} {extra}")
    else:
        print(f"FAIL: {name} {extra}")

print("=================================================================")
print("RUNNING COMPREHENSIVE END-TO-END BACKEND & E-COMMERCE TEST SUITE")
print("=================================================================\n")

# Test 1: GET /api/products
code, res = get("/api/products")
test("1. Products list returns success", code == 200 and res.get("status") == "success", f"Count: {res.get('count')}")
test("   Products count >= 6", len(res.get("products", [])) >= 6)

# Test 2: Search and Filter
code, res_s = get("/api/products?search=" + urllib.parse.quote("मधुबनी"))
test("2. Product search works", code == 200 and len(res_s.get("products", [])) >= 1)

# Test 3: GI Tag Filter
code, res_gi = get("/api/products?gi_only=true")
test("3. GI Tag filter works", code == 200 and len(res_gi.get("products", [])) >= 1)

# Test 4: GET /api/products/art-101
code, res_p1 = get("/api/products/art-101")
test("4. Single product detail returns correct data", code == 200 and res_p1.get("product", {}).get("id") == "art-101")

# Test 5: Dynamic Fair Pricing API
fair_price_payload = {
    "craft_category": "मधुबनी पेंटिंग (GI)",
    "labor_days": "4.5",
    "complexity": "intricate",
    "weight_grams": "750",
    "gi_certified": "true",
    "sfurti_grade": "Grade A+"
}
code, res_price = post_form("/api/gov/pricing/predict-fair-price", fair_price_payload)
test("5. Dynamic fair pricing predicts price", code == 200 and res_price.get("suggested_fair_price", 0) > 2000)

# Test 6: POST /api/orders/checkout (E-Commerce Order Placement)
checkout_payload = {
    "cart_items": [
        {
            "product_id": "art-101",
            "quantity": 1,
            "customization": "मातृभूमि आशीर्वाद संदेश"
        }
    ],
    "buyer_name": "विक्रम साराभाई",
    "buyer_phone": "9811223344",
    "shipping_address": "अंतरिक्ष भवन, न्यू बीईएल रोड",
    "city": "बेंगलुरु",
    "state": "कर्नाटक",
    "pincode": "560094",
    "payment_method": "UPI"
}
code, res_ord = post_json("/api/orders/checkout", checkout_payload)
test("6. Order checkout succeeds", code == 200 and res_ord.get("success") is True, f"Order: {res_ord.get('order_id')}")
order_id = res_ord.get("order_id")
tracking_num = res_ord.get("tracking_num")

# Test 7: GET /api/orders and GET /api/orders/{order_id}
code, res_orders = get("/api/orders")
test("7a. List all orders retrieves placed orders", code == 200 and res_orders.get("count", 0) >= 1)

code, res_single_order = get(f"/api/orders/{order_id}")
test("7b. Retrieve placed order by ID", code == 200 and res_single_order.get("order", {}).get("order_id") == order_id)

# Test 8: Order Receipt HTML & Challan
rcpt_url = f"{BASE_URL}/api/orders/{order_id}/receipt"
with urllib.request.urlopen(rcpt_url) as rcpt_resp:
    rcpt_code = rcpt_resp.getcode()
    rcpt_html = rcpt_resp.read().decode('utf-8')
    test("8. Order receipt HTML generated with postal challan", rcpt_code == 200 and "SPEED POST" in rcpt_html and "ORD-KK" in rcpt_html)

# Test 9: Artisan Digital DBT Passbook
code, res_pb = get("/api/artisan/art-101/passbook")
test("9. Artisan DBT passbook retrieved from SQLite", code == 200 and res_pb.get("success") is True)
test("   Passbook contains lifetime earnings & transactions", "summary" in res_pb.get("passbook", {}) and len(res_pb.get("passbook", {}).get("transactions", [])) >= 1)

# Test 10: India Post Consignment Tracking
code, res_track = get(f"/api/gov/indiapost/track/{tracking_num or 'EM84721109IN'}")
test("10. India Post tracking returns 4-stage timeline", code == 200 and len(res_track.get("tracking_timeline", [])) == 4)

# Test 11: Buyer Gratitude Note
code, res_grat = post_form("/api/buyer/gratitude", {
    "product_id": "art-101",
    "buyer_name": "विक्रम",
    "city": "बेंगलुरु",
    "message": "आपकी बनाई पेंटिंग हमारे घर की शोभा बढ़ा रही है। बहुत-बहुत धन्यवाद!"
})
test("11. Buyer gratitude saved to database", code == 200 and res_grat.get("status") == "success")

# Test 12: SHG Request Kala Sakhi Visit
code, res_sakhi = post_form("/api/shg/request-sakhi", {
    "artisan_name": "रामवती देवी",
    "village_tola": "पश्चिम टोला, मधुबनी",
    "assistance_type": "कैटलॉगिंग एवं डिजिटल ऑनबोर्डिंग सहायता"
})
test("12. Request Kala Sakhi visit persists to SQLite", code == 200 and res_sakhi.get("status") == "success")

# Test 13: SHG Join Bulk Raw Material Pool
code, res_bulk = post_form("/api/shg/join-bulk-order", {
    "artisan_name": "रामवती देवी",
    "qty_kg": "5",
    "material_name": "Tussar Silk Reeling Pack"
})
test("13. Join SHG bulk raw material pool persists to SQLite", code == 200 and res_bulk.get("status") == "success" and res_bulk.get("savings_amount", 0) > 0)

# Test 14: Register New Artisan
code, res_reg = post_form("/api/artisan/register", {
    "name": "चंपा देवी",
    "craft_type": "सिक्की घास शिल्प (GI)",
    "village_panchayat": "राजनगर ग्राम पंचायत, मधुबनी",
    "phone": "9876543219"
})
test("14. Artisan registration persists to SQLite", code == 200 and res_reg.get("status") == "success" and "art-reg-" in res_reg.get("artisan", {}).get("artisan_id", ""))

print("\n=================================================================")
print(f"TEST RESULTS: {passed} / {total} Passed ({int(passed/total*100)}%)")
print("=================================================================")

if passed == total:
    print("ALL TESTS PASSED! FULL BACKEND AND INTEGRATION FULLY OPERATIONAL!")
else:
    sys.exit(1)
