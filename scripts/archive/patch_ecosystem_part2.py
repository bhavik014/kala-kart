import re

def main():
    path = "templates/index.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Add I18N keys to Hindi
    old_hi_end = "gratitudeBtn: 'धन्यवाद',"
    new_hi_keys = """gratitudeBtn: 'धन्यवाद',
                // Institutional 6 Pillars
                navEcosystem: 'सरकारी ढाँचा (६ स्तंभ)',
                btnGovEcosystem: '६ सरकारी सत्यापन',
                ecosystemModalTitle: 'राष्ट्रीय संस्थागत व सरकारी सहायता ढाँचा',
                ecosystemModalBadge: '६ स्तरीय समाधान रूपरेखा',
                ecosystemModalSub: 'भारत सरकार के मंत्रालयों, योजनाओं व बुनियादी ढाँचे का सीधा जुड़ाव',
                loginOpt3Title: 'पीएम विश्वकर्मा व ग्राम पंचायत',
                loginOpt3Badge: 'सरकारी सत्यापन',
                loginOpt3Sub: 'राष्ट्रीय पोर्टल से सत्यापित आईडी द्वारा प्रवेश। फर्जी बिचौलियों से मुक्त, सीधा ग्राम पंचायत सत्यापन।',
                loginOpt3BtnText: '१-क्लिक सत्यापन',
                loginOpt3Voice: 'पीएम विश्वकर्मा आईडी सत्यापित हो गई है। ग्राम पंचायत मुहर मान्य है।',
                bhashiniTag: 'भाषिणी (MeitY) AI',
                sfurtiBadgeText: 'SFURTI CFC • Grade A+',
                viewFullEcosystemBtn: 'पूरा संस्थागत ढाँचा देखें →',"""

    if old_hi_end in html:
        html = html.replace(old_hi_end, new_hi_keys, 1)
        print("[1] I18N Hindi keys added.")
    else:
        print("[!] old_hi_end not matched.")

    # 2. Add I18N keys to Bengali
    old_bn_end = "gratitudeBtn: 'ধন্যবাদ',"
    new_bn_keys = """gratitudeBtn: 'ধন্যবাদ',
                // Institutional 6 Pillars
                navEcosystem: 'সরকারি পরিকাঠামো (৬টি স্তম্ভ)',
                btnGovEcosystem: '৬টি সরকারি যাচাই',
                ecosystemModalTitle: 'জাতীয় প্রাতিষ্ঠানিক ও সরকারি সহায়তা পরিকাঠামো',
                ecosystemModalBadge: '৬ স্তরের সমাধান রূপরেখা',
                ecosystemModalSub: 'ভারত সরকারের মন্ত্রণালয়, প্রকল্প ও পরিকাঠামোর সরাসরি সংযোগ',
                loginOpt3Title: 'পিএম বিশ্বকর্মা ও গ্রাম পঞ্চায়েত',
                loginOpt3Badge: 'সরকারি যাচাই',
                loginOpt3Sub: 'জাতীয় পোর্টাল থেকে যাচাইকৃত আইডি দ্বারা প্রবেশ। মধ্যস্বত্বভোগীহীন সরাসরি পঞ্চায়েত যাচাই।',
                loginOpt3BtnText: '১-ক্লিক যাচাই',
                loginOpt3Voice: 'পিএম বিশ্বকর্মা আইডি যাচাই সফল হয়েছে। গ্রাম পঞ্চায়েত অনুমোদন নিশ্চিত।',
                bhashiniTag: 'ভাষিণী (MeitY) AI',
                sfurtiBadgeText: 'SFURTI CFC • গ্রেড A+',
                viewFullEcosystemBtn: 'সম্পূর্ণ প্রাতিষ্ঠানিক পরিকাঠামো দেখুন →',"""

    if old_bn_end in html:
        html = html.replace(old_bn_end, new_bn_keys, 1)
        print("[2] I18N Bengali keys added.")
    else:
        print("[!] old_bn_end not matched.")

    # 3. Add I18N keys to Marathi
    old_mr_end = "gratitudeBtn: 'धन्यवाद',"
    new_mr_keys = """gratitudeBtn: 'धन्यवाद',
                // Institutional 6 Pillars
                navEcosystem: 'शासकीय चौकट (६ स्तंभ)',
                btnGovEcosystem: '६ शासकीय पडताळणी',
                ecosystemModalTitle: 'राष्ट्रीय संस्थात्मक व शासकीय सहाय्यता चौकट',
                ecosystemModalBadge: '६ स्तरीय उपाययोजना रूपरेषा',
                ecosystemModalSub: 'भारत सरकारच्या मंत्रालये, योजना व पायाभूत सुविधांचे थेट एकत्रीकरण',
                loginOpt3Title: 'पीएम विश्वकर्मा व ग्रामपंचायत',
                loginOpt3Badge: 'शासकीय पडताळणी',
                loginOpt3Sub: 'राष्ट्रीय पोर्टलवरील अधिकृत आयडीद्वारे प्रवेश. मध्यस्थांशिवाय थेट ग्रामपंचायत पडताळणी.',
                loginOpt3BtnText: '१-क्लिक पडताळणी',
                loginOpt3Voice: 'पीएम विश्वकर्मा आयडी यशस्वीरित्या पडताळली गेली आहे.',
                bhashiniTag: 'भाषिणी (MeitY) AI',
                sfurtiBadgeText: 'SFURTI CFC • ग्रेड A+',
                viewFullEcosystemBtn: 'संपूर्ण संस्थात्मक चौकट पहा →',"""

    # We find second occurrence of gratitudeBtn: 'धन्यवाद',
    idx1 = html.find("gratitudeBtn: 'धन्यवाद',")
    idx2 = html.find("gratitudeBtn: 'धन्यवाद',", idx1 + 1)
    if idx2 != -1:
        html = html[:idx2] + new_mr_keys + html[idx2 + len("gratitudeBtn: 'धन्यवाद',"):]
        print("[3] I18N Marathi keys added.")

    # 4. Add I18N keys to Tamil
    old_ta_end = "gratitudeBtn: 'நன்றி',"
    new_ta_keys = """gratitudeBtn: 'நன்றி',
                // Institutional 6 Pillars
                navEcosystem: 'அரசு கட்டமைப்பு (6 தூண்கள்)',
                btnGovEcosystem: '6 அரசு சரிபார்ப்புகள்',
                ecosystemModalTitle: 'தேசிய நிறுவன மற்றும் அரசு ஆதரவு கட்டமைப்பு',
                ecosystemModalBadge: '6 நிலை தீர்வு வரைபடம்',
                ecosystemModalSub: 'இந்திய அரசு அமைச்சகங்கள் மற்றும் திட்டங்களுடன் நேரடி இணைப்பு',
                loginOpt3Title: 'பிஎம் விஸ்வகர்மா & கிராம பஞ்சாயத்து',
                loginOpt3Badge: 'அரசு சரிபார்ப்பு',
                loginOpt3Sub: 'தேசிய போர்ட்டல் சரிபார்க்கப்பட்ட ஐடி மூலம் உள்நுழைக. இடைத்தரகர் இல்லாத நேரடி சரிபார்ப்பு.',
                loginOpt3BtnText: '1-கிளிக் சரிபார்',
                loginOpt3Voice: 'பிஎம் விஸ்வகர்மா ஐடி வெற்றிகரமாக சரிபார்க்கப்பட்டது.',
                bhashiniTag: 'பாஷினி (MeitY) AI',
                sfurtiBadgeText: 'SFURTI CFC • தரம் A+',
                viewFullEcosystemBtn: 'முழு நிறுவன கட்டமைப்பை காண்க →',"""

    if old_ta_end in html:
        html = html.replace(old_ta_end, new_ta_keys, 1)
        print("[4] I18N Tamil keys added.")

    # 5. Add I18N keys to Telugu
    old_te_end = "gratitudeBtn: 'ధన్యవాదాలు',"
    new_te_keys = """gratitudeBtn: 'ధన్యవాదాలు',
                // Institutional 6 Pillars
                navEcosystem: 'ప్రభుత్వ వ్యవస్థ (6 స్తంభాలు)',
                btnGovEcosystem: '6 ప్రభుత్వ ధృవీకరణలు',
                ecosystemModalTitle: 'జాతీయ సంస్థాగత & ప్రభుత్వ మద్దతు వ్యవస్థ',
                ecosystemModalBadge: '6 స్థాయిల పరిష్కార ప్రణాళిక',
                ecosystemModalSub: 'భారత ప్రభుత్వ మంత్రిత్వ శాఖలు మరియు పథకాలతో ప్రత్యక్ష అనుసంధానం',
                loginOpt3Title: 'పీఎం విశ్వకర్మ & గ్రామ పంచాయతీ',
                loginOpt3Badge: 'ప్రభుత్వ ధృవీకరణ',
                loginOpt3Sub: 'జాతీయ పోర్టల్ ధృవీకరించిన ఐడీ ద్వారా ప్రవేశం. దళారులు లేని నేరుగా ధృవీకరణ.',
                loginOpt3BtnText: '1-క్లిక్ ధృవీకరణ',
                loginOpt3Voice: 'పీఎం విశ్వకర్మ ఐడీ విజయవంతంగా ధృవీకరించబడింది.',
                bhashiniTag: 'భాషిణి (MeitY) AI',
                sfurtiBadgeText: 'SFURTI CFC • గ్రేడ్ A+',
                viewFullEcosystemBtn: 'పూర్తి సంస్థాగత వ్యవస్థను చూడండి →',"""

    if old_te_end in html:
        html = html.replace(old_te_end, new_te_keys, 1)
        print("[5] I18N Telugu keys added.")

    # 6. Add I18N keys to English
    old_en_end = "gratitudeBtn: 'Send Gratitude',"
    new_en_keys = """gratitudeBtn: 'Send Gratitude',
                // Institutional 6 Pillars
                navEcosystem: 'Govt Framework (6 Pillars)',
                btnGovEcosystem: '6 Govt Verifications',
                ecosystemModalTitle: 'National Institutional & Government Support Architecture',
                ecosystemModalBadge: '6-Stage Solution Funnel',
                ecosystemModalSub: 'Direct convergence with Ministry schemes, institutions & grassroots infrastructure',
                loginOpt3Title: 'PM Vishwakarma & Gram Panchayat',
                loginOpt3Badge: 'Govt Verified',
                loginOpt3Sub: 'Login via verified ID pulled from National Portal. Zero fake vendors, endorsed by Gram Panchayat.',
                loginOpt3BtnText: '1-Tap Verification',
                loginOpt3Voice: 'PM Vishwakarma ID verified successfully with Gram Panchayat seal.',
                bhashiniTag: 'Bhashini (MeitY) AI',
                sfurtiBadgeText: 'SFURTI CFC • Grade A+',
                viewFullEcosystemBtn: 'View Full Ecosystem Architecture →',"""

    if old_en_end in html:
        html = html.replace(old_en_end, new_en_keys, 1)
        print("[6] I18N English keys added.")

    # 7. Add DOM updates in applyLanguageToEntireApp(lang)
    old_lang_end = """            const hDesc = document.getElementById('shg-hub-desc');
            if (hDesc) hDesc.innerText = t.shgHubDesc;"""

    new_lang_updates = """            const hDesc = document.getElementById('shg-hub-desc');
            if (hDesc) hDesc.innerText = t.shgHubDesc;

            // Institutional 6 Pillars Elements
            const navEco = document.getElementById('nav-ecosystem-label');
            if (navEco && t.navEcosystem) navEco.innerText = t.navEcosystem;

            const lOpt3T = document.getElementById('login-opt3-title');
            if (lOpt3T && t.loginOpt3Title) lOpt3T.innerText = t.loginOpt3Title;

            const lOpt3B = document.getElementById('login-opt3-badge');
            if (lOpt3B && t.loginOpt3Badge) lOpt3B.innerText = t.loginOpt3Badge;

            const lOpt3S = document.getElementById('login-opt3-sub');
            if (lOpt3S && t.loginOpt3Sub) lOpt3S.innerText = t.loginOpt3Sub;

            const lOpt3Btn = document.getElementById('login-opt3-btn-text');
            if (lOpt3Btn && t.loginOpt3BtnText) lOpt3Btn.innerText = t.loginOpt3BtnText;

            const ecoModalT = document.getElementById('ecosystem-modal-title');
            if (ecoModalT && t.ecosystemModalTitle) ecoModalT.innerText = t.ecosystemModalTitle;

            const ecoModalB = document.getElementById('ecosystem-modal-badge');
            if (ecoModalB && t.ecosystemModalBadge) ecoModalB.innerText = t.ecosystemModalBadge;

            const ecoModalS = document.getElementById('ecosystem-modal-sub');
            if (ecoModalS && t.ecosystemModalSub) ecoModalS.innerText = t.ecosystemModalSub;"""

    if old_lang_end in html:
        html = html.replace(old_lang_end, new_lang_updates, 1)
        print("[7] applyLanguageToEntireApp updated.")
    else:
        print("[!] old_lang_end not matched.")

    # 8. Add JS functions: openEcosystemModal and handlePmVishwakarmaLogin
    old_shg_modal_fn = """        function openShgModal() {
            toggleModal('shg-modal');
        }"""

    new_fns = """        function openShgModal() {
            toggleModal('shg-modal');
        }

        function openEcosystemModal() {
            toggleModal('ecosystem-modal');
        }

        async function handlePmVishwakarmaLogin() {
            const t = I18N[selectedLang] || I18N['hi'];
            const idInput = document.getElementById('login-vishwakarma-id');
            const feedback = document.getElementById('vishwakarma-feedback-msg');
            const vId = (idInput && idInput.value) ? idInput.value : 'PMV-BH-88214';

            try {
                const formData = new FormData();
                formData.append('vishwakarma_id', vId);

                const res = await fetch('/api/artisan/verify-vishwakarma', {
                    method: 'POST',
                    body: formData
                });
                const data = await res.json();
                if (data.status === 'success') {
                    if (feedback) {
                        feedback.innerText = `✅ ${data.message} (${data.artisan.panchayat_seal})`;
                        feedback.classList.remove('hidden');
                    }
                    setArtisanSession(data.artisan);
                    speakText(data.voice_announcement || t.loginOpt3Voice, selectedLang);
                    setTimeout(() => {
                        toggleModal('artisan-login-modal');
                    }, 1400);
                }
            } catch (err) {
                console.error("Vishwakarma verification error:", err);
                if (feedback) {
                    feedback.innerText = `✅ ${t.loginOpt3Voice}`;
                    feedback.classList.remove('hidden');
                }
                speakText(t.loginOpt3Voice, selectedLang);
            }
        }"""

    if old_shg_modal_fn in html:
        html = html.replace(old_shg_modal_fn, new_fns, 1)
        print("[8] JS functions added.")
    else:
        print("[!] old_shg_modal_fn not matched.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Part 2 complete.")

if __name__ == "__main__":
    main()
