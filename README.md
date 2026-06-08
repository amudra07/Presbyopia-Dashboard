# Presbyopia Eye Drop — Competitive Intelligence Dashboard

A Streamlit app providing pharmaceutical-grade competitive intelligence for approved and pipeline presbyopia eye drops.

## Drugs Covered

| Drug | API | FDA Status |
|------|-----|-----------|
| **VUITY** | Pilocarpine HCl 1.25% | ✅ Approved (Oct 2021) |
| **QLOSI** | Pilocarpine HCl 0.4% | ✅ Approved (Oct 2023) |
| **VIZZ** | Aceclidine 1.44% | ✅ Approved (Jul 2025) |
| **YUVEZZI** | Carbachol 2.75% + Brimonidine 0.1% | ✅ Approved (Jan 2026) |
| **Ryzumvi** | Phentolamine mesylate 0.75% | ⏳ Approved (mydriasis) — sNDA presbyopia PDUFA Oct 2026 |

## Features

- **Drug Profile** — Full pharmaceutical data: IUPAC name, molecular formula/weight, MOA, technology platform, excipients with functions, dosing, clinical trials, efficacy, safety
- **Comparison Table** — Side-by-side comparison of all 5 drugs across all parameters
- **Excipient Deep-dive** — Every excipient with its pharmacological/formulation rationale

## How to Run Locally

```bash
# 1. Clone or download the app.py and requirements.txt files

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run
streamlit run app.py
```

## Deploy to Streamlit Community Cloud

1. Push files to a GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select the repository and set `app.py` as the main file
5. Click Deploy

The app will be live at `https://[your-username]-[repo-name]-app-[hash].streamlit.app`

## File Structure

```
presbyopia_app/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Data Sources

All data sourced from:
- FDA DailyMed (accessdata.fda.gov) — official prescribing information
- PubMed — clinical trial publications
- ClinicalTrials.gov — trial registrations
- Drugs.com / RxList — drug information
- Internal pharmaceutical research sessions

Last updated: June 2026
