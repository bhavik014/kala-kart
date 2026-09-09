import requests
import io
import time

BASE_URL = "http://localhost:8000"

def test_authentic_voice_pipeline():
    print("=== Testing Authentic Artisan Voice Pipeline ===")
    
    # 1. Create dummy audio recording bytes (simulating MediaRecorder webm chunk)
    # A genuine WebM header snippet with dummy payload
    dummy_webm_header = b"\x1a\x45\xdf\xa3\x9f\x42\x86\x81\x01\x42\xf7\x81\x01\x42\xf2\x81\x04\x42\xf3\x81\x08\x42\x82\x84webm" + b"\x00" * 200
    audio_file_payload = ("artisan_voice.webm", io.BytesIO(dummy_webm_header), "audio/webm")
    
    data = {
        "artisan_name": "रामवती देवी",
        "location": "मधुबनी, बिहार",
        "voice_note": "यह हमारे द्वारा शुद्ध प्राकृतिक रंगों से बनाई गई मधुबनी कलाकृति है।",
        "language": "Hindi",
        "craft_category": "Handicrafts & Painting",
        "price": 3200
    }
    
    files = {
        "audio_file": audio_file_payload
    }
    
    print("Posting to /api/catalog/generate with authentic audio_file...")
    res = requests.post(f"{BASE_URL}/api/catalog/generate", data=data, files=files)
    assert res.status_code == 200, f"Expected 200, got {res.status_code}: {res.text}"
    
    res_data = res.json()
    assert res_data.get("status") == "success", f"Catalog generate failed: {res_data}"
    
    prod = res_data["product"]
    print(f"Created Product ID: {prod['id']}")
    print(f"Product Audio URL: {prod.get('audio_url')}")
    
    # Verify product audio_url is present and points to the saved recorded audio
    audio_url = prod.get("audio_url")
    assert audio_url, "audio_url should not be None"
    assert audio_url.startswith("/static/audio/artisan_"), f"audio_url should start with /static/audio/artisan_, got {audio_url}"
    assert audio_url.endswith(".webm"), f"audio_url should end with .webm, got {audio_url}"
    
    # 2. Fetch the audio file directly from the static server
    print(f"Fetching audio directly from {BASE_URL}{audio_url}...")
    audio_res = requests.get(f"{BASE_URL}{audio_url}")
    assert audio_res.status_code == 200, f"Audio fetch failed with status {audio_res.status_code}"
    assert len(audio_res.content) == len(dummy_webm_header), f"Expected {len(dummy_webm_header)} bytes, got {len(audio_res.content)}"
    assert audio_res.content == dummy_webm_header, "Audio content does not match the uploaded authentic recording!"
    
    content_type = audio_res.headers.get("content-type", "")
    print(f"Static Audio Content-Type: {content_type}")
    assert "audio/webm" in content_type or "audio" in content_type, f"Unexpected content-type: {content_type}"
    
    # 3. Verify that /api/products returns this product with the exact audio_url
    print("Verifying in /api/products marketplace catalog...")
    products_res = requests.get(f"{BASE_URL}/api/products")
    assert products_res.status_code == 200
    prods = products_res.json().get("products", [])
    matched = [p for p in prods if p["id"] == prod["id"]]
    assert len(matched) == 1, f"Product {prod['id']} not found in marketplace!"
    assert matched[0]["audio_url"] == audio_url, f"Marketplace product audio_url mismatch: {matched[0]['audio_url']} vs {audio_url}"
    
    print("=================================================================")
    print("[PASS] AUTHENTIC ARTISAN VOICE RECORDING & PLAYBACK TEST PASSED 100%!")
    print("=================================================================")

if __name__ == "__main__":
    test_authentic_voice_pipeline()
