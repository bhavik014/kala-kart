import re

def main():
    path = "templates/index.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Add nav button
    old_nav = '''                <!-- SHG Cluster Hub Pill -->
                <button onclick="openShgModal()" id="nav-shg-btn"'''
    new_nav = '''                <!-- 6 Pillars Govt Ecosystem Pill -->
                <button onclick="openEcosystemModal()" id="nav-ecosystem-btn" class="hidden md:flex items-center gap-1.5 px-3 py-1.5 text-xs font-stamp font-bold text-[#1e3a8a] bg-[#eff6ff] hover:bg-[#dbeafe] rounded-xl border border-[#93c5fd] shadow-[2px_2px_0px_#1e3a8a] transition">
                    <i data-lucide="landmark" class="w-3.5 h-3.5 text-[#1e3a8a]"></i>
                    <span id="nav-ecosystem-label">सरकारी ढाँचा (६ स्तंभ)</span>
                </button>

                <!-- SHG Cluster Hub Pill -->
                <button onclick="openShgModal()" id="nav-shg-btn"'''

    if old_nav in html:
        html = html.replace(old_nav, new_nav, 1)
        print("[1] Nav button added.")
    else:
        print("[!] Old nav not matched.")

    # 2. Add Option 3 in login modal
    old_opt2 = '''                <!-- Option 2: Kala Passbook QR Scan -->'''
    opt3_block = '''                <!-- Option 3: PM Vishwakarma & Gram Panchayat 1-Tap Verification -->
                <div class="p-4 bg-[#eff6ff] rounded-2xl border-2 border-[#3b82f6] shadow-[3px_3px_0px_#1d4ed8]">
                    <div class="flex items-center justify-between mb-2">
                        <div class="flex items-center gap-2">
                            <span class="w-6 h-6 rounded-full bg-[#1d4ed8] text-white flex items-center justify-center text-xs font-bold font-stamp">3</span>
                            <h4 id="login-opt3-title" class="font-vintage text-base text-[#1e3a8a]">पीएम विश्वकर्मा व ग्राम पंचायत</h4>
                        </div>
                        <span id="login-opt3-badge" class="text-[10px] font-stamp font-bold text-[#1d4ed8] bg-white px-2 py-0.5 rounded border border-[#93c5fd]">सरकारी सत्यापन</span>
                    </div>
                    <p id="login-opt3-sub" class="text-[11px] text-[#475569] mb-2.5">
                        राष्ट्रीय पोर्टल से सत्यापित आईडी द्वारा प्रवेश। फर्जी बिचौलियों से मुक्त, सीधा ग्राम पंचायत सत्यापन।
                    </p>
                    <div class="flex gap-2">
                        <input type="text" id="login-vishwakarma-id" value="PMV-BH-88214" placeholder="PMV-XX-XXXXX" class="flex-1 px-3 py-2 text-xs font-mono font-bold uppercase tracking-wider bg-white border border-[#93c5fd] rounded-xl focus:outline-none">
                        <button type="button" onclick="handlePmVishwakarmaLogin()" id="login-opt3-btn" class="px-3 py-2 bg-[#1d4ed8] hover:bg-[#1e40af] text-white font-bold text-xs rounded-xl shadow-[2px_2px_0px_#1e3a8a] transition flex items-center gap-1.5 flex-shrink-0">
                            <i data-lucide="shield-check" class="w-4 h-4"></i>
                            <span id="login-opt3-btn-text">1-Tap सत्यापन</span>
                        </button>
                    </div>
                    <div id="vishwakarma-feedback-msg" class="hidden mt-2 p-2 bg-white border border-[#3b82f6] rounded-xl text-[11px] font-bold text-[#1d4ed8]"></div>
                </div>

                <!-- Option 2: Kala Passbook QR Scan -->'''
    
    if old_opt2 in html:
        html = html.replace(old_opt2, opt3_block, 1)
        print("[2] Login Option 3 added.")
    else:
        print("[!] Old opt2 not matched.")

    # 3. Add Ecosystem Modal right before </body>
    old_body_end = '''    </div>
</body>
</html>'''

    ecosystem_modal_html = '''    </div>

    <!-- 6-STAGE GOVERNMENT & INSTITUTIONAL ECOSYSTEM ARCHITECTURE MODAL -->
    <div id="ecosystem-modal" class="fixed inset-0 z-50 hidden bg-[#2b2d42]/85 backdrop-blur-md flex items-center justify-center p-4">
        <div class="bg-[#fffdfa] rounded-3xl max-w-4xl w-full p-6 sm:p-8 shadow-[12px_18px_0px_#1e3a8a] border-3 border-[#2b2d42] relative max-h-[92vh] overflow-y-auto">
            <button onclick="toggleModal('ecosystem-modal')" class="absolute top-5 right-5 text-[#6c757d] hover:text-[#2b2d42] p-1.5 rounded-full hover:bg-[#f1f5f9]">
                <i data-lucide="x" class="w-6 h-6"></i>
            </button>

            <!-- Modal Header -->
            <div class="flex items-center gap-3.5 mb-6 border-b-2 border-dashed border-[#93c5fd] pb-4">
                <div class="w-12 h-12 rounded-2xl bg-[#1e3a8a] text-white flex items-center justify-center shadow-[3px_3px_0px_#2b2d42] flex-shrink-0">
                    <i data-lucide="landmark" class="w-6 h-6"></i>
                </div>
                <div>
                    <div class="flex items-center gap-2 flex-wrap">
                        <h3 id="ecosystem-modal-title" class="font-vintage text-2xl text-[#1e3a8a]">राष्ट्रीय संस्थागत व सरकारी सहायता ढाँचा</h3>
                        <span id="ecosystem-modal-badge" class="px-2.5 py-0.5 rounded-full text-[10px] font-stamp font-bold bg-[#eff6ff] text-[#1e3a8a] border border-[#93c5fd]">६ स्तरीय समाधान रूपरेखा</span>
                    </div>
                    <p id="ecosystem-modal-sub" class="text-xs font-stamp text-[#64748b]">भारत सरकार के मौजूदा मंत्रालयों, योजनाओं व बुनियादी ढाँचे का सीधा जुड़ाव</p>
                </div>
            </div>

            <!-- 6 Stages Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                
                <!-- Stage 1 -->
                <div class="p-4 bg-[#eff6ff] rounded-2xl border-2 border-[#93c5fd] shadow-[3px_3px_0px_#93c5fd] flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <div class="flex items-center gap-2">
                                <span class="w-6 h-6 rounded-full bg-[#1d4ed8] text-white flex items-center justify-center text-xs font-bold font-stamp">1</span>
                                <h4 class="font-vintage text-base text-[#1e3a8a]">Zero-Friction Onboarding & Digital Identity</h4>
                            </div>
                            <span class="text-[9px] font-stamp font-bold text-[#1d4ed8] bg-white px-2 py-0.5 rounded border border-[#93c5fd]">पिलर १</span>
                        </div>
                        <div class="mb-2 p-2 bg-white/80 rounded-xl border border-[#bfdbfe]">
                            <span class="text-[10px] font-bold text-[#1e3a8a] block">संस्था / नेटवर्क:</span>
                            <b class="text-xs text-[#0f172a]">PM Vishwakarma & Gram Panchayats</b>
                        </div>
                        <p class="text-xs text-[#334155] leading-relaxed mb-2">
                            <b>समस्या:</b> ई-कॉमर्स में अक्सर फर्जी विक्रेता खाते और बिचौलिए सब्सिडी हड़प लेते हैं।
                        </p>
                        <p class="text-xs text-[#1e3a8a] leading-relaxed bg-white p-2 rounded-xl border border-[#93c5fd]/50">
                            <b>समाधान भूमिका:</b> पीएम विश्वकर्मा पोर्टल से सीधे सत्यापित आईडी प्राप्त करना। ग्राम पंचायत स्थानीय भौतिक सत्यापन डेस्क के रूप में कार्य करती है।
                        </p>
                    </div>
                    <div class="mt-3 pt-2 border-t border-dashed border-[#93c5fd] flex items-center justify-between text-[11px] font-stamp text-[#0369a1]">
                        <span>✓ १-क्लिक विश्वकर्मा सिंक</span>
                        <span>मुहर: #GP-88</span>
                    </div>
                </div>

                <!-- Stage 2 -->
                <div class="p-4 bg-[#fefae0] rounded-2xl border-2 border-[#d4a373] shadow-[3px_3px_0px_#d4a373] flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <div class="flex items-center gap-2">
                                <span class="w-6 h-6 rounded-full bg-[#b45309] text-white flex items-center justify-center text-xs font-bold font-stamp">2</span>
                                <h4 class="font-vintage text-base text-[#2b2d42]">Physical Assisted Tech Hubs</h4>
                            </div>
                            <span class="text-[9px] font-stamp font-bold text-[#b45309] bg-white px-2 py-0.5 rounded border border-[#d4a373]">पिलर २</span>
                        </div>
                        <div class="mb-2 p-2 bg-white/80 rounded-xl border border-[#e7d8c9]">
                            <span class="text-[10px] font-bold text-[#b45309] block">संस्था / नेटवर्क:</span>
                            <b class="text-xs text-[#0f172a]">CSCs (Common Services Centres) & VLEs</b>
                        </div>
                        <p class="text-xs text-[#334155] leading-relaxed mb-2">
                            <b>समस्या:</b> ९८% ग्रामीण शिल्पकारों के पास स्मार्टफोन, हाई-स्पीड इंटरनेट या कैमरा कौशल नहीं है।
                        </p>
                        <p class="text-xs text-[#92400e] leading-relaxed bg-white p-2 rounded-xl border border-[#d4a373]/50">
                            <b>समाधान भूमिका:</b> ग्राम स्तरीय उद्यमी (VLE) तकनीकी साथी बनकर उच्च गुणवत्ता वाली तस्वीरें लेते हैं और आवश्यक डिजिटल उपकरण उपलब्ध कराते हैं।
                        </p>
                    </div>
                    <div class="mt-3 pt-2 border-t border-dashed border-[#d4a373] flex items-center justify-between text-[11px] font-stamp text-[#b45309]">
                        <span>✓ सीएससी डिजिटल कियोस्क</span>
                        <span>कला सखी डोरस्टेप</span>
                    </div>
                </div>

                <!-- Stage 3 -->
                <div class="p-4 bg-[#f0fdf4] rounded-2xl border-2 border-[#86efac] shadow-[3px_3px_0px_#86efac] flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <div class="flex items-center gap-2">
                                <span class="w-6 h-6 rounded-full bg-[#15803d] text-white flex items-center justify-center text-xs font-bold font-stamp">3</span>
                                <h4 class="font-vintage text-base text-[#14532d]">AI Cataloging & Localization</h4>
                            </div>
                            <span class="text-[9px] font-stamp font-bold text-[#15803d] bg-white px-2 py-0.5 rounded border border-[#86efac]">पिलर ३</span>
                        </div>
                        <div class="mb-2 p-2 bg-white/80 rounded-xl border border-[#bbf7d0]">
                            <span class="text-[10px] font-bold text-[#15803d] block">संस्था / नेटवर्क:</span>
                            <b class="text-xs text-[#0f172a]">Bhashini (MeitY) & Computer Vision Pipeline</b>
                        </div>
                        <p class="text-xs text-[#334155] leading-relaxed mb-2">
                            <b>समस्या:</b> कारीगर स्थानीय बोलियों में बोलते हैं, जिसे सामान्य अंग्रेजी ई-कॉमर्स समझ नहीं पाता।
                        </p>
                        <p class="text-xs text-[#166534] leading-relaxed bg-white p-2 rounded-xl border border-[#86efac]/50">
                            <b>समाधान भूमिका:</b> भाषिणी एआई स्थानीय बोलियों को बहुभाषी उत्पाद विवरण में बदलती है। कंप्यूटर विज़न साधारण तस्वीरों को स्टूडियो कैटलॉग में बदलता है।
                        </p>
                    </div>
                    <div class="mt-3 pt-2 border-t border-dashed border-[#86efac] flex items-center justify-between text-[11px] font-stamp text-[#15803d]">
                        <span>✓ भाषिणी बोली अनुवाद</span>
                        <span>एआई बैकग्राउंड रिमूवल</span>
                    </div>
                </div>

                <!-- Stage 4 -->
                <div class="p-4 bg-[#fff7ed] rounded-2xl border-2 border-[#fdba74] shadow-[3px_3px_0px_#fdba74] flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <div class="flex items-center gap-2">
                                <span class="w-6 h-6 rounded-full bg-[#c2410c] text-white flex items-center justify-center text-xs font-bold font-stamp">4</span>
                                <h4 class="font-vintage text-base text-[#7c2d12]">Collective Aggregation & Micro-Logistics</h4>
                            </div>
                            <span class="text-[9px] font-stamp font-bold text-[#c2410c] bg-white px-2 py-0.5 rounded border border-[#fdba74]">पिलर ४</span>
                        </div>
                        <div class="mb-2 p-2 bg-white/80 rounded-xl border border-[#fed7aa]">
                            <span class="text-[10px] font-bold text-[#c2410c] block">संस्था / नेटवर्क:</span>
                            <b class="text-xs text-[#0f172a]">Self-Help Groups (SHGs) & APCs</b>
                        </div>
                        <p class="text-xs text-[#334155] leading-relaxed mb-2">
                            <b>समस्या:</b> दूरदराज के गाँवों से एकल पार्सल भेजना अत्यधिक महंगा पड़ता है।
                        </p>
                        <p class="text-xs text-[#9a3412] leading-relaxed bg-white p-2 rounded-xl border border-[#fdba74]/50">
                            <b>समाधान भूमिका:</b> एकल उत्पादन को थोक बी२बी लॉट में एकत्रित करना। गाँव स्तर पर डाकघर व कूरियर के लिए एकल संकलन केंद्र बनाना।
                        </p>
                    </div>
                    <div class="mt-3 pt-2 border-t border-dashed border-[#fdba74] flex items-center justify-between text-[11px] font-stamp text-[#c2410c]">
                        <span>✓ डाकघर संकलन केंद्र</span>
                        <span>बी२बी बल्क लॉट</span>
                    </div>
                </div>

                <!-- Stage 5 -->
                <div class="p-4 bg-[#faf5ff] rounded-2xl border-2 border-[#d8b4fe] shadow-[3px_3px_0px_#d8b4fe] flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <div class="flex items-center gap-2">
                                <span class="w-6 h-6 rounded-full bg-[#7e22ce] text-white flex items-center justify-center text-xs font-bold font-stamp">5</span>
                                <h4 class="font-vintage text-base text-[#581c87]">Quality Control, Packaging & Design Labs</h4>
                            </div>
                            <span class="text-[9px] font-stamp font-bold text-[#7e22ce] bg-white px-2 py-0.5 rounded border border-[#d8b4fe]">पिलर ५</span>
                        </div>
                        <div class="mb-2 p-2 bg-white/80 rounded-xl border border-[#e9d5ff]">
                            <span class="text-[10px] font-bold text-[#7e22ce] block">संस्था / नेटवर्क:</span>
                            <b class="text-xs text-[#0f172a]">SFURTI Clusters (Common Facility Centres)</b>
                        </div>
                        <p class="text-xs text-[#334155] leading-relaxed mb-2">
                            <b>समस्या:</b> रास्ते में माल टूटने और गैर-मानकीकृत पैकेजिंग से उत्पाद वापसी दर बढ़ जाती है।
                        </p>
                        <p class="text-xs text-[#6b21a8] leading-relaxed bg-white p-2 rounded-xl border border-[#d8b4fe]/50">
                            <b>समाधान भूमिका:</b> स्फूर्ति कॉमन फैसिलिटी सेंटर्स मानक गुणवत्ता जांच, बारकोड टैगिंग और सुरक्षित निर्यात पैकेजिंग सुनिश्चित करते हैं।
                        </p>
                    </div>
                    <div class="mt-3 pt-2 border-t border-dashed border-[#d8b4fe] flex items-center justify-between text-[11px] font-stamp text-[#7e22ce]">
                        <span>✓ SFURTI ग्रेड A+ मुहर</span>
                        <span>एक्सपोर्ट पैकेजिंग</span>
                    </div>
                </div>

                <!-- Stage 6 -->
                <div class="p-4 bg-[#fff1f2] rounded-2xl border-2 border-[#fecdd3] shadow-[3px_3px_0px_#fecdd3] flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <div class="flex items-center gap-2">
                                <span class="w-6 h-6 rounded-full bg-[#be123c] text-white flex items-center justify-center text-xs font-bold font-stamp">6</span>
                                <h4 class="font-vintage text-base text-[#881337]">Skill Upgrades & Hardware Innovation</h4>
                            </div>
                            <span class="text-[9px] font-stamp font-bold text-[#be123c] bg-white px-2 py-0.5 rounded border border-[#fecdd3]">पिलर ६</span>
                        </div>
                        <div class="mb-2 p-2 bg-white/80 rounded-xl border border-[#fecdd3]">
                            <span class="text-[10px] font-bold text-[#be123c] block">संस्था / नेटवर्क:</span>
                            <b class="text-xs text-[#0f172a]">Weavers' Service Centres (WSCs) & RuTAG (IITs)</b>
                        </div>
                        <p class="text-xs text-[#334155] leading-relaxed mb-2">
                            <b>समस्या:</b> पारंपरिक भारी उपकरणों से शारीरिक थकान होती है और शहरी बाज़ार ट्रेंड की समझ नहीं होती।
                        </p>
                        <p class="text-xs text-[#9f1239] leading-relaxed bg-white p-2 rounded-xl border border-[#fecdd3]/50">
                            <b>समाधान भूमिका:</b> बाज़ार ट्रेंड एनालिटिक्स का फीडबैक लूप बुनकर सेवा केंद्रों और आईआईटी के RuTAG तक पहुँचता है ताकि आधुनिक उपकरण विकसित हो सकें।
                        </p>
                    </div>
                    <div class="mt-3 pt-2 border-t border-dashed border-[#fecdd3] flex items-center justify-between text-[11px] font-stamp text-[#be123c]">
                        <span>✓ IIT RuTAG टूल नवाचार</span>
                        <span>WSC कलर पैलेट</span>
                    </div>
                </div>

            </div>
        </div>
    </div>
</body>
</html>'''

    if old_body_end in html:
        html = html.replace(old_body_end, ecosystem_modal_html, 1)
        print("[3] Ecosystem Modal added.")
    else:
        print("[!] Old body end not matched.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Patch stage 1 complete.")

if __name__ == "__main__":
    main()
