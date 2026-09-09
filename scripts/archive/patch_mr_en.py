def main():
    path = "templates/index.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    old_mr = "gratitudeBtn: 'आभार',"
    new_mr = """gratitudeBtn: 'आभार',
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

    old_en = "gratitudeBtn: 'Gratitude',"
    new_en = """gratitudeBtn: 'Gratitude',
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

    if old_mr in html:
        html = html.replace(old_mr, new_mr, 1)
        print("Marathi keys added!")
    if old_en in html:
        html = html.replace(old_en, new_en, 1)
        print("English keys added!")

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    main()
