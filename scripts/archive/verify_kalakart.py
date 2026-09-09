import urllib.request
import urllib.parse
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

def verify_kala_kart():
    # 1. Test homepage
    res = urllib.request.urlopen("http://localhost:8000/")
    print("Homepage HTTP Status:", res.status)
    html = res.read().decode('utf-8')
    print("Contains 'Kala Kart':", 'Kala Kart' in html)
    print("Contains 'gateway-screen':", 'gateway-screen' in html)
    print("Contains 'कारीगर कार्यशाला':", 'कारीगर कार्यशाला' in html)
    print("Contains 'दस्तकार बाज़ार':", 'दस्तकार बाज़ार' in html)
    print("Contains 'नया पंजीकरण':", 'नया पंजीकरण' in html)
    print("Contains 'कला यात्रा':", 'कला यात्रा' in html)
    print("Contains 'दिल से दिल तक':", 'दिल से दिल तक' in html)

    # 2. Test products API
    res_p = urllib.request.urlopen("http://localhost:8000/api/products")
    p_data = json.loads(res_p.read().decode('utf-8'))
    products = p_data.get('products', [])
    print(f"Products available: {len(products)}")

    # 3. Test New Registration for non-Vishwakarma artisans
    reg_data = urllib.parse.urlencode({
        'name': 'सुशीला देवी',
        'craft_type': 'हस्तकरघा रेशम बुनाई',
        'village_panchayat': 'चंपापुर ग्राम पंचायत, बिहार',
        'phone': '9876543210',
        'assist_requested': 'true'
    }).encode()
    req_reg = urllib.request.Request("http://localhost:8000/api/artisan/register", data=reg_data)
    res_reg = urllib.request.urlopen(req_reg)
    reg_res = json.loads(res_reg.read().decode('utf-8'))
    print("Registration Status:", reg_res.get('status'))
    print("Assigned Provisional ID:", reg_res.get('artisan', {}).get('vishwakarma_id'))
    print("Gram Panchayat Seal:", reg_res.get('artisan', {}).get('panchayat_seal'))

if __name__ == "__main__":
    verify_kala_kart()
