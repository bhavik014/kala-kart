import urllib.request
import urllib.parse
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

def test():
    # 1. Test ecosystem framework endpoint
    res = urllib.request.urlopen('http://localhost:8000/api/ecosystem/architecture')
    data = json.loads(res.read().decode('utf-8'))
    print('Ecosystem status:', data.get('status'))
    stages = data.get('framework', {}).get('stages', [])
    print('Number of stages:', len(stages))
    for s in stages:
        print(f"  Stage {s['id']}: {s['stage_name']} -> {s['org_network']}")

    # 2. Test PM Vishwakarma verification endpoint
    post_data = urllib.parse.urlencode({'vishwakarma_id': 'PMV-BH-88214'}).encode()
    req = urllib.request.Request('http://localhost:8000/api/artisan/verify-vishwakarma', data=post_data)
    res2 = urllib.request.urlopen(req)
    v_data = json.loads(res2.read().decode('utf-8'))
    print('Vishwakarma verification status:', v_data.get('status'))
    print('Artisan name:', v_data.get('artisan', {}).get('name'))
    print('Panchayat seal:', v_data.get('artisan', {}).get('panchayat_seal'))

    # 3. Test index.html
    res3 = urllib.request.urlopen('http://localhost:8000/')
    print('Index status code:', res3.status)
    html = res3.read().decode('utf-8')
    print('Has ecosystem-modal:', 'id="ecosystem-modal"' in html)
    print('Has SFURTI stamp:', 'SFURTI CFC' in html)
    print('Has Bhashini badge:', ('Bhashini' in html or 'भाषिणी' in html))
    print('Has Vishwakarma option:', ('PM Vishwakarma' in html or 'पीएम विश्वकर्मा' in html))

if __name__ == "__main__":
    test()
