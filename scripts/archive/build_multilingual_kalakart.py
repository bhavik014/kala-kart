# -*- coding: utf-8 -*-
import os

def generate_template():
    return '''<!DOCTYPE html>
<html lang="hi" class="h-full bg-[#f6f1e9]">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kala Kart (कला कार्ट) — पुश्तैनी ग्रामीण दस्तकारी व आवाज़-व्यापार</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Rozha+One&family=Noto+Serif+Devanagari:wght@400;700&family=Noto+Sans+Bengali:wght@400;700&family=Noto+Sans+Tamil:wght@400;700&family=Noto+Sans+Telugu:wght@400;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Courier+Prime:ital,wght@0,400;0,700;1,400&display=swap');
        
        body { 
            font-family: 'Plus Jakarta Sans', sans-serif; 
            background-color: #f6f1e9;
            background-image: radial-gradient(#d4a373 0.6px, transparent 0.6px);
            background-size: 20px 20px;
            color: #2b2d42;
        }
        
        .font-vintage { font-family: 'Rozha One', 'Noto Serif Devanagari', serif; }
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
    <!-- 0. STEP 1: INITIAL LANGUAGE SELECTION MODAL (MANDATORY ENTRY GATEWAY)       -->
    <!-- ========================================================================= -->
    <div id="initial-lang-modal" class="fixed inset-0 z-50 bg-[#2b2d42]/85 backdrop-blur-md flex items-center justify-center p-4">
        <div class="bg-[#fffdfa] rounded-3xl max-w-lg w-full p-6 sm:p-8 shadow-[12px_16px_0px_#c2593f] border-3 border-[#2b2d42] text-center relative">
            <div class="w-16 h-16 rounded-2xl bg-[#c2593f] text-white flex items-center justify-center text-3xl shadow-[3px_3px_0px_#2b2d42] mx-auto mb-4">
                🇮🇳
            </div>
            
            <span class="stamp-badge px-3 py-1 text-xs font-stamp font-bold uppercase text-[#c2593f] inline-block mb-2">
                Kala Kart • कला कार्ट
            </span>
            <h2 class="font-vintage text-2xl sm:text-3xl text-[#2b2d42] mb-1">
                कृपया अपनी भाषा चुनें
            </h2>
            <p class="text-xs text-[#6c757d] font-stamp mb-6">
                Select Your Regional Language to Proceed
            </p>

            <div class="grid grid-cols-2 gap-3 mb-6">
                <button type="button" onclick="selectInitialLanguage('hi')" class="p-4 rounded-2xl border-2 border-[#d4a373] bg-white hover:bg-[#fefae0] hover:border-[#b45309] transition shadow-[3px_3px_0px_#d4a373] flex flex-col items-center">
                    <span class="font-vintage text-xl text-[#2b2d42]">हिन्दी</span>
                    <span class="text-[10px] font-stamp text-[#6c757d] mt-1">Hindi • उत्तरी भारत</span>
                </button>
                <button type="button" onclick="selectInitialLanguage('bn')" class="p-4 rounded-2xl border-2 border-[#d4a373] bg-white hover:bg-[#fefae0] hover:border-[#b45309] transition shadow-[3px_3px_0px_#d4a373] flex flex-col items-center">
                    <span class="text-xl font-bold text-[#2b2d42]">বাংলা</span>
                    <span class="text-[10px] font-stamp text-[#6c757d] mt-1">Bengali • পশ্চিমবঙ্গ/ত্রিপুরা</span>
                </button>
                <button type="button" onclick="selectInitialLanguage('mr')" class="p-4 rounded-2xl border-2 border-[#d4a373] bg-white hover:bg-[#fefae0] hover:border-[#b45309] transition shadow-[3px_3px_0px_#d4a373] flex flex-col items-center">
                    <span class="font-vintage text-xl text-[#2b2d42]">मराठी</span>
                    <span class="text-[10px] font-stamp text-[#6c757d] mt-1">Marathi • महाराष्ट्र</span>
                </button>
                <button type="button" onclick="selectInitialLanguage('ta')" class="p-4 rounded-2xl border-2 border-[#d4a373] bg-white hover:bg-[#fefae0] hover:border-[#b45309] transition shadow-[3px_3px_0px_#d4a373] flex flex-col items-center">
                    <span class="text-xl font-bold text-[#2b2d42]">தமிழ்</span>
                    <span class="text-[10px] font-stamp text-[#6c757d] mt-1">Tamil • தமிழ்நாடு</span>
                </button>
                <button type="button" onclick="selectInitialLanguage('te')" class="p-4 rounded-2xl border-2 border-[#d4a373] bg-white hover:bg-[#fefae0] hover:border-[#b45309] transition shadow-[3px_3px_0px_#d4a373] flex flex-col items-center">
                    <span class="text-xl font-bold text-[#2b2d42]">తెలుగు</span>
                    <span class="text-[10px] font-stamp text-[#6c757d] mt-1">Telugu • ఆంధ్రప్రదేశ్/తెలంగాణ</span>
                </button>
                <button type="button" onclick="selectInitialLanguage('en')" class="p-4 rounded-2xl border-2 border-[#d4a373] bg-white hover:bg-[#fefae0] hover:border-[#b45309] transition shadow-[3px_3px_0px_#d4a373] flex flex-col items-center">
                    <span class="text-xl font-bold text-[#2b2d42]">English</span>
                    <span class="text-[10px] font-stamp text-[#6c757d] mt-1">Global & Urban Export</span>
                </button>
            </div>

            <p class="text-[11px] font-stamp text-[#6c757d]">
                चयनित भाषा पूरे ऐप में लागू होगी (All text & audio in your dialect)
            </p>
        </div>
    </div>

    <!-- ========================================================================= -->
    <!-- 1. DUAL-ROLE GATEWAY SCREEN (ARTISAN VS BUYER)                             -->
    <!-- ========================================================================= -->
    <div id="gateway-screen" class="fixed inset-0 z-40 bg-[#f6f1e9] flex flex-col justify-between p-4 sm:p-8 overflow-y-auto">
        
        <!-- Top Bar with Active Language Badge -->
        <div class="max-w-5xl mx-auto w-full flex items-center justify-between gap-3 border-b border-dashed border-[#d4a373] pb-4">
            <div class="flex items-center gap-2">
                <span class="font-vintage text-2xl sm:text-3xl text-[#2b2d42]">Kala Kart</span>
                <span id="gw-brand-sub" class="text-xs font-stamp font-bold text-[#c2593f] bg-[#fefae0] px-2.5 py-0.5 rounded border border-[#d4a373]">कला कार्ट</span>
            </div>

            <div class="flex items-center gap-2">
                <button onclick="openLanguagePicker()" class="px-3 py-1.5 text-xs font-stamp font-bold rounded-xl border border-[#d4a373] bg-[#fefae0] text-[#2b2d42] hover:bg-[#faedcd] transition flex items-center gap-1.5 shadow-xs">
                    <i data-lucide="languages" class="w-3.5 h-3.5 text-[#c2593f]"></i>
                    <span id="gw-active-lang">हिन्दी (बदलें)</span>
                </button>
            </div>
        </div>

        <!-- Main Gateway Choice -->
        <div class="max-w-5xl mx-auto w-full my-auto py-8">
            <div class="text-center max-w-2xl mx-auto mb-8">
                <span class="stamp-badge px-3 py-1 text-xs font-stamp font-bold uppercase text-[#c2593f] inline-block mb-3" id="gw-top-badge">
                    भारतीय ग्रामीण आवाज़-व्यापार मंच
                </span>
                <h1 id="gw-title" class="font-vintage text-3xl sm:text-5xl text-[#2b2d42] tracking-tight">
                    कला कार्ट में आपका स्वागत है
                </h1>
                <p id="gw-sub" class="text-xs sm:text-sm text-[#6c757d] font-stamp mt-2 leading-relaxed">
                    कृपया अपनी भूमिका का चयन करें: कारीगर कार्यशाला में काम करना चाहते हैं या सीधे हस्तशिल्प खरीदना चाहते हैं?
                </p>
            </div>

            <!-- Two Distinct Role Cards -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
                
                <!-- CARD 1: ARTISAN WORKSPACE & LOGIN -->
                <div class="vintage-card p-6 sm:p-8 rounded-3xl flex flex-col justify-between relative overflow-hidden bg-[#fffdfa]">
                    <div class="absolute top-0 right-0 w-24 h-24 bg-[#fed7aa]/30 rounded-bl-full pointer-events-none"></div>
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <span class="w-12 h-12 rounded-2xl bg-[#c2593f] text-white flex items-center justify-center text-xl shadow-[2px_2px_0px_#2b2d42]">
                                🧕
                            </span>
                            <span class="text-[10px] font-stamp font-bold text-[#047857] bg-[#ecfdf5] px-2.5 py-1 rounded-full border border-[#a7f3d0]" id="gw-artisan-badge">
                                PM Vishwakarma • PM-AJAY
                            </span>
                        </div>
                        <h3 class="font-vintage text-2xl text-[#2b2d42] mb-2" id="gw-artisan-title">१. कारीगर कार्यशाला (Artisan Hub)</h3>
                        <p class="text-xs text-[#4a4e69] leading-relaxed mb-4" id="gw-artisan-desc">
                            १० सेकंड अपनी बोली में बोलकर स्टूडियो कैटलॉग बनाएं, स्वयं सहायता समूह से कच्चा माल ३६% सस्ता खरीदें और स्पीड पोस्ट पिकअप प्राप्त करें।
                        </p>

                        <!-- Quick Artisan Login Options -->
                        <div class="space-y-2.5 pt-2 border-t border-dashed border-[#d4a373]">
                            <!-- PM Vishwakarma 1-Tap -->
                            <div class="flex gap-2">
                                <input type="text" id="gw-vishwakarma-id" value="PMV-BH-88214" placeholder="PM Vishwakarma ID" class="flex-1 px-3 py-2 text-xs font-mono font-bold bg-white border border-[#d4a373] rounded-xl focus:outline-none">
                                <button onclick="handleGatewayVishwakarmaLogin()" class="px-3 py-2 bg-[#1e3a8a] hover:bg-[#172554] text-white text-xs font-bold rounded-xl shadow-[2px_2px_0px_#2b2d42] transition" id="gw-vish-btn">
                                    सत्यापित करें
                                </button>
                            </div>

                            <!-- Mobile OTP Option -->
                            <div class="flex gap-2">
                                <input type="tel" id="gw-phone" value="9876543210" placeholder="१० अंकों का नंबर" class="flex-1 px-3 py-2 text-xs bg-white border border-[#d4a373] rounded-xl focus:outline-none">
                                <button onclick="speakArtisanOTP()" class="px-2.5 py-2 bg-[#fefae0] text-[#b45309] border border-[#b45309] text-xs font-stamp font-bold rounded-xl hover:bg-[#faedcd] transition" id="gw-otp-btn">
                                    OTP सुनें
                                </button>
                                <button onclick="handleGatewayPhoneLogin()" class="px-3 py-2 bg-[#c2593f] hover:bg-[#a6472e] text-white text-xs font-bold rounded-xl shadow-[2px_2px_0px_#2b2d42] transition" id="gw-login-btn">
                                    प्रवेश
                                </button>
                            </div>

                            <!-- Get Registered Link (For non-Vishwakarma) -->
                            <div class="pt-2 text-center">
                                <button onclick="openRegisterModal()" class="text-xs font-stamp font-bold text-[#b45309] hover:underline flex items-center justify-center gap-1 mx-auto" id="gw-reg-link">
                                    👉 विश्वकर्मा आईडी नहीं है? नया पंजीकरण करें (Get Registered)
                                </button>
                            </div>
                        </div>
                    </div>

                    <button onclick="enterAsArtisan()" class="mt-6 w-full py-3.5 bg-[#2b2d42] hover:bg-[#1e1b4b] text-[#fefae0] font-bold text-xs font-stamp uppercase tracking-wider rounded-xl shadow-[3px_3px_0px_#c2593f] transition flex items-center justify-center gap-2" id="gw-artisan-enter-btn">
                        <i data-lucide="wrench" class="w-4 h-4 text-[#fed7aa]"></i>
                        <span>कारीगर कार्यशाला में प्रवेश करें</span>
                    </button>
                </div>

                <!-- CARD 2: BUYER MARKETPLACE ENTRY -->
                <div class="vintage-card p-6 sm:p-8 rounded-3xl flex flex-col justify-between relative overflow-hidden bg-[#fffdfa]">
                    <div class="absolute top-0 right-0 w-24 h-24 bg-[#a7f3d0]/30 rounded-bl-full pointer-events-none"></div>
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <span class="w-12 h-12 rounded-2xl bg-[#047857] text-white flex items-center justify-center text-xl shadow-[2px_2px_0px_#2b2d42]">
                                🛍️
                            </span>
                            <span class="text-[10px] font-stamp font-bold text-[#c2593f] bg-[#fefae0] px-2.5 py-1 rounded-full border border-[#fed7aa]" id="gw-buyer-badge">
                                १००% बिचौलिया-मुक्त बाज़ार
                            </span>
                        </div>
                        <h3 class="font-vintage text-2xl text-[#2b2d42] mb-2" id="gw-buyer-title">२. ग्राहक दस्तकार बाज़ार (Buyer Marketplace)</h3>
                        <p class="text-xs text-[#4a4e69] leading-relaxed mb-4" id="gw-buyer-desc">
                            भारत के दूरदराज गाँवों से सीधे असली हस्तशिल्प खरीदें। आपकी खरीद का ८५%+ पारिश्रमिक बिना किसी दलाल के सीधे ग्रामीण शिल्पकार के बैंक खाते में जाता है।
                        </p>

                        <!-- Highlights List -->
                        <div class="space-y-2 pt-2 border-t border-dashed border-[#d4a373] text-xs font-stamp text-[#6c757d]">
                            <div class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-[#047857]"></i>
                                <span id="gw-h1">कारीगर की मातृभाषा में मूल कहानी सुनें (भाषिणी AI)</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-[#047857]"></i>
                                <span id="gw-h2">SFURTI Grade A+ लैब व GI टैग प्रमाणित उत्पाद</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-[#047857]"></i>
                                <span id="gw-h3">भारतीय डाक स्पीड पोस्ट से गाँव से सीधा आपके घर प्रेषण</span>
                            </div>
                        </div>
                    </div>

                    <button onclick="enterAsBuyer()" class="mt-6 w-full py-3.5 bg-[#047857] hover:bg-[#065f46] text-white font-bold text-xs font-stamp uppercase tracking-wider rounded-xl shadow-[3px_3px_0px_#2b2d42] transition flex items-center justify-center gap-2" id="gw-buyer-enter-btn">
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
    <!-- 2. MAIN HEADER (ALWAYS ACCESSIBLE WITH 1-CLICK ROLE SWITCH)                -->
    <!-- ========================================================================= -->
    <header class="sticky top-0 z-30 bg-[#fffcf7]/95 backdrop-blur-md border-b-2 border-[#d4a373] shadow-xs">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-3">
            
            <!-- Brand -->
            <div class="flex items-center gap-3">
                <a href="javascript:void(0)" onclick="openGateway()" class="flex items-baseline gap-2">
                    <span class="font-vintage text-2xl sm:text-3xl text-[#2b2d42] tracking-wide">Kala Kart</span>
                    <span id="nav-brand-sub" class="text-xs font-stamp font-bold text-[#c2593f]">कला कार्ट</span>
                </a>
                <span class="hidden sm:inline-flex stamp-badge px-2 py-0.5 text-[10px] font-stamp font-bold text-[#c2593f]">
                    SIH26090
                </span>
            </div>

            <!-- Role Switcher & Eco Pill -->
            <div class="flex items-center gap-2">
                <button onclick="toggleModal('ecosystem-modal')" class="flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-stamp font-bold bg-[#eff6ff] hover:bg-[#dbeafe] text-[#1e3a8a] border border-[#bfdbfe] transition">
                    <i data-lucide="landmark" class="w-3.5 h-3.5"></i>
                    <span id="nav-eco-btn-label">६ सरकारी स्तंभ</span>
                </button>

                <button onclick="switchView('artisan')" id="nav-btn-artisan" class="px-3 py-1.5 rounded-xl text-xs font-stamp font-bold transition flex items-center gap-1.5 border border-[#d4a373] bg-[#fefae0] text-[#b45309] hover:bg-[#faedcd]">
                    <i data-lucide="wrench" class="w-3.5 h-3.5"></i>
                    <span id="nav-artisan-label">कारीगर कार्यशाला</span>
                </button>

                <button onclick="switchView('buyer')" id="nav-btn-buyer" class="px-3 py-1.5 rounded-xl text-xs font-stamp font-bold transition flex items-center gap-1.5 border border-[#047857] bg-[#047857] text-white hover:bg-[#065f46]">
                    <i data-lucide="shopping-bag" class="w-3.5 h-3.5"></i>
                    <span id="nav-buyer-label">दस्तकार बाज़ार</span>
                </button>

                <button onclick="openLanguagePicker()" class="p-2 rounded-xl text-[#2b2d42] bg-[#fefae0] border border-[#d4a373] hover:bg-[#faedcd] transition" title="भाषा बदलें">
                    <i data-lucide="languages" class="w-4 h-4 text-[#c2593f]"></i>
                </button>
            </div>

        </div>
    </header>

    <!-- ========================================================================= -->
    <!-- 3. INTERFACE A: ARTISAN WORKSPACE                                         -->
    <!-- ========================================================================= -->
    <div id="view-artisan" class="hidden flex-1 max-w-6xl w-full mx-auto px-4 sm:px-6 py-6 space-y-6">
        
        <!-- Profile Banner -->
        <div class="vintage-card p-6 rounded-3xl bg-[#fffdfa] border-2 border-[#b45309]">
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div class="flex items-center gap-4">
                    <div class="w-16 h-16 rounded-2xl bg-[#faedcd] border-2 border-[#b45309] flex items-center justify-center text-3xl shadow">
                        🧕
                    </div>
                    <div>
                        <div class="flex items-center gap-2 flex-wrap">
                            <h2 class="font-vintage text-2xl text-[#2b2d42]" id="artisan-dash-name">रामवती देवी</h2>
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
                        <span class="text-[10px] font-stamp text-[#6c757d] block" id="artisan-lbl-dbt">सीधी बैंक आय (DBT)</span>
                        <span class="font-vintage text-xl text-[#047857]" id="artisan-dash-earnings">₹42,850</span>
                    </div>
                    <button onclick="artisanLogout()" class="px-3 py-2 bg-[#f5f5f4] hover:bg-[#e7e5e4] text-[#6c757d] text-xs font-stamp rounded-xl border border-[#d6d3d1]" id="artisan-logout-btn">
                        लॉगआउट
                    </button>
                </div>
            </div>
        </div>

        <!-- 4 Core Artisan Tools -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            <!-- 1. Voice Studio -->
            <div class="vintage-card p-5 rounded-2xl flex flex-col justify-between">
                <div>
                    <div class="w-10 h-10 rounded-xl bg-[#c2593f] text-white flex items-center justify-center mb-3 shadow">
                        <i data-lucide="mic" class="w-5 h-5"></i>
                    </div>
                    <h4 class="font-vintage text-lg text-[#2b2d42]" id="tool1-title">१० सेकंड स्टूडियो</h4>
                    <p class="text-xs text-[#6c757d] mt-1 leading-relaxed" id="tool1-desc">
                        अपनी मातृभाषा में बोलकर नया शिल्प जोड़ें। एआई फोटो चमकाएगा और विवरण लिखेगा।
                    </p>
                </div>
                <button onclick="toggleModal('studio-modal')" class="mt-4 w-full py-2.5 bg-[#c2593f] hover:bg-[#a6472e] text-white text-xs font-bold rounded-xl shadow transition" id="tool1-btn">
                    + नया शिल्प जोड़ें
                </button>
            </div>

            <!-- 2. SHG Hub -->
            <div class="vintage-card p-5 rounded-2xl flex flex-col justify-between">
                <div>
                    <div class="w-10 h-10 rounded-xl bg-[#b45309] text-white flex items-center justify-center mb-3 shadow">
                        <i data-lucide="users-2" class="w-5 h-5"></i>
                    </div>
                    <h4 class="font-vintage text-lg text-[#2b2d42]" id="tool2-title">स्वयं सहायता समूह</h4>
                    <p class="text-xs text-[#6c757d] mt-1 leading-relaxed" id="tool2-desc">
                        कला सखी दीदी को घर बुलाएँ, रेशम धागा ३६% सस्ता खरीदें या टूल फंड लें।
                    </p>
                </div>
                <button onclick="toggleModal('shg-modal')" class="mt-4 w-full py-2.5 bg-[#b45309] hover:bg-[#92400e] text-white text-xs font-bold rounded-xl shadow transition" id="tool2-btn">
                    समूह केंद्र खोलें
                </button>
            </div>

            <!-- 3. Govt Ecosystem -->
            <div class="vintage-card p-5 rounded-2xl flex flex-col justify-between">
                <div>
                    <div class="w-10 h-10 rounded-xl bg-[#1e3a8a] text-white flex items-center justify-center mb-3 shadow">
                        <i data-lucide="landmark" class="w-5 h-5"></i>
                    </div>
                    <h4 class="font-vintage text-lg text-[#2b2d42]" id="tool3-title">सरकारी सहायता ढाँचा</h4>
                    <p class="text-xs text-[#6c757d] mt-1 leading-relaxed" id="tool3-desc">
                        पीएम विश्वकर्मा टूलकिट ₹15,000, SFURTI लैब व आईआईटी RuTAG नवाचार।
                    </p>
                </div>
                <button onclick="toggleModal('ecosystem-modal')" class="mt-4 w-full py-2.5 bg-[#1e3a8a] hover:bg-[#172554] text-white text-xs font-bold rounded-xl shadow transition" id="tool3-btn">
                    ६ स्तंभ देखें
                </button>
            </div>

            <!-- 4. India Post -->
            <div class="vintage-card p-5 rounded-2xl flex flex-col justify-between">
                <div>
                    <div class="w-10 h-10 rounded-xl bg-[#047857] text-white flex items-center justify-center mb-3 shadow">
                        <i data-lucide="truck" class="w-5 h-5"></i>
                    </div>
                    <h4 class="font-vintage text-lg text-[#2b2d42]" id="tool4-title">डाकघर पिकअप</h4>
                    <p class="text-xs text-[#6c757d] mt-1 leading-relaxed" id="tool4-desc">
                        तैयार पार्सल के लिए ग्रामीण डाक सेवक को अपने घर या गाँव डिपो पर बुलाएँ।
                    </p>
                </div>
                <button onclick="requestIndiaPostPickup('art-101', 'मधुबनी सिल्क कैनवास')" class="mt-4 w-full py-2.5 bg-[#047857] hover:bg-[#065f46] text-white text-xs font-bold rounded-xl shadow transition" id="tool4-btn">
                    पिकअप अनुरोध भेजें
                </button>
            </div>
        </div>

        <!-- Artisan's Listed Products -->
        <div class="pt-4 border-t border-dashed border-[#d4a373]">
            <div class="flex items-center justify-between mb-4">
                <h3 class="font-vintage text-xl text-[#2b2d42]" id="artisan-my-prods-title">आपके सूचीबद्ध हस्तशिल्प (Live on Marketplace)</h3>
                <span class="text-xs font-stamp text-[#047857] font-bold" id="artisan-my-prods-stat">४ उत्पाद सक्रिय बाज़ार में हैं</span>
            </div>
            <div id="artisan-my-products-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                <!-- Filled by JS -->
            </div>
        </div>

    </div>

    <!-- ========================================================================= -->
    <!-- 4. INTERFACE B: BUYER MARKETPLACE                                         -->
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
                <span class="text-[#047857] font-bold" id="mkt-wage-tag">८५%+ सीधा कारीगर को</span> • <span id="mkt-middlemen-tag">१००% बिचौलिया-मुक्त</span>
            </div>
        </div>

        <!-- Full Folk Vintage Marketplace Cards -->
        <div id="buyer-products-grid" class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- Rendered by JS -->
        </div>

    </div>

    <!-- ========================================================================= -->
    <!-- 5. ALL INTERACTIVE MODALS                                                  -->
    <!-- ========================================================================= -->

    <!-- NEW ARTISAN REGISTRATION MODAL -->
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
                    <h3 class="font-vintage text-2xl text-[#2b2d42]" id="reg-modal-title">कारीगर नया पंजीकरण</h3>
                    <p class="text-xs font-stamp text-[#6c757d]" id="reg-modal-sub">ग्राम पंचायत व पीएम विश्वकर्मा निःशुल्क सहायता</p>
                </div>
            </div>

            <p class="text-xs text-[#4a4e69] leading-relaxed mb-4 bg-[#fefae0] p-3 rounded-2xl border border-[#d4a373]" id="reg-modal-notice">
                यदि आपके पास पीएम विश्वकर्मा आईडी नहीं है, तो अपना विवरण दर्ज करें। हम आपको तुरंत अस्थायी आईडी देंगे और स्थानीय <b>कला सखी / CSC VLE</b> आपके घर आकर बायोमेट्रिक व टूलकिट अनुदान पूरा करेंगे।
            </p>

            <form onsubmit="handleRegistrationSubmit(event)" class="space-y-3">
                <div>
                    <label class="block text-[11px] font-stamp font-bold text-[#2b2d42] uppercase mb-1" id="reg-lbl-name">कारीगर का नाम *</label>
                    <input type="text" id="reg-name" required value="कमला देवी" class="w-full px-3.5 py-2 text-xs font-bold bg-[#f6f1e9] border border-[#d4a373] rounded-xl focus:bg-white focus:outline-none">
                </div>

                <div>
                    <label class="block text-[11px] font-stamp font-bold text-[#2b2d42] uppercase mb-1" id="reg-lbl-craft">शिल्प विधा / कार्य *</label>
                    <select id="reg-craft" class="w-full px-3.5 py-2 text-xs font-bold bg-[#f6f1e9] border border-[#d4a373] rounded-xl focus:bg-white focus:outline-none">
                        <option value="मधुबनी चित्रकला">मधुबनी चित्रकला (Painting)</option>
                        <option value="पॉटरी व मिट्टी शिल्प">पॉटरी व मिट्टी शिल्प (Pottery)</option>
                        <option value="हस्तकरघा रेशम बुनाई">हस्तकरघा रेशम बुनाई (Handloom Silk)</option>
                        <option value="काष्ठ नक्काशी शिल्प">काष्ठ नक्काशी शिल्प (Woodcraft)</option>
                    </select>
                </div>

                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-[11px] font-stamp font-bold text-[#2b2d42] uppercase mb-1" id="reg-lbl-panchayat">ग्राम पंचायत *</label>
                        <input type="text" id="reg-panchayat" required value="रंती ग्राम पंचायत, बिहार" class="w-full px-3.5 py-2 text-xs font-bold bg-[#f6f1e9] border border-[#d4a373] rounded-xl focus:bg-white focus:outline-none">
                    </div>
                    <div>
                        <label class="block text-[11px] font-stamp font-bold text-[#2b2d42] uppercase mb-1" id="reg-lbl-phone">मोबाइल नंबर *</label>
                        <input type="tel" id="reg-phone" required value="9876543210" class="w-full px-3.5 py-2 text-xs font-bold bg-[#f6f1e9] border border-[#d4a373] rounded-xl focus:bg-white focus:outline-none">
                    </div>
                </div>

                <div class="flex items-start gap-2 pt-1">
                    <input type="checkbox" id="reg-assist" checked class="mt-0.5 rounded text-[#047857]">
                    <label for="reg-assist" class="text-[11px] text-[#4a4e69] leading-tight" id="reg-lbl-assist">
                        <b>कला सखी / CSC VLE सहायता:</b> घर आकर फोटो लेने व ₹15,000 टूलकिट फॉर्म भरने का अनुरोध करें।
                    </label>
                </div>

                <button type="submit" id="reg-btn-submit" class="w-full py-3 bg-[#047857] hover:bg-[#065f46] text-white font-bold text-xs rounded-xl shadow-[2px_2px_0px_#2b2d42] transition mt-2">
                    पंजीकरण करें व कार्यशाला में जुड़ें (Get Registered)
                </button>
            </form>
            <div id="reg-feedback" class="hidden mt-3 p-2.5 bg-[#ecfdf5] border border-[#a7f3d0] rounded-xl text-xs font-bold text-[#065f46]"></div>
        </div>
    </div>

    <!-- 6-STAGE GOVT ECOSYSTEM MODAL (FULL ARCHITECTURE) -->
    <div id="ecosystem-modal" class="fixed inset-0 z-50 hidden bg-[#2b2d42]/85 backdrop-blur-md flex items-center justify-center p-4">
        <div class="bg-[#fffdfa] rounded-3xl max-w-4xl w-full p-6 sm:p-8 shadow-[12px_18px_0px_#1e3a8a] border-3 border-[#2b2d42] relative max-h-[92vh] overflow-y-auto">
            <button onclick="toggleModal('ecosystem-modal')" class="absolute top-5 right-5 text-[#6c757d] hover:text-[#2b2d42] p-1">
                <i data-lucide="x" class="w-6 h-6"></i>
            </button>

            <div class="flex items-center gap-3.5 mb-6 border-b-2 border-dashed border-[#93c5fd] pb-4">
                <div class="w-12 h-12 rounded-2xl bg-[#1e3a8a] text-white flex items-center justify-center shadow-[3px_3px_0px_#2b2d42]">
                    <i data-lucide="landmark" class="w-6 h-6"></i>
                </div>
                <div>
                    <h3 class="font-vintage text-2xl text-[#1e3a8a]" id="eco-modal-title">राष्ट्रीय संस्थागत व सरकारी सहायता ढाँचा</h3>
                    <p class="text-xs font-stamp text-[#64748b]" id="eco-modal-sub">६ स्तरीय समाधान रूपरेखा • भारत सरकार के मंत्रालयों का सीधा जुड़ाव</p>
                </div>
            </div>

            <!-- 6 Stages Grid (Exact from Reference Screenshots) -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <!-- Stage 1 -->
                <div class="p-4 bg-[#eff6ff] rounded-2xl border-2 border-[#93c5fd] shadow-[3px_3px_0px_#93c5fd]">
                    <div class="flex items-center justify-between mb-1.5">
                        <b class="text-sm font-vintage text-[#1e3a8a]">१. शून्य-टाइपिंग डिजिटल पहचान</b>
                        <span class="text-[9px] font-stamp font-bold text-[#1d4ed8] bg-white px-2 py-0.5 rounded border border-[#93c5fd]">पिलर १</span>
                    </div>
                    <div class="mb-2 p-1.5 bg-white rounded-lg border border-[#bfdbfe] text-[11px] font-stamp">
                        <b>संस्था:</b> PM Vishwakarma & Gram Panchayats
                    </div>
                    <p class="text-xs text-[#334155] leading-relaxed mb-2">
                        <b>समस्या:</b> ई-कॉमर्स में अक्सर फर्जी विक्रेता खाते और बिचौलिए सब्सिडी हड़प लेते हैं।
                    </p>
                    <p class="text-xs text-[#1e3a8a] leading-relaxed bg-white p-2 rounded-xl border border-[#93c5fd]/50">
                        <b>समाधान भूमिका:</b> पीएम विश्वकर्मा पोर्टल से सीधे सत्यापित आईडी प्राप्त करना। ग्राम पंचायत स्थानीय भौतिक सत्यापन डेस्क के रूप में कार्य करती है।
                    </p>
                </div>

                <!-- Stage 2 -->
                <div class="p-4 bg-[#fefae0] rounded-2xl border-2 border-[#d4a373] shadow-[3px_3px_0px_#d4a373]">
                    <div class="flex items-center justify-between mb-1.5">
                        <b class="text-sm font-vintage text-[#2b2d42]">२. ग्राम स्तरीय डिजिटल सहायता केंद्र</b>
                        <span class="text-[9px] font-stamp font-bold text-[#b45309] bg-white px-2 py-0.5 rounded border border-[#d4a373]">पिलर २</span>
                    </div>
                    <div class="mb-2 p-1.5 bg-white rounded-lg border border-[#e7d8c9] text-[11px] font-stamp">
                        <b>संस्था:</b> CSCs (Common Services Centres) & VLEs
                    </div>
                    <p class="text-xs text-[#334155] leading-relaxed mb-2">
                        <b>समस्या:</b> ९८% ग्रामीण शिल्पकारों के पास स्मार्टफोन, इंटरनेट या कैमरा कौशल नहीं है।
                    </p>
                    <p class="text-xs text-[#92400e] leading-relaxed bg-white p-2 rounded-xl border border-[#d4a373]/50">
                        <b>समाधान भूमिका:</b> ग्राम स्तरीय उद्यमी (VLE) तकनीकी साथी बनकर उच्च गुणवत्ता वाली तस्वीरें लेते हैं और आवश्यक डिजिटल उपकरण उपलब्ध कराते हैं।
                    </p>
                </div>

                <!-- Stage 3 -->
                <div class="p-4 bg-[#f0fdf4] rounded-2xl border-2 border-[#86efac] shadow-[3px_3px_0px_#86efac]">
                    <div class="flex items-center justify-between mb-1.5">
                        <b class="text-sm font-vintage text-[#14532d]">३. एआई कैटलॉगिंग व स्थानीयकरण</b>
                        <span class="text-[9px] font-stamp font-bold text-[#15803d] bg-white px-2 py-0.5 rounded border border-[#86efac]">पिलर ३</span>
                    </div>
                    <div class="mb-2 p-1.5 bg-white rounded-lg border border-[#bbf7d0] text-[11px] font-stamp">
                        <b>संस्था:</b> Bhashini (MeitY) & Computer Vision Pipeline
                    </div>
                    <p class="text-xs text-[#334155] leading-relaxed mb-2">
                        <b>समस्या:</b> कारीगर स्थानीय बोलियों में बोलते हैं, जिसे सामान्य अंग्रेजी ई-कॉमर्स समझ नहीं पाता।
                    </p>
                    <p class="text-xs text-[#166534] leading-relaxed bg-white p-2 rounded-xl border border-[#86efac]/50">
                        <b>समाधान भूमिका:</b> भाषिणी एआई स्थानीय बोलियों को बहुभाषी उत्पाद विवरण में बदलती है। कंप्यूटर विज़न साधारण तस्वीरों को स्टूडियो कैटलॉग में बदलता है।
                    </p>
                </div>

                <!-- Stage 4 -->
                <div class="p-4 bg-[#fff7ed] rounded-2xl border-2 border-[#fdba74] shadow-[3px_3px_0px_#fdba74]">
                    <div class="flex items-center justify-between mb-1.5">
                        <b class="text-sm font-vintage text-[#7c2d12]">४. सामूहिक संकलन व सूक्ष्म-लॉजिस्टिक्स</b>
                        <span class="text-[9px] font-stamp font-bold text-[#c2410c] bg-white px-2 py-0.5 rounded border border-[#fdba74]">पिलर ४</span>
                    </div>
                    <div class="mb-2 p-1.5 bg-white rounded-lg border border-[#fed7aa] text-[11px] font-stamp">
                        <b>संस्था:</b> Self-Help Groups (SHGs) & APCs
                    </div>
                    <p class="text-xs text-[#334155] leading-relaxed mb-2">
                        <b>समस्या:</b> दूरदराज के गाँवों से एकल पार्सल भेजना अत्यधिक महंगा पड़ता है।
                    </p>
                    <p class="text-xs text-[#9a3412] leading-relaxed bg-white p-2 rounded-xl border border-[#fdba74]/50">
                        <b>समाधान भूमिका:</b> एकल उत्पादन को थोक बी२बी लॉट में एकत्रित करना। गाँव स्तर पर डाकघर व कूरियर के लिए एकल संकलन केंद्र बनाना।
                    </p>
                </div>

                <!-- Stage 5 -->
                <div class="p-4 bg-[#faf5ff] rounded-2xl border-2 border-[#d8b4fe] shadow-[3px_3px_0px_#d8b4fe]">
                    <div class="flex items-center justify-between mb-1.5">
                        <b class="text-sm font-vintage text-[#581c87]">५. गुणवत्ता नियंत्रण, पैकेजिंग व लैब</b>
                        <span class="text-[9px] font-stamp font-bold text-[#7e22ce] bg-white px-2 py-0.5 rounded border border-[#d8b4fe]">पिलर ५</span>
                    </div>
                    <div class="mb-2 p-1.5 bg-white rounded-lg border border-[#e9d5ff] text-[11px] font-stamp">
                        <b>संस्था:</b> SFURTI Clusters (Common Facility Centres)
                    </div>
                    <p class="text-xs text-[#334155] leading-relaxed mb-2">
                        <b>समस्या:</b> रास्ते में माल टूटने और गैर-मानकीकृत पैकेजिंग से उत्पाद वापसी दर बढ़ जाती है।
                    </p>
                    <p class="text-xs text-[#6b21a8] leading-relaxed bg-white p-2 rounded-xl border border-[#d8b4fe]/50">
                        <b>समाधान भूमिका:</b> स्फूर्ति कॉमन फैसिलिटी सेंटर्स मानक गुणवत्ता जांच, बारकोड टैगिंग और सुरक्षित निर्यात पैकेजिंग सुनिश्चित करते हैं।
                    </p>
                </div>

                <!-- Stage 6 -->
                <div class="p-4 bg-[#fff1f2] rounded-2xl border-2 border-[#fecdd3] shadow-[3px_3px_0px_#fecdd3]">
                    <div class="flex items-center justify-between mb-1.5">
                        <b class="text-sm font-vintage text-[#881337]">६. कौशल उन्नयन व हार्डवेयर नवाचार</b>
                        <span class="text-[9px] font-stamp font-bold text-[#be123c] bg-white px-2 py-0.5 rounded border border-[#fecdd3]">पिलर ६</span>
                    </div>
                    <div class="mb-2 p-1.5 bg-white rounded-lg border border-[#fecdd3] text-[11px] font-stamp">
                        <b>संस्था:</b> Weavers' Service Centres (WSCs) & RuTAG (IITs)
                    </div>
                    <p class="text-xs text-[#334155] leading-relaxed mb-2">
                        <b>समस्या:</b> पारंपरिक भारी उपकरणों से शारीरिक थकान होती है और शहरी बाज़ार ट्रेंड की समझ नहीं होती।
                    </p>
                    <p class="text-xs text-[#9f1239] leading-relaxed bg-white p-2 rounded-xl border border-[#fecdd3]/50">
                        <b>समाधान भूमिका:</b> बाज़ार ट्रेंड एनालिटिक्स का फीडबैक लूप बुनकर सेवा केंद्रों और आईआईटी के RuTAG तक पहुँचता है ताकि आधुनिक उपकरण विकसित हो सकें।
                    </p>
                </div>
            </div>
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
                    <label class="block text-[10px] font-stamp font-bold text-[#2b2d42] uppercase mb-1">संदेश</label>
                    <textarea id="gratitude-buyer-msg" rows="2" required class="w-full px-3 py-2 text-xs bg-[#f6f1e9] border border-[#d4a373] rounded-xl focus:bg-white focus:outline-none">दीदी, आपकी कला हमारे घर में बहुत सुंदर लग रही है!</textarea>
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

            <div class="space-y-2 text-xs font-stamp text-[#2b2d42]">
                <div class="flex justify-between">
                    <span>स्पीड पोस्ट ट्रैकिंग:</span>
                    <b class="text-[#047857]" id="tag-tracking-num">SP-IND-884912</b>
                </div>
                <div class="flex justify-between">
                    <span>शिल्पकार:</span>
                    <b id="tag-artisan-name">रामवती देवी</b>
                </div>
                <div class="flex justify-between">
                    <span>SFURTI CFC मुहर:</span>
                    <b class="text-[#1e3a8a]">Grade A+ Certified</b>
                </div>
            </div>

            <div class="mt-4 p-3 bg-white rounded-xl border border-[#d4a373] text-center">
                <span class="text-xl">👍</span>
                <span class="text-[10px] font-stamp text-[#047857] block font-bold mt-1">शिल्पकार प्रामाणिकता सत्यापित</span>
            </div>
        </div>
    </div>

    <!-- ========================================================================= -->
    <!-- 6. COMPREHENSIVE MULTILINGUAL DICTIONARY & JAVASCRIPT LOGIC                -->
    <!-- ========================================================================= -->
    <script>
        let currentLang = 'hi';
        let currentView = 'buyer';
        let cachedProducts = [];
        let currentArtisan = null;
        let isRecording = false;

        // Comprehensive I18N across all 6 languages
        const I18N = {
            'hi': {
                code: 'hi',
                langName: 'हिन्दी',
                brandSub: 'कला कार्ट',
                gwTopBadge: 'भारतीय ग्रामीण आवाज़-व्यापार मंच',
                gwTitle: 'कला कार्ट में आपका स्वागत है',
                gwSub: 'कृपया अपनी भूमिका का चयन करें: कारीगर कार्यशाला में काम करना चाहते हैं या सीधे हस्तशिल्प खरीदना चाहते हैं?',
                gwArtisanTitle: '१. कारीगर कार्यशाला (Artisan Hub)',
                gwArtisanDesc: '१० सेकंड अपनी बोली में बोलकर स्टूडियो कैटलॉग बनाएं, स्वयं सहायता समूह से कच्चा माल ३६% सस्ता खरीदें और स्पीड पोस्ट पिकअप प्राप्त करें।',
                gwVishBtn: 'सत्यापित करें',
                gwOtpBtn: 'OTP सुनें',
                gwLoginBtn: 'प्रवेश',
                gwRegLink: '👉 विश्वकर्मा आईडी नहीं है? नया पंजीकरण करें (Get Registered)',
                gwArtisanEnterBtn: 'कारीगर कार्यशाला में प्रवेश करें',
                gwBuyerTitle: '२. ग्राहक दस्तकार बाज़ार (Buyer Marketplace)',
                gwBuyerDesc: 'भारत के दूरदराज गाँवों से सीधे असली हस्तशिल्प खरीदें। आपकी खरीद का ८५%+ पारिश्रमिक बिना किसी दलाल के सीधे ग्रामीण शिल्पकार के बैंक खाते में जाता है।',
                gwH1: 'कारीगर की मातृभाषा में मूल कहानी सुनें (भाषिणी AI)',
                gwH2: 'SFURTI Grade A+ लैब व GI टैग प्रमाणित उत्पाद',
                gwH3: 'भारतीय डाक स्पीड पोस्ट से गाँव से सीधा आपके घर प्रेषण',
                gwBuyerEnterBtn: 'सीधे बाज़ार में प्रवेश करें (Enter Marketplace)',
                navArtisanLabel: 'कारीगर कार्यशाला',
                navBuyerLabel: 'दस्तकार बाज़ार',
                navEcoBtnLabel: '६ सरकारी स्तंभ',
                mktWageTag: '८५%+ सीधा कारीगर को',
                mktMiddlemenTag: '१००% बिचौलिया-मुक्त',
                bcatAll: 'सभी हस्तशिल्प',
                bcatPaint: 'मधुबनी चित्रकला',
                bcatPottery: 'खुर्जा पॉटरी',
                bcatSilk: 'भागलपुरी सिल्क',
                bcatWood: 'सहारनपुर काष्ठ शिल्प',
                voiceWelcome: 'कला कार्ट में आपका स्वागत है। अपनी भूमिका चुनें।'
            },
            'bn': {
                code: 'bn',
                langName: 'বাংলা',
                brandSub: 'কলা কার্ট',
                gwTopBadge: 'ভারতীয় গ্রামীণ ভয়েস কমার্স প্ল্যাটফর্ম',
                gwTitle: 'কলা কার্টে আপনাকে স্বাগতম',
                gwSub: 'অনুগ্রহ করে আপনার ভূমিকা নির্বাচন করুন: কারিগর হিসেবে কাজ করবেন নাকি সরাসরি হস্তশিল্প কিনবেন?',
                gwArtisanTitle: '১. কারিগর কর্মশালা (Artisan Hub)',
                gwArtisanDesc: '১০ সেকেন্ড নিজের ভাষায় কথা বলে ক্যাটালগ তৈরি করুন, স্বনির্ভর দল থেকে ৩৬% সাশ্রয়ে কাঁচামাল কিনুন এবং স্পিড পোস্ট পিকআপ নিন।',
                gwVishBtn: 'যাচাই করুন',
                gwOtpBtn: 'OTP শুনুন',
                gwLoginBtn: 'প্রবেশ',
                gwRegLink: '👉 বিশ্বকর্মা আইডি নেই? নতুন নিবন্ধন করুন (Get Registered)',
                gwArtisanEnterBtn: 'কারিগর কর্মশালায় প্রবেশ করুন',
                gwBuyerTitle: '২. ক্রেতা বাজার (Buyer Marketplace)',
                gwBuyerDesc: 'গ্রামের কারিগরদের থেকে সরাসরি খাঁটি হস্তশিল্প কিনুন। আপনার খরচের ৮৫%+ সরাসরি শিল্পীর ব্যাংক অ্যাকাউন্টে যায়।',
                gwH1: 'মাতৃভাষায় কারিগরের মূল গল্প শুনুন (ভাষিণী AI)',
                gwH2: 'SFURTI গ্রেড A+ ল্যাব ও GI ট্যাগ প্রত্যয়িত পণ্য',
                gwH3: 'ভারতীয় ডাক স্পিড পোস্ট মারফত সরাসরি বাড়িতে ডেলিভারি',
                gwBuyerEnterBtn: 'সরাসরি বাজারে প্রবেশ করুন (Enter Marketplace)',
                navArtisanLabel: 'কারিগর কর্মশালা',
                navBuyerLabel: 'কারিগর বাজার',
                navEcoBtnLabel: '৬টি সরকারি স্তম্ভ',
                mktWageTag: '৮৫%+ সরাসরি কারিগরকে',
                mktMiddlemenTag: '১০০% মধ্যস্বত্বভোগীহীন',
                bcatAll: 'সমস্ত হস্তশিল্প',
                bcatPaint: 'মধুবনী চিত্রকর্ম',
                bcatPottery: 'খুরজা মৃৎশিল্প',
                bcatSilk: 'ভাগলপুরী তসর রেশম',
                bcatWood: 'সাহারানপুর দারুশিল্প',
                voiceWelcome: 'কলা কার্টে আপনাকে স্বাগতম।'
            },
            'mr': {
                code: 'mr',
                langName: 'मराठी',
                brandSub: 'कला कार्ट',
                gwTopBadge: 'भारतीय ग्रामीण व्हॉइस-टू-कॉमर्स मंच',
                gwTitle: 'कला कार्ट मध्ये आपले स्वागत आहे',
                gwSub: 'कृपया आपली भूमिका निवडा: कारागीर कार्यशाळेत काम करायचे आहे की थेट हस्तकला खरेदी करायची आहे?',
                gwArtisanTitle: '१. कारागीर कार्यशाळा (Artisan Hub)',
                gwArtisanDesc: '१० सेकंद स्वतःच्या भाषेत बोलून स्टुडिओ कॅटलॉग बनवा, बचत गटातून ३६% स्वस्त कच्चा माल खरेदी करा व टपाल पिकअप मिळवा.',
                gwVishBtn: 'पडताळणी करा',
                gwOtpBtn: 'OTP ऐका',
                gwLoginBtn: 'प्रवेश',
                gwRegLink: '👉 विश्वकर्मा आयडी नाही? नवीन नोंदणी करा (Get Registered)',
                gwArtisanEnterBtn: 'कारागीर कार्यशाळेत प्रवेश करा',
                gwBuyerTitle: '२. ग्राहक दस्तकार बाजार (Buyer Marketplace)',
                gwBuyerDesc: 'थेट ग्रामीण कारागिरांकडून अस्सल हस्तकला खरेदी करा. आपल्या खरेदीचा ८५%+ मोबदला थेट कारागिराच्या खात्यात जमा होतो.',
                gwH1: 'मातृभाषेत कारागिराची मूळ कथा ऐका (भाषिणी AI)',
                gwH2: 'SFURTI ग्रेड A+ लॅब व GI टॅग प्रमाणित उत्पादने',
                gwH3: 'भारतीय टपाल स्पीड पोस्टने थेट आपल्या घरी वितरण',
                gwBuyerEnterBtn: 'थेट बाजारात प्रवेश करा (Enter Marketplace)',
                navArtisanLabel: 'कारागीर कार्यशाळा',
                navBuyerLabel: 'दस्तकार बाजार',
                navEcoBtnLabel: '६ शासकीय स्तंभ',
                mktWageTag: '८५%+ थेट कारागिराला',
                mktMiddlemenTag: '१००% मध्यस्थमुक्त',
                bcatAll: 'सर्व हस्तकला',
                bcatPaint: 'मधुबनी चित्रकला',
                bcatPottery: 'खुर्जा कुंभारकाम',
                bcatSilk: 'भागलपुरी कोसा रेशीम',
                bcatWood: 'सहारनपूर काष्ठशिल्प',
                voiceWelcome: 'कला कार्ट मध्ये आपले स्वागत आहे.'
            },
            'ta': {
                code: 'ta',
                langName: 'தமிழ்',
                brandSub: 'கலா கார்ட்',
                gwTopBadge: 'இந்திய கிராமப்புற குரல் வழி வர்த்தக தளம்',
                gwTitle: 'கலா கார்ட்டுக்கு உங்களை வரவேற்கிறோம்',
                gwSub: 'தயவுசெய்து உங்கள் பங்கைத் தேர்ந்தெடுக்கவும்: கைவினைஞராக பணியாற்ற விரும்புகிறீர்களா அல்லது நேரடியாக வாங்க விரும்புகிறீர்களா?',
                gwArtisanTitle: '1. கைவினைஞர் பட்டறை (Artisan Hub)',
                gwArtisanDesc: '10 வினாடிகள் தாய்மொழியில் பேசி பட்டியல் உருவாக்குங்கள், சுயஉதவி குழு மூலம் 36% மலிவாக மூலப்பொருள் பெறுங்கள்.',
                gwVishBtn: 'சரிபார்',
                gwOtpBtn: 'OTP கேள்',
                gwLoginBtn: 'உள்நுழை',
                gwRegLink: '👉 விஸ்வகர்மா ஐடி இல்லையா? புதிய பதிவு செய்க (Get Registered)',
                gwArtisanEnterBtn: 'கைவினைஞர் பட்டறைக்குள் நுழைக',
                gwBuyerTitle: '2. வாங்குபவர் சந்தை (Buyer Marketplace)',
                gwBuyerDesc: 'கிராமப்புற கைவினைஞர்களிடமிருந்து நேரடியாக அசல் கைவினைப்பொருட்களை வாங்குங்கள். 85%+ நேரடியாக கலைஞரின் வங்கி கணக்கிற்கு செல்கிறது.',
                gwH1: 'தாய்மொழியில் கைவினைஞரின் கதையைக் கேளுங்கள் (பாஷினி AI)',
                gwH2: 'SFURTI தரம் A+ மற்றும் GI சான்றளிக்கப்பட்ட பொருட்கள்',
                gwH3: 'இந்திய அஞ்சல் ஸ்பீட் போஸ்ட் மூலம் உங்கள் வீட்டிற்கு விநியோகம்',
                gwBuyerEnterBtn: 'நேரடியாக சந்தைக்குள் நுழைக (Enter Marketplace)',
                navArtisanLabel: 'கைவினைஞர் பட்டறை',
                navBuyerLabel: 'கைவினைஞர் சந்தை',
                navEcoBtnLabel: '6 அரசு தூண்கள்',
                mktWageTag: '85%+ நேரடியாக கலைஞருக்கு',
                mktMiddlemenTag: '100% இடைத்தரகர் இல்லாதது',
                bcatAll: 'அனைத்து கைவினைப்பொருட்கள்',
                bcatPaint: 'மதுபனி ஓவியம்',
                bcatPottery: 'குர்ஜா மண்பாண்டம்',
                bcatSilk: 'பாகல்பூர் பட்டு',
                bcatWood: 'சஹாரன்பூர் மரவேலை',
                voiceWelcome: 'கலா கார்ட்டுக்கு உங்களை வரவேற்கிறோம்.'
            },
            'te': {
                code: 'te',
                langName: 'తెలుగు',
                brandSub: 'కళా కార్ట్',
                gwTopBadge: 'భారతీయ గ్రామీణ వాయిస్ కామర్స్ వేదిక',
                gwTitle: 'కళా కార్ట్‌కు మీకు స్వాగతం',
                gwSub: 'దయచేసి మీ పాత్రను ఎంచుకోండి: కళాకారునిగా పనిచేయాలనుకుంటున్నారా లేదా నేరుగా హస్తకళలను కొనాలనుకుంటున్నారా?',
                gwArtisanTitle: '1. కళాకారుల వర్క్‌షాప్ (Artisan Hub)',
                gwArtisanDesc: '10 సెకన్ల మీ మాతృభాషలో మాట్లాడి కేటలాగ్ తయారు చేయండి, స్వయం సహాయక సంఘం ద్వారా 36% చౌకగా ముడిసరుకు పొందండి.',
                gwVishBtn: 'ధృవీకరించండి',
                gwOtpBtn: 'OTP వినండి',
                gwLoginBtn: 'ప్రవేశించండి',
                gwRegLink: '👉 విశ్వకర్మ ఐడీ లేదా? కొత్త నమోదు చేయండి (Get Registered)',
                gwArtisanEnterBtn: 'కళాకారుల వర్క్‌షాప్‌లోకి ప్రవేశించండి',
                gwBuyerTitle: '2. కొనుగోలుదారుల మార్కెట్ (Buyer Marketplace)',
                gwBuyerDesc: 'గ్రామీణ కళాకారుల నుండి నేరుగా నిజమైన హస్తకళలను కొనుగోలు చేయండి. మీ కొనుగోలులో 85%+ నేరుగా కళాకారుడికి చేరుతుంది.',
                gwH1: 'మాతృభాషలో కళాకారుడి మూల కథ వినండి (భాషిణి AI)',
                gwH2: 'SFURTI గ్రేడ్ A+ మరియు GI ధృవీకరించబడిన ఉత్పత్తులు',
                gwH3: 'భారతీయ తపాలా స్పీడ్ పోస్ట్ ద్వారా నేరుగా మీ ఇంటికి డెలివరీ',
                gwBuyerEnterBtn: 'నేరుగా మార్కెట్‌లోకి ప్రవేశించండి (Enter Marketplace)',
                navArtisanLabel: 'కళాకారుల వర్క్‌షాప్',
                navBuyerLabel: 'కళాకారుల మార్కెట్',
                navEcoBtnLabel: '6 ప్రభుత్వ స్తంభాలు',
                mktWageTag: '85%+ నేరుగా కళాకారునికి',
                mktMiddlemenTag: '100% దళారులు లేనిది',
                bcatAll: 'అన్ని హస్తకళలు',
                bcatPaint: 'మధుబని చిత్రలేఖనం',
                bcatPottery: 'ఖుర్జా కుండల కళ',
                bcatSilk: 'భాగల్పూర్ టస్సార్ పట్టు',
                bcatWood: 'సహారన్‌పూర్ చెక్క కళ',
                voiceWelcome: 'కళా కార్ట్‌కు మీకు స్వాగతం.'
            },
            'en': {
                code: 'en',
                langName: 'English',
                brandSub: 'Kala Kart',
                gwTopBadge: 'Rural Indian Voice-to-Commerce Platform',
                gwTitle: 'Welcome to Kala Kart',
                gwSub: 'Please select your role: Work in the Artisan Studio or buy authentic crafts as a customer?',
                gwArtisanTitle: '1. Artisan Workspace (Artisan Hub)',
                gwArtisanDesc: 'Speak for 10 seconds in your dialect to create listings, pool bulk silk yarn with SHGs at 36% discount, and schedule Speed Post pickups.',
                gwVishBtn: 'Verify ID',
                gwOtpBtn: 'Hear OTP',
                gwLoginBtn: 'Enter',
                gwRegLink: '👉 No Vishwakarma ID? Get Registered with Gram Panchayat',
                gwArtisanEnterBtn: 'Enter Artisan Workspace',
                gwBuyerTitle: '2. Buyer Marketplace (Direct Crafts)',
                gwBuyerDesc: 'Buy authentic handmade crafts directly from rural artisans. 85%+ of your payment flows directly into the craftsperson’s bank account.',
                gwH1: 'Listen to the artisan’s original story in their dialect (Bhashini AI)',
                gwH2: 'SFURTI Grade A+ laboratory testing & GI Tag certified',
                gwH3: 'Direct dispatch from the village depot via India Post Speed Post',
                gwBuyerEnterBtn: 'Enter Buyer Marketplace',
                navArtisanLabel: 'Artisan Studio',
                navBuyerLabel: 'Buyer Market',
                navEcoBtnLabel: '6 Govt Pillars',
                mktWageTag: '85%+ Direct to Artisan',
                mktMiddlemenTag: '100% Middleman-Free',
                bcatAll: 'All Crafts',
                bcatPaint: 'Madhubani Paintings',
                bcatPottery: 'Khurja Pottery',
                bcatSilk: 'Bhagalpuri Tussar Silk',
                bcatWood: 'Saharanpur Woodcraft',
                voiceWelcome: 'Welcome to Kala Kart. Please choose your role.'
            }
        };

        // Select Initial Language (Step 0)
        function selectInitialLanguage(langCode) {
            currentLang = langCode;
            document.getElementById('initial-lang-modal').classList.add('hidden');
            applyLanguageToEntireApp(langCode);
            playVoice(I18N[langCode].voiceWelcome);
        }

        function openLanguagePicker() {
            document.getElementById('initial-lang-modal').classList.remove('hidden');
        }

        // Apply 100% strict single-language translations across the whole DOM
        function applyLanguageToEntireApp(lang) {
            const t = I18N[lang] || I18N['hi'];

            // Gateway screen elements
            setElText('gw-brand-sub', t.brandSub);
            setElText('gw-active-lang', `${t.langName} (बदलें)`);
            setElText('gw-top-badge', t.gwTopBadge);
            setElText('gw-title', t.gwTitle);
            setElText('gw-sub', t.gwSub);
            setElText('gw-artisan-title', t.gwArtisanTitle);
            setElText('gw-artisan-desc', t.gwArtisanDesc);
            setElText('gw-vish-btn', t.gwVishBtn);
            setElText('gw-otp-btn', t.gwOtpBtn);
            setElText('gw-login-btn', t.gwLoginBtn);
            setElText('gw-reg-link', t.gwRegLink);
            setElText('gw-artisan-enter-btn', t.gwArtisanEnterBtn);
            setElText('gw-buyer-title', t.gwBuyerTitle);
            setElText('gw-buyer-desc', t.gwBuyerDesc);
            setElText('gw-h1', t.gwH1);
            setElText('gw-h2', t.gwH2);
            setElText('gw-h3', t.gwH3);
            setElText('gw-buyer-enter-btn', t.gwBuyerEnterBtn);

            // Nav header elements
            setElText('nav-brand-sub', t.brandSub);
            setElText('nav-eco-btn-label', t.navEcoBtnLabel);
            setElText('nav-artisan-label', t.navArtisanLabel);
            setElText('nav-buyer-label', t.navBuyerLabel);

            // Marketplace filter pill elements
            setElText('mkt-wage-tag', t.mktWageTag);
            setElText('mkt-middlemen-tag', t.mktMiddlemenTag);
            setElText('bcat-all', t.bcatAll);
            setElText('bcat-paint', t.bcatPaint);
            setElText('bcat-pottery', t.bcatPottery);
            setElText('bcat-silk', t.bcatSilk);
            setElText('bcat-wood', t.bcatWood);

            renderAllProductViews();
        }

        function setElText(id, text) {
            const el = document.getElementById(id);
            if (el && text) el.innerText = text;
        }

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

        function renderAllProductViews() {
            renderBuyerMarketplace(cachedProducts);
            renderArtisanProducts(cachedProducts);
            lucide.createIcons();
        }

        // Render Buyer Marketplace Cards
        function renderBuyerMarketplace(products) {
            const container = document.getElementById('buyer-products-grid');
            if (!container) return;

            container.innerHTML = products.map(p => {
                const title = currentLang === 'hi' ? p.title : (currentLang === 'en' ? p.title : p.title);
                const story = currentLang === 'hi' ? p.story_hi : (p.story_en || p.story_hi);
                const voiceScript = p.raw_voice_transcript || story;
                const lifecycle = p.craft_lifecycle || [];
                const impact = p.family_impact || {};
                const gratitude = p.buyer_gratitude && p.buyer_gratitude[0] ? p.buyer_gratitude[0] : null;
                const inst = p.institutional_framework || {};

                return `
                <div class="vintage-card rounded-3xl overflow-hidden flex flex-col justify-between">
                    <!-- Card Media -->
                    <div class="relative bg-[#f6f1e9] aspect-[16/10] overflow-hidden">
                        <img src="${p.studio_image_url || p.raw_image_url}" alt="${title}" class="w-full h-full object-cover">
                        
                        <!-- GI Tag -->
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
                            
                            <!-- Voice Player with Soundwave Equalizer -->
                            <div class="flex items-center gap-3 p-2.5 bg-[#fefae0] border border-[#d4a373] rounded-2xl mb-3 shadow-[2px_2px_0px_#d4a373]">
                                <button onclick="playVoice('${voiceScript.replace(/'/g, "\\\\'")}')" class="w-9 h-9 rounded-full bg-[#c2593f] hover:bg-[#a6472e] text-white flex items-center justify-center shadow hover:scale-105 active:scale-95 transition flex-shrink-0">
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

                            <!-- Detail Toggle Buttons -->
                            <div class="flex items-center gap-2 mb-3">
                                <button onclick="toggleCardDetail('${p.id}', 'yatra')" class="px-2.5 py-1 text-[11px] font-stamp font-bold text-[#b45309] bg-[#fefae0] hover:bg-[#faedcd] border border-[#d4a373] rounded-xl transition flex items-center gap-1">
                                    <i data-lucide="compass" class="w-3.5 h-3.5 text-[#c2593f]"></i>
                                    <span>कला यात्रा (४ दिन)</span>
                                </button>
                                <button onclick="toggleCardDetail('${p.id}', 'impact')" class="px-2.5 py-1 text-[11px] font-stamp font-bold text-[#047857] bg-[#ecfdf5] hover:bg-[#d1fae5] border border-[#a7f3d0] rounded-xl transition flex items-center gap-1">
                                    <i data-lucide="heart" class="w-3.5 h-3.5 text-[#059669]"></i>
                                    <span>परिवार प्रभाव</span>
                                </button>
                                <button onclick="toggleCardDetail('${p.id}', 'ecosystem')" class="px-2.5 py-1 text-[11px] font-stamp font-bold text-[#1e3a8a] bg-[#eff6ff] hover:bg-[#dbeafe] border border-[#bfdbfe] rounded-xl transition flex items-center gap-1">
                                    <i data-lucide="landmark" class="w-3.5 h-3.5 text-[#1e3a8a]"></i>
                                    <span>६ सरकारी सत्यापन</span>
                                </button>
                            </div>

                            <!-- Collapsible 4-Step Kala Yatra -->
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
                            <!-- Collapsible 6-Stage Government Architecture Section -->
                            <div id="ecosystem-section-${p.id}" class="hidden p-3.5 bg-[#eff6ff] border-2 border-[#bfdbfe] rounded-2xl mb-3 shadow-[2px_2px_0px_#bfdbfe]">
                                <div class="flex items-center justify-between mb-2 pb-1 border-b border-dashed border-[#bfdbfe]">
                                    <span class="text-[11px] font-stamp font-bold text-[#1e3a8a] flex items-center gap-1.5">
                                        <i data-lucide="landmark" class="w-3.5 h-3.5 text-[#1e3a8a]"></i>
                                        ६-स्तरीय राष्ट्रीय सत्यापन (Govt Infrastructure)
                                    </span>
                                    <button onclick="toggleModal('ecosystem-modal')" class="text-[10px] font-stamp font-bold text-[#2563eb] hover:underline flex items-center gap-0.5">
                                        विस्तृत विवरण ↗
                                    </button>
                                </div>
                                
                                <div class="space-y-1.5 text-[10px]">
                                    <div class="p-1.5 bg-white rounded-lg border border-[#bfdbfe]/70 flex items-center justify-between">
                                        <span class="font-bold text-[#1e3a8a]">१. पीएम विश्वकर्मा:</span>
                                        <span class="font-mono text-[#047857] font-bold">${inst.stage_1_identity ? inst.stage_1_identity.vishwakarma_id : 'PMV-BH-88214'} (${inst.stage_1_identity ? inst.stage_1_identity.gp_seal : 'GP सत्यापित'})</span>
                                    </div>
                                    <div class="p-1.5 bg-white rounded-lg border border-[#bfdbfe]/70 flex items-center justify-between">
                                        <span class="font-bold text-[#1e3a8a]">२. डिजिटल सहायता केंद्र:</span>
                                        <span class="text-[#334155]">${inst.stage_2_assisted ? inst.stage_2_assisted.csc_id : 'CSC डिजिटल केंद्र #941'} • ${inst.stage_2_assisted ? inst.stage_2_assisted.vle_operator : 'VLE ऑपरेटर'}</span>
                                    </div>
                                    <div class="p-1.5 bg-white rounded-lg border border-[#bfdbfe]/70 flex items-center justify-between">
                                        <span class="font-bold text-[#1e3a8a]">३. भाषिणी MeitY AI:</span>
                                        <span class="text-[#334155]">${inst.stage_3_ai ? inst.stage_3_ai.engine : 'भाषिणी MeitY AI'} (${inst.stage_3_ai ? inst.stage_3_ai.dialect : 'स्थानीय बोली अनुवाद'})</span>
                                    </div>
                                    <div class="p-1.5 bg-white rounded-lg border border-[#bfdbfe]/70 flex items-center justify-between">
                                        <span class="font-bold text-[#1e3a8a]">४. संकलन व लॉजिस्टिक्स:</span>
                                        <span class="text-[#334155]">${inst.stage_4_aggregation ? inst.stage_4_aggregation.apc_lot : 'SHG क्लस्टर थोक लॉट'}</span>
                                    </div>
                                    <div class="p-1.5 bg-white rounded-lg border border-[#bfdbfe]/70 flex items-center justify-between">
                                        <span class="font-bold text-[#1e3a8a]">५. SFURTI CFC लैब:</span>
                                        <span class="text-[#047857] font-bold">${inst.stage_5_qc ? inst.stage_5_qc.grade : 'Grade A+'} • #${inst.stage_5_qc ? inst.stage_5_qc.barcode : 'SFURTI-CFC'}</span>
                                    </div>
                                    <div class="p-1.5 bg-white rounded-lg border border-[#bfdbfe]/70 flex items-center justify-between">
                                        <span class="font-bold text-[#1e3a8a]">६. टूल डिज़ाइन व नवाचार:</span>
                                        <span class="text-[#b45309] font-bold">${inst.stage_6_innovation ? inst.stage_6_innovation.tool : 'IIT RuTAG टूल नवाचार'}</span>
                                    </div>
                                </div>
                            </div>

                            <!-- Gratitude Wall Item -->
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

        // Render Artisan My-Products
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

        function toggleCardDetail(id, type) {
            const sec = document.getElementById(`${type}-section-${id}`);
            if (sec) sec.classList.toggle('hidden');
        }

        // Voice playback with regional dialect
        function playVoice(text) {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                const utter = new SpeechSynthesisUtterance(text);
                const langMap = { 'hi': 'hi-IN', 'bn': 'bn-IN', 'mr': 'mr-IN', 'ta': 'ta-IN', 'te': 'te-IN', 'en': 'en-IN' };
                utter.lang = langMap[currentLang] || 'hi-IN';
                utter.rate = 0.92;
                window.speechSynthesis.speak(utter);
            }
        }

        // Switch Between Views
        function switchView(view) {
            currentView = view;
            const vArtisan = document.getElementById('view-artisan');
            const vBuyer = document.getElementById('view-buyer');
            const btnArtisan = document.getElementById('nav-btn-artisan');
            const btnBuyer = document.getElementById('nav-btn-buyer');

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

        // Gateway Actions
        function enterAsArtisan() {
            document.getElementById('gateway-screen').classList.add('hidden');
            switchView('artisan');
            playVoice("कारीगर कार्यशाला में आपका स्वागत है।");
        }

        function enterAsBuyer() {
            document.getElementById('gateway-screen').classList.add('hidden');
            switchView('buyer');
            playVoice("कला कार्ट दस्तकार बाज़ार में आपका स्वागत है।");
        }

        function openGateway() {
            document.getElementById('gateway-screen').classList.remove('hidden');
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
            playVoice("नमस्ते! आपका कला कार्ट लॉगिन कोड है: पांच, चार, एक, आठ।");
        }

        // New Registration
        function openRegisterModal() {
            toggleModal('register-modal');
        }

        async function handleRegistrationSubmit(e) {
            e.preventDefault();
            const btn = document.getElementById('reg-btn-submit');
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
                    playVoice(data.voice_announcement);
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

        function setArtisanProfile(artisan) {
            currentArtisan = artisan;
            setElText('artisan-dash-name', artisan.name);
            setElText('artisan-dash-status', artisan.panchayat_seal || '✓ ग्राम पंचायत सत्यापित');
            setElText('artisan-dash-details', `${artisan.gram_panchayat} • ID: ${artisan.vishwakarma_id}`);
            setElText('artisan-dash-earnings', artisan.total_earnings || '₹42,850');
        }

        function artisanLogout() {
            currentArtisan = null;
            openGateway();
        }

        // Studio Voice Recording
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

        // India Post Pickup
        function requestIndiaPostPickup(id, title) {
            const track = `SP-IND-${Math.floor(100000 + Math.random() * 900000)}`;
            alert(`📮 भारतीय डाक स्पीड पोस्ट अनुरोध सफल!\n\n📦 शिल्प: ${title}\n🏷️ Speed Post Tracking No: ${track}\n👨‍🌾 ग्रामीण डाक सेवक आज शाम आपके पते से पार्सल संग्रह करेंगे।`);
        }

        function openPostalTag(id, artisanName) {
            setElText('tag-artisan-name', artisanName);
            setElText('tag-tracking-num', `SP-IND-${Math.floor(100000 + Math.random() * 900000)}`);
            toggleModal('postal-tag-modal');
        }

        let activeGratitudeArtisan = "";
        function openGratitudeModal(id, artisanName) {
            activeGratitudeArtisan = artisanName;
            setElText('gratitude-artisan-name', artisanName);
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
            playVoice(data.message);
        }

        async function joinBulkRawMaterials() {
            const fb = document.getElementById('bulk-fb');
            const res = await fetch('/api/shg/join-bulk-order', { method: 'POST' });
            const data = await res.json();
            fb.innerText = `✅ ${data.message}`;
            fb.classList.remove('hidden');
            playVoice(data.message);
        }

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
    content = generate_template()
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Template successfully written to {target} ({len(content)} bytes)")

if __name__ == "__main__":
    main()
