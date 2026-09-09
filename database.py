# -*- coding: utf-8 -*-
"""
Kala Kart (कला कार्ट) — Persistent Relational Database Engine
Built on SQLite with WAL mode for fast concurrent read/write operations.
Zero external database dependencies required.
"""

import sqlite3
import json
import os
import time
import uuid

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "kalakart.db")

def get_connection():
    """Returns a thread-safe connection to the SQLite database with row_factory."""
    conn = sqlite3.connect(DB_PATH, timeout=20.0)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes all database tables and seeds initial authentic crafts and artisans if empty."""
    conn = get_connection()
    cursor = conn.cursor()

    # 1. Products Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        title_hi TEXT,
        category TEXT NOT NULL,
        materials_json TEXT,
        suggested_price INTEGER NOT NULL,
        price_range TEXT,
        story_en TEXT,
        story_hi TEXT,
        raw_voice_transcript TEXT,
        audio_url TEXT,
        studio_image_url TEXT,
        raw_image_url TEXT,
        qr_code_id TEXT,
        trust_score INTEGER DEFAULT 98,
        gi_tag_no TEXT,
        thumbprint_id TEXT,
        artisan_id TEXT,
        artisan_name TEXT,
        artisan_location TEXT,
        artisan_experience TEXT,
        artisan_photo TEXT,
        hands_photo TEXT,
        artisan_quote TEXT,
        natural_swatches_json TEXT,
        family_impact_json TEXT,
        craft_lifecycle_json TEXT,
        institutional_json TEXT,
        buyer_gratitude_json TEXT,
        studio_rules_json TEXT,
        likes INTEGER DEFAULT 0,
        created_at TEXT
    );
    """)

    # 2. Orders Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id TEXT PRIMARY KEY,
        tracking_num TEXT UNIQUE NOT NULL,
        dbt_ref TEXT NOT NULL,
        order_date TEXT,
        est_delivery TEXT,
        buyer_name TEXT NOT NULL,
        buyer_phone TEXT,
        shipping_address TEXT,
        city TEXT,
        state TEXT,
        pincode TEXT,
        full_address TEXT,
        cart_items_json TEXT NOT NULL,
        subtotal INTEGER NOT NULL,
        shipping_fee INTEGER NOT NULL,
        total_amount INTEGER NOT NULL,
        artisan_remittance INTEGER NOT NULL,
        platform_fee INTEGER NOT NULL,
        sfurti_reserve INTEGER NOT NULL,
        payment_method TEXT NOT NULL,
        status TEXT NOT NULL,
        speed_post_hub TEXT,
        created_at TEXT
    );
    """)

    # 3. Artisans Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS artisans (
        artisan_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        phone TEXT,
        vishwakarma_id TEXT,
        trade TEXT,
        gram_panchayat TEXT,
        panchayat_seal TEXT,
        verification_status TEXT,
        tool_grant TEXT,
        total_earnings INTEGER DEFAULT 0,
        bank_status TEXT,
        community TEXT,
        sfurti_cluster TEXT,
        rutag_support TEXT,
        passbook_qr TEXT,
        registered_at TEXT
    );
    """)

    # 4. Postal Pickups Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS postal_pickups (
        pickup_id TEXT PRIMARY KEY,
        consignment_no TEXT UNIQUE NOT NULL,
        artisan_id TEXT,
        artisan_name TEXT NOT NULL,
        product_title TEXT NOT NULL,
        village_pincode TEXT NOT NULL,
        weight_kg REAL DEFAULT 0.85,
        scheduled_time TEXT,
        status TEXT NOT NULL,
        created_at TEXT
    );
    """)

    # 5. Gratitude Notes Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS gratitude_notes (
        note_id TEXT PRIMARY KEY,
        product_id TEXT NOT NULL,
        buyer_name TEXT NOT NULL,
        city TEXT,
        message TEXT NOT NULL,
        created_at TEXT
    );
    """)

    # 6. SHG Bulk Orders Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS shg_orders (
        order_id TEXT PRIMARY KEY,
        artisan_id TEXT,
        artisan_name TEXT NOT NULL,
        material_name TEXT NOT NULL,
        quantity_kg REAL NOT NULL,
        discounted_price INTEGER NOT NULL,
        retail_price INTEGER NOT NULL,
        savings INTEGER NOT NULL,
        status TEXT NOT NULL,
        created_at TEXT
    );
    """)

    # 7. Sakhi Requests Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sakhi_requests (
        request_id TEXT PRIMARY KEY,
        artisan_id TEXT,
        artisan_name TEXT NOT NULL,
        village_pincode TEXT NOT NULL,
        assistance_type TEXT NOT NULL,
        scheduled_visit TEXT,
        status TEXT NOT NULL,
        created_at TEXT
    );
    """)

    
    try:
        cursor.execute("ALTER TABLE products ADD COLUMN studio_rules_json TEXT;")
    except Exception:
        pass

    conn.commit()

    # Check if seed products exist; if not, seed them
    cursor.execute("SELECT COUNT(*) as count FROM products;")
    row = cursor.fetchone()
    if row["count"] == 0:
        seed_initial_database(conn)

    conn.close()

def seed_initial_database(conn):
    """Seeds the 6 authentic master crafts and seed artisans."""
    cursor = conn.cursor()

    seed_artisans = [
        {
            "artisan_id": "art-101",
            "name": "श्रीमती सुमित्रा देवी (Sumitra Devi)",
            "phone": "9876543210",
            "vishwakarma_id": "PMV-BH-88214",
            "trade": "मिथिला चित्रकला (Madhubani Painting)",
            "gram_panchayat": "रंती ग्राम पंचायत, मधुबनी, बिहार",
            "panchayat_seal": "GP-VERIFIED-BH-2026",
            "verification_status": "सत्यापित लाभार्थी (PM Vishwakarma Certified)",
            "tool_grant": "₹15,000 टूलकिट अनुदान स्वीकृत",
            "total_earnings": 42850,
            "bank_status": "Aadhaar Linked DBT Active (Gramin Bank of Bihar)",
            "community": "गंगा महिला स्वयं सहायता समूह #14",
            "sfurti_cluster": "मधुबनी हैंडीक्राफ्ट सीएफसी (SFURTI)",
            "rutag_support": "आईआईटी रुड़की रूरल टेक लैब समर्थित",
            "passbook_qr": "KALA-PASSBOOK-MD-883",
            "registered_at": "2026-01-15 10:00:00"
        },
        {
            "artisan_id": "art-102",
            "name": "राम कुमार प्रजापति (Ram Kumar Prajapati)",
            "phone": "9823456781",
            "vishwakarma_id": "PMV-UP-71920",
            "trade": "खुर्जा पारंपरिक कुंभकारी (Pottery)",
            "gram_panchayat": "खुर्जा नगर पंचायत, बुलंदशहर, उत्तर प्रदेश",
            "panchayat_seal": "GP-VERIFIED-UP-2026",
            "verification_status": "सत्यापित लाभार्थी (PM Vishwakarma Certified)",
            "tool_grant": "₹15,000 टूलकिट अनुदान स्वीकृत",
            "total_earnings": 36400,
            "bank_status": "Aadhaar Linked DBT Active (Prathama UP Gramin Bank)",
            "community": "खुर्जा कुम्हार शिल्प संघ",
            "sfurti_cluster": "SFURTI खुर्जा सिरेमिक क्लस्टर",
            "rutag_support": "आईआईटी दिल्ली समर्थित सौर चाक",
            "passbook_qr": "KALA-PASSBOOK-UP-719",
            "registered_at": "2026-02-10 11:30:00"
        }
    ]

    for a in seed_artisans:
        cursor.execute("""
        INSERT INTO artisans (
            artisan_id, name, phone, vishwakarma_id, trade, gram_panchayat,
            panchayat_seal, verification_status, tool_grant, total_earnings,
            bank_status, community, sfurti_cluster, rutag_support, passbook_qr, registered_at
        ) VALUES (
            :artisan_id, :name, :phone, :vishwakarma_id, :trade, :gram_panchayat,
            :panchayat_seal, :verification_status, :tool_grant, :total_earnings,
            :bank_status, :community, :sfurti_cluster, :rutag_support, :passbook_qr, :registered_at
        )
        """, a)

    seed_products = [
        {
            "id": "art-101",
            "artisan_id": "art-101",
            "artisan_name": "श्रीमती सुमित्रा देवी (Sumitra Devi)",
            "artisan_experience": "32 वर्षों से मधुबनी कला साधना",
            "artisan_location": "जितवारपुर, मधुबनी, बिहार",
            "artisan_photo": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=200&q=80",
            "hands_photo": "https://images.unsplash.com/photo-1579783902614-a3fb3927b675?auto=format&fit=crop&w=800&q=80",
            "artisan_quote": "यह सिर्फ पेंटिंग नहीं, हमारी कुलदेवी का आशीर्वाद और नानी का प्यार है जो अब आपके घर जाएगा।",
            "title": "Authentic Madhubani Handpainted Tree of Life Silk Canvas",
            "title_hi": "मिथिला कोहबर व कल्पवृक्ष पारंपरिक सिल्क चित्रकला",
            "category": "Handicrafts & Painting",
            "materials_json": json.dumps(["Tussar Silk Canvas", "Natural Mineral Dyes", "Bamboo Pen Work"]),
            "suggested_price": 2450,
            "price_range": "₹2,200 - ₹2,800",
            "story_en": "Handcrafted with natural mineral pigments on Tussar silk canvas, this exquisite Madhubani art depicts the sacred Tree of Life and peacocks, symbolizing eternal harmony. Created over 4 days of intricate line work.",
            "story_hi": "यह प्राकृतिक खनिज रंगों और तुषार सिल्क कैनवास पर बनी प्रामाणिक मधुबनी पेंटिंग है। यह जीवन के पवित्र कल्पवृक्ष और मयूर जोड़े का प्रतीक है, जो घर में सुख, समृद्धि और शांति लाती है।",
            "raw_voice_transcript": "Yeh hamari traditional Madhubani painting hai. Isme natural colors aur kachni style se peacock aur Tree of Life banaya gaya hai. Ek painting me 4 din lagte hain.",
            "audio_url": "/static/audio/sample_art101.mp3",
            "studio_image_url": "https://images.unsplash.com/photo-1579783902614-a3fb3927b675?auto=format&fit=crop&w=800&q=80",
            "raw_image_url": "https://images.unsplash.com/photo-1579783902614-a3fb3927b675?auto=format&fit=crop&w=800&q=80",
            "qr_code_id": "QR-MADHUBANI-101",
            "trust_score": 98,
            "gi_tag_no": "GI-BH-MD-088",
            "thumbprint_id": "SUMITRA-THUMB-2026",
            "natural_swatches_json": json.dumps([
                {"hex": "#a83e2b", "name": "Mithila Vermilion", "regional_name": "सिंदूर लाल"},
                {"hex": "#e9c46a", "name": "Turmeric Ochre", "regional_name": "हल्दी पीला"},
                {"hex": "#264653", "name": "Kachni Charcoal", "regional_name": "काजल काला"},
                {"hex": "#2a9d8f", "name": "Forest Bael Leaf", "regional_name": "बेल पत्र हरा"}
            ]),
            "family_impact_json": json.dumps({
                "beneficiary": "प्रिया (बेटी, उम्र 8 वर्ष)",
                "impact_story": "इस महीने के 4 ऑर्डर्स ने बिटिया प्रिया की कक्षा 4 की सालभर की पुस्तकें व स्कूल ड्रेस का खर्च उठाया।",
                "progress_pct": 78,
                "goal_label": "कार्यशाला की नई पक्की छत (Monsoon Proofing)",
                "goal_stat": "₹19,500 / ₹25,000 सुरक्षित"
            }),
            "craft_lifecycle_json": json.dumps([
                {"step": "1. नीम की कलम", "desc": "जंगली नीम की पतली टहनी से कलम बनाकर शुद्ध गोंद लगाना", "days": "दिन 1"},
                {"step": "2. प्राकृतिक रंग", "desc": "पलाश के फूल (पीला), काजल (काला), तांबे की भस्म (हरा)", "days": "दिन 2"},
                {"step": "3. कच्चा सिल्क शोधन", "desc": "भागलपुरी तुषार सिल्क पर गोबर लेप से कैनवास तैयार करना", "days": "दिन 3"},
                {"step": "4. 4 दिन की साधना", "desc": "बिना स्केल के हाथ से कछनी व भरनी शैली में रेखांकन", "days": "दिन 4"}
            ]),
            "institutional_json": json.dumps({
                "stage_1_identity": {"vishwakarma_id": "PMV-BH-88214", "gp_seal": "रंती ग्राम पंचायत मुहर"},
                "stage_2_raw_material": {"cfc_hub": "मधुबनी SFURTI सिल्क क्लस्टर", "discount_pct": "36% बचत"},
                "stage_3_catalog": {"engine": "MeitY Bhashini IndicASR (मैथिली)", "languages": 6},
                "stage_4_authenticity": {"digilocker_uri": "GI-BH-MD-088 (GI Registry)", "status": "सत्यापित"},
                "stage_5_logistics": {"consignment_no": "EM829104721IN", "hub": "मधुबनी डाकघर पिकअप"},
                "stage_6_market": {"wage_guarantee": "८५% सीधा DBT खाता", "platform_fee": "१०% पारदर्शी"}
            }),
            "buyer_gratitude_json": json.dumps([
                {
                    "buyer_name": "अनामिका शर्मा",
                    "city": "Bengaluru",
                    "message": "दीदी, आपकी पेंटिंग हमारे नए घर के मुख्य द्वार पर लगी है। सब पूछते हैं कहाँ से ली!",
                    "time": "2 दिन पहले"
                }
            ]),
            "likes": 42,
            "created_at": "2026-09-01 10:00:00"
        },
        {
            "id": "art-102",
            "artisan_id": "art-102",
            "artisan_name": "राम कुमार प्रजापति (Ram Kumar Prajapati)",
            "artisan_experience": "24 वर्षों का पुस्तैनी कुंभकारी कौशल",
            "artisan_location": "खुर्जा, बुलंदशहर, उत्तर प्रदेश",
            "artisan_photo": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=200&q=80",
            "hands_photo": "https://images.unsplash.com/photo-1578749556568-bc2c40e68b61?auto=format&fit=crop&w=800&q=80",
            "artisan_quote": "यह मिट्टी गंगा की तलहटी से आती है, 1200 डिग्री भट्टी में तपकर इसमें नीलमणि सी चमक आती है।",
            "title": "Terracotta Handcrafted Blue-Glazed Ceramic Tea Kettle",
            "title_hi": "खुर्जा हाथ से गढ़ा नीलमणि ग्लेज़्ड पॉटरी केतली",
            "category": "Pottery & Ceramics",
            "materials_json": json.dumps(["Riverbed Terracotta", "Cobalt Mineral Glaze", "Lead-Free Ceramic Clay"]),
            "suggested_price": 1250,
            "price_range": "₹1,100 - ₹1,450",
            "story_en": "Molded on a traditional potter wheel using fine riverbed clay and glazed with cobalt Persian blue minerals, this kettle is lead-free, food-safe, and fired at 1200°C for exceptional durability.",
            "story_hi": "यह खुर्जा की प्रसिद्ध पारंपरिक पॉटरी केतली है। गंगा कछार की मिट्टी को तीन बार छानकर चाक पर गढ़ा गया है और सीसा-मुक्त (Lead-Free) प्राकृतिक कोबाल्ट ग्लेज़ से रंगा गया है।",
            "raw_voice_transcript": "Khurja ki mitti ko 3 bar chhan kar chak par dhalta hoon. Persian blue glaze lead-free hai aur 1200 degree bhatti me pakti hai.",
            "audio_url": "/static/audio/sample_art102.mp3",
            "studio_image_url": "https://images.unsplash.com/photo-1578749556568-bc2c40e68b61?auto=format&fit=crop&w=800&q=80",
            "raw_image_url": "https://images.unsplash.com/photo-1578749556568-bc2c40e68b61?auto=format&fit=crop&w=800&q=80",
            "qr_code_id": "QR-KHURJA-102",
            "trust_score": 97,
            "gi_tag_no": "GI-UP-KH-012",
            "thumbprint_id": "RAMKUMAR-THUMB-2026",
            "natural_swatches_json": json.dumps([
                {"hex": "#1d3557", "name": "Cobalt Persian Blue", "regional_name": "फारसी नीला"},
                {"hex": "#457b9d", "name": "Sky Turquoise", "regional_name": "आसमानी फिरोज़ा"},
                {"hex": "#f1faee", "name": "Kaolin White", "regional_name": "चीनी मिट्टी श्वेत"},
                {"hex": "#e76f51", "name": "Terracotta Ochre", "regional_name": "पक्की मिट्टी"}
            ]),
            "family_impact_json": json.dumps({
                "beneficiary": "रोहन (बेटा, आईटीआई छात्र)",
                "impact_story": "इस हफ्ते के ऑर्डर्स से बेटे रोहन के इलेक्ट्रीशियन डिप्लोमा की सेमेस्टर फीस भरी गई।",
                "progress_pct": 82,
                "goal_label": "सौर ऊर्जा चालित आधुनिक इलेक्ट्रिक चाक (Solar Wheel)",
                "goal_stat": "₹14,200 / ₹18,000 सुरक्षित"
            }),
            "craft_lifecycle_json": json.dumps([
                {"step": "1. मिट्टी छानना", "desc": "गंगा कछार की दोमट मिट्टी को महीन कपड़े से ३ बार छानना", "days": "दिन 1"},
                {"step": "2. चाक पर ढलाई", "desc": "हाथ से चाक घुमाकर केतली व टोटी का सटीक संतुलन", "days": "दिन 2"},
                {"step": "3. प्राकृतिक लेप", "desc": "कोबाल्ट खनिज व क्वार्ट्ज़ चूरे से हाथ से नक्काशीदार ग्लेज़", "days": "दिन 3"},
                {"step": "4. 1200° भट्ठी", "desc": "पारंपरिक लकड़ी भट्ठी में २४ घंटे तक पकाना", "days": "दिन 4"}
            ]),
            "institutional_json": json.dumps({
                "stage_1_identity": {"vishwakarma_id": "PMV-UP-71920", "gp_seal": "खुर्जा नगर पंचायत सत्यापन"},
                "stage_2_raw_material": {"cfc_hub": "SFURTI खुर्जा सिरेमिक क्लस्टर", "discount_pct": "34% बचत"},
                "stage_3_catalog": {"engine": "MeitY Bhashini IndicASR (खड़ी बोली)", "languages": 6},
                "stage_4_authenticity": {"digilocker_uri": "GI-UP-KH-012 (GI Registry)", "status": "सत्यापित"},
                "stage_5_logistics": {"consignment_no": "EM829491823IN", "hub": "बुलंदशहर डाकघर पिकअप"},
                "stage_6_market": {"wage_guarantee": "८५% सीधा DBT खाता", "platform_fee": "१०% पारदर्शी"}
            }),
            "buyer_gratitude_json": json.dumps([
                {
                    "buyer_name": "Vikram Sethi",
                    "city": "New Delhi",
                    "message": "The kettle keeps chai warm for so long and the cobalt blue glaze looks stunning on our breakfast table!",
                    "time": "1 दिन पहले"
                }
            ]),
            "likes": 38,
            "created_at": "2026-09-02 11:30:00"
        },
        {
            "id": "art-103",
            "artisan_id": "art-103",
            "artisan_name": "मो. मुख्तार अंसारी (Mukhtar Ansari)",
            "artisan_experience": "38 वर्षों का पैतृक हाथकरघा अनुभव",
            "artisan_location": "नाथनगर, भागलपुर, बिहार",
            "artisan_photo": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=200&q=80",
            "hands_photo": "https://images.unsplash.com/photo-1606760227091-3dd870d97f1d?auto=format&fit=crop&w=800&q=80",
            "artisan_quote": "यह शुद्ध कोसा रेशम की बुनाई है। हर धागा हाथ से ताना-बाना बुनकर जीवन भर चलने वाला लचीलापन देता है।",
            "title": "Pure Handwoven Bhagalpuri Tussar Silk Stole",
            "title_hi": "भागलपुरी शुद्ध हाथकरघा तुषार सिल्क दुपट्टा",
            "category": "Textiles & Handloom",
            "materials_json": json.dumps(["Wild Kosa Tussar Silk", "Madder Root Natural Dye", "Pitloom Handweave"]),
            "suggested_price": 2890,
            "price_range": "₹2,600 - ₹3,200",
            "story_en": "Woven on pit looms using authentic non-violent wild Kosa silk, dyed naturally with madder root and indigo. Features a luxurious, breathable texture that softens with every wash.",
            "story_hi": "यह भागलपुर के प्रसिद्ध हथकरघे पर बुना हुआ शुद्ध तुषार (कोसा) रेशमी दुपट्टा है। मंजीठा की जड़ और प्राकृतिक नील से रंगे इस दुपट्टे में अद्भुत प्राकृतिक आभा और रेशमी कोमलता है।",
            "raw_voice_transcript": "Bhagalpuri kosa silk ko ped ke patton se natural rangkar hathkargha par buna hai. Manjitha aur neem ki chhal se rang pakka rehta hai.",
            "audio_url": "/static/audio/sample_art103.mp3",
            "studio_image_url": "https://images.unsplash.com/photo-1606760227091-3dd870d97f1d?auto=format&fit=crop&w=800&q=80",
            "raw_image_url": "https://images.unsplash.com/photo-1606760227091-3dd870d97f1d?auto=format&fit=crop&w=800&q=80",
            "qr_code_id": "QR-BHAGALPUR-103",
            "trust_score": 99,
            "gi_tag_no": "GI-BH-TS-044",
            "thumbprint_id": "MUKHTAR-THUMB-2026",
            "natural_swatches_json": json.dumps([
                {"hex": "#d4a373", "name": "Golden Raw Tussar", "regional_name": "स्वर्ण तुषार"},
                {"hex": "#9d0208", "name": "Madder Root Crimson", "regional_name": "मंजीठा लाल"},
                {"hex": "#1a365d", "name": "Natural Indigo", "regional_name": "प्राकृतिक नील"},
                {"hex": "#f4a261", "name": "Marigold Gold", "regional_name": "गेंदा पीला"}
            ]),
            "family_impact_json": json.dumps({
                "beneficiary": "ज़ोया (पोती, उम्र 6 वर्ष)",
                "impact_story": "इस महीने के बुनकर लाभ से पोती ज़ोया के लिए चश्मा व प्राथमिक विद्यालय की ट्यूशन फीस दी गई।",
                "progress_pct": 88,
                "goal_label": "नया जैकार्ड हाथकरघा (Jacquard Loom Upgrade)",
                "goal_stat": "₹22,000 / ₹25,000 सुरक्षित"
            }),
            "craft_lifecycle_json": json.dumps([
                {"step": "1. कोकून रीलिंग", "desc": "जंगली कोसा को हाथ से कातकर बारीक धागा तैयार करना", "days": "दिन 1"},
                {"step": "2. वानस्पतिक रंगाई", "desc": "मंजीठा व अनार के छिलके से रेशम के लच्छों की रंगाई", "days": "दिन 2"},
                {"step": "3. ताना-बाना बिछाना", "desc": "खड्डे वाले हथकरघे पर ३००० रेशमी धागों का विन्यास", "days": "दिन 3"},
                {"step": "4. हाथ की बुनाई", "desc": "पैरों के पेडल व हाथ की शटल से महीन ज़री बुनाई", "days": "दिन 4"}
            ]),
            "institutional_json": json.dumps({
                "stage_1_identity": {"vishwakarma_id": "PMV-BH-66104", "gp_seal": "नाथनगर बुनकर समिति मुहर"},
                "stage_2_raw_material": {"cfc_hub": "भागलपुर SFURTI सिल्क पार्क", "discount_pct": "38% बचत"},
                "stage_3_catalog": {"engine": "MeitY Bhashini IndicASR (अंगिका)", "languages": 6},
                "stage_4_authenticity": {"digilocker_uri": "GI-BH-TS-044 (Silk Mark Certified)", "status": "सत्यापित"},
                "stage_5_logistics": {"consignment_no": "EM829871109IN", "hub": "भागलपुर हेड पोस्ट ऑफिस पिकअप"},
                "stage_6_market": {"wage_guarantee": "८५% सीधा DBT खाता", "platform_fee": "१०% पारदर्शी"}
            }),
            "buyer_gratitude_json": json.dumps([
                {
                    "buyer_name": "Shreya Mukherjee",
                    "city": "Kolkata",
                    "message": "The natural lustre of this Tussar stole is unmatched by any branded retail showroom. Heartfelt thanks Mukhtar ji!",
                    "time": "3 दिन पहले"
                }
            ]),
            "likes": 56,
            "created_at": "2026-09-03 14:15:00"
        },
        {
            "id": "art-104",
            "artisan_id": "art-104",
            "artisan_name": "उस्ताद इलियास अहमद (Ustad Iliyas Ahmed)",
            "artisan_experience": "41 वर्षों का जालीदार नक्काशी तजुर्बा",
            "artisan_location": "सहारनपुर, उत्तर प्रदेश",
            "artisan_photo": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=200&q=80",
            "hands_photo": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?auto=format&fit=crop&w=800&q=80",
            "artisan_quote": "शीशम की लकड़ी में रूह होती है। हमारी छेनी और हथौड़ी उस रूह को तराशकर पीढ़ियों तक जीवित रखती है।",
            "title": "Intricately Carved Sheesham Wood Keepsake Chest",
            "title_hi": "सहारनपुर जालीदार शीशम काष्ठ नक्काशी संदूक",
            "category": "Woodcraft & Carving",
            "materials_json": json.dumps(["Aged Sheesham Rosewood", "Natural Beeswax Finish", "Brass Fittings"]),
            "suggested_price": 1850,
            "price_range": "₹1,650 - ₹2,100",
            "story_en": "Carved from legally sourced aged seasoned Sheesham rosewood, featuring Mughal fretwork lattices and finished with pure beeswax. Perfect for jewelry, watches, or precious heirlooms.",
            "story_hi": "यह सहारनपुर की प्रसिद्ध हस्त-नक्काशीदार शीशम की संदूकची है। पीतल के कब्जों और बारीक मुग़ल जालीदार नक्काशी से सजी इस संदूकची को प्राकृतिक मधुमक्खी मोम (Beeswax) से पॉलिश किया गया है।",
            "raw_voice_transcript": "Saharanpur ki pakki Sheesham lakdi par traditional jali cutting ki hai. Isme natural beeswax polish hai, koi chemical paint nahi.",
            "audio_url": "/static/audio/sample_art104.mp3",
            "studio_image_url": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?auto=format&fit=crop&w=800&q=80",
            "raw_image_url": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?auto=format&fit=crop&w=800&q=80",
            "qr_code_id": "QR-WOOD-104",
            "trust_score": 98,
            "gi_tag_no": "GI-UP-SW-031",
            "thumbprint_id": "ILIYAS-THUMB-2026",
            "natural_swatches_json": json.dumps([
                {"hex": "#582f0e", "name": "Rich Sheesham Brown", "regional_name": "शीशम काष्ठ"},
                {"hex": "#7f4f24", "name": "Teak Amber", "regional_name": "सागवान अंबर"},
                {"hex": "#ddb892", "name": "Raw Beeswax Finish", "regional_name": "मधुमक्खी मोम"},
                {"hex": "#331800", "name": "Deep Ebony Accent", "regional_name": "आबनूस"}
            ]),
            "family_impact_json": json.dumps({
                "beneficiary": "आरिफ़ (शागिर्द व युवा कारीगर)",
                "impact_story": "इस महीने के काम से कार्यशाला के 3 युवा प्रशिक्षुओं को पूरे महीने का उचित मानदेय दिया जा सका।",
                "progress_pct": 91,
                "goal_label": "धूल-मुक्त पर्यावरण अनुकूल काष्ठ कार्यशाला",
                "goal_stat": "₹27,500 / ₹30,000 सुरक्षित"
            }),
            "craft_lifecycle_json": json.dumps([
                {"step": "1. काष्ठ सीजनिंग", "desc": "प्राकृतिक धूप में २ वर्ष सुखाई गई परिपक्व शीशम की छंटाई", "days": "दिन 1"},
                {"step": "2. जाली रेखांकन", "desc": "पारंपरिक मुग़ल ज्यामितीय रूपांकनों का हाथ से अंकन", "days": "दिन 2"},
                {"step": "3. छेनी से नक्काशी", "desc": "बारीक छेनी से एक-एक छेद हाथ से आर-पार काटना", "days": "दिन 3"},
                {"step": "4. मोम पॉलिश", "desc": "शुद्ध मधुमक्खी मोम व अखरोट तेल से अंतिम चमक", "days": "दिन 4"}
            ]),
            "institutional_json": json.dumps({
                "stage_1_identity": {"vishwakarma_id": "PMV-UP-89012", "gp_seal": "सहारनपुर काष्ठ दस्तकार परिषद"},
                "stage_2_raw_material": {"cfc_hub": "SFURTI सहारनपुर काष्ठ क्लस्टर", "discount_pct": "35% बचत"},
                "stage_3_catalog": {"engine": "MeitY Bhashini IndicASR (उर्दू-हिन्दी)", "languages": 6},
                "stage_4_authenticity": {"digilocker_uri": "GI-UP-SW-031 (GI Verified)", "status": "सत्यापित"},
                "stage_5_logistics": {"consignment_no": "EM829188402IN", "hub": "सहारनपुर मुख्य डाकघर पिकअप"},
                "stage_6_market": {"wage_guarantee": "८५% सीधा DBT खाता", "platform_fee": "१०% पारदर्शी"}
            }),
            "buyer_gratitude_json": json.dumps([
                {
                    "buyer_name": "Lt. Col. Arvind Sharma",
                    "city": "Chandigarh",
                    "message": "Exemplary craftsmanship. The wood aroma and precise hinge fitting shows masterclass dedication.",
                    "time": "4 दिन पहले"
                }
            ]),
            "likes": 47,
            "created_at": "2026-09-04 16:20:00"
        },
        {
            "id": "art-105",
            "artisan_id": "art-105",
            "artisan_name": "मंगतू राम कश्यप (Mangtu Ram Kashyap)",
            "artisan_experience": "29 वर्षों की बस्तरिया ढोकरा धातु साधना",
            "artisan_location": "कोंडागांव, बस्तर, छत्तीसगढ़",
            "artisan_photo": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=200&q=80",
            "hands_photo": "https://images.unsplash.com/photo-1544816155-12df9643f363?auto=format&fit=crop&w=800&q=80",
            "artisan_quote": "ढोकरा मोम-ढलाई ४००० साल पुरानी हड़प्पा काल की विधि है। हर पीस दुनिया में एकमात्र और अनोखा होता है।",
            "title": "Bastariya Traditional Dhokra Bell Metal Bull (Nandi)",
            "title_hi": "बस्तर ढोकरा पारम्परिक घंटी धातु नंदी शिल्प",
            "category": "Handicrafts & Painting",
            "materials_json": json.dumps(["Lost Wax Molten Brass", "Riverbed Clay Mold", "Natural Beeswax"]),
            "suggested_price": 3200,
            "price_range": "₹2,900 - ₹3,600",
            "story_en": "Crafted via the ancient 4,000-year-old lost-wax casting technique using brass and natural beeswax. Each piece is completely unique as the clay mold is broken to retrieve the sculpture.",
            "story_hi": "यह छत्तीसगढ़ के बस्तर अंचल का ४००० वर्ष प्राचीन ढोकरा शिल्प है। प्राकृतिक मधुमक्खी मोम और घंटी धातु (कांसा-पीतल) से ढली यह नंदी प्रतिमा अद्वितीय है क्योंकि हर मूर्ति के बाद मिट्टी का सांचा तोड़ दिया जाता है।",
            "raw_voice_transcript": "Bastar ke jungle ke madhumakkhi mom aur mitti se dhalai ki hai. Har ek Dhokra pratima anokhi hoti hai, sancha todna padta hai.",
            "audio_url": "/static/audio/sample_art105.mp3",
            "studio_image_url": "https://images.unsplash.com/photo-1544816155-12df9643f363?auto=format&fit=crop&w=800&q=80",
            "raw_image_url": "https://images.unsplash.com/photo-1544816155-12df9643f363?auto=format&fit=crop&w=800&q=80",
            "qr_code_id": "QR-DHOKRA-105",
            "trust_score": 99,
            "gi_tag_no": "GI-CG-DH-029",
            "thumbprint_id": "MANGTU-THUMB-2026",
            "natural_swatches_json": json.dumps([
                {"hex": "#c59b27", "name": "Molten Brass Gold", "regional_name": "कांसा पीतल"},
                {"hex": "#3a3a3a", "name": "Burnt Charcoal Patina", "regional_name": "कोयला पातिना"},
                {"hex": "#8d5b4c", "name": "River Clay Core", "regional_name": "नदी कछार मिट्टी"},
                {"hex": "#d4a373", "name": "Beeswax Amber", "regional_name": "मोम अंबर"}
            ]),
            "family_impact_json": json.dumps({
                "beneficiary": "सुमित्रा (पत्नी व मोम-तार शिल्पी)",
                "impact_story": "इस महीने के ढोकरा ऑर्डर्स से कार्यशाला के लिए नया धातु-पिघलाने वाला फर्नेस खरीदा जा सका।",
                "progress_pct": 85,
                "goal_label": "बस्तर जनजातीय कारीगर शेड निर्माण",
                "goal_stat": "₹25,500 / ₹30,000 सुरक्षित"
            }),
            "craft_lifecycle_json": json.dumps([
                {"step": "1. मिट्टी का कोर", "desc": "नदी की मिट्टी और भूसी मिलाकर मूल आकृति बनाना", "days": "दिन 1"},
                {"step": "2. मोम के महीन तार", "desc": "मधुमक्खी मोम को गर्म पानी में खींचकर धागे बनाना", "days": "दिन 2"},
                {"step": "3. भट्ठी में पकाना", "desc": "मोम पिघलकर बाहर निकलती है और खाली जगह में कांसा भरता है", "days": "दिन 3"},
                {"step": "4. सांचा तोड़ना", "desc": "मिट्टी तोड़कर धातु की मूल मूर्ति निकालना व घिसाई", "days": "दिन 4"}
            ]),
            "institutional_json": json.dumps({
                "stage_1_identity": {"vishwakarma_id": "PMV-CG-55219", "gp_seal": "कोंडागांव ग्राम सभा मुहर"},
                "stage_2_raw_material": {"cfc_hub": "TRIFED बस्तर ढोकरा विकास केंद्र", "discount_pct": "39% बचत"},
                "stage_3_catalog": {"engine": "MeitY Bhashini IndicASR (हल्बी व छत्तीसगढ़ी)", "languages": 6},
                "stage_4_authenticity": {"digilocker_uri": "GI-CG-DH-029 (Tribal Craft Certified)", "status": "सत्यापित"},
                "stage_5_logistics": {"consignment_no": "EM829447192IN", "hub": "कोंडागांव स्पीड पोस्ट पिकअप"},
                "stage_6_market": {"wage_guarantee": "८५% सीधा DBT खाता", "platform_fee": "१०% पारदर्शी"}
            }),
            "buyer_gratitude_json": json.dumps([
                {
                    "buyer_name": "Devika Narayanan",
                    "city": "Chennai",
                    "message": "The rustic, tribal elegance of this Dhokra piece is magical. True museum-grade heritage art!",
                    "time": "3 दिन पहले"
                }
            ]),
            "likes": 64,
            "created_at": "2026-09-05 09:30:00"
        },
        {
            "id": "art-106",
            "artisan_id": "art-106",
            "artisan_name": "के. वी. वेंकटेश (K. V. Venkatesh)",
            "artisan_experience": "27 वर्षों की पारंपरिक चन्नापट्टना काष्ठकला",
            "artisan_location": "चन्नापट्टना, रामनगर, कर्नाटक",
            "artisan_photo": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=200&q=80",
            "hands_photo": "https://images.unsplash.com/photo-1513542789411-b6a5d4f31634?auto=format&fit=crop&w=800&q=80",
            "artisan_quote": "हमारे खिलौने बच्चों के लिए 100% सुरक्षित हैं क्योंकि इनमें सिर्फ हल्दी, कुमकुम और पेड़ों की प्राकृतिक लाख का रंग है।",
            "title": "Channapatna Natural Lacquer-Turned Stacking Tower",
            "title_hi": "चन्नापट्टना प्राकृतिक लाख-रंजित काष्ठ खिलौना",
            "category": "Woodcraft & Carving",
            "materials_json": json.dumps(["Wrightia Tinctoria Ivory Wood", "Natural Tree Lacquer", "Organic Vegetable Dyes"]),
            "suggested_price": 750,
            "price_range": "₹650 - ₹900",
            "story_en": "Turned on a traditional lathe from soft ivory wood (Wrightia Tinctoria) and finished with non-toxic natural lac colored with turmeric, indigo, and kumkum. Completely child-safe and eco-friendly.",
            "story_hi": "यह कर्नाटक के विश्वप्रसिद्ध चन्नापट्टना की पारंपरिक खिलौना कला है। नरम 'आइवरी काष्ठ' पर खराद चलाकर हल्दी, कुमकुम और प्राकृतिक लाख से रंगा गया यह खिलौना बच्चों के लिए १००% सुरक्षित व विष-मुक्त (Non-Toxic) है।",
            "raw_voice_transcript": "Channapatna aalele Wrightia wood lakkhi natural haldi kumkum banna kotti makkalige 100% safe madidivi.",
            "audio_url": "/static/audio/sample_art106.mp3",
            "studio_image_url": "https://images.unsplash.com/photo-1513542789411-b6a5d4f31634?auto=format&fit=crop&w=800&q=80",
            "raw_image_url": "https://images.unsplash.com/photo-1513542789411-b6a5d4f31634?auto=format&fit=crop&w=800&q=80",
            "qr_code_id": "QR-CHANNAPATNA-106",
            "trust_score": 98,
            "gi_tag_no": "GI-KT-CP-009",
            "thumbprint_id": "VENKATESH-THUMB-2026",
            "natural_swatches_json": json.dumps([
                {"hex": "#d62828", "name": "Kumkum Scarlet", "regional_name": "रोली कुमकुम"},
                {"hex": "#003049", "name": "Indigo Night", "regional_name": "गहरा नील"},
                {"hex": "#fcbf49", "name": "Pure Turmeric", "regional_name": "शुद्ध हल्दी"},
                {"hex": "#eae2b7", "name": "Wrightia Ivory Wood", "regional_name": "आइवरी काष्ठ"}
            ]),
            "family_impact_json": json.dumps({
                "beneficiary": "मान्या (बेटी, उम्र 10 वर्ष)",
                "impact_story": "खिलौनों के सतत विक्रय से बेटी मान्या को संगीत विद्यालय में दाखिला दिलाया गया।",
                "progress_pct": 89,
                "goal_label": "बाल-सुरक्षित प्राकृतिक रंग अनुसंधान किट",
                "goal_stat": "₹12,000 / ₹15,000 सुरक्षित"
            }),
            "craft_lifecycle_json": json.dumps([
                {"step": "1. आइवरी काष्ठ छिलाई", "desc": "हल्की सफेद लकड़ी को खराद मशीन पर गोलाई देना", "days": "दिन 1"},
                {"step": "2. प्राकृतिक लाख शोधन", "desc": "हल्दी व कुमकुम को गर्म लाख में मिलाकर रंगीन छड़ियां बनाना", "days": "दिन 2"},
                {"step": "3. घूर्णन रंगाई", "desc": "घूमते हुए खिलौने पर लाख की छड़ी दबाकर घर्षण से रंग चढ़ाना", "days": "दिन 3"},
                {"step": "4. ताड़-पत्र पॉलिश", "desc": "ताड़ के सूखे पत्ते से रगड़कर शीशे जैसी प्राकृतिक चमक देना", "days": "दिन 4"}
            ]),
            "institutional_json": json.dumps({
                "stage_1_identity": {"vishwakarma_id": "PMV-KT-33418", "gp_seal": "चन्नापट्टना नगर पालिका मुहर"},
                "stage_2_raw_material": {"cfc_hub": "कर्नाटक हस्तशिल्प विकास निगम क्लस्टर", "discount_pct": "33% बचत"},
                "stage_3_catalog": {"engine": "MeitY Bhashini IndicASR (कन्नड़)", "languages": 6},
                "stage_4_authenticity": {"digilocker_uri": "GI-KT-CP-009 (Toy Safety Standard ISO/IS 9873)", "status": "सत्यापित"},
                "stage_5_logistics": {"consignment_no": "EM829331908IN", "hub": "रामनगर डाकघर पिकअप"},
                "stage_6_market": {"wage_guarantee": "८५% सीधा DBT खाता", "platform_fee": "१०% पारदर्शी"}
            }),
            "buyer_gratitude_json": json.dumps([
                {
                    "buyer_name": "Aparna Iyer",
                    "city": "Bengaluru",
                    "message": "My toddler loves playing with this! So comforting to know there are zero harmful chemicals or plastics.",
                    "time": "2 दिन पहले"
                }
            ]),
            "likes": 51,
            "created_at": "2026-09-06 17:00:00"
        }
    ]

    for p in seed_products:
        cursor.execute("""
        INSERT INTO products (
            id, title, title_hi, category, materials_json, suggested_price,
            price_range, story_en, story_hi, raw_voice_transcript, audio_url,
            studio_image_url, raw_image_url, qr_code_id, trust_score, gi_tag_no,
            thumbprint_id, artisan_id, artisan_name, artisan_location, artisan_photo,
            hands_photo, artisan_quote, natural_swatches_json, family_impact_json,
            craft_lifecycle_json, institutional_json, buyer_gratitude_json, likes, created_at
        ) VALUES (
            :id, :title, :title_hi, :category, :materials_json, :suggested_price,
            :price_range, :story_en, :story_hi, :raw_voice_transcript, :audio_url,
            :studio_image_url, :raw_image_url, :qr_code_id, :trust_score, :gi_tag_no,
            :thumbprint_id, :artisan_id, :artisan_name, :artisan_location, :artisan_photo,
            :hands_photo, :artisan_quote, :natural_swatches_json, :family_impact_json,
            :craft_lifecycle_json, :institutional_json, :buyer_gratitude_json, :likes, :created_at
        )
        """, p)

    conn.commit()

# =============================================================================
# PRODUCTS REPOSITORY
# =============================================================================

def format_product_row(row):
    """Converts a SQLite row into a clean dictionary with parsed JSON fields."""
    if not row:
        return None
    d = dict(row)
    for json_field, key in [
        ("materials_json", "materials"),
        ("natural_swatches_json", "natural_pigment_swatches"),
        ("family_impact_json", "family_impact"),
        ("craft_lifecycle_json", "craft_lifecycle"),
        ("institutional_json", "institutional_framework"),
        ("buyer_gratitude_json", "buyer_gratitude"),
        ("studio_rules_json", "studio_rules_report")
    ]:
        val = d.pop(json_field, None)
        try:
            d[key] = json.loads(val) if val else ([] if "json" in json_field and json_field != "studio_rules_json" else None)
        except Exception:
            d[key] = [] if json_field != "studio_rules_json" else None
            
    d["price"] = d.get("suggested_price")
    d["natural_swatches"] = d.get("natural_pigment_swatches", [])
    if not d.get("studio_rules_report"):
        d["studio_rules_report"] = {
            "lighting": "5500K Daylight Studio Standard (Auto-Exposure Balanced)",
            "contrast": "Micro-contrast Enhanced for Handcrafted Texture",
            "shadows": "Ambient Shadow Noise Neutralized",
            "aspect_ratio": "4:3 E-Commerce Gallery Standard (800x600)",
            "watermark_seal": "Cryptographic GI & Studio Seal Imprinted",
            "status": "Grade A+ Studio Certified"
        }
    return d

def get_all_products(category=None, search=None, gi_only=False, sort_by=None):
    """Retrieves products from SQLite with optional filtering and sorting."""
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM products WHERE 1=1"
    params = {}

    if category and category != 'all':
        query += " AND category = :category"
        params["category"] = category

    if gi_only:
        query += " AND gi_tag_no IS NOT NULL AND gi_tag_no != ''"

    if search:
        query += " AND (title LIKE :s OR title_hi LIKE :s OR artisan_name LIKE :s OR artisan_location LIKE :s OR category LIKE :s)"
        params["s"] = f"%{search}%"

    if sort_by == 'price_asc':
        query += " ORDER BY suggested_price ASC"
    elif sort_by == 'price_desc':
        query += " ORDER BY suggested_price DESC"
    else:
        query += " ORDER BY created_at DESC"

    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return [format_product_row(r) for r in rows]

def get_product_by_id(product_id):
    """Retrieves a single product by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = :id", {"id": product_id})
    row = cursor.fetchone()
    conn.close()
    return format_product_row(row)

def insert_product(prod_data):
    """Inserts or replaces a product in SQLite."""
    conn = get_connection()
    cursor = conn.cursor()

    params = {
        "id": prod_data["id"],
        "title": prod_data.get("title", ""),
        "title_hi": prod_data.get("title_hi", prod_data.get("title", "")),
        "category": prod_data.get("category", "Handicrafts & Painting"),
        "materials_json": json.dumps(prod_data.get("materials", [])),
        "suggested_price": int(prod_data.get("suggested_price", 1500)),
        "price_range": prod_data.get("price_range", f"₹{int(prod_data.get('suggested_price', 1500)*0.9):,} - ₹{int(prod_data.get('suggested_price', 1500)*1.15):,}"),
        "story_en": prod_data.get("story_en", ""),
        "story_hi": prod_data.get("story_hi", ""),
        "raw_voice_transcript": prod_data.get("raw_voice_transcript", ""),
        "audio_url": prod_data.get("audio_url", ""),
        "studio_image_url": prod_data.get("studio_image_url", ""),
        "raw_image_url": prod_data.get("raw_image_url", ""),
        "qr_code_id": prod_data.get("qr_code_id", f"QR-{prod_data['id']}"),
        "trust_score": int(prod_data.get("trust_score", 98)),
        "gi_tag_no": prod_data.get("gi_tag_no", "GI-CERTIFIED"),
        "thumbprint_id": prod_data.get("thumbprint_id", f"THUMB-{prod_data['id']}"),
        "artisan_id": prod_data.get("artisan_id", "art-101"),
        "artisan_name": prod_data.get("artisan_name", "Rural Artisan"),
        "artisan_location": prod_data.get("artisan_location", "India"),
        "artisan_experience": prod_data.get("artisan_experience", "20+ Years"),
        "artisan_photo": prod_data.get("artisan_photo", ""),
        "hands_photo": prod_data.get("hands_photo", ""),
        "artisan_quote": prod_data.get("artisan_quote", ""),
        "natural_swatches_json": json.dumps(prod_data.get("natural_pigment_swatches", prod_data.get("natural_swatches", []))),
        "family_impact_json": json.dumps(prod_data.get("family_impact", {})),
        "craft_lifecycle_json": json.dumps(prod_data.get("craft_lifecycle", [])),
        "institutional_json": json.dumps(prod_data.get("institutional_framework", {})),
        "buyer_gratitude_json": json.dumps(prod_data.get("buyer_gratitude", [])),
        "studio_rules_json": json.dumps(prod_data.get("studio_rules_report", {
            "lighting": "5500K Daylight Studio Standard (Auto-Exposure Balanced)",
            "contrast": "Micro-contrast Enhanced for Handcrafted Texture",
            "shadows": "Ambient Shadow Noise Neutralized",
            "aspect_ratio": "4:3 E-Commerce Gallery Standard (800x600)",
            "watermark_seal": "Cryptographic GI & Studio Seal Imprinted",
            "status": "Grade A+ Studio Certified"
        })),
        "likes": int(prod_data.get("likes", 0)),
        "created_at": prod_data.get("created_at", time.strftime("%Y-%m-%d %H:%M:%S"))
    }

    cursor.execute("""
    INSERT OR REPLACE INTO products (
        id, title, title_hi, category, materials_json, suggested_price,
        price_range, story_en, story_hi, raw_voice_transcript, audio_url,
        studio_image_url, raw_image_url, qr_code_id, trust_score, gi_tag_no,
        thumbprint_id, artisan_id, artisan_name, artisan_location, artisan_experience,
        artisan_photo, hands_photo, artisan_quote, natural_swatches_json,
        family_impact_json, craft_lifecycle_json, institutional_json,
        buyer_gratitude_json, studio_rules_json, likes, created_at
    ) VALUES (
        :id, :title, :title_hi, :category, :materials_json, :suggested_price,
        :price_range, :story_en, :story_hi, :raw_voice_transcript, :audio_url,
        :studio_image_url, :raw_image_url, :qr_code_id, :trust_score, :gi_tag_no,
        :thumbprint_id, :artisan_id, :artisan_name, :artisan_location, :artisan_experience,
        :artisan_photo, :hands_photo, :artisan_quote, :natural_swatches_json,
        :family_impact_json, :craft_lifecycle_json, :institutional_json,
        :buyer_gratitude_json, :studio_rules_json, :likes, :created_at
    )
    """, params)

    conn.commit()
    conn.close()
    return get_product_by_id(prod_data["id"])

def delete_product(product_id):
    """Deletes a product by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = :id", {"id": product_id})
    affected = cursor.rowcount
    conn.commit()
    conn.close()
    return affected > 0

# =============================================================================
# ORDERS & FINANCIAL LEDGER REPOSITORY
# =============================================================================

def format_order_row(row):
    """Formats an order row into a clean dictionary."""
    if not row:
        return None
    d = dict(row)
    cart_raw = d.pop("cart_items_json", "[]")
    try:
        d["cart_items"] = json.loads(cart_raw)
    except Exception:
        d["cart_items"] = []
    d["receipt_url"] = f"/api/orders/{d['order_id']}/receipt"
    return d

def insert_order(order_data):
    """Inserts a new order into SQLite and updates the corresponding artisan's earnings."""
    conn = get_connection()
    cursor = conn.cursor()

    params = {
        "order_id": order_data["order_id"],
        "tracking_num": order_data["tracking_num"],
        "dbt_ref": order_data["dbt_ref"],
        "order_date": order_data.get("order_date", time.strftime("%d %b %Y, %I:%M %p")),
        "est_delivery": order_data.get("est_delivery", time.strftime("%d %b %Y", time.localtime(time.time() + 4 * 86400))),
        "buyer_name": order_data["buyer_name"],
        "buyer_phone": order_data.get("buyer_phone", ""),
        "shipping_address": order_data.get("shipping_address", ""),
        "city": order_data.get("city", ""),
        "state": order_data.get("state", ""),
        "pincode": order_data.get("pincode", ""),
        "full_address": order_data.get("full_address", ""),
        "cart_items_json": json.dumps(order_data.get("cart_items", [])),
        "subtotal": int(order_data["subtotal"]),
        "shipping_fee": int(order_data.get("shipping_fee", 0)),
        "total_amount": int(order_data["total_amount"]),
        "artisan_remittance": int(order_data["artisan_remittance"]),
        "platform_fee": int(order_data.get("platform_fee", int(order_data["subtotal"] * 0.10))),
        "sfurti_reserve": int(order_data.get("sfurti_reserve", int(order_data["subtotal"] * 0.05))),
        "payment_method": order_data.get("payment_method", "UPI"),
        "status": order_data.get("status", "CONFIRMED_DISPATCH_SCHEDULED"),
        "speed_post_hub": order_data.get("speed_post_hub", "Delhi NSH (National Sorting Hub)"),
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    cursor.execute("""
    INSERT INTO orders (
        order_id, tracking_num, dbt_ref, order_date, est_delivery, buyer_name,
        buyer_phone, shipping_address, city, state, pincode, full_address,
        cart_items_json, subtotal, shipping_fee, total_amount, artisan_remittance,
        platform_fee, sfurti_reserve, payment_method, status, speed_post_hub, created_at
    ) VALUES (
        :order_id, :tracking_num, :dbt_ref, :order_date, :est_delivery, :buyer_name,
        :buyer_phone, :shipping_address, :city, :state, :pincode, :full_address,
        :cart_items_json, :subtotal, :shipping_fee, :total_amount, :artisan_remittance,
        :platform_fee, :sfurti_reserve, :payment_method, :status, :speed_post_hub, :created_at
    )
    """, params)

    # Automatically create scheduled India Post pickup
    pickup_params = {
        "pickup_id": f"PKP-{uuid.uuid4().hex[:8].upper()}",
        "consignment_no": order_data["tracking_num"],
        "artisan_id": order_data.get("cart_items", [{}])[0].get("id", "art-101"),
        "artisan_name": order_data.get("cart_items", [{}])[0].get("artisan_name", "Rural Artisan"),
        "product_title": order_data.get("cart_items", [{}])[0].get("title", "Artisanal Craft"),
        "village_pincode": "847211",
        "weight_kg": 0.85,
        "scheduled_time": "आज शाम ०४:३० बजे (Today 4:30 PM)",
        "status": "PICKUP_SCHEDULED",
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    cursor.execute("""
    INSERT OR IGNORE INTO postal_pickups (
        pickup_id, consignment_no, artisan_id, artisan_name, product_title,
        village_pincode, weight_kg, scheduled_time, status, created_at
    ) VALUES (
        :pickup_id, :consignment_no, :artisan_id, :artisan_name, :product_title,
        :village_pincode, :weight_kg, :scheduled_time, :status, :created_at
    )
    """, pickup_params)

    # Update artisan earnings
    artisan_payout = int(order_data["artisan_remittance"])
    cursor.execute("""
    UPDATE artisans
    SET total_earnings = total_earnings + :amt
    WHERE artisan_id = 'art-101' OR vishwakarma_id = 'PMV-BH-88214'
    """, {"amt": artisan_payout})

    conn.commit()
    conn.close()
    return get_order_by_id(order_data["order_id"])

def get_order_by_id(order_id):
    """Retrieves an order by order_id or tracking_num."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM orders
    WHERE order_id = :val OR tracking_num = :val
    """, {"val": order_id})
    row = cursor.fetchone()
    conn.close()
    return format_order_row(row)

def get_all_orders():
    """Returns all placed orders sorted by date."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders ORDER BY created_at DESC")
    rows = cursor.fetchall()
    conn.close()
    return [format_order_row(r) for r in rows]

# =============================================================================
# ARTISAN REPOSITORY & DBT DIGITAL PASSBOOK
# =============================================================================

def get_artisan_by_id(artisan_id):
    """Retrieves artisan profile by ID or Vishwakarma ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM artisans
    WHERE artisan_id = :id OR vishwakarma_id = :id OR phone = :id
    """, {"id": artisan_id})
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def insert_artisan(artisan_data):
    """Inserts a newly registered rural artisan."""
    conn = get_connection()
    cursor = conn.cursor()

    params = {
        "artisan_id": artisan_data["artisan_id"],
        "name": artisan_data["name"],
        "phone": artisan_data.get("phone", ""),
        "vishwakarma_id": artisan_data.get("vishwakarma_id", f"PMV-IN-{uuid.uuid4().hex[:6].upper()}"),
        "trade": artisan_data.get("trade", "हस्तशिल्प / Handicrafts"),
        "gram_panchayat": artisan_data.get("gram_panchayat", "रंती ग्राम पंचायत, बिहार"),
        "panchayat_seal": artisan_data.get("panchayat_seal", "GP-VERIFIED-2026"),
        "verification_status": artisan_data.get("verification_status", "सत्यापित लाभार्थी (PM Vishwakarma Certified)"),
        "tool_grant": artisan_data.get("tool_grant", "₹15,000 टूलकिट अनुदान स्वीकृत"),
        "total_earnings": int(artisan_data.get("total_earnings", 0)),
        "bank_status": artisan_data.get("bank_status", "Aadhaar Linked DBT Active"),
        "community": artisan_data.get("community", "महिला स्वयं सहायता समूह क्लस्टर"),
        "sfurti_cluster": artisan_data.get("sfurti_cluster", "SFURTI कॉमन फैसिलिटी सेंटर"),
        "rutag_support": artisan_data.get("rutag_support", "आईआईटी रूरल टेक्नोलॉजी एक्शन लैब"),
        "passbook_qr": artisan_data.get("passbook_qr", f"KALA-PASSBOOK-{artisan_data['artisan_id']}"),
        "registered_at": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    cursor.execute("""
    INSERT OR REPLACE INTO artisans (
        artisan_id, name, phone, vishwakarma_id, trade, gram_panchayat,
        panchayat_seal, verification_status, tool_grant, total_earnings,
        bank_status, community, sfurti_cluster, rutag_support, passbook_qr, registered_at
    ) VALUES (
        :artisan_id, :name, :phone, :vishwakarma_id, :trade, :gram_panchayat,
        :panchayat_seal, :verification_status, :tool_grant, :total_earnings,
        :bank_status, :community, :sfurti_cluster, :rutag_support, :passbook_qr, :registered_at
    )
    """, params)

    conn.commit()
    conn.close()
    return get_artisan_by_id(artisan_data["artisan_id"])

def get_artisan_dbt_passbook(artisan_id="art-101"):
    """Computes real DBT passbook transactions from orders and grants."""
    artisan = get_artisan_by_id(artisan_id) or get_artisan_by_id("art-101")
    orders = get_all_orders()

    transactions = [
        {
            "date": "2026-08-15",
            "type": "GOVT_TOOL_GRANT",
            "description": "प्रधानमंत्री विश्वकर्मा आधुनिक टूलकिट अनुदान (Ministry of MSME)",
            "utr_ref": "PFMS-TOOL-992144A",
            "amount": 15000,
            "status": "CREDITED_SUCCESS"
        }
    ]

    total_order_earnings = 0
    for o in orders:
        transactions.append({
            "date": o.get("order_date", time.strftime("%d %b %Y")),
            "type": "CRAFT_SALE_85PCT_DBT",
            "description": f"कलाकृति विक्रय प्रत्यक्ष पारिश्रमिक • ऑर्डर {o['order_id']} ({o.get('payment_method', 'UPI')})",
            "utr_ref": o.get("dbt_ref", "DBT-PMV-88192"),
            "amount": o["artisan_remittance"],
            "status": "SETTLED_TO_BANK"
        })
        total_order_earnings += o["artisan_remittance"]

    total_lifetime = (artisan.get("total_earnings", 42850) if artisan else 42850) + total_order_earnings

    art_id = artisan.get("artisan_id", "art-101") if artisan else "art-101"
    art_name = artisan.get("name", "रामवती देवी") if artisan else "रामवती देवी"
    art_vishwakarma = artisan.get("vishwakarma_id", "PMV-BH-88214") if artisan else "PMV-BH-88214"
    art_panchayat = artisan.get("gram_panchayat", "रंती ग्राम पंचायत, बिहार") if artisan else "रंती ग्राम पंचायत, बिहार"

    return {
        "artisan": {
            "id": art_id,
            "name": art_name,
            "vishwakarma_id": art_vishwakarma,
            "gram_panchayat": art_panchayat,
            "bank_account_masked": "SBI-XXXX-8492",
            "ifsc_code": "SBIN0001234",
            "dbt_seeded": True
        },
        "summary": {
            "lifetime_sales": total_lifetime,
            "order_sales_earnings": total_order_earnings,
            "settled_remittances_count": len(transactions),
            "toolkit_grant_amount": 15000
        },
        "artisan_id": art_id,
        "artisan_name": art_name,
        "vishwakarma_id": art_vishwakarma,
        "gram_panchayat": art_panchayat,
        "bank_account_masked": "SBI-XXXX-8492",
        "ifsc_code": "SBIN0001234",
        "dbt_seeded": True,
        "total_lifetime_earnings": total_lifetime,
        "order_sales_earnings": total_order_earnings,
        "transactions_count": len(transactions),
        "transactions": transactions
    }

# =============================================================================
# INDIA POST DYNAMIC TRACKING ENGINE
# =============================================================================

def get_postal_tracking_timeline(consignment_no):
    """Constructs a live tracking timeline from real orders or scheduled pickups."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM orders WHERE tracking_num = :cn OR order_id = :cn", {"cn": consignment_no})
    order_row = cursor.fetchone()

    cursor.execute("SELECT * FROM postal_pickups WHERE consignment_no = :cn", {"cn": consignment_no})
    pickup_row = cursor.fetchone()

    conn.close()

    order = format_order_row(order_row) if order_row else None
    dest_city = order.get("city", "New Delhi") if order else "New Delhi"
    dest_pin = order.get("pincode", "110001") if order else "110001"
    hub = order.get("speed_post_hub", "Delhi NSH (National Sorting Hub)") if order else "Delhi NSH Hub"

    timeline = [
        {
            "status_title": "डाकघर में बुकिंग व पार्सल पिकअप (Booked & Picked Up)",
            "location": "Ranti SO (Madhubani, Bihar - 847211)",
            "timestamp": order.get("order_date", "06 Sep 2026, 02:30 PM") if order else "06 Sep 2026, 02:30 PM",
            "completed": True,
            "remarks": "Gramin Dak Sevak (GDS #081 - मनोज सिंह) द्वारा सीधे कारीगर के घर से उठाया गया।"
        },
        {
            "status_title": "SFURTI क्लस्टर गुणवत्ता जांच व बारकोड स्कैन (CFC Quality Check)",
            "location": "SFURTI Common Facility Centre Hub, Madhubani",
            "timestamp": "06 Sep 2026, 06:45 PM",
            "completed": True,
            "remarks": "हस्तशिल्प की प्रामाणिकता व सुरक्षित पैकेजिंग सत्यापित। लेड-फ्री लैब मुहर संलग्न।"
        },
        {
            "status_title": "नेशनल सॉर्टिंग हब प्रेषण (In Transit via RMS Rail Hub)",
            "location": "Patna National Sorting Hub (NSH)",
            "timestamp": "07 Sep 2026, 06:15 AM",
            "completed": True,
            "remarks": f"रेल डाक सेवा (RMS) द्वारा गंतव्य सॉर्टिंग केंद्र {hub} को प्रेषित।"
        },
        {
            "status_title": "गंतव्य डाकघर वितरण हेतु तैयार (Out for Delivery)",
            "location": f"{dest_city} Head Post Office ({dest_pin})",
            "timestamp": order.get("est_delivery", "08 Sep 2026") if order else "08 Sep 2026",
            "completed": False,
            "remarks": "अनुमानित सुपुर्दगी: डाकिया द्वारा आपके पते पर सुरक्षित वितरण।"
        }
    ]

    return {
        "status": "success",
        "consignment_number": consignment_no,
        "carrier": "India Post (Department of Posts • Government of India)",
        "service_type": "Speed Post Guaranteed Domestic (SP-Priority)",
        "origin": "Ranti SO (Madhubani, Bihar - 847211)",
        "destination": f"{dest_city} ({dest_pin})",
        "current_status": "IN_TRANSIT_NATIONAL_HUB",
        "tracking_timeline": timeline
    }

# =============================================================================
# GRATITUDE & SHG HUB REPOSITORY
# =============================================================================

def add_gratitude_note(product_id, buyer_name, city, message):
    """Inserts a buyer gratitude note and links it to the product."""
    conn = get_connection()
    cursor = conn.cursor()

    note_id = f"NOTE-{uuid.uuid4().hex[:8].upper()}"
    now = time.strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO gratitude_notes (note_id, product_id, buyer_name, city, message, created_at)
    VALUES (:note_id, :product_id, :buyer_name, :city, :message, :created_at)
    """, {
        "note_id": note_id,
        "product_id": product_id,
        "buyer_name": buyer_name,
        "city": city,
        "message": message,
        "created_at": now
    })

    prod = get_product_by_id(product_id)
    if prod:
        existing = prod.get("buyer_gratitude", [])
        existing.insert(0, {
            "buyer_name": buyer_name,
            "city": city,
            "message": message,
            "time": "अभी-अभी (Just now)"
        })
        cursor.execute("""
        UPDATE products
        SET buyer_gratitude_json = :bg
        WHERE id = :id
        """, {"bg": json.dumps(existing), "id": product_id})

    conn.commit()
    conn.close()
    return {"note_id": note_id, "status": "success"}

def create_shg_bulk_order(artisan_name, material_name, quantity_kg, discounted_price, retail_price):
    """Creates a group raw material purchase order with 36% discount."""
    conn = get_connection()
    cursor = conn.cursor()

    order_id = f"SHG-BULK-{uuid.uuid4().hex[:6].upper()}"
    savings = retail_price - discounted_price

    cursor.execute("""
    INSERT INTO shg_orders (
        order_id, artisan_id, artisan_name, material_name, quantity_kg,
        discounted_price, retail_price, savings, status, created_at
    ) VALUES (
        :order_id, 'art-101', :artisan_name, :material_name, :quantity_kg,
        :discounted_price, :retail_price, :savings, 'DISPATCH_SCHEDULED_CFC', :created_at
    )
    """, {
        "order_id": order_id,
        "artisan_name": artisan_name,
        "material_name": material_name,
        "quantity_kg": quantity_kg,
        "discounted_price": discounted_price,
        "retail_price": retail_price,
        "savings": savings,
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S")
    })

    conn.commit()
    conn.close()
    return {
        "status": "success",
        "order_id": order_id,
        "bulk_order_id": order_id,
        "material_name": material_name,
        "quantity_kg": quantity_kg,
        "discounted_price": discounted_price,
        "savings": savings,
        "savings_amount": savings,
        "message": f"सामूहिक खरीद सफलतापूर्वक दर्ज! SFURTI सीएफसी से ३६% बचत के साथ माल रवाना।"
    }

def request_kala_sakhi_visit(artisan_name, village_pincode, assistance_type="डिजिटल ऑनबोर्डिंग व वॉइस कैटलॉग सहायता"):
    """Schedules a Kala Sakhi / CSC VLE field helper visit."""
    conn = get_connection()
    cursor = conn.cursor()

    req_id = f"SAKHI-REQ-{uuid.uuid4().hex[:6].upper()}"
    visit_time = "आज शाम ०५:०० बजे (Today 5:00 PM)"

    cursor.execute("""
    INSERT INTO sakhi_requests (
        request_id, artisan_id, artisan_name, village_pincode, assistance_type,
        scheduled_visit, status, created_at
    ) VALUES (
        :request_id, 'art-101', :artisan_name, :village_pincode, :assistance_type,
        :scheduled_visit, 'SAKHI_ASSIGNED', :created_at
    )
    """, {
        "request_id": req_id,
        "artisan_name": artisan_name,
        "village_pincode": village_pincode,
        "assistance_type": assistance_type,
        "scheduled_visit": visit_time,
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S")
    })

    conn.commit()
    conn.close()
    sakhi_name = "सुनीता कुमारी (प्रमाणित कला सखी - VLE #941)"
    return {
        "status": "success",
        "request_id": req_id,
        "sakhi_name": sakhi_name,
        "assigned_sakhi": sakhi_name,
        "scheduled_time": visit_time,
        "scheduled_visit": visit_time,
        "message": f"कला सखी सहायता अनुरोध स्वीकृत! {sakhi_name} आज शाम ५ बजे आपके घर पहुंचेंगी।"
    }

# Initialize database on module load
init_db()
