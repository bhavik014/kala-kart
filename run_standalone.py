import http.server
import socketserver
import json
import os
import urllib.parse

PORT = 8000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
UPLOADS_DIR = os.path.join(BASE_DIR, "uploads")

os.makedirs(UPLOADS_DIR, exist_ok=True)

PRODUCTS_DB = [
    {
        "id": "art-101",
        "artisan_name": "Ramawati Devi",
        "artisan_location": "Madhubani, Bihar",
        "artisan_community": "Self-Help Group (SHG) / PM-AJAY Beneficiary",
        "title": "Authentic Madhubani Handpainted Tree of Life Silk Canvas",
        "category": "Handicrafts & Painting",
        "raw_voice_transcript": "Yeh hamari traditional Madhubani painting hai. Isme natural colors aur kachni style se peacock banaya gaya hai.",
        "story_en": "Handcrafted with natural mineral pigments on Tussar silk canvas, this exquisite Madhubani art depicts the sacred Tree of Life and mating peacocks, symbolizing eternal prosperity and harmony.",
        "story_hi": "यह प्राकृतिक खनिज रंगों और तुषार सिल्क कैनवास पर बनी प्रामाणिक मधुबनी पेंटिंग है। यह जीवन के पवित्र वृक्ष और मयूर जोड़े का प्रतीक है।",
        "materials": ["Tussar Silk Canvas", "Natural Dyes", "Bamboo Pen Work"],
        "suggested_price": 2450,
        "price_range": "₹2,200 - ₹2,800",
        "fair_wage_share": "85% directly to Ramawati Devi",
        "studio_image_url": "https://images.unsplash.com/photo-1579783902614-a3fb3927b675?auto=format&fit=crop&w=800&q=80",
        "qr_code_id": "QR-MADHUBANI-101",
        "trust_score": 98,
        "created_at": "2026-09-07 10:30:00"
    },
    {
        "id": "art-102",
        "artisan_name": "Kishan Lal Prajapati",
        "artisan_location": "Khurja, Uttar Pradesh",
        "artisan_community": "Artisan Co-operative Society",
        "title": "Terracotta Handcrafted Blue-Glazed Ceramic Tea Kettle",
        "category": "Pottery & Ceramics",
        "raw_voice_transcript": "Mitti ka hand-molded kettle hai, double-fired 1100 degree pe. Lead-free organic blue glaze lagaya hai.",
        "story_en": "Double-fired at 1100°C in traditional wood kilns, this lead-free glazed ceramic tea kettle preserves heat while adding rustic elegance to your tea ritual.",
        "story_hi": "1100°C की पारंपरिक भट्टी में पकाई गई यह सीसा-मुक्त सिरेमिक चाय की केतली चाय की गर्मी बनाए रखती है।",
        "materials": ["Natural Clay", "Lead-Free Cobalt Glaze", "Double Wood Fired"],
        "suggested_price": 1250,
        "price_range": "₹1,100 - ₹1,400",
        "fair_wage_share": "88% directly to Kishan Lal",
        "studio_image_url": "https://images.unsplash.com/photo-1578749556568-bc2c40e68b61?auto=format&fit=crop&w=800&q=80",
        "qr_code_id": "QR-CERAMIC-102",
        "trust_score": 96,
        "created_at": "2026-09-07 11:15:00"
    }
]

class ArtisanaHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/" or parsed.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            index_file = os.path.join(TEMPLATES_DIR, "index.html")
            with open(index_file, "rb") as f:
                self.wfile.write(f.read())
        elif parsed.path == "/api/products":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success", "products": PRODUCTS_DB}).encode("utf-8"))
        else:
            super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/api/export/whatsapp":
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            
            # Simple form decode
            params = urllib.parse.parse_qs(body)
            product_id = params.get('product_id', ['art-101'])[0]
            
            product = next((p for p in PRODUCTS_DB if p["id"] == product_id), PRODUCTS_DB[0])
            
            wa_text = f"🎨 *{product['title']}*\n\n" \
                      f"👤 *Maker:* {product['artisan_name']} ({product['artisan_location']})\n" \
                      f"✨ *Materials:* {', '.join(product['materials'])}\n" \
                      f"💰 *Fair Price:* ₹{product['suggested_price']} ({product['fair_wage_share']})\n\n" \
                      f"📖 *Artisan Story:* {product['story_en']}\n\n" \
                      f"🛡️ *Authenticity Badge:* {product['qr_code_id']} (Trust Score: {product['trust_score']}%)"
                      
            wa_url = f"https://api.whatsapp.com/send?text={urllib.parse.quote(wa_text)}"
            
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success", "whatsapp_share_url": wa_url}).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    print(f"🚀 Artisana AI Server running at http://localhost:{PORT}")
    with socketserver.TCPServer(("", PORT), ArtisanaHandler) as httpd:
        httpd.serve_forever()
