def main():
    path = "templates/index.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Add SFURTI CFC Stamp on product image
    old_img_badge = """                        <!-- Direct Wage Share Badge -->
                        <div class="absolute bottom-3 right-3 bg-[#2b2d42] text-[#fefae0] px-3 py-1.5 rounded-xl text-xs font-stamp font-bold shadow flex items-center gap-1.5">
                            <i data-lucide="award" class="w-3.5 h-3.5 text-[#fefae0]"></i>
                            <span>${t.fairWageBadgeText}</span>
                        </div>"""

    new_img_badge = """                        <!-- SFURTI CFC Quality Stamp & Barcode -->
                        <div class="absolute top-3 right-3 bg-[#1e3a8a] text-white px-2.5 py-1 rounded-lg text-[9px] font-stamp font-bold shadow flex items-center gap-1 border border-[#93c5fd]">
                            <i data-lucide="shield-check" class="w-3 h-3 text-[#93c5fd]"></i>
                            <span>${t.sfurtiBadgeText}</span>
                        </div>

                        <!-- Direct Wage Share Badge -->
                        <div class="absolute bottom-3 right-3 bg-[#2b2d42] text-[#fefae0] px-3 py-1.5 rounded-xl text-xs font-stamp font-bold shadow flex items-center gap-1.5">
                            <i data-lucide="award" class="w-3.5 h-3.5 text-[#fefae0]"></i>
                            <span>${t.fairWageBadgeText}</span>
                        </div>"""

    if old_img_badge in html:
        html = html.replace(old_img_badge, new_img_badge, 1)
        print("[1] SFURTI CFC stamp added to image.")
    else:
        print("[!] old_img_badge not matched.")

    # 2. Add Bhashini MeitY AI badge to voice player
    old_voice_title = """                                    <div class="flex items-center justify-between">
                                        <span class="text-xs font-bold text-[#2b2d42]">${t.voiceStoryTitle}</span>"""

    new_voice_title = """                                    <div class="flex items-center justify-between">
                                        <div class="flex items-center gap-1.5">
                                            <span class="text-xs font-bold text-[#2b2d42]">${t.voiceStoryTitle}</span>
                                            <span class="text-[9px] font-stamp font-bold text-[#1e3a8a] bg-[#eff6ff] px-1.5 py-0.5 rounded border border-[#bfdbfe]">${t.bhashiniTag}</span>
                                        </div>"""

    if old_voice_title in html:
        html = html.replace(old_voice_title, new_voice_title, 1)
        print("[2] Bhashini AI badge added to voice player.")
    else:
        print("[!] old_voice_title not matched.")

    # 3. Add 3rd toggle chip for Govt Ecosystem
    old_toggle_chips = """                                <button onclick="toggleCardDetail('${p.id}', 'impact')" id="btn-impact-${p.id}" class="px-2.5 py-1 text-[11px] font-stamp font-bold text-[#047857] bg-[#ecfdf5] hover:bg-[#d1fae5] border border-[#a7f3d0] rounded-xl transition flex items-center gap-1">
                                    <i data-lucide="heart" class="w-3.5 h-3.5 text-[#059669]"></i>
                                    <span>${t.btnImpact}</span>
                                    <i data-lucide="chevron-down" class="w-3 h-3 transition-transform" id="arrow-impact-${p.id}"></i>
                                </button>
                            </div>"""

    new_toggle_chips = """                                <button onclick="toggleCardDetail('${p.id}', 'impact')" id="btn-impact-${p.id}" class="px-2.5 py-1 text-[11px] font-stamp font-bold text-[#047857] bg-[#ecfdf5] hover:bg-[#d1fae5] border border-[#a7f3d0] rounded-xl transition flex items-center gap-1">
                                    <i data-lucide="heart" class="w-3.5 h-3.5 text-[#059669]"></i>
                                    <span>${t.btnImpact}</span>
                                    <i data-lucide="chevron-down" class="w-3 h-3 transition-transform" id="arrow-impact-${p.id}"></i>
                                </button>

                                <button onclick="toggleCardDetail('${p.id}', 'gov')" id="btn-gov-${p.id}" class="px-2.5 py-1 text-[11px] font-stamp font-bold text-[#1e3a8a] bg-[#eff6ff] hover:bg-[#dbeafe] border border-[#93c5fd] rounded-xl transition flex items-center gap-1">
                                    <i data-lucide="landmark" class="w-3.5 h-3.5 text-[#1e3a8a]"></i>
                                    <span>${t.btnGovEcosystem}</span>
                                    <i data-lucide="chevron-down" class="w-3 h-3 transition-transform" id="arrow-gov-${p.id}"></i>
                                </button>
                            </div>"""

    if old_toggle_chips in html:
        html = html.replace(old_toggle_chips, new_toggle_chips, 1)
        print("[3] 3rd toggle chip added.")
    else:
        print("[!] old_toggle_chips not matched.")

    # 4. Add gov-section after impact-section
    old_impact_section = """                                <span class="text-[9px] font-stamp text-[#6c757d] block mt-1">${impact.goal_label} • ${impact.progress_pct}%</span>
                            </div>

                            <!-- 5. DIL SE DIL TAK: 2-Way Buyer Gratitude Wall -->"""

    new_gov_section = """                                <span class="text-[9px] font-stamp text-[#6c757d] block mt-1">${impact.goal_label} • ${impact.progress_pct}%</span>
                            </div>

                            <!-- 6-STAGE INSTITUTIONAL GOVT VERIFICATION -->
                            <div id="gov-section-${p.id}" class="hidden p-3 bg-[#f8fafc] border border-[#cbd5e1] rounded-2xl mb-3 space-y-2">
                                <div class="flex items-center justify-between border-b border-dashed border-[#cbd5e1] pb-1.5">
                                    <span class="text-[10px] font-stamp font-bold text-[#1e3a8a] flex items-center gap-1">
                                        <i data-lucide="shield-check" class="w-3 h-3 text-[#1e3a8a]"></i>
                                        ${t.btnGovEcosystem}
                                    </span>
                                    <button onclick="openEcosystemModal()" class="text-[9px] font-stamp font-bold text-[#1e3a8a] hover:underline">
                                        ${t.viewFullEcosystemBtn}
                                    </button>
                                </div>
                                <div class="grid grid-cols-2 gap-1.5 text-[10px] font-stamp">
                                    <div class="bg-white p-2 rounded-xl border border-[#cbd5e1]">
                                        <span class="text-[#1d4ed8] font-bold block">१. पीएम विश्वकर्मा</span>
                                        <span class="text-[#334155] text-[9px] block truncate">ID: ${p.institutional_verification ? p.institutional_verification.stage_1_identity.id : 'PMV-BH-88214'}</span>
                                        <span class="text-[#047857] text-[8px] font-bold">✓ ग्राम पंचायत सत्यापित</span>
                                    </div>
                                    <div class="bg-white p-2 rounded-xl border border-[#cbd5e1]">
                                        <span class="text-[#b45309] font-bold block">२. सीएससी वीएलई हब</span>
                                        <span class="text-[#334155] text-[9px] block truncate">${p.institutional_verification ? p.institutional_verification.stage_2_tech_hub.hub : 'CSC Digital Kendra'}</span>
                                        <span class="text-[#047857] text-[8px] font-bold">✓ डिजिटल फोटो असिस्ट</span>
                                    </div>
                                    <div class="bg-white p-2 rounded-xl border border-[#cbd5e1]">
                                        <span class="text-[#15803d] font-bold block">३. भाषिणी (MeitY)</span>
                                        <span class="text-[#334155] text-[9px] block truncate">मातृभाषा बोली एआई</span>
                                        <span class="text-[#047857] text-[8px] font-bold">✓ बहुभाषी रूपांतरण</span>
                                    </div>
                                    <div class="bg-white p-2 rounded-xl border border-[#cbd5e1]">
                                        <span class="text-[#c2410c] font-bold block">४. SHG / APC संकलन</span>
                                        <span class="text-[#334155] text-[9px] block truncate">थोक बी२बी लॉट संचय</span>
                                        <span class="text-[#047857] text-[8px] font-bold">✓ गाँव डाकघर हब</span>
                                    </div>
                                    <div class="bg-white p-2 rounded-xl border border-[#cbd5e1]">
                                        <span class="text-[#7e22ce] font-bold block">५. SFURTI CFC लैब</span>
                                        <span class="text-[#334155] text-[9px] block truncate">Grade A+ • बारकोड</span>
                                        <span class="text-[#047857] text-[8px] font-bold">✓ निर्यात पैकेजिंग</span>
                                    </div>
                                    <div class="bg-white p-2 rounded-xl border border-[#cbd5e1]">
                                        <span class="text-[#be123c] font-bold block">६. RuTAG (IIT) व WSC</span>
                                        <span class="text-[#334155] text-[9px] block truncate">एर्गोनॉमिक टूल सुधार</span>
                                        <span class="text-[#047857] text-[8px] font-bold">✓ ट्रेंड्स फीडबैक लूप</span>
                                    </div>
                                </div>
                            </div>

                            <!-- 5. DIL SE DIL TAK: 2-Way Buyer Gratitude Wall -->"""

    if old_impact_section in html:
        html = html.replace(old_impact_section, new_gov_section, 1)
        print("[4] gov-section added.")
    else:
        print("[!] old_impact_section not matched.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Card patch complete.")

if __name__ == "__main__":
    main()
