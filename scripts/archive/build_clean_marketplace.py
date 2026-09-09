import os

def generate_index_html():
    return '''<!DOCTYPE html>
<html lang="hi" class="h-full bg-[#fbf9f5]">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Artisana AI — पुश्तैनी हस्तशिल्प बाज़ार • Fair Rural Heritage</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Rozha+One&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Courier+Prime:ital,wght@0,400;0,700;1,400&display=swap');
        
        body { 
            font-family: 'Plus Jakarta Sans', sans-serif; 
            background-color: #fbf9f5;
            color: #1c1917;
        }
        
        .font-vintage { font-family: 'Rozha One', serif; }
        .font-stamp { font-family: 'Courier Prime', monospace; }

        /* Minimal Postal Stamp */
        .indie-stamp {
            border: 1px dashed #b45309;
            background: #fffdfa;
            box-shadow: 2px 2px 0px #b45309;
        }

        .craft-card {
            background: #ffffff;
            border: 1px solid #e7e5e4;
            transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .craft-card:hover {
            transform: translateY(-2px);
            border-color: #b45309;
            box-shadow: 0 10px 25px -5px rgba(180, 83, 9, 0.08);
        }

        /* Sound equalizer bar */
        .sound-wave-bar {
            display: inline-block;
            width: 3px;
            height: 12px;
            background: #b45309;
            border-radius: 2px;
            animation: bounce 0.8s ease-in-out infinite alternate;
        }
        @keyframes bounce {
            from { height: 4px; }
            to { height: 14px; }
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: #fbf9f5; }
        ::-webkit-scrollbar-thumb { background: #d6d3d1; border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: #a8a29e; }
    </style>
</head>
<body class="min-h-full flex flex-col text-[#1c1917] selection:bg-[#fef08a] selection:text-[#1c1917]">

    <!-- 1. MINIMAL EDITORIAL TOPBAR -->
    <header class="sticky top-0 z-40 bg-[#fbf9f5]/95 backdrop-blur-md border-b border-[#e7e5e4]">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
            
            <!-- Brand Mark -->
            <div class="flex items-center gap-3">
                <a href="/" class="flex items-baseline gap-2 group">
                    <span class="font-vintage text-2xl tracking-tight text-[#1c1917] group-hover:text-[#b45309] transition-colors">Artisana</span>
                    <span id="brand-subname" class="text-xs font-stamp font-medium text-[#b45309]">आर्टिसाना</span>
                </a>
                <span class="hidden md:inline-flex items-center px-2 py-0.5 rounded text-[10px] font-stamp font-bold bg-[#f5f5f4] text-[#78716c] border border-[#e7e5e4]">
                    SIH26090
                </span>
            </div>

            <!-- Search Bar with Voice Button -->
            <div class="flex-1 max-w-md hidden sm:block">
                <div class="relative flex items-center">
                    <i data-lucide="search" class="w-4 h-4 text-[#a8a29e] absolute left-3.5 pointer-events-none"></i>
                    <input type="text" id="marketplace-search" oninput="handleSearch(this.value)" placeholder="खोजें: मधुबनी, तुषार सिल्क, खुर्जा केतली..." class="w-full pl-9 pr-10 py-1.5 text-xs bg-[#f5f5f4] border border-[#e7e5e4] rounded-full focus:bg-white focus:border-[#b45309] focus:outline-none transition-all placeholder:text-[#a8a29e]">
                    <button type="button" onclick="handleVoiceSearch()" title="बोलकर खोजें" class="absolute right-2 p-1 text-[#b45309] hover:bg-[#fed7aa]/40 rounded-full transition">
                        <i data-lucide="mic" class="w-4 h-4"></i>
                    </button>
                </div>
            </div>

            <!-- Action Controls -->
            <div class="flex items-center gap-2 sm:gap-3">
                <!-- Language Selector Pill -->
                <button onclick="openLanguageModal()" class="flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-medium text-[#44403c] hover:bg-[#f5f5f4] border border-[#e7e5e4] transition">
                    <i data-lucide="languages" class="w-3.5 h-3.5 text-[#b45309]"></i>
                    <span id="current-lang-label">हिन्दी</span>
                </button>

                <!-- Artisan Corner (Login & Register) -->
                <button onclick="openArtisanModal()" id="artisan-corner-btn" class="flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-semibold bg-[#1c1917] hover:bg-[#292524] text-white shadow-sm transition">
                    <i data-lucide="user" class="w-3.5 h-3.5 text-[#fed7aa]"></i>
                    <span id="artisan-corner-label">कारीगर कॉर्नर</span>
                </button>

                <!-- Cart / Bag Button -->
                <button onclick="toggleCartDrawer()" class="relative flex items-center justify-center p-2 rounded-full text-[#1c1917] hover:bg-[#f5f5f4] border border-[#e7e5e4] transition">
                    <i data-lucide="shopping-bag" class="w-4 h-4"></i>
                    <span id="cart-count-badge" class="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-[#b45309] text-white text-[9px] font-bold flex items-center justify-center">0</span>
                </button>
            </div>

        </div>
    </header>

    <!-- LOGGED IN ARTISAN NOTIFICATION STRIP (Hidden by default) -->
    <div id="artisan-session-strip" class="hidden bg-[#fefae0] border-b border-[#fed7aa] px-4 py-2">
        <div class="max-w-7xl mx-auto flex items-center justify-between text-xs flex-wrap gap-2">
            <div class="flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-[#047857] animate-ping"></span>
                <span class="font-bold text-[#2b2d42]" id="strip-artisan-welcome">नमस्ते, रामवती देवी जी!</span>
                <span class="text-[#78716c] font-stamp" id="strip-artisan-id">ID: PMV-BH-88214</span>
                <span class="px-2 py-0.5 rounded-full bg-[#ecfdf5] text-[#047857] font-stamp text-[10px] font-bold" id="strip-artisan-seal">✓ ग्राम पंचायत सत्यापित</span>
            </div>
            <div class="flex items-center gap-3">
                <span class="font-stamp text-[#047857] font-bold" id="strip-artisan-earnings">कुल आय: ₹42,850</span>
                <button onclick="toggleModal('studio-modal')" class="px-2.5 py-1 bg-[#b45309] text-white rounded-lg text-[11px] font-semibold hover:bg-[#92400e]">
                    + नया शिल्प जोड़ें
                </button>
                <button onclick="artisanLogout()" class="text-[#78716c] hover:text-[#b45309] underline text-[11px]">
                    लॉगआउट
                </button>
            </div>
        </div>
    </div>

    <!-- 2. CRAFT CATEGORY PILL STRIP -->
    <div class="bg-[#fbf9f5] border-b border-[#e7e5e4]/60 sticky top-16 z-30 py-2.5">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center gap-2 overflow-x-auto no-scrollbar">
            <button onclick="filterCategory('all')" id="cat-pill-all" class="category-pill active px-3.5 py-1.5 rounded-full text-xs font-semibold whitespace-nowrap bg-[#1c1917] text-white transition">
                सभी हस्तशिल्प
            </button>
            <button onclick="filterCategory('Handicrafts & Painting')" id="cat-pill-paint" class="category-pill px-3.5 py-1.5 rounded-full text-xs font-medium whitespace-nowrap bg-white text-[#44403c] hover:bg-[#f5f5f4] border border-[#e7e5e4] transition">
                मधुबनी चित्रकला
            </button>
            <button onclick="filterCategory('Pottery & Ceramics')" id="cat-pill-pottery" class="category-pill px-3.5 py-1.5 rounded-full text-xs font-medium whitespace-nowrap bg-white text-[#44403c] hover:bg-[#f5f5f4] border border-[#e7e5e4] transition">
                खुर्जा पॉटरी व सिरेमिक
            </button>
            <button onclick="filterCategory('Textiles & Weaving')" id="cat-pill-textiles" class="category-pill px-3.5 py-1.5 rounded-full text-xs font-medium whitespace-nowrap bg-white text-[#44403c] hover:bg-[#f5f5f4] border border-[#e7e5e4] transition">
                भागलपुरी सिल्क वस्त्र
            </button>
            <button onclick="filterCategory('Woodcraft & Carving')" id="cat-pill-wood" class="category-pill px-3.5 py-1.5 rounded-full text-xs font-medium whitespace-nowrap bg-white text-[#44403c] hover:bg-[#f5f5f4] border border-[#e7e5e4] transition">
                सहारनपुर काष्ठ शिल्प
            </button>
            
            <div class="h-4 w-[1px] bg-[#d6d3d1] mx-1"></div>

            <!-- Quick Access Badges -->
            <button onclick="openEcosystemModal()" class="flex items-center gap-1 px-3 py-1.5 rounded-full text-xs font-stamp font-semibold bg-[#eff6ff] text-[#1e3a8a] border border-[#bfdbfe] hover:bg-[#dbeafe] whitespace-nowrap transition">
                <i data-lucide="landmark" class="w-3 h-3"></i>
                <span id="quick-eco-label">६ सरकारी सत्यापन</span>
            </button>
            <button onclick="openShgModal()" class="flex items-center gap-1 px-3 py-1.5 rounded-full text-xs font-stamp font-semibold bg-[#fefae0] text-[#b45309] border border-[#fed7aa] hover:bg-[#faedcd] whitespace-nowrap transition">
                <i data-lucide="users" class="w-3 h-3"></i>
                <span id="quick-shg-label">महिला SHG क्लस्टर</span>
            </button>
        </div>
    </div>

    <!-- 3. COMPACT EDITORIAL HERO (Calm, Soulful, No Clutter) -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-8 pb-4">
        <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 pb-6 border-b border-[#e7e5e4]">
            <div class="max-w-2xl">
                <div class="flex items-center gap-2 mb-2">
                    <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-[11px] font-stamp font-bold bg-[#ecfdf5] text-[#047857] border border-[#a7f3d0]">
                        १० सेकंड वॉइस-टू-कॉमर्स • ८५%+ सीधा पारिश्रमिक
                    </span>
                </div>
                <h1 id="hero-title" class="font-vintage text-3xl sm:text-4xl lg:text-5xl text-[#1c1917] tracking-tight leading-tight">
                    पुश्तैनी कला साधना, सीधा गाँव से।
                </h1>
                <p id="hero-desc" class="text-sm text-[#78716c] mt-2 leading-relaxed font-light">
                    मातृभाषा की आवाज से सत्यापित भारतीय हस्तशिल्प। हर खरीद का अधिकांश हिस्सा सीधा कारीगर के बैंक खाते में जाता है, बिना किसी बिचौलिए के।
                </p>
            </div>

            <!-- Voice Studio Launch Pill -->
            <div class="flex items-center gap-3">
                <button onclick="toggleModal('studio-modal')" class="flex items-center gap-2 px-4 py-2.5 rounded-xl bg-[#b45309] hover:bg-[#92400e] text-white text-xs font-semibold shadow-sm transition">
                    <i data-lucide="mic" class="w-4 h-4"></i>
                    <span id="hero-studio-btn">कारीगर स्टूडियो (आवाज़ से जोड़ें)</span>
                </button>
            </div>
        </div>
    </section>

    <!-- 4. PRODUCT CATALOG GRID -->
    <main class="flex-1 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 w-full">
        <!-- Grid Header -->
        <div class="flex items-center justify-between mb-6">
            <span class="text-xs font-stamp font-bold text-[#78716c] uppercase tracking-wider">
                <span id="catalog-counter">४</span> शिल्प उपलब्ध
            </span>
            <span class="text-xs font-stamp text-[#047857] font-semibold flex items-center gap-1">
                <i data-lucide="truck" class="w-3.5 h-3.5"></i>
                स्पीड पोस्ट ग्रामीण संकलन सक्रिय
            </span>
        </div>

        <!-- Cards Container -->
        <div id="products-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <!-- Rendered by JS -->
        </div>
    </main>

    <!-- 5. MINIMAL FOOTER -->
    <footer class="bg-[#f5f5f4] border-t border-[#e7e5e4] mt-16 py-10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-[#78716c] font-stamp">
            <div class="flex items-center gap-2">
                <span class="font-vintage text-base text-[#1c1917]">Artisana AI</span>
                <span>• PM Vishwakarma, NRLM SHG, Bhashini (MeitY) & SFURTI समर्थित</span>
            </div>
            <div class="flex items-center gap-4">
                <span>स्मार्ट इंडिया हैकाथॉन २०२६</span>
                <span>समस्या क्रमांक: SIH26090</span>
            </div>
        </div>
    </footer>

    <!-- ==================== MODALS & DRAWERS ==================== -->

    <!-- HERITAGE PASSPORT MODAL (Comprehensive Craft & Govt Provenance) -->
    <div id="passport-modal" class="fixed inset-0 z-50 hidden bg-[#1c1917]/70 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl max-w-2xl w-full p-6 sm:p-8 shadow-2xl border border-[#e7e5e4] relative max-h-[92vh] overflow-y-auto">
            <button onclick="toggleModal('passport-modal')" class="absolute top-5 right-5 text-[#a8a29e] hover:text-[#1c1917] p-1.5 rounded-full hover:bg-[#f5f5f4]">
                <i data-lucide="x" class="w-5 h-5"></i>
            </button>

            <div id="passport-content">
                <!-- Dynamically loaded by openPassportModal(productId) -->
            </div>
        </div>
    </div>

    <!-- CART / BAG SLIDE-OVER DRAWER -->
    <div id="cart-drawer" class="fixed inset-0 z-50 hidden">
        <div class="absolute inset-0 bg-[#1c1917]/50 backdrop-blur-xs" onclick="toggleCartDrawer()"></div>
        <div class="absolute right-0 top-0 bottom-0 w-full max-w-md bg-white shadow-2xl flex flex-col justify-between p-6">
            <div>
                <div class="flex items-center justify-between pb-4 border-b border-[#e7e5e4]">
                    <h3 class="font-vintage text-xl text-[#1c1917]">आपका झोला (Shopping Bag)</h3>
                    <button onclick="toggleCartDrawer()" class="p-1 text-[#a8a29e] hover:text-[#1c1917]">
                        <i data-lucide="x" class="w-5 h-5"></i>
                    </button>
                </div>
                
                <div id="cart-items-container" class="py-4 space-y-3">
                    <p class="text-xs text-[#78716c] font-stamp text-center py-8">झोला खाली है। पसंदीदा शिल्प जोड़ें।</p>
                </div>
            </div>

            <div class="pt-4 border-t border-[#e7e5e4] space-y-3">
                <div class="flex justify-between text-sm font-semibold">
                    <span>कुल मूल्य:</span>
                    <span id="cart-total-amount" class="font-vintage text-lg">₹0</span>
                </div>
                <div class="p-3 bg-[#ecfdf5] border border-[#a7f3d0] rounded-xl text-xs text-[#065f46]">
                    <b>सीधा पारिश्रमिक प्रभाव:</b> <span id="cart-artisan-share">₹0 (८५%)</span> कारीगर के खाते में तुरंत जमा होगा।
                </div>
                <button onclick="handleCheckout()" class="w-full py-3 bg-[#b45309] hover:bg-[#92400e] text-white text-xs font-semibold rounded-xl transition shadow">
                    स्पीड पोस्ट से मँगवाएँ (Order via India Post)
                </button>
            </div>
        </div>
    </div>

    <!-- ARTISAN AUTH & REGISTRATION MODAL (With "Get Registered" Option) -->
    <div id="artisan-auth-modal" class="fixed inset-0 z-50 hidden bg-[#1c1917]/70 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-[#fffdfa] rounded-3xl max-w-lg w-full p-6 sm:p-8 shadow-2xl border-2 border-[#1c1917] relative">
            <button onclick="toggleModal('artisan-auth-modal')" class="absolute top-5 right-5 text-[#a8a29e] hover:text-[#1c1917] p-1">
                <i data-lucide="x" class="w-5 h-5"></i>
            </button>

            <!-- Modal Tabs: Login vs New Registration -->
            <div class="flex border-b border-[#e7e5e4] mb-6">
                <button onclick="switchAuthTab('login')" id="tab-btn-login" class="flex-1 pb-3 text-xs font-semibold text-[#b45309] border-b-2 border-[#b45309]">
                    कारीगर प्रवेश (Login)
                </button>
                <button onclick="switchAuthTab('register')" id="tab-btn-register" class="flex-1 pb-3 text-xs font-semibold text-[#78716c] hover:text-[#1c1917]">
                    नया पंजीकरण (Get Registered)
                </button>
            </div>

            <!-- TAB 1: EXISTING LOGIN -->
            <div id="auth-panel-login" class="space-y-4">
                <div class="p-3 bg-[#ecfdf5] border border-[#a7f3d0] rounded-xl flex items-center gap-2.5">
                    <button type="button" onclick="speakLoginGuide()" class="w-8 h-8 rounded-full bg-[#047857] text-white flex items-center justify-center flex-shrink-0">
                        <i data-lucide="volume-2" class="w-4 h-4"></i>
                    </button>
                    <div>
                        <span class="text-xs font-bold text-[#065f46] block">आवाज़ से निर्देश सुनें</span>
                        <span class="text-[10px] font-stamp text-[#047857]">शून्य-टाइपिंग ग्रामीण प्रवेश</span>
                    </div>
                </div>

                <!-- Option A: PM Vishwakarma ID -->
                <div class="p-4 bg-white rounded-2xl border border-[#e7e5e4] shadow-sm">
                    <span class="text-[10px] font-stamp font-bold text-[#1e3a8a] bg-[#eff6ff] px-2 py-0.5 rounded">विकल्प १</span>
                    <h4 class="font-vintage text-base text-[#1c1917] mt-1 mb-2">पीएम विश्वकर्मा आईडी (1-Tap)</h4>
                    <div class="flex gap-2">
                        <input type="text" id="login-vishwakarma-id" value="PMV-BH-88214" class="flex-1 px-3 py-2 text-xs font-mono font-bold bg-[#f5f5f4] border border-[#e7e5e4] rounded-xl focus:bg-white focus:outline-none">
                        <button type="button" onclick="handlePmVishwakarmaLogin()" class="px-3.5 py-2 bg-[#1e3a8a] hover:bg-[#172554] text-white font-semibold text-xs rounded-xl transition">
                            सत्यापित करें
                        </button>
                    </div>
                </div>

                <!-- Option B: Voice OTP -->
                <div class="p-4 bg-white rounded-2xl border border-[#e7e5e4] shadow-sm">
                    <span class="text-[10px] font-stamp font-bold text-[#b45309] bg-[#fefae0] px-2 py-0.5 rounded">विकल्प २</span>
                    <h4 class="font-vintage text-base text-[#1c1917] mt-1 mb-2">मोबाइल नंबर + बोलता OTP</h4>
                    <div class="flex gap-2 mb-2">
                        <input type="tel" id="login-phone" value="9876543210" placeholder="१० अंकों का नंबर" class="flex-1 px-3 py-2 text-xs bg-[#f5f5f4] border border-[#e7e5e4] rounded-xl focus:bg-white focus:outline-none">
                        <button type="button" onclick="speakArtisanOTP()" class="px-3 py-2 bg-[#f5f5f4] hover:bg-[#e7e5e4] text-[#44403c] text-xs font-stamp rounded-xl transition flex items-center gap-1">
                            <i data-lucide="volume-2" class="w-3.5 h-3.5"></i>
                            <span>OTP सुनें</span>
                        </button>
                    </div>
                    <div class="flex gap-2">
                        <input type="text" id="login-otp" value="5418" class="w-28 text-center px-3 py-2 text-xs font-bold font-mono tracking-widest bg-[#f5f5f4] border border-[#e7e5e4] rounded-xl focus:bg-white focus:outline-none">
                        <button type="button" onclick="handleArtisanPhoneLogin()" class="flex-1 py-2 bg-[#b45309] hover:bg-[#92400e] text-white text-xs font-semibold rounded-xl transition">
                            प्रवेश करें
                        </button>
                    </div>
                </div>

                <!-- Option C: Postal Passbook QR -->
                <button type="button" onclick="handlePassbookScan()" class="w-full py-2.5 bg-[#f5f5f4] hover:bg-[#e7e5e4] text-[#1c1917] text-xs font-stamp font-bold rounded-xl border border-[#e7e5e4] transition flex items-center justify-center gap-2">
                    <i data-lucide="qr-code" class="w-4 h-4"></i>
                    <span>डाक कला पासबुक (QR स्कैन करें)</span>
                </button>
            </div>

            <!-- TAB 2: NEW REGISTRATION (For Artisans without Vishwakarma ID) -->
            <div id="auth-panel-register" class="hidden space-y-4">
                <div class="p-3 bg-[#eff6ff] border border-[#bfdbfe] rounded-xl">
                    <span class="text-xs font-bold text-[#1e3a8a] block">ग्राम पंचायत व पीएम विश्वकर्मा नया पंजीकरण</span>
                    <span class="text-[11px] text-[#3b82f6]">यदि आपके पास आईडी नहीं है, तो यहाँ अपना विवरण दर्ज करें।</span>
                </div>

                <form onsubmit="handleNewRegistration(event)" class="space-y-3">
                    <div>
                        <label class="block text-[11px] font-stamp text-[#78716c] uppercase mb-1">कारीगर का नाम *</label>
                        <input type="text" id="reg-artisan-name" required value="कमला देवी" class="w-full px-3 py-2 text-xs bg-white border border-[#e7e5e4] rounded-xl focus:border-[#b45309] focus:outline-none">
                    </div>

                    <div>
                        <label class="block text-[11px] font-stamp text-[#78716c] uppercase mb-1">शिल्प विधा / कार्य *</label>
                        <select id="reg-craft-trade" class="w-full px-3 py-2 text-xs bg-white border border-[#e7e5e4] rounded-xl focus:border-[#b45309] focus:outline-none">
                            <option value="मधुबनी चित्रकला">मधुबनी चित्रकला (Painting)</option>
                            <option value="खुर्जा पॉटरी व मिट्टी शिल्प">खुर्जा पॉटरी व मिट्टी शिल्प (Pottery)</option>
                            <option value="हस्तकरघा रेशम बुनाई">हस्तकरघा रेशम बुनाई (Handloom Weaving)</option>
                            <option value="काष्ठ नक्काशी शिल्प">काष्ठ नक्काशी शिल्प (Woodcraft)</option>
                        </select>
                    </div>

                    <div class="grid grid-cols-2 gap-2">
                        <div>
                            <label class="block text-[11px] font-stamp text-[#78716c] uppercase mb-1">ग्राम पंचायत *</label>
                            <input type="text" id="reg-panchayat" required value="रंती ग्राम पंचायत, बिहार" class="w-full px-3 py-2 text-xs bg-white border border-[#e7e5e4] rounded-xl focus:border-[#b45309] focus:outline-none">
                        </div>
                        <div>
                            <label class="block text-[11px] font-stamp text-[#78716c] uppercase mb-1">मोबाइल नंबर *</label>
                            <input type="tel" id="reg-phone" required value="9876543210" class="w-full px-3 py-2 text-xs bg-white border border-[#e7e5e4] rounded-xl focus:border-[#b45309] focus:outline-none">
                        </div>
                    </div>

                    <div class="flex items-start gap-2 pt-1">
                        <input type="checkbox" id="reg-assist-check" checked class="mt-0.5 rounded text-[#b45309]">
                        <label for="reg-assist-check" class="text-[11px] text-[#44403c] leading-tight">
                            <b>कला सखी / CSC VLE सहायता:</b> घर आकर बायोमेट्रिक सत्यापन और ₹15,000 टूलकिट सहायता दर्ज करें।
                        </label>
                    </div>

                    <button type="submit" id="reg-submit-btn" class="w-full py-3 bg-[#047857] hover:bg-[#065f46] text-white font-semibold text-xs rounded-xl shadow transition mt-2">
                        पंजीकरण दर्ज करें व तुरंत जुड़ें (Get Registered)
                    </button>
                </form>
                <div id="reg-feedback-msg" class="hidden p-2.5 bg-[#ecfdf5] border border-[#a7f3d0] rounded-xl text-xs font-bold text-[#065f46]"></div>
            </div>

        </div>
    </div>

    <!-- LANGUAGE GATEWAY MODAL -->
    <div id="language-modal" class="fixed inset-0 z-50 hidden bg-[#1c1917]/70 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl max-w-sm w-full p-6 shadow-2xl border border-[#e7e5e4] text-center">
            <h3 class="font-vintage text-2xl text-[#1c1917] mb-1">मातृभाषा का चयन करें</h3>
            <p class="text-xs text-[#78716c] mb-5">Select Your Regional Language</p>

            <div class="grid grid-cols-2 gap-2 mb-6">
                <button onclick="changeAppLang('hi')" class="p-3 rounded-xl border border-[#e7e5e4] hover:border-[#b45309] hover:bg-[#fefae0] text-sm font-semibold transition">
                    हिन्दी
                </button>
                <button onclick="changeAppLang('bn')" class="p-3 rounded-xl border border-[#e7e5e4] hover:border-[#b45309] hover:bg-[#fefae0] text-sm font-semibold transition">
                    বাংলা
                </button>
                <button onclick="changeAppLang('mr')" class="p-3 rounded-xl border border-[#e7e5e4] hover:border-[#b45309] hover:bg-[#fefae0] text-sm font-semibold transition">
                    मराठी
                </button>
                <button onclick="changeAppLang('ta')" class="p-3 rounded-xl border border-[#e7e5e4] hover:border-[#b45309] hover:bg-[#fefae0] text-sm font-semibold transition">
                    தமிழ்
                </button>
                <button onclick="changeAppLang('te')" class="p-3 rounded-xl border border-[#e7e5e4] hover:border-[#b45309] hover:bg-[#fefae0] text-sm font-semibold transition">
                    తెలుగు
                </button>
                <button onclick="changeAppLang('en')" class="p-3 rounded-xl border border-[#e7e5e4] hover:border-[#b45309] hover:bg-[#fefae0] text-sm font-semibold transition">
                    English
                </button>
            </div>

            <button onclick="toggleModal('language-modal')" class="text-xs font-stamp text-[#78716c] hover:underline">
                बंद करें (Close)
            </button>
        </div>
    </div>

    <!-- 6-STAGE GOVT ECOSYSTEM MODAL (Accessible from top bar) -->
    <div id="ecosystem-modal" class="fixed inset-0 z-50 hidden bg-[#1c1917]/75 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl max-w-3xl w-full p-6 sm:p-8 shadow-2xl border border-[#e7e5e4] relative max-h-[90vh] overflow-y-auto">
            <button onclick="toggleModal('ecosystem-modal')" class="absolute top-5 right-5 text-[#a8a29e] hover:text-[#1c1917] p-1">
                <i data-lucide="x" class="w-5 h-5"></i>
            </button>

            <div class="flex items-center gap-3 mb-6 pb-4 border-b border-[#e7e5e4]">
                <div class="w-10 h-10 rounded-xl bg-[#eff6ff] text-[#1e3a8a] flex items-center justify-center">
                    <i data-lucide="landmark" class="w-5 h-5"></i>
                </div>
                <div>
                    <h3 class="font-vintage text-2xl text-[#1c1917]">राष्ट्रीय संस्थागत व सरकारी सहायता ढाँचा</h3>
                    <p class="text-xs text-[#78716c] font-stamp">६ मंत्रालयों व योजनाओं का ग्रामीण कारीगरों के साथ सीधा जुड़ाव</p>
                </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                <div class="p-3.5 bg-[#f8fafc] rounded-2xl border border-[#e2e8f0]">
                    <b class="text-[#1e3a8a] block font-stamp">१. पीएम विश्वकर्मा व ग्राम पंचायत</b>
                    <span class="text-[#64748b] block text-[11px] mt-1">शून्य फर्जी विक्रेता • सीधा नेशनल पोर्टल से सत्यापित आईडी</span>
                </div>
                <div class="p-3.5 bg-[#f8fafc] rounded-2xl border border-[#e2e8f0]">
                    <b class="text-[#b45309] block font-stamp">२. CSC कॉमन सर्विस सेंटर व VLE</b>
                    <span class="text-[#64748b] block text-[11px] mt-1">बिना स्मार्टफोन वाले शिल्पकारों हेतु गाँव में डिजिटल फोटो सहायता</span>
                </div>
                <div class="p-3.5 bg-[#f8fafc] rounded-2xl border border-[#e2e8f0]">
                    <b class="text-[#047857] block font-stamp">३. भाषिणी (MeitY) वॉइस एआई</b>
                    <span class="text-[#64748b] block text-[11px] mt-1">स्थानीय ग्रामीण बोलियों का बहुभाषी उत्पाद विवरण में स्वतः रूपांतरण</span>
                </div>
                <div class="p-3.5 bg-[#f8fafc] rounded-2xl border border-[#e2e8f0]">
                    <b class="text-[#c2410c] block font-stamp">४. महिला SHG व APC संकलन</b>
                    <span class="text-[#64748b] block text-[11px] mt-1">थोक बी२बी आर्डर पूर्ति व गाँव स्तर पर एकल डाकघर संकलन केंद्र</span>
                </div>
                <div class="p-3.5 bg-[#f8fafc] rounded-2xl border border-[#e2e8f0]">
                    <b class="text-[#7e22ce] block font-stamp">५. SFURTI कॉमन फैसिलिटी सेंटर्स</b>
                    <span class="text-[#64748b] block text-[11px] mt-1">Grade A+ गुणवत्ता जांच, बारकोड टैगिंग व सुरक्षित निर्यात पैकेजिंग</span>
                </div>
                <div class="p-3.5 bg-[#f8fafc] rounded-2xl border border-[#e2e8f0]">
                    <b class="text-[#be123c] block font-stamp">६. RuTAG (IITs) व बुनकर सेवा केंद्र</b>
                    <span class="text-[#64748b] block text-[11px] mt-1">बाज़ार मांग का सीधा फीडबैक लूप और एर्गोनॉमिक औजार नवाचार</span>
                </div>
            </div>
        </div>
    </div>

    <!-- SHG CLUSTER HUB MODAL -->
    <div id="shg-modal" class="fixed inset-0 z-50 hidden bg-[#1c1917]/75 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl max-w-xl w-full p-6 shadow-2xl border border-[#e7e5e4] relative max-h-[90vh] overflow-y-auto">
            <button onclick="toggleModal('shg-modal')" class="absolute top-5 right-5 text-[#a8a29e] hover:text-[#1c1917] p-1">
                <i data-lucide="x" class="w-5 h-5"></i>
            </button>

            <div class="flex items-center gap-3 mb-5 pb-3 border-b border-[#e7e5e4]">
                <div class="w-10 h-10 rounded-xl bg-[#fefae0] text-[#b45309] flex items-center justify-center">
                    <i data-lucide="users" class="w-5 h-5"></i>
                </div>
                <div>
                    <h3 class="font-vintage text-xl text-[#1c1917]">गंगा महिला स्वयं सहायता समूह</h3>
                    <p class="text-xs text-[#78716c] font-stamp">क्लस्टर #14 • 18 महिला दस्तकार दीदियाँ</p>
                </div>
            </div>

            <div class="space-y-3 text-xs">
                <div class="p-3.5 bg-[#fffdfa] rounded-xl border border-[#fed7aa]">
                    <div class="flex items-center justify-between mb-1">
                        <b class="text-[#b45309]">🧕 कला सखी दीदी ऑनबोर्डिंग</b>
                        <span class="text-[10px] font-stamp text-[#047857] font-bold">सुनीता दीदी सक्रिय</span>
                    </div>
                    <p class="text-[#78716c] text-[11px]">स्मार्टफोन न होने पर कला सखी दीदी घर आकर वॉइस स्टोरी रिकॉर्ड करेंगी।</p>
                    <button onclick="requestKalaSakhi()" class="mt-2 px-3 py-1.5 bg-[#b45309] text-white text-[11px] font-semibold rounded-lg">
                        कला सखी दीदी को घर बुलाएँ
                    </button>
                    <div id="sakhi-feedback" class="hidden mt-2 p-2 bg-[#ecfdf5] text-[#065f46] font-bold rounded"></div>
                </div>

                <div class="p-3.5 bg-[#fefae0] rounded-xl border border-[#d4a373]">
                    <div class="flex items-center justify-between mb-1">
                        <b class="text-[#1c1917]">📦 सामूहिक कच्चा माल थोक खरीद</b>
                        <span class="text-[10px] font-bold text-[#047857] bg-white px-2 py-0.5 rounded">36% बचत</span>
                    </div>
                    <p class="text-[#78716c] text-[11px]">भागलपुरी कोसा सिल्क यार्न थोक खरीद: ₹1,150/kg (बाज़ार: ₹1,800/kg)।</p>
                    <button onclick="joinBulkRawMaterials()" class="mt-2 px-3 py-1.5 bg-[#047857] text-white text-[11px] font-semibold rounded-lg">
                        सामूहिक आर्डर में जुड़ें (-₹3,250 बचत)
                    </button>
                    <div id="bulk-feedback" class="hidden mt-2 p-2 bg-white text-[#047857] font-bold rounded"></div>
                </div>
            </div>
        </div>
    </div>

    <!-- VOICE STUDIO MODAL (Upload / Record Craft Item) -->
    <div id="studio-modal" class="fixed inset-0 z-50 hidden bg-[#1c1917]/75 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl max-w-lg w-full p-6 sm:p-8 shadow-2xl border border-[#e7e5e4] relative">
            <button onclick="toggleModal('studio-modal')" class="absolute top-5 right-5 text-[#a8a29e] hover:text-[#1c1917] p-1">
                <i data-lucide="x" class="w-5 h-5"></i>
            </button>

            <div class="text-center mb-6">
                <span class="w-12 h-12 rounded-full bg-[#fefae0] text-[#b45309] inline-flex items-center justify-center mb-2">
                    <i data-lucide="mic" class="w-6 h-6"></i>
                </span>
                <h3 class="font-vintage text-2xl text-[#1c1917]">१० सेकंड वॉइस स्टूडियो</h3>
                <p class="text-xs text-[#78716c]">अपनी भाषा में बोलें, एआई स्टूडियो कैटलॉग तैयार करेगा</p>
            </div>

            <form onsubmit="handleStudioSubmit(event)" class="space-y-4">
                <div>
                    <label class="block text-xs font-stamp text-[#78716c] uppercase mb-1">शिल्प की कच्ची तस्वीर</label>
                    <input type="file" id="studio-photo" accept="image/*" class="w-full text-xs text-[#78716c] file:mr-3 file:py-2 file:px-4 file:rounded-xl file:border-0 file:text-xs file:font-semibold file:bg-[#f5f5f4] file:text-[#1c1917] hover:file:bg-[#e7e5e4]">
                </div>

                <div class="p-4 bg-[#fbf9f5] border border-[#e7e5e4] rounded-2xl text-center">
                    <button type="button" onclick="toggleVoiceRecording()" id="voice-rec-btn" class="w-14 h-14 rounded-full bg-[#b45309] text-white inline-flex items-center justify-center shadow-lg hover:scale-105 active:scale-95 transition">
                        <i data-lucide="mic" class="w-6 h-6"></i>
                    </button>
                    <span id="voice-rec-status" class="block text-xs text-[#78716c] font-stamp mt-2 font-semibold">माइक्रोफ़ोन दबाएँ और १० सेकंड बोलें</span>
                </div>

                <button type="submit" class="w-full py-3 bg-[#1c1917] hover:bg-[#292524] text-white font-semibold text-xs rounded-xl transition shadow">
                    कैटलॉग तैयार करें व बाज़ार में जोड़ें
                </button>
            </form>
        </div>
    </div>

    <!-- JAVASCRIPT LOGIC -->
    <script>
        let selectedLang = 'hi';
        let cachedProducts = [];
        let cart = [];
        let currentArtisan = null;
        let isRecording = false;

        // I18N LOCALIZATION DICTIONARY
        const I18N = {
            'hi': {
                brandSub: 'आर्टिसाना',
                heroTitle: 'पुश्तैनी कला साधना, सीधा गाँव से।',
                heroDesc: 'मातृभाषा की आवाज से सत्यापित भारतीय हस्तशिल्प। हर खरीद का अधिकांश हिस्सा सीधा कारीगर के बैंक खाते में जाता है, बिना किसी बिचौलिए के।',
                heroStudioBtn: 'कारीगर स्टूडियो (आवाज़ से जोड़ें)',
                artisanCornerLabel: 'कारीगर कॉर्नर',
                allCrafts: 'सभी हस्तशिल्प',
                searchPlaceholder: 'खोजें: मधुबनी, तुषार सिल्क, खुर्जा केतली...',
                directWageShare: '८५% सीधा कारीगर को',
                listenVoiceSnippet: 'आवाज़ सुनें 🔊',
                addToBag: 'बैग में जोड़ें',
                passportBtn: 'विरासत पासपोर्ट 📜',
                giCertified: 'GI प्रमाणित',
                sfurtiGrade: 'SFURTI CFC • Grade A+'
            },
            'bn': {
                brandSub: 'আর্টিসানা',
                heroTitle: 'ঐতিহ্যবাহী গ্রামীণ শিল্প, সরাসরি তাঁত থেকে।',
                heroDesc: 'মাতৃভাষার বর্ণনায় তৈরি ভারতের প্রথম ভয়েস কমার্স প্ল্যাটফর্ম। প্রতিটি ক্রয়ের ৮৫%+ সরাসরি শিল্পীর ব্যাংক অ্যাকাউন্টে যায়।',
                heroStudioBtn: 'কারিগর স্টুডিও (ভয়েস)',
                artisanCornerLabel: 'কারিগর কর্নার',
                allCrafts: 'সমস্ত হস্তশিল্প',
                searchPlaceholder: 'খুঁজুন: মধুবনী, তসর সিল্ক, খুরজা কেটলি...',
                directWageShare: '৮৫% সরাসরি কারিগরের কাছে',
                listenVoiceSnippet: 'কণ্ঠস্বর শুনুন 🔊',
                addToBag: 'ব্যাগে যোগ করুন',
                passportBtn: 'ঐতিহ্য পাসপোর্ট 📜',
                giCertified: 'GI প্রত্যয়িত',
                sfurtiGrade: 'SFURTI CFC • গ্রেড A+'
            },
            'mr': {
                brandSub: 'आर्टिसाना',
                heroTitle: 'परंपरागत हस्तकला, थेट ग्रामीण भागातून.',
                heroDesc: 'मातृभाषेतील आवाजातून साकारलेली भारतीय हस्तकला. प्रत्येक खरेदीचा ८५%+ मोबदला थेट कारागिराच्या बँक खात्यात.',
                heroStudioBtn: 'कारागीर स्टुडिओ (आवाजाने जोडा)',
                artisanCornerLabel: 'कारागीर कॉर्नर',
                allCrafts: 'सर्व हस्तकला',
                searchPlaceholder: 'शोधा: मधुबनी, कोसा सिल्क, खुर्जा किटली...',
                directWageShare: '८५% थेट कारागिराला',
                listenVoiceSnippet: 'आवाज ऐका 🔊',
                addToBag: 'पिशवीत जोडा',
                passportBtn: 'वारसा पासपोर्ट 📜',
                giCertified: 'GI प्रमाणित',
                sfurtiGrade: 'SFURTI CFC • ग्रेड A+'
            },
            'ta': {
                brandSub: 'ஆர்ட்டிசானா',
                heroTitle: 'பாரம்பரிய கைவினை, கிராமத்து தறியிலிருந்து.',
                heroDesc: 'தாய்மொழி குரல் மூலம் உருவாக்கப்பட்ட இந்தியாவின் முதல் நேரடி கைவினை சந்தை. 85%+ நேரடியாக கலைஞரின் வங்கி கணக்கிற்கு.',
                heroStudioBtn: 'கைவினைஞர் ஸ்டுடியோ',
                artisanCornerLabel: 'கைவினைஞர் பகுதி',
                allCrafts: 'அனைத்து கைவினைப்பொருட்கள்',
                searchPlaceholder: 'தேடுக: மதுபனி, டஸ்ஸார் பட்டு, குர்ஜா கெட்டில்...',
                directWageShare: '85% நேரடியாக கலைஞருக்கு',
                listenVoiceSnippet: 'குரல் கேளுங்கள் 🔊',
                addToBag: 'பையில் சேர்க்கவும்',
                passportBtn: 'பாரம்பரிய பாஸ்போர்ட் 📜',
                giCertified: 'GI சான்றளிக்கப்பட்டது',
                sfurtiGrade: 'SFURTI CFC • தரம் A+'
            },
            'te': {
                brandSub: 'ఆర్టిసానా',
                heroTitle: 'సాంప్రదాయ హస్తకళ, నేరుగా గ్రామీణ మగ్గం నుండి.',
                heroDesc: 'మాతృభాష స్వరంతో ధృవీకరించబడిన హస్తకళలు. ప్రతి కొనుగోలులో 85%+ నేరుగా కళాకారుడి బ్యాంక్ ఖాతాకు చేరుతుంది.',
                heroStudioBtn: 'కళాకారుల స్టూడియో',
                artisanCornerLabel: 'కళాకారుల మూల',
                allCrafts: 'అన్ని హస్తకళలు',
                searchPlaceholder: 'వెతకండి: మధుబని, టస్సార్ సిల్క్, ఖుర్జా కేటిల్...',
                directWageShare: '85% నేరుగా కళాకారునికి',
                listenVoiceSnippet: 'వాయిస్ వినండి 🔊',
                addToBag: 'బ్యాగ్‌లో చేర్చండి',
                passportBtn: 'వారసత్వ పాస్‌పోర్ట్ 📜',
                giCertified: 'GI ధృవీకరించబడింది',
                sfurtiGrade: 'SFURTI CFC • గ్రేడ్ A+'
            },
            'en': {
                brandSub: 'Artisana',
                heroTitle: 'Heritage Craftsmanship, Straight from the Loom.',
                heroDesc: 'Empowered by 10-second regional voice recordings. 85%+ of every purchase flows directly into rural artisans’ bank accounts without middlemen.',
                heroStudioBtn: 'Artisan Studio (Voice)',
                artisanCornerLabel: 'Artisan Hub',
                allCrafts: 'All Crafts',
                searchPlaceholder: 'Search: Madhubani, Tussar Silk, Khurja Kettle...',
                directWageShare: '85% Direct to Artisan',
                listenVoiceSnippet: 'Listen Story 🔊',
                addToBag: 'Add to Bag',
                passportBtn: 'Heritage Passport 📜',
                giCertified: 'GI Certified',
                sfurtiGrade: 'SFURTI CFC • Grade A+'
            }
        };

        // Fetch products from API
        async function fetchProducts() {
            try {
                const res = await fetch('/api/products');
                const data = await res.json();
                cachedProducts = data.products || [];
                renderMarketplace(cachedProducts);
            } catch (err) {
                console.error("Failed to load products:", err);
            }
        }

        // Render Minimal Editorial Marketplace Cards
        function renderMarketplace(products) {
            const container = document.getElementById('products-grid');
            if (!container) return;
            const counter = document.getElementById('catalog-counter');
            if (counter) counter.innerText = products.length;

            const t = I18N[selectedLang] || I18N['hi'];

            container.innerHTML = products.map(p => {
                const title = selectedLang === 'hi' ? p.title : (p.story_en ? p.title : p.title);
                const story = selectedLang === 'hi' ? p.story_hi : p.story_en;
                const voice = p.raw_voice_transcript || p.story_hi || p.story_en;
                const artisanShare = Math.round(p.suggested_price * 0.85);

                return `
                <article class="craft-card rounded-2xl overflow-hidden flex flex-col justify-between">
                    <!-- Image Container -->
                    <div class="relative aspect-[4/3] bg-[#f5f5f4] overflow-hidden group">
                        <img src="${p.studio_image_url || p.raw_image_url}" alt="${p.title}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                        
                        <!-- GI Tag Stamp -->
                        <span class="absolute top-3 left-3 px-2 py-0.5 rounded text-[10px] font-stamp font-bold bg-white/95 text-[#b45309] border border-[#fed7aa] shadow-xs">
                            ${p.gi_tag_no || t.giCertified}
                        </span>

                        <!-- SFURTI CFC Stamp -->
                        <span class="absolute top-3 right-3 px-2 py-0.5 rounded text-[9px] font-stamp font-bold bg-[#1e3a8a] text-white shadow-xs">
                            ${t.sfurtiGrade}
                        </span>

                        <!-- Voice Snippet Player Floating Chip -->
                        <div class="absolute bottom-3 inset-x-3 flex items-center justify-between p-2 rounded-xl bg-white/90 backdrop-blur-md border border-[#e7e5e4] shadow-sm">
                            <button type="button" onclick="playVoiceSnippet('${p.id}', '${voice.replace(/'/g, "\\\\'")}')" class="flex items-center gap-1.5 text-xs font-semibold text-[#1c1917] hover:text-[#b45309] transition">
                                <span class="w-6 h-6 rounded-full bg-[#b45309] text-white flex items-center justify-center">
                                    <i data-lucide="volume-2" class="w-3.5 h-3.5 ml-0.5"></i>
                                </span>
                                <span>${t.listenVoiceSnippet}</span>
                            </button>
                            <span class="text-[10px] font-stamp text-[#047857] font-bold">
                                ${t.directWageShare}
                            </span>
                        </div>
                    </div>

                    <!-- Card Body -->
                    <div class="p-5 flex-1 flex flex-col justify-between space-y-3">
                        <div>
                            <div class="flex items-center justify-between text-xs text-[#78716c] font-stamp mb-1">
                                <span class="truncate">${p.artisan_name}</span>
                                <span class="text-[#047857] font-bold">✓ सत्यापित</span>
                            </div>
                            <h3 class="font-vintage text-xl text-[#1c1917] line-clamp-1 leading-snug">${title}</h3>
                            <p class="text-xs text-[#78716c] line-clamp-2 mt-1 font-light leading-relaxed">${story}</p>
                        </div>

                        <!-- Price & Action Bar -->
                        <div class="pt-3 border-t border-[#f5f5f4] flex items-center justify-between gap-2">
                            <div>
                                <span class="text-[10px] font-stamp text-[#a8a29e] block">उचित मूल्य (Fair Price)</span>
                                <span class="font-vintage text-2xl text-[#1c1917]">₹${p.suggested_price}</span>
                            </div>

                            <div class="flex items-center gap-1.5">
                                <button onclick="openPassportModal('${p.id}')" title="विरासत पासपोर्ट" class="p-2 rounded-xl text-[#44403c] hover:text-[#b45309] hover:bg-[#f5f5f4] border border-[#e7e5e4] transition">
                                    <i data-lucide="file-text" class="w-4 h-4"></i>
                                </button>
                                <button onclick="addToBag('${p.id}')" class="px-3.5 py-2 bg-[#1c1917] hover:bg-[#b45309] text-white rounded-xl text-xs font-semibold shadow-xs transition flex items-center gap-1.5">
                                    <i data-lucide="shopping-bag" class="w-3.5 h-3.5"></i>
                                    <span>${t.addToBag}</span>
                                </button>
                            </div>
                        </div>
                    </div>
                </article>
                `;
            }).join('');

            lucide.createIcons();
        }

        // Voice playback with Speech Synthesis
        function playVoiceSnippet(id, script) {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                const utter = new SpeechSynthesisUtterance(script);
                const langMap = { 'hi': 'hi-IN', 'bn': 'bn-IN', 'mr': 'mr-IN', 'ta': 'ta-IN', 'te': 'te-IN', 'en': 'en-IN' };
                utter.lang = langMap[selectedLang] || 'hi-IN';
                utter.rate = 0.95;
                window.speechSynthesis.speak(utter);
            }
        }

        // Category Filter
        function filterCategory(cat) {
            document.querySelectorAll('.category-pill').forEach(btn => {
                btn.classList.remove('bg-[#1c1917]', 'text-white');
                btn.classList.add('bg-white', 'text-[#44403c]');
            });

            if (cat === 'all') {
                document.getElementById('cat-pill-all').classList.add('bg-[#1c1917]', 'text-white');
                renderMarketplace(cachedProducts);
            } else {
                const filtered = cachedProducts.filter(p => p.category.includes(cat) || p.category === cat);
                renderMarketplace(filtered);
            }
        }

        // Search Filter
        function handleSearch(query) {
            const q = query.toLowerCase().trim();
            if (!q) {
                renderMarketplace(cachedProducts);
                return;
            }
            const filtered = cachedProducts.filter(p => 
                p.title.toLowerCase().includes(q) ||
                p.category.toLowerCase().includes(q) ||
                p.artisan_name.toLowerCase().includes(q) ||
                (p.story_hi && p.story_hi.toLowerCase().includes(q))
            );
            renderMarketplace(filtered);
        }

        // Voice search simulation
        function handleVoiceSearch() {
            const input = document.getElementById('marketplace-search');
            input.value = "तुषार सिल्क";
            handleSearch("तुषार सिल्क");
            playVoiceSnippet('search', "तुषार सिल्क खोजा जा रहा है।");
        }

        // Open Heritage Passport Modal
        function openPassportModal(productId) {
            const p = cachedProducts.find(item => item.id === productId);
            if (!p) return;

            const inst = p.institutional_verification || {};
            const container = document.getElementById('passport-content');
            const story = selectedLang === 'hi' ? p.story_hi : p.story_en;
            const lifecycle = p.craft_lifecycle || [];

            container.innerHTML = `
                <div class="flex items-center gap-3 mb-4 pb-3 border-b border-[#e7e5e4]">
                    <img src="${p.artisan_photo}" alt="${p.artisan_name}" class="w-12 h-12 rounded-full object-cover border-2 border-[#b45309]">
                    <div>
                        <span class="text-[10px] font-stamp font-bold text-[#b45309] uppercase">विरासत पासपोर्ट • Provenance Passport</span>
                        <h3 class="font-vintage text-xl text-[#1c1917]">${p.artisan_name}</h3>
                        <p class="text-xs text-[#78716c] font-stamp">${p.artisan_location} • ${p.artisan_experience}</p>
                    </div>
                </div>

                <div class="space-y-4 text-xs text-[#44403c]">
                    <!-- Story & Voice -->
                    <div class="p-3 bg-[#fbf9f5] rounded-xl border border-[#e7e5e4]">
                        <div class="flex items-center justify-between mb-1.5">
                            <b class="text-xs text-[#1c1917]">कारीगर की मूल कथा (भाषिणी MeitY AI)</b>
                            <button onclick="playVoiceSnippet('${p.id}', '${p.raw_voice_transcript || story}')" class="text-xs text-[#b45309] font-semibold hover:underline flex items-center gap-1">
                                <i data-lucide="volume-2" class="w-3.5 h-3.5"></i>
                                <span>आवाज़ सुनें</span>
                            </button>
                        </div>
                        <p class="text-xs leading-relaxed text-[#78716c] italic font-serif">"${p.raw_voice_transcript || story}"</p>
                    </div>

                    <!-- 4-Step Craft Lifecycle -->
                    <div>
                        <b class="text-xs text-[#1c1917] block mb-2 font-stamp uppercase">हस्तशिल्प निर्माण चक्र (Craft Lifecycle)</b>
                        <div class="grid grid-cols-2 gap-2">
                            ${lifecycle.map(s => `
                                <div class="p-2 bg-white rounded-lg border border-[#e7e5e4]">
                                    <span class="text-[10px] font-stamp text-[#b45309] font-bold block">${s.days} • ${s.step}</span>
                                    <span class="text-[10px] text-[#78716c] block mt-0.5">${s.desc}</span>
                                </div>
                            `).join('')}
                        </div>
                    </div>

                    <!-- 6-Stage Govt Verification Grid -->
                    <div>
                        <b class="text-xs text-[#1e3a8a] block mb-2 font-stamp uppercase">६ स्तरीय सरकारी सत्यापन (Institutions)</b>
                        <div class="grid grid-cols-2 gap-1.5 text-[10px] font-stamp">
                            <div class="p-2 bg-[#f8fafc] rounded-lg border border-[#e2e8f0]">
                                <span class="text-[#1e3a8a] font-bold block">1. PM Vishwakarma ID</span>
                                <span class="text-[#475569]">${inst.stage_1_identity ? inst.stage_1_identity.id : 'PMV-BH-88214'}</span>
                            </div>
                            <div class="p-2 bg-[#f8fafc] rounded-lg border border-[#e2e8f0]">
                                <span class="text-[#b45309] font-bold block">2. CSC VLE Tech Hub</span>
                                <span class="text-[#475569]">${inst.stage_2_tech_hub ? inst.stage_2_tech_hub.hub : 'CSC Kendra'}</span>
                            </div>
                            <div class="p-2 bg-[#f8fafc] rounded-lg border border-[#e2e8f0]">
                                <span class="text-[#047857] font-bold block">3. Bhashini AI Engine</span>
                                <span class="text-[#475569]">मातृभाषा बोली अनुवाद</span>
                            </div>
                            <div class="p-2 bg-[#f8fafc] rounded-lg border border-[#e2e8f0]">
                                <span class="text-[#c2410c] font-bold block">4. SHG / APC Cluster</span>
                                <span class="text-[#475569]">गंगा महिला स्वयं सहायता समूह</span>
                            </div>
                            <div class="p-2 bg-[#f8fafc] rounded-lg border border-[#e2e8f0]">
                                <span class="text-[#7e22ce] font-bold block">5. SFURTI CFC QC</span>
                                <span class="text-[#475569]">Grade A+ • बारकोड प्रमाणित</span>
                            </div>
                            <div class="p-2 bg-[#f8fafc] rounded-lg border border-[#e2e8f0]">
                                <span class="text-[#be123c] font-bold block">6. RuTAG IIT Tech</span>
                                <span class="text-[#475569]">एर्गोनॉमिक टूल सुधार</span>
                            </div>
                        </div>
                    </div>

                    <!-- Speed Post Tracking -->
                    <div class="p-3 bg-[#fefae0] rounded-xl border border-[#fed7aa] flex items-center justify-between">
                        <div>
                            <span class="text-[10px] font-stamp font-bold text-[#b45309] block">भारतीय डाक स्पीड पोस्ट रसीद</span>
                            <span class="text-xs font-mono font-bold text-[#1c1917]">SPEED-POST-IND-${p.id.toUpperCase()}</span>
                        </div>
                        <span class="px-2 py-0.5 rounded text-[10px] font-stamp bg-white text-[#047857] border border-[#a7f3d0] font-bold">
                            गाँव संकलन तैयार
                        </span>
                    </div>
                </div>
            `;
            lucide.createIcons();
            toggleModal('passport-modal');
        }

        // Cart Actions
        function addToBag(productId) {
            const p = cachedProducts.find(item => item.id === productId);
            if (!p) return;
            cart.push(p);
            updateCartUI();
            toggleCartDrawer();
        }

        function toggleCartDrawer() {
            document.getElementById('cart-drawer').classList.toggle('hidden');
        }

        function updateCartUI() {
            const countBadge = document.getElementById('cart-count-badge');
            if (countBadge) countBadge.innerText = cart.length;

            const container = document.getElementById('cart-items-container');
            const totalEl = document.getElementById('cart-total-amount');
            const wageShareEl = document.getElementById('cart-artisan-share');

            if (!container) return;

            if (cart.length === 0) {
                container.innerHTML = `<p class="text-xs text-[#78716c] font-stamp text-center py-8">झोला खाली है। पसंदीदा शिल्प जोड़ें।</p>`;
                if (totalEl) totalEl.innerText = '₹0';
                if (wageShareEl) wageShareEl.innerText = '₹0 (८५%)';
                return;
            }

            const total = cart.reduce((sum, item) => sum + item.suggested_price, 0);
            const artisanDirect = Math.round(total * 0.85);

            if (totalEl) totalEl.innerText = `₹${total}`;
            if (wageShareEl) wageShareEl.innerText = `₹${artisanDirect} (८५%)`;

            container.innerHTML = cart.map((item, idx) => `
                <div class="flex items-center justify-between p-2.5 bg-[#fbf9f5] rounded-xl border border-[#e7e5e4]">
                    <div class="flex items-center gap-2.5 min-w-0">
                        <img src="${item.studio_image_url || item.raw_image_url}" class="w-10 h-10 rounded-lg object-cover">
                        <div class="min-w-0">
                            <span class="text-xs font-semibold text-[#1c1917] block truncate">${item.title}</span>
                            <span class="text-[10px] text-[#78716c] font-stamp">${item.artisan_name}</span>
                        </div>
                    </div>
                    <div class="text-right">
                        <span class="text-xs font-vintage font-bold text-[#1c1917] block">₹${item.suggested_price}</span>
                        <button onclick="removeFromBag(${idx})" class="text-[10px] text-[#b45309] hover:underline">हटाएँ</button>
                    </div>
                </div>
            `).join('');
        }

        function removeFromBag(idx) {
            cart.splice(idx, 1);
            updateCartUI();
        }

        function handleCheckout() {
            if (cart.length === 0) return;
            const track = `SP-IND-${Math.floor(100000 + Math.random() * 900000)}`;
            alert(`📮 भारतीय डाक स्पीड पोस्ट आर्डर सफल!\n\n📦 ट्रैकिंग नंबर: ${track}\n👨‍🌾 ग्रामीण डाक सेवक आज शाम आपके पते के लिए गाँव संकलन केंद्र से पार्सल रवाना करेंगे।`);
            cart = [];
            updateCartUI();
            toggleCartDrawer();
        }

        // Modal Helpers
        function toggleModal(id) {
            const el = document.getElementById(id);
            if (el) el.classList.toggle('hidden');
        }

        function openLanguageModal() { toggleModal('language-modal'); }
        function openArtisanModal() { toggleModal('artisan-auth-modal'); }
        function openEcosystemModal() { toggleModal('ecosystem-modal'); }
        function openShgModal() { toggleModal('shg-modal'); }

        // Switch Tabs in Artisan Modal
        function switchAuthTab(tab) {
            const btnLogin = document.getElementById('tab-btn-login');
            const btnReg = document.getElementById('tab-btn-register');
            const panelLogin = document.getElementById('auth-panel-login');
            const panelReg = document.getElementById('auth-panel-register');

            if (tab === 'login') {
                btnLogin.classList.add('text-[#b45309]', 'border-b-2', 'border-[#b45309]');
                btnLogin.classList.remove('text-[#78716c]');
                btnReg.classList.remove('text-[#b45309]', 'border-b-2', 'border-[#b45309]');
                btnReg.classList.add('text-[#78716c]');
                panelLogin.classList.remove('hidden');
                panelReg.classList.add('hidden');
            } else {
                btnReg.classList.add('text-[#b45309]', 'border-b-2', 'border-[#b45309]');
                btnReg.classList.remove('text-[#78716c]');
                btnLogin.classList.remove('text-[#b45309]', 'border-b-2', 'border-[#b45309]');
                btnLogin.classList.add('text-[#78716c]');
                panelReg.classList.remove('hidden');
                panelLogin.classList.add('hidden');
            }
        }

        // PM Vishwakarma ID Login
        async function handlePmVishwakarmaLogin() {
            const vId = document.getElementById('login-vishwakarma-id').value;
            const formData = new FormData();
            formData.append('vishwakarma_id', vId);

            try {
                const res = await fetch('/api/artisan/verify-vishwakarma', { method: 'POST', body: formData });
                const data = await res.json();
                if (data.status === 'success') {
                    setArtisanSession(data.artisan);
                    playVoiceSnippet('auth', data.voice_announcement);
                    toggleModal('artisan-auth-modal');
                }
            } catch (err) {
                console.error(err);
            }
        }

        // Phone Login
        async function handleArtisanPhoneLogin() {
            const formData = new FormData();
            formData.append('phone', document.getElementById('login-phone').value);
            formData.append('otp', document.getElementById('login-otp').value);

            try {
                const res = await fetch('/api/artisan/login', { method: 'POST', body: formData });
                const data = await res.json();
                if (data.status === 'success') {
                    setArtisanSession(data.artisan);
                    playVoiceSnippet('auth', "स्वागत है! आपका आर्टिसाना खाता खुल गया है।");
                    toggleModal('artisan-auth-modal');
                }
            } catch (err) {
                console.error(err);
            }
        }

        // New Registration for Non-Vishwakarma Artisans
        async function handleNewRegistration(e) {
            e.preventDefault();
            const btn = document.getElementById('reg-submit-btn');
            const feedback = document.getElementById('reg-feedback-msg');
            btn.disabled = true;

            const formData = new FormData();
            formData.append('name', document.getElementById('reg-artisan-name').value);
            formData.append('craft_type', document.getElementById('reg-craft-trade').value);
            formData.append('village_panchayat', document.getElementById('reg-panchayat').value);
            formData.append('phone', document.getElementById('reg-phone').value);
            formData.append('assist_requested', document.getElementById('reg-assist-check').checked);

            try {
                const res = await fetch('/api/artisan/register', { method: 'POST', body: formData });
                const data = await res.json();
                if (data.status === 'success') {
                    feedback.innerText = `✅ ${data.message}`;
                    feedback.classList.remove('hidden');
                    playVoiceSnippet('reg', data.voice_announcement);
                    setArtisanSession(data.artisan);
                    setTimeout(() => {
                        toggleModal('artisan-auth-modal');
                    }, 2000);
                }
            } catch (err) {
                console.error(err);
            }
        }

        // Set Artisan Session
        function setArtisanSession(artisan) {
            currentArtisan = artisan;
            const strip = document.getElementById('artisan-session-strip');
            if (strip) strip.classList.remove('hidden');

            const nameEl = document.getElementById('strip-artisan-welcome');
            if (nameEl) nameEl.innerText = `नमस्ते, ${artisan.name}!`;

            const idEl = document.getElementById('strip-artisan-id');
            if (idEl) idEl.innerText = `ID: ${artisan.vishwakarma_id}`;

            const sealEl = document.getElementById('strip-artisan-seal');
            if (sealEl) sealEl.innerText = artisan.panchayat_seal;

            const earnEl = document.getElementById('strip-artisan-earnings');
            if (earnEl) earnEl.innerText = `कुल आय: ${artisan.total_earnings}`;

            const cornerBtn = document.getElementById('artisan-corner-label');
            if (cornerBtn) cornerBtn.innerText = artisan.name.split(' ')[0] + ' ✓';
        }

        function artisanLogout() {
            currentArtisan = null;
            document.getElementById('artisan-session-strip').classList.add('hidden');
            const cornerBtn = document.getElementById('artisan-corner-label');
            if (cornerBtn) cornerBtn.innerText = 'कारीगर कॉर्नर';
            playVoiceSnippet('logout', "लॉगआउट संपन्न हुआ।");
        }

        // Audio Guidance helpers
        function speakLoginGuide() {
            playVoiceSnippet('guide', "नमस्ते! आर्टिसाना में आपका स्वागत है। लॉगिन करने के लिए अपनी विश्वकर्मा आईडी या मोबाइल नंबर दर्ज करें। यदि आईडी नहीं है, तो नया पंजीकरण चुनें।");
        }

        function speakArtisanOTP() {
            playVoiceSnippet('otp', "नमस्ते! आपका आर्टिसाना कोड है: पांच, चार, एक, आठ।");
        }

        function handlePassbookScan() {
            handlePmVishwakarmaLogin();
        }

        // Studio Upload
        async function handleStudioSubmit(e) {
            e.preventDefault();
            alert("✅ एआई स्टूडियो कैटलॉग तैयार हो गया है! नया शिल्प बाज़ार में जोड़ दिया गया है।");
            toggleModal('studio-modal');
        }

        function toggleVoiceRecording() {
            const btn = document.getElementById('voice-rec-btn');
            const status = document.getElementById('voice-rec-status');
            isRecording = !isRecording;
            if (isRecording) {
                btn.classList.add('animate-ping');
                status.innerText = "🔴 रिकॉर्डिंग जारी... बोलिए";
            } else {
                btn.classList.remove('animate-ping');
                status.innerText = "✅ 10-सेकंड वॉइस सुरक्षित!";
            }
        }

        // Kala Sakhi & Bulk Order Helpers
        async function requestKalaSakhi() {
            const fb = document.getElementById('sakhi-feedback');
            const res = await fetch('/api/shg/request-sakhi', { method: 'POST' });
            const data = await res.json();
            fb.innerText = `✅ ${data.message}`;
            fb.classList.remove('hidden');
            playVoiceSnippet('sakhi', data.message);
        }

        async function joinBulkRawMaterials() {
            const fb = document.getElementById('bulk-feedback');
            const res = await fetch('/api/shg/join-bulk-order', { method: 'POST' });
            const data = await res.json();
            fb.innerText = `✅ ${data.message}`;
            fb.classList.remove('hidden');
            playVoiceSnippet('bulk', data.message);
        }

        // Change Language
        function changeAppLang(code) {
            selectedLang = code;
            const t = I18N[code] || I18N['hi'];
            document.getElementById('current-lang-label').innerText = code.toUpperCase();
            document.getElementById('brand-subname').innerText = t.brandSub;
            document.getElementById('hero-title').innerText = t.heroTitle;
            document.getElementById('hero-desc').innerText = t.heroDesc;
            document.getElementById('hero-studio-btn').innerText = t.heroStudioBtn;
            document.getElementById('artisan-corner-label').innerText = t.artisanCornerLabel;
            document.getElementById('cat-pill-all').innerText = t.allCrafts;
            document.getElementById('marketplace-search').placeholder = t.searchPlaceholder;

            toggleModal('language-modal');
            renderMarketplace(cachedProducts);
        }

        // On Load
        window.onload = () => {
            fetchProducts();
            lucide.createIcons();
        };
    </script>
</body>
</html>'''

def main():
    target = "templates/index.html"
    content = generate_index_html()
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Minimal indie marketplace generated at {target} ({len(content)} chars)")

if __name__ == "__main__":
    main()
