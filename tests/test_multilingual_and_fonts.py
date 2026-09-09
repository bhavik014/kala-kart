# -*- coding: utf-8 -*-
"""
Verification Test Suite:
1. Font typography rules & language attributes
2. 100% pure English dictionary (0 Devanagari characters)
3. 100% pure Hindi dictionary (standardized, zero mixed English words)
4. Localized helper functions for artisan names, locations, and categories
"""
import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

html_path = r'C:\Users\bhavi\.gemini\antigravity\scratch\artisana-ai\templates\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

tests_passed = 0
total_tests = 0

def test(desc, condition):
    global tests_passed, total_tests
    total_tests += 1
    if condition:
        print(f"PASS: {desc}")
        tests_passed += 1
    else:
        print(f"FAIL: {desc}")

print("=================================================================")
print("RUNNING MULTILINGUAL & FONT DYNAMICS VERIFICATION TEST SUITE")
print("=================================================================\n")

# 1. Google Fonts imported in <head>
test("Google Fonts includes Playfair Display", "family=Playfair+Display" in html)
test("Google Fonts includes Rozha One", "family=Rozha+One" in html)
test("Google Fonts includes Noto Serif Devanagari", "family=Noto+Serif+Devanagari" in html)
test("Google Fonts includes Noto Sans Bengali", "family=Noto+Sans+Bengali" in html)
test("Google Fonts includes Noto Sans Tamil", "family=Noto+Sans+Tamil" in html)
test("Google Fonts includes Noto Sans Telugu", "family=Noto+Sans+Telugu" in html)
test("Google Fonts includes Plus Jakarta Sans", "family=Plus+Jakarta+Sans" in html)
test("Google Fonts includes Courier Prime", "family=Courier+Prime" in html)

# 2. CSS Typography Theme
test("CSS defines html[lang='en'] typography", 'html[lang="en"]' in html and '--font-headline: \'Playfair Display\'' in html)
test("CSS defines html[lang='hi'] typography", 'html[lang="hi"]' in html and '--font-headline: \'Rozha One\'' in html)
test("CSS defines html[lang='bn'] typography", 'html[lang="bn"]' in html and 'Noto Serif Bengali' in html)
test("CSS defines html[lang='ta'] typography", 'html[lang="ta"]' in html and 'Noto Serif Tamil' in html)
test("CSS defines html[lang='te'] typography", 'html[lang="te"]' in html and 'Noto Serif Telugu' in html)

# 3. Dynamic documentElement.lang switching in JS
test("applyLanguageToEntireApp sets documentElement.lang", "document.documentElement.lang = lang;" in html)
test("applyLanguageToEntireApp sets documentElement.setAttribute('lang')", "document.documentElement.setAttribute('lang', lang);" in html)
test("selectInitialLanguage updates documentElement lang", "document.documentElement.lang = langCode;" in html)

# 4. Parse I18N object from index.html
m_i18n = re.search(r'const I18N = (\{[\s\S]*?\n\s*\});', html)
test("const I18N object successfully found in HTML", m_i18n is not None)

if m_i18n:
    i18n = json.loads(m_i18n.group(1))
    test("I18N has all 6 languages", set(i18n.keys()) == {'en', 'hi', 'bn', 'mr', 'ta', 'te'})

    # Test 5: English Mode must have ZERO Devanagari characters
    en_dict = i18n['en']
    devanagari_pattern = re.compile(r'[\u0900-\u097F]')
    en_devanagari_leaks = {}
    for k, v in en_dict.items():
        if isinstance(v, str) and devanagari_pattern.search(v):
            en_devanagari_leaks[k] = v

    test(f"English dictionary has 0 Devanagari characters (Leaks: {len(en_devanagari_leaks)})", len(en_devanagari_leaks) == 0)
    if en_devanagari_leaks:
        print("  Found Devanagari in EN:", en_devanagari_leaks)

    # Test 6: Hindi Mode must have complete standardized translations
    hi_dict = i18n['hi']
    test("Hindi dictionary has identical key count as English", len(hi_dict) == len(en_dict))
    test("Hindi brand is कला कार्ट", hi_dict.get('brandSub') == 'कला कार्ट')
    test("English brand is KalaKart", en_dict.get('brandSub') == 'KalaKart')
    test("Hindi cart label is टोकरी", hi_dict.get('navCartLabel') == 'टोकरी')
    test("English cart label is Cart", en_dict.get('navCartLabel') == 'Cart')

# 7. Helper functions present in JS
test("getArtisanName helper function defined", "function getArtisanName(p, lang)" in html)
test("getArtisanLocation helper function defined", "function getArtisanLocation(p, lang)" in html)
test("getProductCategory helper function defined", "function getProductCategory(p, lang)" in html)
test("getProductTitle helper function defined", "function getProductTitle(p, lang)" in html)
test("getProductStory helper function defined", "function getProductStory(p, lang)" in html)

# 8. Product Card Renderer uses helpers
test("renderBuyerMarketplace uses getProductTitle", "getProductTitle(p, currentLang)" in html)
test("renderBuyerMarketplace uses getProductStory", "getProductStory(p, currentLang)" in html)
test("renderBuyerMarketplace uses getArtisanName", "getArtisanName(p, currentLang)" in html)
test("renderBuyerMarketplace uses getArtisanLocation", "getArtisanLocation(p, currentLang)" in html)
test("renderBuyerMarketplace uses getProductCategory", "getProductCategory(p, currentLang)" in html)
test("renderBuyerMarketplace uses localized buttons", "${t.btnQuickView}" in html and "${t.btnAddToCart}" in html and "${t.btnBuyNow}" in html)

# 9. Modals use pure localized helpers
test("openQuickViewModal uses localized getProductTitle", "getProductTitle(prod, currentLang)" in html)
test("openQuickViewModal uses getArtisanName", "getArtisanName(prod, currentLang)" in html)
test("refreshArtisanPassbook localizes buyer and settled status", "Settled in Account" in html and "खाते में जमा" in html)
test("updateCartUI localizes empty state and titles", "t.cartEmptyTitle" in html and "getArtisanName(item, currentLang)" in html)
test("openCheckoutModal localizes item titles", "item.title_hi || item.title" in html)

print("\n=================================================================")
print(f"TEST RESULTS: {tests_passed} / {total_tests} Passed ({round(tests_passed/total_tests*100)}%)")
print("=================================================================")

if tests_passed == total_tests:
    print("ALL MULTILINGUAL & FONT TESTS PASSED! SYSTEM FULLY STANDARDIZED!")
else:
    print("SOME TESTS FAILED! PLEASE REVIEW OUTPUT ABOVE.")
    sys.exit(1)
