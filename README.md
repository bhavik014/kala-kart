# Artisana AI — Voice-to-Commerce Platform for Rural Artisans

**Smart India Hackathon (SIH) 2026**  
**Problem Statement ID**: `SIH26090`  
**Sponsor Ministry**: Ministry of Social Justice and Empowerment (MoSJE)  
**Target Beneficiaries**: PM-AJAY beneficiaries, SHGs, traditional craftspeople, rural artisans  

---

## 📌 Executive Summary & Pitch

**Artisana AI** is a voice-first, multimodal e-commerce studio built for rural artisans who face digital literacy barriers. Over 98% of surveyed artisans in India have never completed an online listing due to complex English web forms, professional studio photography rules, pricing confusion, and lack of digital cataloging tools.

With **Artisana AI**, an artisan simply:
1. Speaks for **10 seconds in their native language/dialect** describing their craft.
2. Takes **1 photo** on a basic mobile phone.

Our multimodal AI pipeline:
- Enhances raw phone photos into studio-grade product imagery.
- Generates structured multilingual story descriptions (English, Hindi, regional dialects).
- Recommends fair market pricing with a transparent direct-to-artisan wage share (85%+).
- Creates an instant shareable WhatsApp Business catalog and QR-code authenticity badge.

---

## 👥 Team of 6 Role Allocation (SIH Hackathon Strategy)

| Role | Member | Responsibilities |
| :--- | :--- | :--- |
| **Person 1 — Frontend / UI / UX** | Student 1 | Mobile-first PWA interface, voice recorder UI, high-contrast accessible layout. |
| **Person 2 — Backend & API** | Student 2 | FastAPI REST server, media processing queue, image storage, WhatsApp API. |
| **Person 3 — AI / ML Pipeline** | Student 3 | Pillow image enhancement filters, Gemini Multimodal Vision prompt chain, TTS. |
| **Person 4 — Data & Research** | Student 4 | Handicraft product taxonomy, fair price benchmarks, artisan community datasets. |
| **Person 5 — Product Integration** | Student 5 | QR code generator, WhatsApp catalog export, offline PWA service worker. |
| **Person 6 — Pitch & Documentation** | Student 6 | Live demo script, slide deck, judge Q&A prep, architecture diagrams. |

---

## ⚡ How to Run Locally

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Launch FastAPI Application
```bash
python app.py
```
Or with uvicorn:
```bash
uvicorn app:app --reload --port 8000
```

### 3. Open Web Browser
Navigate to `http://localhost:8000` to access the live PWA application!

---

## 🏆 90-Second Live Pitch Script for Judges

1. **00–15s (Problem)**: "Judges, 98% of rural artisans in India never complete an online listing because of complex English forms and studio photo requirements."
2. **15–45s (Solution)**: "Watch Savita Devi record a 5-second voice note in her native language and snap 1 rough photo."
3. **45–75s (AI Magic)**: "Our app cleans the background into studio lighting, extracts materials, calculates fair artisan pricing (₹2,450 with 85% direct wage share), and generates a QR trust badge."
4. **75–90s (Export & Buyer)**: "With 1 click, the artisan exports a complete WhatsApp Business catalog and buyers listen to the authentic voice story!"
