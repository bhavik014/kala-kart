import urllib.request
import urllib.parse
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

def test_all():
    # 1. Test homepage
    res = urllib.request.urlopen("http://localhost:8000/")
    print("Homepage HTTP Status:", res.status)
    html = res.read().decode('utf-8')
    print("HTML length:", len(html))
    print("Contains 'Artisana':", 'Artisana' in html)
    print("Contains 'नया पंजीकरण':", 'नया पंजीकरण' in html)
    print("Contains 'विरासत पासपोर्ट':", 'विरासत पासपोर्ट' in html)

    # 2. Test products API
    res_p = urllib.request.urlopen("http://localhost:8000/api/products")
    p_data = json.loads(res_p.read().decode('utf-8'))
    products = p_data.get('products', [])
    print(f"Products loaded: {len(products)}")
    for p in products:
        print(f" - [{p['id']}] {p['title']} ({p['category']}) by {p['artisan_name']} - Rs {p['suggested_price']}")

    # 3. Test New Registration without Vishwakarma ID
    reg_data = urllib.parse.urlencode({
        'name': 'कमला देवी',
        'craft_type': 'मधुबनी चित्रकला',
        'village_panchayat': 'रंती ग्राम पंचायत, बिहार',
        'phone': '9876543210',
        'assist_requested': 'true'
    }).encode()
    req_reg = urllib.request.Request("http://localhost:8000/api/artisan/register", data=reg_data)
    res_reg = urllib.request.urlopen(req_reg)
    reg_res = json.loads(res_reg.read().decode('utf-8'))
    print("Registration Status:", reg_res.get('status'))
    print("Assigned Provisional ID:", reg_res.get('artisan', {}).get('vishwakarma_id'))
    print("Panchayat Seal Token:", reg_res.get('artisan', {}).get('panchayat_seal'))
    print("Voice Announcement:", reg_res.get('voice_announcement'))

if __name__ == "__main__":
    test_all()
