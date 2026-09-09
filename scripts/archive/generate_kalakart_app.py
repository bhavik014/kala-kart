import sys

def build_template():
    return '''<!DOCTYPE html>
<html lang="hi" class="h-full bg-[#f6f1e9]">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kala Kart — पुश्तैनी हस्तशिल्प बाज़ार व कारीगर कार्यशाला</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Rozha+One&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Courier+Prime:ital,wght@0,400;0,700;1,400&display=swap');
        
        body { 
            font-family: 'Plus Jakarta Sans', sans-serif; 
            background-color: #f6f1e9;
            background-image: radial-gradient(#d4a373 0.6px, transparent 0.6px);
            background-size: 20px 20px;
            color: #2b2d42;
        }
        
        .font-vintage { font-family: 'Rozha One', serif; }
        .font-stamp { font-family: 'Courier Prime', monospace; }
        
        /* Indie Stamp & Wax Seal Effect */
        .stamp-badge {
            border: 2px dashed #b45309;
            background: #fefae0;
            box-shadow: 3px 3px 0px #c2593f;
            transform: rotate(-1deg);
        }

        .gi-tag-stamp {
            border: 2px solid #b45309;
            background: #fefae0;
            position: relative;
            box-shadow: 2px 2px 0px #2b2d42;
        }
        
        .vintage-card {
            background: #fffcf7;
            border: 2px solid #e7d8c9;
            box-shadow: 5px 7px 0px #d4a373;
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }
        
        .vintage-card:hover {
            transform: translateY(-3px);
            box-shadow: 8px 12px 0px #c2593f;
            border-color: #c2593f;
        }

        /* Sound wave equalizer animation */
        .sound-wave-bar {
            display: inline-block;
            width: 3.5px;
            height: 14px;
            background: #c2593f;
            border-radius: 2px;
            animation: soundWave 0.9s ease-in-out infinite alternate;
        }
        @keyframes soundWave {
            0% { height: 4px; }
            100% { height: 18px; }
        }
    </style>
</head>
<body class="min-h-full flex flex-col selection:bg-[#fed7aa] selection:text-[#2b2d42]">

    <!-- ========================================================================= -->
    <!-- 1. FIRST SCREEN: DUAL ROLE GATEWAY (CARRIER / ARTISAN vs BUYER)           -->
    <!-- ========================================================================= -->
    <div id="gateway-screen" class="fixed inset-0 z-50 bg-[#f6f1e9] flex flex-col justify-between p-4 sm:p-8 overflow-y-auto">
        
        <!-- Top Bar with Language Selector -->
        <div class="max-w-5xl mx-auto w-full flex items-center justify-between gap-3 border-b border-dashed border-[#d4a373] pb-4">
            <div class="flex items-center gap-2">
                <span class="font-vintage text-2xl text-[#2b2d42]">Kala Kart</span>
                <span class="text-xs font-stamp font-bold text-[#c2593f] bg-[#fefae0] px-2 py-0.5 rounded border border-[#d4a373]">कला कार्ट • SIH26090</span>
            </div>

            <!-- Regional Language Switcher -->
            <div class="flex items-center gap-1.5 flex-wrap">
                <span class="text-[11px] font-stamp text-[#6c757d] mr-1 hidden sm:inline">मातृभाषा:</span>
                <button onclick="setLanguage('hi')" id="lang-btn-hi" class="px-2.5 py-1 text-xs font-bold rounded-lg border border-[#b45309] bg-[#b45309] text-white">हिन्दी</button>
                <button onclick="setLanguage('bn')" id="lang-btn-bn" class="px-2.5 py-1 text-xs font-bold rounded-lg border border-[#d4a373] bg-white text-[#2b2d42] hover:bg-[#faedcd]">বাংলা</button>
                <button onclick="setLanguage('mr')" id="lang-btn-mr" class="px-2.5 py-1 text-xs font-bold rounded-lg border border-[#d4a373] bg-white text-[#2b2d42] hover:bg-[#faedcd]">मराठी</button>
                <button onclick="setLanguage('ta')" id="lang-btn-ta" class="px-2.5 py-1 text-xs font-bold rounded-lg border border-[#d4a373] bg-white text-[#2b2d42] hover:bg-[#faedcd]">தமிழ்</button>
                <button onclick="setLanguage('te')" id="lang-btn-te" class="px-2.5 py-1 text-xs font-bold rounded-lg border border-[#d4a373] bg-white text-[#2b2d42] hover:bg-[#faedcd]">తెలుగు</button>
                <button onclick="setLanguage('en')" id="lang-btn-en" class="px-2.5 py-1 text-xs font-bold rounded-lg border border-[#d4a373] bg-white text-[#2b2d42] hover:bg-[#faedcd]">English</button>
            </div>
        </div>

        <!-- Main Gateway Choice -->
        <div class="max-w-5xl mx-auto w-full my-auto py-8">
            <div class="text-center max-w-2xl mx-auto mb-8">
                <span class="stamp-badge px-3 py-1 text-xs font-stamp font-bold uppercase text-[#c2593f] inline-block mb-3">
                    भारतीय ग्रामीण वॉइस-टू-कॉमर्स मंच
                </span>
                <h1 id="gateway-title" class="font-vintage text-3xl sm:text-5xl text-[#2b2d42] tracking-tight">
                    कला कार्ट में आपका स्वागत है
                </h1>
                <p id="gateway-sub" class="text-xs sm:text-sm text-[#6c757d] font-stamp mt-2 leading-relaxed">
                    कृपया अपनी भूमिका का चयन करें: आप कारीगर के रूप में अपना काम करना चाहते हैं, या सीधे हस्तशिल्प खरीदना चाहते हैं?
                </p>
            </div>

            <!-- Two Distinct Interfaces Cards -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
                
                <!-- CARD 1: ARTISAN ENTRY (कारीगर प्रवेश) -->
                <div class="vintage-card p-6 sm:p-8 rounded-3xl flex flex-col justify-between relative overflow-hidden bg-[#fffdfa]">
                    <div class="absolute top-0 right-0 w-24 h-24 bg-[#fed7aa]/30 rounded-bl-full pointer-events-none"></div>
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <span class="w-12 h-12 rounded-2xl bg-[#c2593f] text-white flex items-center justify-center text-xl shadow-[2px_2px_0px_#2b2d42]">
                                🧕
                            </span>
                            <span class="text-[10px] font-stamp font-bold text-[#047857] bg-[#ecfdf5] px-2.5 py-1 rounded-full border border-[#a7f3d0]">
                                PM-AJAY • PM Vishwakarma
                            </span>
                        </div>
                        <h3 class="font-vintage text-2xl text-[#2b2d42] mb-2">१. कारीगर कार्यशाला (Artisan Hub)</h3>
                        <p class="text-xs text-[#4a4e69] leading-relaxed mb-4">
                            १० सेकंड अपनी बोली में बोलकर स्टूडियो कैटलॉग बनाएं, स्वयं सहायता समूह (SHG) से कच्चा माल थोक में खरीदें और स्पीड पोस्ट पिकअप शेड्यूल करें।
                        </p>

                        <!-- Quick Artisan Login Options -->
                        <div class="space-y-2.5 pt-2 border-t border-dashed border-[#d4a373]">
                            <!-- PM Vishwakarma 1-Tap -->
                            <div class="flex gap-2">
                                <input type="text" id="gw-vishwakarma-id" value="PMV-BH-88214" placeholder="PM Vishwakarma ID" class="flex-1 px-3 py-2 text-xs font-mono font-bold bg-white border border-[#d4a373] rounded-xl">
                                <button onclick="handleGatewayVishwakarmaLogin()" class="px-3 py-2 bg-[#1e3a8a] text-white text-xs font-bold rounded-xl shadow-[2px_2px_0px_#2b2d42] hover:bg-[#172554]">
                                    सत्यापित करें
                                </button>
                            </div>

                            <!-- Mobile OTP Option -->
                            <div class="flex gap-2">
                                <input type="tel" id="gw-phone" value="9876543210" placeholder="मोबाइल नंबर" class="flex-1 px-3 py-2 text-xs bg-white border border-[#d4a373] rounded-xl">
                                <button onclick="speakArtisanOTP()" class="px-2.5 py-2 bg-[#fefae0] text-[#b45309] border border-[#b45309] text-xs font-stamp font-bold rounded-xl hover:bg-[#faedcd]">
                                    OTP सुनें
                                </button>
                                <button onclick="handleGatewayPhoneLogin()" class="px-3 py-2 bg-[#c2593f] text-white text-xs font-bold rounded-xl shadow-[2px_2px_0px_#2b2d42] hover:bg-[#a6472e]">
                                    प्रवेश
                                </button>
                            </div>

                            <!-- Get Registered Link (For non-Vishwakarma) -->
                            <div class="pt-2 text-center">
                                <button onclick="openRegisterModal()" class="text-xs font-stamp font-bold text-[#b45309] hover:underline flex items-center justify-center gap-1 mx-auto">
                                    <span>👉 विश्वकर्मा आईडी नहीं है? नया पंजीकरण करें (Get Registered)</span>
                                </button>
                            </div>
                        </div>
                    </div>

                    <button onclick="enterAsArtisan()" class="mt-6 w-full py-3.5 bg-[#2b2d42] hover:bg-[#1e1b4b] text-[#fefae0] font-bold text-xs font-stamp uppercase tracking-wider rounded-xl shadow-[3px_3px_0px_#c2593f] transition flex items-center justify-center gap-2">
                        <i data-lucide="wrench" class="w-4 h-4 text-[#fed7aa]"></i>
                        <span>कारीगर कार्यशाला में प्रवेश करें</span>
                    </button>
                </div>

                <!-- CARD 2: BUYER ENTRY (खरीदार प्रवेश / बाज़ार) -->
                <div class="vintage-card p-6 sm:p-8 rounded-3xl flex flex-col justify-between relative overflow-hidden bg-[#fffdfa]">
                    <div class="absolute top-0 right-0 w-24 h-24 bg-[#a7f3d0]/30 rounded-bl-full pointer-events-none"></div>
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <span class="w-12 h-12 rounded-2xl bg-[#047857] text-white flex items-center justify-center text-xl shadow-[2px_2px_0px_#2b2d42]">
                                🛍️
                            </span>
                            <span class="text-[10px] font-stamp font-bold text-[#c2593f] bg-[#fefae0] px-2.5 py-1 rounded-full border border-[#fed7aa]">
                                १००% बिचौलिया-मुक्त बाज़ार
                            </span>
                        </div>
                        <h3 class="font-vintage text-2xl text-[#2b2d42] mb-2">२. ग्राहक दस्तकार बाज़ार (Buyer Marketplace)</h3>
                        <p class="text-xs text-[#4a4e69] leading-relaxed mb-4">
                            भारत के दूरदराज गाँवों से सीधे असली हस्तशिल्प खरीदें। आपकी खरीद का ८५%+ पारिश्रमिक बिना किसी दलाल के सीधे ग्रामीण शिल्पकार के बैंक खाते में जाता है।
                        </p>

                        <!-- Highlights List -->
                        <div class="space-y-2 pt-2 border-t border-dashed border-[#d4a373] text-xs font-stamp text-[#6c757d]">
                            <div class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-[#047857]"></i>
                                <span>कारीगर की मातृभाषा में मूल कहानी सुनें (भाषिणी AI)</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-[#047857]"></i>
                                <span>SFURTI Grade A+ लैब व GI टैग प्रमाणित उत्पाद</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-[#047857]"></i>
                                <span>भारतीय डाक स्पीड पोस्ट से गाँव से सीधा आपके घर प्रेषण</span>
                            </div>
                        </div>
                    </div>

                    <button onclick="enterAsBuyer()" class="mt-6 w-full py-3.5 bg-[#047857] hover:bg-[#065f46] text-white font-bold text-xs font-stamp uppercase tracking-wider rounded-xl shadow-[3px_3px_0px_#2b2d42] transition flex items-center justify-center gap-2">
                        <i data-lucide="shopping-bag" class="w-4 h-4 text-white"></i>
                        <span>सीधे बाज़ार में प्रवेश करें (Enter Marketplace)</span>
                    </button>
                </div>

            </div>
        </div>

        <div class="text-center text-[11px] font-stamp text-[#6c757d] border-t border-dashed border-[#d4a373] pt-3">
            Kala Kart • PM Vishwakarma, Ministry of Social Justice & Empowerment, Bhashini (MeitY) व भारतीय डाक समर्थित
        </div>
    </div>

    <!-- ========================================================================= -->
    <!-- 2. MAIN NAVIGATION HEADER (VISIBLE AFTER GATEWAY)                          -->
    <!-- ========================================================================= -->
    <header class="sticky top-0 z-40 bg-[#fffcf7]/95 backdrop-blur-md border-b-2 border-[#d4a373] shadow-xs">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-3">
            
            <!-- Brand & Tag -->
            <div class="flex items-center gap-3">
                <a href="javascript:void(0)" onclick="openGateway()" class="flex items-baseline gap-2">
                    <span class="font-vintage text-2xl sm:text-3xl text-[#2b2d42] tracking-wide">Kala Kart</span>
                    <span id="header-brand-sub" class="text-xs font-stamp font-bold text-[#c2593f]">कला कार्ट</span>
                </a>
                <span class="hidden sm:inline-flex stamp-badge px-2 py-0.5 text-[10px] font-stamp font-bold text-[#c2593f]">
                    SIH26090
                </span>
            </div>

            <!-- Role Switcher & Active View Indicator -->
            <div class="flex items-center gap-2">
                <!-- Switch View Buttons -->
                <button onclick="switchView('artisan')" id="nav-switch-artisan" class="px-3 py-1.5 rounded-xl text-xs font-stamp font-bold transition flex items-center gap-1.5 border border-[#d4a373] bg-[#fefae0] text-[#b45309] hover:bg-[#faedcd]">
                    <i data-lucide="wrench" class="w-3.5 h-3.5"></i>
                    <span id="nav-artisan-label">कारीगर कार्यशाला</span>
                </button>

                <button onclick="switchView('buyer')" id="nav-switch-buyer" class="px-3 py-1.5 rounded-xl text-xs font-stamp font-bold transition flex items-center gap-1.5 border border-[#047857] bg-[#047857] text-white hover:bg-[#065f46]">
                    <i data-lucide="shopping-bag" class="w-3.5 h-3.5"></i>
                    <span id="nav-buyer-label">दस्तकार बाज़ार</span>
                </button>

                <!-- Language Button -->
                <button onclick="openGatewayLanguage()" class="p-2 rounded-xl text-[#2b2d42] bg-[#fefae0] border border-[#d4a373] hover:bg-[#faedcd] transition" title="भाषा बदलें">
                    <i data-lucide="languages" class="w-4 h-4 text-[#c2593f]"></i>
                </button>
            </div>

        </div>
    </header>

    <!-- ========================================================================= -->
    <!-- 3. INTERFACE A: ARTISAN WORKSPACE (कारीगर कार्यशाला)                        -->
    <!-- ========================================================================= -->
    <div id="view-artisan" class="hidden flex-1 max-w-6xl w-full mx-auto px-4 sm:px-6 py-6 space-y-6">
        
        <!-- Artisan Profile & Verification Badge Banner -->
        <div class="vintage-card p-6 rounded-3xl bg-[#fffdfa] border-2 border-[#b45309]">
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div class="flex items-center gap-4">
                    <div class="w-16 h-16 rounded-2xl bg-[#faedcd] border-2 border-[#b45309] flex items-center justify-center text-3xl shadow">
                        🧕
                    </div>
                    <div>
                        <div class="flex items-center gap-2 flex-wrap">
                            <h2 class="font-vintage text-2xl text-[#2b2d42]" id="artisan-dash-name">रामवती देवी (Kala Sadheka)</h2>
                            <span class="px-2.5 py-0.5 rounded-full text-[10px] font-stamp font-bold bg-[#ecfdf5] text-[#047857] border border-[#a7f3d0]" id="artisan-dash-status">
                                ✓ ग्राम पंचायत सत्यापित
                            </span>
                        </div>
                        <p class="text-xs font-stamp text-[#6c757d] mt-1" id="artisan-dash-details">
                            रंती ग्राम पंचायत, मधुबनी, बिहार • PM Vishwakarma ID: PMV-BH-88214
                        </p>
                    </div>
                </div>

                <div class="flex items-center gap-4 text-right">
                    <div class="bg-[#fefae0] p-3 rounded-2xl border border-[#d4a373]">
                        <span class="text-[10px] font-stamp text-[#6c757d] block">सीधी बैंक आय (DBT)</span>
                        <span class="font-vintage text-xl text-[#047857]" id="artisan-dash-earnings">₹42,850</span>
                    </div>
                    <button onclick="artisanLogout()" class="px-3 py-2 bg-[#f5f5f4] hover:bg-[#e7e5e4] text-[#6c757d] text-xs font-stamp rounded-xl border border-[#d6d3d1]">
                        लॉगआउट
                    </button>
                </div>
            </div>
        </div>

        <!-- 4 Primary Artisan Work Pillars -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            
            <!-- Work Tool 1: 10-Second Voice Studio -->
            <div class="vintage-card p-5 rounded-2xl flex flex-col justify-between">
                <div>
                    <div class="w-10 h-10 rounded-xl bg-[#c2593f] text-white flex items-center justify-center mb-3 shadow">
                        <i data-lucide="mic" class="w-5 h-5"></i>
                    </div>
                    <h4 class="font-vintage text-lg text-[#2b2d42]">१० सेकंड स्टूडियो</h4>
                    <p class="text-xs text-[#6c757d] mt-1 leading-relaxed">
                        अपनी मातृभाषा में बोलकर नया हस्तशिल्प जोड़ें। एआई फोटो चमकाएगा और विवरण लिखेगा।
                    </p>
                </div>
                <button onclick="toggleModal('studio-modal')" class="mt-4 w-full py-2.5 bg-[#c2593f] hover:bg-[#a6472e] text-white text-xs font-bold rounded-xl shadow transition">
                    + नया शिल्प जोड़ें
                </button>
            </div>

            <!-- Work Tool 2: SHG Cluster Hub -->
            <div class="vintage-card p-5 rounded-2xl flex flex-col justify-between">
                <div>
                    <div class="w-10 h-10 rounded-xl bg-[#b45309] text-white flex items-center justify-center mb-3 shadow">
                        <i data-lucide="users-2" class="w-5 h-5"></i>
                    </div>
                    <h4 class="font-vintage text-lg text-[#2b2d42]">स्वयं सहायता समूह</h4>
                    <p class="text-xs text-[#6c757d] mt-1 leading-relaxed">
                        कला सखी दीदी को घर बुलाएँ, रेशम धागा थोक में ३६% सस्ता खरीदें या टूल फंड लें।
                    </p>
                </div>
                <button onclick="toggleModal('shg-modal')" class="mt-4 w-full py-2.5 bg-[#b45309] hover:bg-[#92400e] text-white text-xs font-bold rounded-xl shadow transition">
                    समूह केंद्र खोलें
                </button>
            </div>

            <!-- Work Tool 3: 6 Government Pillars -->
            <div class="vintage-card p-5 rounded-2xl flex flex-col justify-between">
                <div>
                    <div class="w-10 h-10 rounded-xl bg-[#1e3a8a] text-white flex items-center justify-center mb-3 shadow">
                        <i data-lucide="landmark" class="w-5 h-5"></i>
                    </div>
                    <h4 class="font-vintage text-lg text-[#2b2d42]">सरकारी सहायता ढाँचा</h4>
                    <p class="text-xs text-[#6c757d] mt-1 leading-relaxed">
                        पीएम विश्वकर्मा टूलकिट ₹15,000, SFURTI लैब ग्रेडिंग और आईआईटी RuTAG नवाचार।
                    </p>
                </div>
                <button onclick="toggleModal('ecosystem-modal')" class="mt-4 w-full py-2.5 bg-[#1e3a8a] hover:bg-[#172554] text-white text-xs font-bold rounded-xl shadow transition">
                    ६ स्तंभ देखें
                </button>
            </div>

            <!-- Work Tool 4: India Post Speed Post Dispatch -->
            <div class="vintage-card p-5 rounded-2xl flex flex-col justify-between">
                <div>
                    <div class="w-10 h-10 rounded-xl bg-[#047857] text-white flex items-center justify-center mb-3 shadow">
                        <i data-lucide="truck" class="w-5 h-5"></i>
                    </div>
                    <h4 class="font-vintage text-lg text-[#2b2d42]">डाकघर पिकअप</h4>
                    <p class="text-xs text-[#6c757d] mt-1 leading-relaxed">
                        तैयार पार्सल के लिए ग्रामीण डाक सेवक (GDS) को अपने गाँव के घर या डिपो पर बुलाएँ।
                    </p>
                </div>
                <button onclick="requestIndiaPostPickup('art-101', 'मधुबनी सिल्क कैनवास')" class="mt-4 w-full py-2.5 bg-[#047857] hover:bg-[#065f46] text-white text-xs font-bold rounded-xl shadow transition">
                    पिकअप अनुरोध भेजें
                </button>
            </div>

        </div>

        <!-- Artisan's Live Products in Store -->
        <div class="pt-4 border-t border-dashed border-[#d4a373]">
            <div class="flex items-center justify-between mb-4">
                <h3 class="font-vintage text-xl text-[#2b2d42]">आपके सूचीबद्ध हस्तशिल्प (Live on Marketplace)</h3>
                <span class="text-xs font-stamp text-[#047857] font-bold">४ उत्पाद सक्रिय बाज़ार में हैं</span>
            </div>
            <div id="artisan-my-products-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                <!-- Filled by JS -->
            </div>
        </div>

    </div>

    <!-- ========================================================================= -->
    <!-- 4. INTERFACE B: BUYER MARKETPLACE (दस्तकार बाज़ार)                        -->
    <!-- ========================================================================= -->
    <div id="view-buyer" class="flex-1 max-w-6xl w-full mx-auto px-4 sm:px-6 py-6 space-y-6">
        
        <!-- Marketplace Category Filter Strip -->
        <div class="flex items-center justify-between gap-3 flex-wrap pb-3 border-b border-dashed border-[#d4a373]">
            <div class="flex items-center gap-2 overflow-x-auto pb-1">
                <button onclick="filterMarketplaceCategory('all')" id="bcat-all" class="bcat-pill active px-3.5 py-1.5 rounded-xl text-xs font-stamp font-bold bg-[#c2593f] text-white shadow-[2px_2px_0px_#2b2d42]">
                    सभी हस्तशिल्प
                </button>
                <button onclick="filterMarketplaceCategory('Handicrafts & Painting')" id="bcat-paint" class="bcat-pill px-3.5 py-1.5 rounded-xl text-xs font-stamp font-bold bg-[#fefae0] text-[#2b2d42] border border-[#d4a373] hover:bg-[#faedcd]">
                    मधुबनी चित्रकला
                </button>
                <button onclick="filterMarketplaceCategory('Pottery & Ceramics')" id="bcat-pottery" class="bcat-pill px-3.5 py-1.5 rounded-xl text-xs font-stamp font-bold bg-[#fefae0] text-[#2b2d42] border border-[#d4a373] hover:bg-[#faedcd]">
                    खुर्जा पॉटरी
                </button>
                <button onclick="filterMarketplaceCategory('Textiles & Weaving')" id="bcat-silk" class="bcat-pill px-3.5 py-1.5 rounded-xl text-xs font-stamp font-bold bg-[#fefae0] text-[#2b2d42] border border-[#d4a373] hover:bg-[#faedcd]">
                    भागलपुरी सिल्क
                </button>
                <button onclick="filterMarketplaceCategory('Woodcraft & Carving')" id="bcat-wood" class="bcat-pill px-3.5 py-1.5 rounded-xl text-xs font-stamp font-bold bg-[#fefae0] text-[#2b2d42] border border-[#d4a373] hover:bg-[#faedcd]">
                    सहारनपुर काष्ठ शिल्प
                </button>
            </div>

            <div class="text-xs font-stamp text-[#6c757d]">
                <span class="text-[#047857] font-bold">८५%+ सीधा कारीगर को</span> • १००% बिचौलिया-मुक्त
            </div>
        </div>

        <!-- Full Folk Vintage Marketplace Cards -->
        <div id="buyer-products-grid" class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- Rendered by JS -->
        </div>

    </div>

    <!-- ========================================================================= -->
    <!-- 5. MODALS & SUB-FLOWS                                                      -->
    <!-- ========================================================================= -->

    <!-- NEW ARTISAN REGISTRATION MODAL (For Artisans without Vishwakarma ID) -->
    <div id="register-modal" class="fixed inset-0 z-50 hidden bg-[#2b2d42]/80 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-[#fffdfa] rounded-3xl max-w-lg w-full p-6 sm:p-8 shadow-[10px_14px_0px_#047857] border-3 border-[#2b2d42] relative">
            <button onclick="toggleModal('register-modal')" class="absolute top-5 right-5 text-[#6c757d] hover:text-[#2b2d42] p-1">
                <i data-lucide="x" class="w-6 h-6"></i>
            </button>

            <div class="flex items-center gap-3 mb-4">
                <span class="w-10 h-10 rounded-xl bg-[#ecfdf5] text-[#047857] flex items-center justify-center font-bold text-lg border border-[#a7f3d0]">
                    🪪
                </span>
                <div>
                    <h3 class="font-vintage text-2xl text-[#2b2d42]">कारीगर नया पंजीकरण</h3>
                    <p class="text-xs font-stamp text-[#6c757d]">ग्राम पंचायत व पीएम विश्वकर्मा निःशुल्क सहायता</p>
                </div>
            </div>

            <p class="text-xs text-[#4a4e69] leading-relaxed mb-4 bg-[#fefae0] p-3 rounded-2xl border border-[#d4a373]">
                यदि आपके पास पीएम विश्वकर्मा आईडी नहीं है, तो अपना विवरण दर्ज करें। हम आपको तुरंत अस्थायी आईडी देंगे और स्थानीय <b>कला सखी / CSC VLE</b> आपके घर आकर बायोमेट्रिक व टूलकिट अनुदान पूरा करेंगे।
            </p>

            <form onsubmit="handleRegistrationSubmit(event)" class="space-y-3">
                <div>
                    <label class="block text-[11px] font-stamp font-bold text-[#2b2d42] uppercase mb-1">कारीगर का नाम *</label>
                    <input type="text" id="reg-name" required value="कमला देवी" class="w-full px-3.5 py-2 text-xs font-bold bg-[#f6f1e9] border border-[#d4a373] rounded-xl focus:bg-white focus:outline-none">
                </div>

                <div>
                    <label class="block text-[11px] font-stamp font-bold text-[#2b2d42] uppercase mb-1">शिल्प विधा / कार्य *</label>
                    <select id="reg-craft" class="w-full px-3.5 py-2 text-xs font-bold bg-[#f6f1e9] border border-[#d4a373] rounded-xl focus:bg-white focus:outline-none">
                        <option value="मधुबनी चित्रकला">मधुबनी चित्रकला (Madhubani Painting)</option>
                        <option value="पॉटरी व मिट्टी शिल्प">पॉटरी व मिट्टी शिल्प (Khurja Pottery)</option>
                        <option value="हस्तकरघा रेशम बुनाई">हस्तकरघा रेशम बुनाई (Handloom Silk)</option>
                        <option value="काष्ठ नक्काशी शिल्प">काष्ठ नक्काशी शिल्प (Woodcraft)</option>
                    </select>
                </div>

                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-[11px] font-stamp font-bold text-[#2b2d42] uppercase mb-1">ग्राम पंचायत *</label>
                        <input type="text" id="reg-panchayat" required value="रंती ग्राम पंचायत, बिहार" class="w-full px-3.5 py-2 text-xs font-bold bg-[#f6f1e9] border border-[#d4a373] rounded-xl focus:bg-white focus:outline-none">
                    </div>
                    <div>
                        <label class="block text-[11px] font-stamp font-bold text-[#2b2d42] uppercase mb-1">मोबाइल नंबर *</label>
                        <input type="tel" id="reg-phone" required value="9876543210" class="w-full px-3.5 py-2 text-xs font-bold bg-[#f6f1e9] border border-[#d4a373] rounded-xl focus:bg-white focus:outline-none">
                    </div>
                </div>

                <div class="flex items-start gap-2 pt-1">
                    <input type="checkbox" id="reg-assist" checked class="mt-0.5 rounded text-[#047857]">
                    <label for="reg-assist" class="text-[11px] text-[#4a4e69] leading-tight">
                        <b>कला सखी / CSC VLE सहायता:</b> घर आकर फोटो लेने व ₹15,000 टूलकिट फॉर्म भरने का अनुरोध करें।
                    </label>
                </div>

                <button type="submit" id="reg-btn" class="w-full py-3 bg-[#047857] hover:bg-[#065f46] text-white font-bold text-xs rounded-xl shadow-[2px_2px_0px_#2b2d42] transition mt-2">
                    पंजीकरण करें व कार्यशाला में जुड़ें (Get Registered)
                </button>
            </form>
            <div id="reg-feedback" class="hidden mt-3 p-2.5 bg-[#ecfdf5] border border-[#a7f3d0] rounded-xl text-xs font-bold text-[#065f46]"></div>
        </div>
    </div>

    <!-- SHG CLUSTER HUB MODAL -->
    <div id="shg-modal" class="fixed inset-0 z-50 hidden bg-[#2b2d42]/80 backdrop-blur-md flex items-center justify-center p-4">
        <div class="bg-[#fffdfa] rounded-3xl max-w-2xl w-full p-6 sm:p-8 shadow-[10px_16px_0px_#b45309] border-3 border-[#2b2d42] relative max-h-[90vh] overflow-y-auto">
            <button onclick="toggleModal('shg-modal')" class="absolute top-5 right-5 text-[#6c757d] hover:text-[#2b2d42] p-1">
                <i data-lucide="x" class="w-6 h-6"></i>
            </button>

            <div class="flex items-center gap-3.5 mb-6 border-b-2 border-dashed border-[#d4a373] pb-4">
                <div class="w-12 h-12 rounded-2xl bg-[#b45309] text-white flex items-center justify-center shadow-[3px_3px_0px_#2b2d42]">
                    <i data-lucide="users-2" class="w-6 h-6"></i>
                </div>
                <div>
                    <h3 class="font-vintage text-2xl text-[#2b2d42]">गंगा महिला स्वयं सहायता समूह</h3>
                    <p class="text-xs font-stamp text-[#6c757d]">क्लस्टर #14 • 18 महिला दस्तकार दीदियाँ • NRLM / PM-AJAY</p>
                </div>
            </div>

            <div class="space-y-4 text-xs">
                <!-- Pillar 1: Kala Sakhi Doorstep -->
                <div class="p-4 bg-white rounded-2xl border-2 border-[#d4a373] shadow-[3px_3px_0px_#d4a373]">
                    <div class="flex items-center justify-between mb-2">
                        <b class="font-vintage text-base text-[#2b2d42]">🧕 कला सखी दीदी ऑनबोर्डिंग सहायता</b>
                        <span class="text-[10px] font-stamp text-[#047857] font-bold">सुनीता दीदी (मास्टर ट्रेनर)</span>
                    </div>
                    <p class="text-[#4a4e69] leading-relaxed mb-3">
                        स्मार्टफोन न होने पर कला सखी दीदी अपने समूह फोन से आपके घर आकर बोलचाल और फोटो कैटलॉग तैयार करेंगी।
                    </p>
                    <button onclick="requestKalaSakhi()" class="px-3.5 py-2 bg-[#c2593f] text-white font-bold rounded-xl shadow-[2px_2px_0px_#2b2d42]">
                        कला सखी दीदी को घर बुलाएँ
                    </button>
                    <div id="sakhi-fb" class="hidden mt-2 p-2 bg-[#ecfdf5] text-[#065f46] font-bold rounded-xl"></div>
                </div>

                <!-- Pillar 2: Bulk Raw Materials -->
                <div class="p-4 bg-[#fefae0] rounded-2xl border-2 border-[#b45309] shadow-[3px_3px_0px_#b45309]">
                    <div class="flex items-center justify-between mb-2">
                        <b class="font-vintage text-base text-[#2b2d42]">📦 सामूहिक कच्चा माल थोक खरीद</b>
                        <span class="text-xs font-bold text-[#047857] bg-white px-2 py-0.5 rounded">36% सीधी बचत</span>
                    </div>
                    <p class="text-[#4a4e69] leading-relaxed mb-3">
                        भागलपुरी तुषार सिल्क यार्न: थोक समूह दर <b>₹1,150/kg</b> (फुटकर बाज़ार दर: <s>₹1,800/kg</s>)।
                    </p>
                    <button onclick="joinBulkRawMaterials()" class="px-3.5 py-2 bg-[#047857] text-white font-bold rounded-xl shadow-[2px_2px_0px_#2b2d42]">
                        सामूहिक आर्डर में जुड़ें (-₹3,250 बचत)
                    </button>
                    <div id="bulk-fb" class="hidden mt-2 p-2 bg-white text-[#047857] font-bold rounded-xl"></div>
                </div>
            </div>
        </div>
    </div>

    <!-- 6-STAGE GOVT ECOSYSTEM MODAL -->
    <div id="ecosystem-modal" class="fixed inset-0 z-50 hidden bg-[#2b2d42]/80 backdrop-blur-md flex items-center justify-center p-4">
        <div class="bg-[#fffdfa] rounded-3xl max-w-3xl w-full p-6 sm:p-8 shadow-[10px_16px_0px_#1e3a8a] border-3 border-[#2b2d42] relative max-h-[90vh] overflow-y-auto">
            <button onclick="toggleModal('ecosystem-modal')" class="absolute top-5 right-5 text-[#6c757d] hover:text-[#2b2d42] p-1">
                <i data-lucide="x" class="w-6 h-6"></i>
            </button>

            <div class="flex items-center gap-3.5 mb-6 border-b-2 border-dashed border-[#d4a373] pb-4">
                <div class="w-12 h-12 rounded-2xl bg-[#1e3a8a] text-white flex items-center justify-center shadow-[3px_3px_0px_#2b2d42]">
                    <i data-lucide="landmark" class="w-6 h-6"></i>
                </div>
                <div>
                    <h3 class="font-vintage text-2xl text-[#2b2d42]">राष्ट्रीय संस्थागत व सरकारी सहायता ढाँचा</h3>
                    <p class="text-xs font-stamp text-[#6c757d]">६ मंत्रालयों व योजनाओं का ग्रामीण कारीगरों से सीधा जुड़ाव</p>
                </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                <div class="p-3 bg-white rounded-xl border border-[#d4a373]">
                    <b class="text-[#1e3a8a] block font-vintage text-sm">१. पीएम विश्वकर्मा व ग्राम पंचायत</b>
                    <span class="text-[#4a4e69] text-[11px] mt-1 block">शून्य फर्जी विक्रेता • सीधा नेशनल पोर्टल से सत्यापित आईडी</span>
                </div>
                <div class="p-3 bg-white rounded-xl border border-[#d4a373]">
                    <b class="text-[#b45309] block font-vintage text-sm">२. CSC कॉमन सर्विस सेंटर व VLE</b>
                    <span class="text-[#4a4e69] text-[11px] mt-1 block">बिना स्मार्टफोन वाले शिल्पकारों हेतु गाँव में डिजिटल फोटो सहायता</span>
                </div>
                <div class="p-3 bg-white rounded-xl border border-[#d4a373]">
                    <b class="text-[#047857] block font-vintage text-sm">३. भाषिणी (MeitY) वॉइस एआई</b>
                    <span class="text-[#4a4e69] text-[11px] mt-1 block">स्थानीय ग्रामीण बोलियों का बहुभाषी उत्पाद विवरण में स्वतः रूपांतरण</span>
                </div>
                <div class="p-3 bg-white rounded-xl border border-[#d4a373]">
                    <b class="text-[#c2410c] block font-vintage text-sm">४. महिला SHG व APC संकलन</b>
                    <span class="text-[#4a4e69] text-[11px] mt-1 block">थोक बी२बी आर्डर पूर्ति व गाँव स्तर पर एकल डाकघर संकलन केंद्र</span>
                </div>
                <div class="p-3 bg-white rounded-xl border border-[#d4a373]">
                    <b class="text-[#7e22ce] block font-vintage text-sm">५. SFURTI कॉमन फैसिलिटी सेंटर्स</b>
                    <span class="text-[#4a4e69] text-[11px] mt-1 block">Grade A+ गुणवत्ता जांच, बारकोड टैगिंग व सुरक्षित निर्यात पैकेजिंग</span>
                </div>
                <div class="p-3 bg-white rounded-xl border border-[#d4a373]">
                    <b class="text-[#be123c] block font-vintage text-sm">६. RuTAG (IITs) व बुनकर सेवा केंद्र</b>
                    <span class="text-[#4a4e69] text-[11px] mt-1 block">बाज़ार मांग का सीधा फीडबैक लूप और एर्गोनॉमिक औजार नवाचार</span>
                </div>
            </div>
        </div>
    </div>

    <!-- VOICE STUDIO MODAL -->
    <div id="studio-modal" class="fixed inset-0 z-50 hidden bg-[#2b2d42]/80 backdrop-blur-md flex items-center justify-center p-4">
        <div class="bg-[#fffdfa] rounded-3xl max-w-lg w-full p-6 sm:p-8 shadow-[10px_14px_0px_#c2593f] border-3 border-[#2b2d42] relative">
            <button onclick="toggleModal('studio-modal')" class="absolute top-5 right-5 text-[#6c757d] hover:text-[#2b2d42] p-1">
                <i data-lucide="x" class="w-6 h-6"></i>
            </button>

            <div class="text-center mb-5">
                <span class="w-12 h-12 rounded-2xl bg-[#c2593f] text-white inline-flex items-center justify-center text-xl shadow mb-2">
                    🎙️
                </span>
                <h3 class="font-vintage text-2xl text-[#2b2d42]">१० सेकंड वॉइस स्टूडियो</h3>
                <p class="text-xs font-stamp text-[#6c757d]">अपनी बोली में बोलें, भाषिणी एआई कैटलॉग तैयार करेगा</p>
            </div>

            <form onsubmit="handleStudioSubmit(event)" class="space-y-4">
                <div>
                    <label class="block text-xs font-stamp text-[#2b2d42] uppercase font-bold mb-1">शिल्प की कच्ची तस्वीर</label>
                    <input type="file" id="studio-photo" accept="image/*" class="w-full text-xs font-bold text-[#6c757d] file:mr-3 file:py-2 file:px-4 file:rounded-xl file:border-0 file:text-xs file:font-bold file:bg-[#fefae0] file:text-[#b45309] hover:file:bg-[#faedcd]">
                </div>

                <div class="p-4 bg-[#fefae0] border-2 border-dashed border-[#b45309] rounded-2xl text-center">
                    <button type="button" onclick="toggleVoiceRecord()" id="voice-rec-btn" class="w-14 h-14 rounded-full bg-[#c2593f] text-white inline-flex items-center justify-center shadow hover:scale-105 transition">
                        <i data-lucide="mic" class="w-6 h-6"></i>
                    </button>
                    <span id="voice-status-text" class="block text-xs font-stamp font-bold text-[#b45309] mt-2">माइक दबाएँ और १० सेकंड बोलें</span>
                </div>

                <button type="submit" class="w-full py-3 bg-[#2b2d42] hover:bg-[#1e1b4b] text-[#fefae0] font-bold text-xs rounded-xl shadow-[2px_2px_0px_#c2593f] transition">
                    कैटलॉग तैयार करें व बाज़ार में जोड़ें
                </button>
            </form>
        </div>
    </div>

    <!-- DIL SE DIL TAK GRATITUDE MODAL -->
    <div id="gratitude-modal" class="fixed inset-0 z-50 hidden bg-[#2b2d42]/75 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-[#fffcf7] rounded-3xl max-w-lg w-full p-6 sm:p-8 shadow-[8px_12px_0px_#c2593f] border-2 border-[#2b2d42] relative">
            <button onclick="toggleModal('gratitude-modal')" class="absolute top-5 right-5 text-[#6c757d] hover:text-[#2b2d42] p-1">
                <i data-lucide="x" class="w-6 h-6"></i>
            </button>

            <div class="flex items-center gap-3 mb-4">
                <div class="w-12 h-12 rounded-2xl bg-[#fee2e2] text-[#c2593f] border border-[#fca5a5] flex items-center justify-center shadow">
                    <i data-lucide="heart" class="w-6 h-6 fill-[#c2593f]"></i>
                </div>
                <div>
                    <h3 class="font-vintage text-2xl text-[#2b2d42]">दिल से दिल तक • धन्यवाद संदेश</h3>
                    <p class="text-xs font-stamp text-[#6c757d]">To: <b id="gratitude-artisan-name" class="text-[#c2593f]">कारीगर</b></p>
                </div>
            </div>

            <p class="text-xs text-[#4a4e69] leading-relaxed mb-4 font-serif italic bg-[#fefae0] p-3 rounded-2xl border border-[#d4a373]">
                "आपका यह छोटा सा धन्यवाद संदेश सीधा ग्रामीण डाकघर साउंडबॉक्स पर गूंजेगा और कारीगर के चेहरे पर सच्ची मुस्कान लाएगा।"
            </p>

            <form onsubmit="handleGratitudeSubmit(event)" class="space-y-3">
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-[10px] font-stamp font-bold text-[#2b2d42] uppercase mb-1">आपका नाम</label>
                        <input type="text" id="gratitude-buyer-name" required value="अनामिका शर्मा" class="w-full px-3 py-2 text-xs bg-[#f6f1e9] border border-[#d4a373] rounded-xl focus:bg-white focus:outline-none">
                    </div>
                    <div>
                        <label class="block text-[10px] font-stamp font-bold text-[#2b2d42] uppercase mb-1">शहर</label>
                        <input type="text" id="gratitude-buyer-city" required value="Bengaluru" class="w-full px-3 py-2 text-xs bg-[#f6f1e9] border border-[#d4a373] rounded-xl focus:bg-white focus:outline-none">
                    </div>
                </div>

                <div>
                    <label class="block text-[10px] font-stamp font-bold text-[#2b2d42] uppercase mb-1">धन्यवाद संदेश</label>
                    <textarea id="gratitude-buyer-msg" rows="2" required class="w-full px-3 py-2 text-xs bg-[#f6f1e9] border border-[#d4a373] rounded-xl focus:bg-white focus:outline-none">दीदी, आपकी कला हमारे घर के मुख्य द्वार पर बहुत सुंदर लग रही है!</textarea>
                </div>

                <button type="submit" class="w-full py-2.5 bg-[#c2593f] hover:bg-[#a6472e] text-white font-bold text-xs rounded-xl shadow-[2px_2px_0px_#2b2d42] transition">
                    💌 संदेश भेजें
                </button>
            </form>
        </div>
    </div>

    <!-- POSTAL TAG MODAL -->
    <div id="postal-tag-modal" class="fixed inset-0 z-50 hidden bg-[#2b2d42]/80 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-[#fefae0] rounded-3xl max-w-md w-full p-6 shadow-[8px_12px_0px_#b45309] border-3 border-[#b45309] relative">
            <button onclick="toggleModal('postal-tag-modal')" class="absolute top-5 right-5 text-[#6c757d] hover:text-[#2b2d42] p-1">
                <i data-lucide="x" class="w-6 h-6"></i>
            </button>

            <div class="border-b-2 border-dashed border-[#b45309] pb-3 mb-4 text-center">
                <span class="text-xs font-stamp font-bold text-[#b45309] block">भारतीय डाक • SPEED POST PARCEL TAG</span>
                <h3 class="font-vintage text-xl text-[#2b2d42]">पार्सल रसीद व प्रमाण पत्र</h3>
            </div>

            <div class="space-y-2.5 text-xs font-stamp text-[#2b2d42]">
                <div class="flex justify-between">
                    <span>स्पीड पोस्ट ट्रैकिंग:</span>
                    <b class="text-[#047857]" id="tag-tracking-num">SP-IND-884912</b>
                </div>
                <div class="flex justify-between">
                    <span>शिल्पकार:</span>
                    <b id="tag-artisan-name">रामवती देवी</b>
                </div>
                <div class="flex justify-between">
                    <span>ग्राम पंचायत:</span>
                    <span id="tag-panchayat">रंती, मधुबनी (बिहार)</span>
                </div>
                <div class="flex justify-between">
                    <span>SFURTI CFC मुहर:</span>
                    <b class="text-[#1e3a8a]">Grade A+ Certified</b>
                </div>
            </div>

            <div class="mt-4 p-3 bg-white rounded-xl border border-[#d4a373] text-center">
                <span class="text-[10px] font-stamp text-[#6c757d] block">अंगूठा निशान व डिजिटल मुहर</span>
                <span class="text-xl">👍</span>
                <span class="text-[10px] font-stamp text-[#047857] block font-bold mt-1">शिल्पकार प्रामाणिकता सत्यापित</span>
            </div>
        </div>
    </div>

    <!-- ========================================================================= -->
    <!-- 6. JAVASCRIPT APP STATE & LOGIC                                           -->
    <!-- ========================================================================= -->
    <script>
        let currentLang = 'hi';
        let currentView = 'buyer'; // 'artisan' or 'buyer'
        let cachedProducts = [];
        let currentArtisan = null;
        let isRecording = false;

        // Fetch products from backend
        async function fetchProducts() {
            try {
                const res = await fetch('/api/products');
                const data = await res.json();
                cachedProducts = data.products || [];
                renderAllProductViews();
            } catch (err) {
                console.error("Error fetching products:", err);
            }
        }

        // Render both Artisan My-Products & Buyer Full Marketplace Cards
        function renderAllProductViews() {
            renderBuyerMarketplace(cachedProducts);
            renderArtisanProducts(cachedProducts);
            lucide.createIcons();
        }

        // Render Buyer Marketplace Cards (The rich folk vintage cards user loves)
        function renderBuyerMarketplace(products) {
            const container = document.getElementById('buyer-products-grid');
            if (!container) return;

            container.innerHTML = products.map(p => {
                const title = p.title;
                const story = currentLang === 'hi' ? p.story_hi : p.story_en;
                const voiceScript = p.raw_voice_transcript || story;
                const lifecycle = p.craft_lifecycle || [];
                const impact = p.family_impact || {};
                const gratitude = p.buyer_gratitude && p.buyer_gratitude[0] ? p.buyer_gratitude[0] : null;

                return `
                <div class="vintage-card rounded-3xl overflow-hidden flex flex-col justify-between">
                    <!-- Card Media Header -->
                    <div class="relative bg-[#f6f1e9] aspect-[16/10] overflow-hidden">
                        <img src="${p.studio_image_url || p.raw_image_url}" alt="${title}" class="w-full h-full object-cover">
                        
                        <!-- GI Tag Stamp -->
                        <div class="gi-tag-stamp absolute top-3 left-3 px-2.5 py-1 text-[10px] font-stamp font-bold text-[#c2593f] flex items-center gap-1 shadow">
                            <i data-lucide="shield-check" class="w-3.5 h-3.5"></i>
                            <span>${p.gi_tag_no || 'GI प्रमाणित'}</span>
                        </div>

                        <!-- SFURTI CFC Stamp -->
                        <div class="absolute top-3 right-3 bg-[#1e3a8a] text-white px-2 py-0.5 rounded-lg text-[9px] font-stamp font-bold shadow flex items-center gap-1">
                            <i data-lucide="award" class="w-3 h-3 text-[#bfdbfe]"></i>
                            <span>SFURTI CFC Grade A+</span>
                        </div>

                        <!-- Direct Wage Share Badge -->
                        <div class="absolute bottom-3 right-3 bg-[#2b2d42] text-[#fefae0] px-2.5 py-1 rounded-xl text-[10px] font-stamp font-bold shadow flex items-center gap-1">
                            <i data-lucide="check" class="w-3.5 h-3.5 text-[#a7f3d0]"></i>
                            <span>८५%+ सीधा कारीगर को</span>
                        </div>

                        <!-- Thumbprint Seal Badge -->
                        <div class="absolute bottom-3 left-3 bg-[#fff5f5] text-[#991b1b] border border-[#991b1b] px-2 py-0.5 rounded-lg text-[10px] font-stamp font-bold shadow">
                            अंगूठा निशान प्रमाणित
                        </div>
                    </div>

                    <!-- Card Body -->
                    <div class="p-5 flex-1 flex flex-col justify-between space-y-3">
                        <div>
                            <div class="flex items-center justify-between mb-1.5 flex-wrap gap-1">
                                <span class="text-[10px] font-stamp font-bold uppercase text-[#c2593f] bg-[#fefae0] px-2 py-0.5 rounded border border-[#d4a373]">
                                    ${p.category}
                                </span>
                                <button onclick="toggleModal('shg-modal')" class="text-[10px] font-stamp text-[#047857] bg-[#ecfdf5] hover:bg-[#d1fae5] px-2 py-0.5 rounded border border-[#a7f3d0] font-bold flex items-center gap-1">
                                    🤝 गंगा SHG द्वारा प्रमाणित
                                </button>
                            </div>

                            <h3 class="font-vintage text-xl text-[#2b2d42] mb-1">${title}</h3>
                            <p class="text-xs text-[#4a4e69] leading-relaxed mb-3">${story}</p>
                            
                            <!-- Voice Player -->
                            <div class="flex items-center gap-3 p-2.5 bg-[#fefae0] border border-[#d4a373] rounded-2xl mb-3 shadow-[2px_2px_0px_#d4a373]">
                                <button onclick="playVoiceText('${voiceScript.replace(/'/g, "\\\\'")}')" class="w-9 h-9 rounded-full bg-[#c2593f] hover:bg-[#a6472e] text-white flex items-center justify-center shadow hover:scale-105 active:scale-95 transition flex-shrink-0">
                                    <i data-lucide="volume-2" class="w-4 h-4 ml-0.5"></i>
                                </button>
                                <div class="flex-1 min-w-0">
                                    <div class="flex items-center justify-between">
                                        <div class="flex items-center gap-1.5">
                                            <span class="text-xs font-bold text-[#2b2d42]">कारीगर की आवाज़</span>
                                            <span class="text-[9px] font-stamp font-bold text-[#1e3a8a] bg-[#eff6ff] px-1.5 py-0.5 rounded border border-[#bfdbfe]">भाषिणी MeitY AI</span>
                                        </div>
                                        <div class="flex items-center gap-0.5">
                                            <span class="sound-wave-bar" style="animation-delay: 0.1s"></span>
                                            <span class="sound-wave-bar" style="animation-delay: 0.3s"></span>
                                            <span class="sound-wave-bar" style="animation-delay: 0.2s"></span>
                                        </div>
                                    </div>
                                    <p class="text-[11px] text-[#6c757d] truncate font-serif italic">"${voiceScript}"</p>
                                </div>
                            </div>

                            <!-- Detail Toggles -->
                            <div class="flex items-center gap-2 mb-3">
                                <button onclick="toggleCardDetail('${p.id}', 'yatra')" class="px-2.5 py-1 text-[11px] font-stamp font-bold text-[#b45309] bg-[#fefae0] hover:bg-[#faedcd] border border-[#d4a373] rounded-xl transition flex items-center gap-1">
                                    <i data-lucide="compass" class="w-3.5 h-3.5 text-[#c2593f]"></i>
                                    <span>कला यात्रा (४ दिन)</span>
                                </button>
                                <button onclick="toggleCardDetail('${p.id}', 'impact')" class="px-2.5 py-1 text-[11px] font-stamp font-bold text-[#047857] bg-[#ecfdf5] hover:bg-[#d1fae5] border border-[#a7f3d0] rounded-xl transition flex items-center gap-1">
                                    <i data-lucide="heart" class="w-3.5 h-3.5 text-[#059669]"></i>
                                    <span>परिवार प्रभाव</span>
                                </button>
                                <button onclick="toggleModal('ecosystem-modal')" class="px-2.5 py-1 text-[11px] font-stamp font-bold text-[#1e3a8a] bg-[#eff6ff] hover:bg-[#dbeafe] border border-[#bfdbfe] rounded-xl transition flex items-center gap-1">
                                    <i data-lucide="landmark" class="w-3.5 h-3.5 text-[#1e3a8a]"></i>
                                    <span>६ सरकारी सत्यापन</span>
                                </button>
                            </div>

                            <!-- Collapsible Kala Yatra -->
                            <div id="yatra-section-${p.id}" class="hidden p-3 bg-[#f6f1e9] border border-[#e7d8c9] rounded-2xl mb-3">
                                <span class="text-[10px] font-stamp font-bold text-[#2b2d42] block mb-2">हस्तशिल्प निर्माण चक्र (Kala Yatra)</span>
                                <div class="grid grid-cols-2 gap-2 text-[10px]">
                                    ${lifecycle.map(s => `
                                        <div class="bg-white p-2 rounded-xl border border-[#d4a373]/40">
                                            <span class="font-stamp text-[#c2593f] font-bold block">${s.days} • ${s.step}</span>
                                            <span class="text-[#6c757d] block mt-0.5">${s.desc}</span>
                                        </div>
                                    `).join('')}
                                </div>
                            </div>

                            <!-- Collapsible Family Impact -->
                            <div id="impact-section-${p.id}" class="hidden p-3 bg-[#ecfdf5] border border-[#a7f3d0] rounded-2xl mb-3">
                                <div class="flex items-center justify-between text-xs font-bold text-[#065f46] mb-1">
                                    <span>${impact.beneficiary || 'परिवार'}</span>
                                    <span>${impact.goal_stat || ''}</span>
                                </div>
                                <p class="text-[11px] text-[#047857] mb-2">${impact.impact_story || ''}</p>
                                <div class="w-full bg-white h-2 rounded-full overflow-hidden">
                                    <div class="bg-[#059669] h-full" style="width: ${impact.progress_pct || 70}%"></div>
                                </div>
                            </div>

                            <!-- Gratitude Strip -->
                            <div class="p-2.5 bg-[#fefae0]/70 border border-dashed border-[#d4a373] rounded-2xl mb-2 flex items-center justify-between">
                                <div class="min-w-0 flex-1 pr-2">
                                    <span class="text-[10px] font-bold text-[#2b2d42] block">💌 दिल से दिल तक</span>
                                    <p class="text-[10px] text-[#4a4e69] truncate italic mt-0.5">
                                        "${gratitude ? gratitude.message : 'दीदी, आपकी कला बहुत सुंदर है!'}" — <b>${gratitude ? gratitude.buyer_name : 'ग्राहक'}</b>
                                    </p>
                                </div>
                                <button onclick="openGratitudeModal('${p.id}', '${p.artisan_name}')" class="px-2.5 py-1.5 bg-[#c2593f] hover:bg-[#a6472e] text-white text-[10px] font-bold rounded-xl shadow transition">
                                    धन्यवाद
                                </button>
                            </div>

                            <!-- Fair Wage Barometer -->
                            <div class="p-2.5 bg-[#f6f1e9] border border-[#e7d8c9] rounded-xl">
                                <div class="flex items-center justify-between text-[10px] font-stamp font-bold text-[#2b2d42] mb-1">
                                    <span>उचित पारिश्रमिक विभाजन</span>
                                    <span class="text-[#047857]">सीधा कारीगर को (८५%)</span>
                                </div>
                                <div class="w-full bg-[#e7d8c9] h-1.5 rounded-full overflow-hidden flex">
                                    <div class="bg-[#047857] h-full" style="width: 85%"></div>
                                    <div class="bg-[#d97706] h-full" style="width: 10%"></div>
                                    <div class="bg-[#4b5563] h-full" style="width: 5%"></div>
                                </div>
                            </div>
                        </div>

                        <!-- Card Action Footer -->
                        <div class="pt-3 border-t border-dashed border-[#d4a373] flex items-center justify-between gap-2">
                            <div>
                                <span class="text-[9px] font-stamp text-[#6c757d] block">उचित बाज़ार मूल्य</span>
                                <span class="font-vintage text-2xl text-[#2b2d42]">₹${p.suggested_price}</span>
                            </div>

                            <div class="flex items-center gap-1.5">
                                <button onclick="openPostalTag('${p.id}', '${p.artisan_name}')" class="px-2.5 py-2 bg-[#fefae0] text-[#b45309] border border-[#b45309] rounded-xl text-[11px] font-stamp font-bold hover:bg-[#faedcd] transition shadow-[2px_2px_0px_#b45309]">
                                    डाक रसीद
                                </button>
                                <button onclick="requestIndiaPostPickup('${p.id}', '${title.replace(/'/g, "\\\\'")}')" class="px-3 py-2 bg-[#b45309] text-white rounded-xl text-[11px] font-stamp font-bold hover:bg-[#92400e] transition shadow-[2px_2px_0px_#2b2d42]">
                                    डाकघर पिकअप
                                </button>
                                <button onclick="shareWhatsApp('${title.replace(/'/g, "\\\\'")}', ${p.suggested_price})" class="px-3 py-2 bg-[#047857] text-white rounded-xl text-xs font-bold hover:bg-[#065f46] transition shadow-[2px_2px_0px_#2b2d42]">
                                    खरीदें (Buy)
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
                `;
            }).join('');
        }

        // Render Artisan My-Products View
        function renderArtisanProducts(products) {
            const container = document.getElementById('artisan-my-products-grid');
            if (!container) return;

            container.innerHTML = products.map(p => `
                <div class="vintage-card p-4 rounded-2xl bg-white flex items-center gap-3">
                    <img src="${p.studio_image_url || p.raw_image_url}" class="w-16 h-16 rounded-xl object-cover border border-[#d4a373]">
                    <div class="min-w-0 flex-1">
                        <span class="text-[9px] font-stamp font-bold text-[#c2593f] uppercase block">${p.category}</span>
                        <h4 class="font-vintage text-sm text-[#2b2d42] truncate">${p.title}</h4>
                        <div class="flex items-center justify-between mt-1">
                            <span class="font-vintage text-sm font-bold text-[#047857]">₹${p.suggested_price}</span>
                            <span class="text-[9px] font-stamp text-[#047857] font-bold">✓ स्पीड पोस्ट तैयार</span>
                        </div>
                    </div>
                </div>
            `).join('');
        }

        // Card Detail Toggle
        function toggleCardDetail(id, type) {
            const sec = document.getElementById(`${type}-section-${id}`);
            if (sec) sec.classList.toggle('hidden');
        }

        // Play Voice via SpeechSynthesis
        function playVoiceText(text) {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                const utter = new SpeechSynthesisUtterance(text);
                const langMap = { 'hi': 'hi-IN', 'bn': 'bn-IN', 'mr': 'mr-IN', 'ta': 'ta-IN', 'te': 'te-IN', 'en': 'en-IN' };
                utter.lang = langMap[currentLang] || 'hi-IN';
                utter.rate = 0.92;
                window.speechSynthesis.speak(utter);
            }
        }

        // Switch Between Artisan & Buyer Interfaces
        function switchView(view) {
            currentView = view;
            const vArtisan = document.getElementById('view-artisan');
            const vBuyer = document.getElementById('view-buyer');
            const btnArtisan = document.getElementById('nav-switch-artisan');
            const btnBuyer = document.getElementById('nav-switch-buyer');

            if (view === 'artisan') {
                vArtisan.classList.remove('hidden');
                vBuyer.classList.add('hidden');
                btnArtisan.classList.add('bg-[#b45309]', 'text-white');
                btnArtisan.classList.remove('bg-[#fefae0]', 'text-[#b45309]');
                btnBuyer.classList.remove('bg-[#047857]', 'text-white');
                btnBuyer.classList.add('bg-[#fefae0]', 'text-[#2b2d42]');
            } else {
                vBuyer.classList.remove('hidden');
                vArtisan.classList.add('hidden');
                btnBuyer.classList.add('bg-[#047857]', 'text-white');
                btnBuyer.classList.remove('bg-[#fefae0]', 'text-[#2b2d42]');
                btnArtisan.classList.remove('bg-[#b45309]', 'text-white');
                btnArtisan.classList.add('bg-[#fefae0]', 'text-[#b45309]');
            }
        }

        // Gateway Enter Actions
        function enterAsArtisan() {
            document.getElementById('gateway-screen').classList.add('hidden');
            switchView('artisan');
            playVoiceText("कारीगर कार्यशाला में आपका स्वागत है। आप अपनी आवाज से सामान जोड़ सकते हैं।");
        }

        function enterAsBuyer() {
            document.getElementById('gateway-screen').classList.add('hidden');
            switchView('buyer');
            playVoiceText("कला कार्ट दस्तकार बाज़ार में आपका स्वागत है।");
        }

        function openGateway() {
            document.getElementById('gateway-screen').classList.remove('hidden');
        }

        function openGatewayLanguage() {
            openGateway();
        }

        // Set Language
        function setLanguage(lang) {
            currentLang = lang;
            ['hi', 'bn', 'mr', 'ta', 'te', 'en'].forEach(l => {
                const btn = document.getElementById(`lang-btn-${l}`);
                if (btn) {
                    if (l === lang) {
                        btn.classList.add('bg-[#b45309]', 'text-white');
                        btn.classList.remove('bg-white', 'text-[#2b2d42]');
                    } else {
                        btn.classList.remove('bg-[#b45309]', 'text-white');
                        btn.classList.add('bg-white', 'text-[#2b2d42]');
                    }
                }
            });

            // Localized Greetings
            const welcomes = {
                'hi': 'कला कार्ट में आपका स्वागत है',
                'bn': 'কলা কার্টে আপনাকে স্বাগতম',
                'mr': 'कला कार्ट मध्ये आपले स्वागत आहे',
                'ta': 'கலா கார்ட்டுக்கு உங்களை வரவேற்கிறோம்',
                'te': 'కళా కార్ట్‌కు మీకు స్వాగతం',
                'en': 'Welcome to Kala Kart'
            };
            const subs = {
                'hi': 'कृपया अपनी भूमिका का चयन करें: कारीगर कार्यशाला या ग्राहक दस्तकार बाज़ार',
                'bn': 'আপনার ভূমিকা নির্বাচন করুন: কারিগর কর্মশালা অথবা ক্রেতা বাজার',
                'mr': 'आपली भूमिका निवडा: कारागीर कार्यशाळा किंवा ग्राहक बाजार',
                'ta': 'உங்கள் பங்கைத் தேர்வுசெய்யவும்: கைவினைஞர் பட்டறை அல்லது வாங்குபவர் சந்தை',
                'te': 'మీ పాత్రను ఎంచుకోండి: కళాకారుల వర్క్‌షాప్ లేదా కొనుగోలుదారుల మార్కెట్',
                'en': 'Please select your role: Artisan Workspace or Buyer Marketplace'
            };

            const tEl = document.getElementById('gateway-title');
            const sEl = document.getElementById('gateway-sub');
            if (tEl) tEl.innerText = welcomes[lang] || welcomes['hi'];
            if (sEl) sEl.innerText = subs[lang] || subs['hi'];

            renderAllProductViews();
        }

        // Filter Buyer Marketplace
        function filterMarketplaceCategory(cat) {
            document.querySelectorAll('.bcat-pill').forEach(b => {
                b.classList.remove('bg-[#c2593f]', 'text-white');
                b.classList.add('bg-[#fefae0]', 'text-[#2b2d42]');
            });

            if (cat === 'all') {
                document.getElementById('bcat-all').classList.add('bg-[#c2593f]', 'text-white');
                renderBuyerMarketplace(cachedProducts);
            } else {
                const filtered = cachedProducts.filter(p => p.category.includes(cat) || p.category === cat);
                renderBuyerMarketplace(filtered);
            }
        }

        // Artisan Logins
        async function handleGatewayVishwakarmaLogin() {
            const vId = document.getElementById('gw-vishwakarma-id').value || 'PMV-BH-88214';
            const formData = new FormData();
            formData.append('vishwakarma_id', vId);

            try {
                const res = await fetch('/api/artisan/verify-vishwakarma', { method: 'POST', body: formData });
                const data = await res.json();
                if (data.status === 'success') {
                    setArtisanProfile(data.artisan);
                    enterAsArtisan();
                }
            } catch (err) {
                console.error(err);
                enterAsArtisan();
            }
        }

        async function handleGatewayPhoneLogin() {
            enterAsArtisan();
        }

        function speakArtisanOTP() {
            playVoiceText("नमस्ते! आपका कला कार्ट लॉगिन कोड है: पांच, चार, एक, आठ।");
        }

        // New Registration for Non-Vishwakarma Artisans
        function openRegisterModal() {
            toggleModal('register-modal');
        }

        async function handleRegistrationSubmit(e) {
            e.preventDefault();
            const btn = document.getElementById('reg-btn');
            const fb = document.getElementById('reg-feedback');
            btn.disabled = true;

            const formData = new FormData();
            formData.append('name', document.getElementById('reg-name').value);
            formData.append('craft_type', document.getElementById('reg-craft').value);
            formData.append('village_panchayat', document.getElementById('reg-panchayat').value);
            formData.append('phone', document.getElementById('reg-phone').value);
            formData.append('assist_requested', document.getElementById('reg-assist').checked);

            try {
                const res = await fetch('/api/artisan/register', { method: 'POST', body: formData });
                const data = await res.json();
                if (data.status === 'success') {
                    fb.innerText = `✅ ${data.message}`;
                    fb.classList.remove('hidden');
                    playVoiceText(data.voice_announcement);
                    setArtisanProfile(data.artisan);
                    setTimeout(() => {
                        toggleModal('register-modal');
                        enterAsArtisan();
                    }, 1800);
                }
            } catch (err) {
                console.error(err);
                enterAsArtisan();
            }
        }

        // Set Artisan Profile
        function setArtisanProfile(artisan) {
            currentArtisan = artisan;
            document.getElementById('artisan-dash-name').innerText = artisan.name;
            document.getElementById('artisan-dash-status').innerText = artisan.panchayat_seal || '✓ ग्राम पंचायत सत्यापित';
            document.getElementById('artisan-dash-details').innerText = `${artisan.gram_panchayat} • ID: ${artisan.vishwakarma_id}`;
            document.getElementById('artisan-dash-earnings').innerText = artisan.total_earnings || '₹42,850';
        }

        function artisanLogout() {
            currentArtisan = null;
            openGateway();
        }

        // Voice Studio Handlers
        function toggleVoiceRecord() {
            isRecording = !isRecording;
            const btn = document.getElementById('voice-rec-btn');
            const text = document.getElementById('voice-status-text');
            if (isRecording) {
                btn.classList.add('animate-pulse', 'ring-4', 'ring-red-400');
                text.innerText = "🔴 रिकॉर्डिंग जारी... बोलिए";
            } else {
                btn.classList.remove('animate-pulse', 'ring-4', 'ring-red-400');
                text.innerText = "✅ १०-सेकंड आवाज सुरक्षित!";
            }
        }

        function handleStudioSubmit(e) {
            e.preventDefault();
            alert("✅ एआई स्टूडियो कैटलॉग तैयार हो गया! आपका नया हस्तशिल्प बाज़ार में लाइव है।");
            toggleModal('studio-modal');
        }

        // India Post Pickup Alert
        function requestIndiaPostPickup(id, title) {
            const track = `SP-IND-${Math.floor(100000 + Math.random() * 900000)}`;
            alert(`📮 भारतीय डाक स्पीड पोस्ट अनुरोध सफल!\n\n📦 शिल्प: ${title}\n🏷️ Speed Post Tracking No: ${track}\n👨‍🌾 ग्रामीण डाक सेवक आज शाम आपके पते से पार्सल संग्रह करेंगे।`);
        }

        function openPostalTag(id, artisanName) {
            document.getElementById('tag-artisan-name').innerText = artisanName;
            document.getElementById('tag-tracking-num').innerText = `SP-IND-${Math.floor(100000 + Math.random() * 900000)}`;
            toggleModal('postal-tag-modal');
        }

        // Gratitude Wall
        let activeGratitudeArtisan = "";
        function openGratitudeModal(id, artisanName) {
            activeGratitudeArtisan = artisanName;
            document.getElementById('gratitude-artisan-name').innerText = artisanName;
            toggleModal('gratitude-modal');
        }

        function handleGratitudeSubmit(e) {
            e.preventDefault();
            alert(`💌 धन्यवाद संदेश भेजा गया! आपका संदेश ${activeGratitudeArtisan} के गाँव में पहुँचेगा।`);
            toggleModal('gratitude-modal');
        }

        function shareWhatsApp(title, price) {
            const text = encodeURIComponent(`नमस्ते! मैं कला कार्ट पर यह प्रामाणिक हस्तशिल्प खरीदना चाहता हूँ: ${title} (मूल्य: ₹${price})। कृपया Speed Post विवरण भेजें।`);
            window.open(`https://wa.me/919876543210?text=${text}`, '_blank');
        }

        // Kala Sakhi & Bulk Order Helpers
        async function requestKalaSakhi() {
            const fb = document.getElementById('sakhi-fb');
            const res = await fetch('/api/shg/request-sakhi', { method: 'POST' });
            const data = await res.json();
            fb.innerText = `✅ ${data.message}`;
            fb.classList.remove('hidden');
            playVoiceText(data.message);
        }

        async function joinBulkRawMaterials() {
            const fb = document.getElementById('bulk-fb');
            const res = await fetch('/api/shg/join-bulk-order', { method: 'POST' });
            const data = await res.json();
            fb.innerText = `✅ ${data.message}`;
            fb.classList.remove('hidden');
            playVoiceText(data.message);
        }

        // Modal Helper
        function toggleModal(id) {
            const el = document.getElementById(id);
            if (el) el.classList.toggle('hidden');
        }

        // Window Onload
        window.onload = () => {
            fetchProducts();
            lucide.createIcons();
        };
    </script>
</body>
</html>'''

def main():
    target = "templates/index.html"
    content = build_template()
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Kala Kart dual-interface template written successfully to {target} ({len(content)} bytes)")

if __name__ == "__main__":
    main()
