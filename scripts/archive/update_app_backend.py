def main():
    path = "app.py"
    with open(path, "r", encoding="utf-8") as f:
        code = f.read()

    # 1. Add art-103 and art-104 to PRODUCTS_DB
    old_prod_end = """        "created_at": "2026-09-04 11:15:00"
    }
]"""

    new_products = """        "created_at": "2026-09-04 11:15:00"
    },
    {
        "id": "art-103",
        "artisan_name": "Sitara Begum (सितारा बेगम)",
        "artisan_experience": "22 वर्षों से भागलपुरी कोसा सिल्क बुनाई",
        "artisan_location": "Champanagar, Bhagalpur, Bihar",
        "artisan_community": "Bunkar Mahila Self-Help Group / PM-AJAY",
        "artisan_photo": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=200&q=80",
        "hands_photo": "https://images.unsplash.com/photo-1606760227091-3dd870d97f1d?auto=format&fit=crop&w=800&q=80",
        "artisan_quote": "ताना-बाना जब खद्दर पर बैठता है, तो रेशम की चमक में हमारी मेहनत मुस्कुराती है।",
        "title": "Pure Handwoven Bhagalpuri Tussar Silk Stole",
        "category": "Textiles & Weaving",
        "raw_voice_transcript": "Desi Tussar Kosa silk stole hai. Natural tree bark colors se hand-dyed hai. Traditional pit loom par 3 din me buni hai.",
        "story_en": "Handwoven on traditional pit looms in Bhagalpur, this pure organic Tussar silk stole is dyed using natural pomegranate and tree bark extracts, offering an ethereal golden sheen.",
        "story_hi": "भागलपुर के पारंपरिक गड्ढा करघे (Pit Loom) पर बुना गया यह शुद्ध तुषार कोसा सिल्क स्टोल अनार के छिलकों और प्राकृतिक छाल से रंगा गया है।",
        "materials": ["Pure Tussar Silk", "Pomegranate Peel Dye", "Pit Loom Woven"],
        "suggested_price": 2890,
        "price_range": "₹2,600 - ₹3,200",
        "fair_wage_share": "87% directly to Sitara Begum",
        "studio_image_url": "https://images.unsplash.com/photo-1606760227091-3dd870d97f1d?auto=format&fit=crop&w=800&q=80",
        "raw_image_url": "https://images.unsplash.com/photo-1606760227091-3dd870d97f1d?auto=format&fit=crop&w=800&q=80",
        "qr_code_id": "QR-SILK-103",
        "trust_score": 99,
        "gi_tag_no": "GI-BH-SILK-029",
        "thumbprint_id": "SITARA-THUMB-2026",
        "family_impact": {
            "beneficiary": "ज़ोया (बेटी, नर्सिंग छात्रा)",
            "impact_story": "इस बुनकरी से बिटिया ज़ोया के नर्सिंग कॉलेज की प्रयोगशाला फीस सुरक्षित हुई।",
            "progress_pct": 82,
            "goal_label": "नया सौर ऊर्जा चालित हैंडलूम चरखा",
            "goal_stat": "₹16,400 / ₹20,000 सुरक्षित"
        },
        "craft_lifecycle": [
            {"step": "1. कोकून कताई", "desc": "जंगली कोसा कोकून से हाथ से रेशम का धागा काढ़ना", "days": "दिन 1"},
            {"step": "2. वानस्पतिक रंगाई", "desc": "अनार छिलका व आंवला रस में जैविक रंगाई", "days": "दिन 2"},
            {"step": "3. गड्ढा करघा ताना", "desc": "बांस के फ्रेम पर 1200 रेशमी धागों की तनाई", "days": "दिन 3"},
            {"step": "4. हाथ बुनाई व फिनिश", "desc": "शटल से बारीक बुनाई और धूप में हवादार सुखाई", "days": "दिन 4"}
        ],
        "buyer_gratitude": [
            {
                "buyer_name": "Smita Sen",
                "city": "Kolkata",
                "message": "The golden luster of the Tussar silk is unmatched. Outstanding pure handloom!",
                "time": "1 दिन पहले"
            }
        ],
        "likes": 56,
        "institutional_verification": {
            "stage_1_identity": {
                "badge": "PM Vishwakarma Certified",
                "badge_hi": "पीएम विश्वकर्मा सत्यापित",
                "id": "PMV-BH-67129",
                "panchayat": "चंपापुर ग्राम पंचायत सत्यापित",
                "org": "PM Vishwakarma & Gram Panchayat"
            },
            "stage_2_tech_hub": {
                "hub": "CSC Weavers Kendra #551",
                "vle": "अब्दुल रऊफ (VLE)",
                "org": "CSCs & VLEs"
            },
            "stage_3_ai": {
                "engine": "Bhashini MeitY Speech AI",
                "dialect": "Angika Dialect -> Multilingual",
                "org": "Bhashini (MeitY) & CV Pipeline"
            },
            "stage_4_aggregation": {
                "apc_lot": "Bhagalpur Silk Artisans Producer Co. (B2B Bulk Eligible)",
                "org": "Self-Help Groups & APCs"
            },
            "stage_5_qc": {
                "lab": "SFURTI Bhagalpur Textile CFC",
                "grade": "Grade A+ (Silk Mark Certified)",
                "barcode": "SFURTI-SILK-99021",
                "org": "SFURTI Clusters (CFCs)"
            },
            "stage_6_innovation": {
                "wing": "RuTAG (IIT Kharagpur) & WSC",
                "tool": "Ergonomic Fly-Shuttle Attachment",
                "org": "WSCs & RuTAG (IITs)"
            }
        },
        "created_at": "2026-09-04 12:00:00"
    },
    {
        "id": "art-104",
        "artisan_name": "Harishankar Dhiman (हरिशंकर धीमान)",
        "artisan_experience": "35 वर्षों से सहारनपुर काष्ठ नक्काशी",
        "artisan_location": "Saharanpur, Uttar Pradesh",
        "artisan_community": "Vishwakarma Woodcrafters Guild",
        "artisan_photo": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=200&q=80",
        "hands_photo": "https://images.unsplash.com/photo-1541123437800-1bb1317badc2?auto=format&fit=crop&w=800&q=80",
        "artisan_quote": "शीशम की लकड़ी की अपनी खुशबू होती है। जब रुखानी से बेल-बूटे तराशते हैं, तो लकड़ी अमर हो जाती है।",
        "title": "Intricately Carved Sheesham Wood Keepsake Chest",
        "category": "Woodcraft & Carving",
        "raw_voice_transcript": "Purani paki hui Sheesham ki lakdi se banaya hai. Hath ki chheni se jaali work aur brass inlay kiya hai. Natural walnut beeswax polish hai.",
        "story_en": "Carved by hand from aged, sustainably sourced Indian Rosewood (Sheesham), this heritage keepsake chest features delicate floral latticework and pure brass inlays, finished with organic beeswax.",
        "story_hi": "सहारनपुर की पारंपरिक जाली नक्काशी और पीतल की जड़ाई से सजी यह पुरानी शीशम की संदूकची शुद्ध मधुमक्खी के मोम से पॉलिश की गई है।",
        "materials": ["Seasoned Sheesham Wood", "Brass Wire Inlay", "Beeswax Polish"],
        "suggested_price": 1850,
        "price_range": "₹1,600 - ₹2,100",
        "fair_wage_share": "86% directly to Harishankar",
        "studio_image_url": "https://images.unsplash.com/photo-1541123437800-1bb1317badc2?auto=format&fit=crop&w=800&q=80",
        "raw_image_url": "https://images.unsplash.com/photo-1541123437800-1bb1317badc2?auto=format&fit=crop&w=800&q=80",
        "qr_code_id": "QR-WOOD-104",
        "trust_score": 97,
        "gi_tag_no": "GI-UP-WOOD-044",
        "thumbprint_id": "HARISHANKAR-THUMB-2026",
        "family_impact": {
            "beneficiary": "राहुल (पोता, स्कूल छात्र)",
            "impact_story": "इस संदूक की बिक्री से पोते राहुल के विज्ञान प्रोजेक्ट और स्कूल बस का सालभर का पास बना।",
            "progress_pct": 90,
            "goal_label": "धूल-मुक्त वुडवर्किंग एयर फिल्टर मशीन",
            "goal_stat": "₹18,000 / ₹20,000 सुरक्षित"
        },
        "craft_lifecycle": [
            {"step": "1. सूखी शीशम चयन", "desc": "10 वर्ष पुरानी धूप में पकी दरार-मुक्त शीशम छांटना", "days": "दिन 1"},
            {"step": "2. हाथ से रंदा व कटाई", "desc": "पारंपरिक रंदे से चिकनाई व कोनों की चूल-जोड़ कटाई", "days": "दिन 2"},
            {"step": "3. जाली नक्काशी", "desc": "बारीक रुखानी और हथौड़ी से पुष्प जाल तराशना", "days": "दिन 3"},
            {"step": "4. पीतल जड़ाई व मोम", "desc": "पीतल के तारों की नक्काशी व मोम से अंतिम चमक", "days": "दिन 4"}
        ],
        "buyer_gratitude": [
            {
                "buyer_name": "Arjun Kapoor",
                "city": "Mumbai",
                "message": "The brass inlay work and rosewood fragrance are mesmerizing. Absolute heirloom quality.",
                "time": "4 दिन पहले"
            }
        ],
        "likes": 48,
        "institutional_verification": {
            "stage_1_identity": {
                "badge": "PM Vishwakarma Certified",
                "badge_hi": "पीएम विश्वकर्मा सत्यापित",
                "id": "PMV-UP-44109",
                "panchayat": "सहारनपुर ग्रामीण पंचायत सत्यापित",
                "org": "PM Vishwakarma & Gram Panchayat"
            },
            "stage_2_tech_hub": {
                "hub": "CSC Woodcraft Hub #204",
                "vle": "प्रमोद धीमान (VLE)",
                "org": "CSCs & VLEs"
            },
            "stage_3_ai": {
                "engine": "Bhashini MeitY Speech AI",
                "dialect": "Western Hindi / Khari Boli -> Multilingual",
                "org": "Bhashini (MeitY) & CV Pipeline"
            },
            "stage_4_aggregation": {
                "apc_lot": "Saharanpur Woodcraft Artisan Co. (B2B Bulk Export)",
                "org": "Self-Help Groups & APCs"
            },
            "stage_5_qc": {
                "lab": "SFURTI Saharanpur CFC",
                "grade": "Grade A+ (Moisture & Termite Tested)",
                "barcode": "SFURTI-WOOD-33918",
                "org": "SFURTI Clusters (CFCs)"
            },
            "stage_6_innovation": {
                "wing": "RuTAG (IIT Roorkee)",
                "tool": "Low-Vibration Ergonomic Chisel Handles",
                "org": "WSCs & RuTAG (IITs)"
            }
        },
        "created_at": "2026-09-04 13:00:00"
    }
]"""

    if old_prod_end in code:
        code = code.replace(old_prod_end, new_products, 1)
        print("[1] Added art-103 and art-104 products.")
    else:
        print("[!] Could not match old_prod_end")

    # 2. Add /api/artisan/register endpoint
    register_endpoint = '''@app.post("/api/artisan/register")
async def register_artisan(
    name: str = Form(...),
    craft_type: str = Form("हस्तशिल्प / Handloom"),
    village_panchayat: str = Form("रंती ग्राम पंचायत, बिहार"),
    phone: str = Form(""),
    assist_requested: bool = Form(True)
):
    import random
    token_num = random.randint(1000, 9999)
    temp_id = f"PMV-REG-{token_num}"
    panchayat_token = f"GP-DESK-{token_num}"
    
    new_artisan = {
        "id": f"art-reg-{token_num}",
        "name": name.strip(),
        "vishwakarma_id": temp_id,
        "trade": craft_type,
        "gram_panchayat": village_panchayat.strip(),
        "panchayat_seal": f"{panchayat_token} (प्रारंभिक सत्यापन)",
        "verification_status": "नया पंजीकरण दर्ज • ग्राम पंचायत सत्यापन प्रतीक्षित",
        "tool_grant": "₹15,000 टूलकिट अनुदान प्रक्रियाधीन",
        "total_earnings": "₹0 (नया खाता)",
        "bank_status": "बैंक खाता सत्यापन लिंक भेजा गया",
        "community": "महिला स्वयं सहायता समूह क्लस्टर",
        "assist_status": "कला सखी / CSC VLE को सूचना भेजी गई (आज शाम भेंट)" if assist_requested else "स्वयं सत्यापन",
        "is_new_registration": True
    }
    
    announcement = f"नमस्ते {name} जी! आपका आर्टिसाना और ग्राम पंचायत पंजीकरण दर्ज हो गया है। आपका टोकन नंबर है {token_num}।"
    
    return JSONResponse(content={
        "status": "success",
        "message": f"पंजीकरण सफल! ग्राम पंचायत टोकन: {panchayat_token} • अस्थायी आईडी: {temp_id}",
        "artisan": new_artisan,
        "voice_announcement": announcement
    })

'''

    old_main = 'if __name__ == "__main__":'
    if old_main in code:
        code = code.replace(old_main, register_endpoint + old_main, 1)
        print("[2] Added POST /api/artisan/register.")
    else:
        print("[!] Could not match old_main")

    with open(path, "w", encoding="utf-8") as f:
        f.write(code)
    print("Backend update complete.")

if __name__ == "__main__":
    main()
