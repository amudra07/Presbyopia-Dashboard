import streamlit as st
import pandas as pd

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Presbyopia Eye Drop – Competitive Intelligence",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# CSS — LIGHT THEME
# ─────────────────────────────────────────────
st.markdown("""
<style>
html,body,[class*="css"]{font-family:'DM Sans','Inter',sans-serif;}
[data-testid="stSidebar"]{background:#f7f8fa;border-right:1px solid #e5e8ef;}
[data-testid="stSidebar"] p,[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,[data-testid="stSidebar"] h3{color:#111827!important;}

.drug-hero{background:#fff;border:1.5px solid #e5e8ef;border-radius:14px;
  padding:24px 28px;margin-bottom:20px;box-shadow:0 2px 8px rgba(0,0,0,0.05);}
.drug-name{font-size:28px;font-weight:700;margin:0 0 4px 0;}
.drug-generic{font-size:15px;color:#5a5f78;margin:0 0 16px 0;}

.badge{display:inline-block;font-size:11px;font-weight:600;padding:4px 12px;
  border-radius:20px;margin-right:6px;margin-bottom:4px;letter-spacing:.03em;}
.badge-approved{background:#e6f9f0;color:#0d6b35;border:1px solid #b3e6cc;}
.badge-pending{background:#fff8e6;color:#8a5c00;border:1px solid #ffd980;}
.badge-rx{background:#e8f0fb;color:#1a4d9e;border:1px solid #b3c8f0;}

.info-card{background:#f7f8fa;border:1px solid #e5e8ef;border-radius:10px;
  padding:16px 18px;margin-bottom:12px;height:100%;}
.info-card-title{font-size:10px;font-weight:700;letter-spacing:.09em;
  text-transform:uppercase;color:#9098b0;margin-bottom:8px;}
.info-card-value{font-size:14px;color:#2c3150;line-height:1.65;}
.info-card-value b{color:#111827;font-weight:600;}
.info-card-value .hl{color:#0d6b35;font-weight:600;}
.info-card-value .warn{color:#a05c00;font-weight:600;}
.info-card-value .danger{color:#b91c1c;font-weight:600;}

.excip-table{width:100%;border-collapse:collapse;font-size:13px;}
.excip-table th{background:#f0f2f7;color:#6b7280;font-size:10px;font-weight:700;
  letter-spacing:.07em;text-transform:uppercase;padding:9px 12px;
  text-align:left;border-bottom:1.5px solid #d1d5de;}
.excip-table td{padding:9px 12px;color:#374151;border-bottom:1px solid #edf0f5;
  vertical-align:top;line-height:1.6;}
.excip-table tr:nth-child(even) td{background:#fafbfc;}
.excip-table tr:last-child td{border-bottom:none;}
.excip-table td b{color:#111827;}
.excip-role{display:inline-block;font-size:10px;padding:2px 8px;border-radius:10px;
  background:#e8f0fb;color:#1a4d9e;font-weight:600;}

.trial-box{background:#f0f5ff;border:1px solid #c7d9f5;border-left:4px solid #3b72d9;
  border-radius:8px;padding:14px 16px;margin-bottom:10px;}
.trial-box-title{font-size:13px;font-weight:700;color:#1a3d8a;margin-bottom:6px;}
.trial-box-body{font-size:13px;color:#374151;line-height:1.65;}

.pk-table{width:100%;border-collapse:collapse;font-size:12px;}
.pk-table th{background:#f0f2f7;color:#374151;font-size:10px;font-weight:700;
  padding:9px 12px;text-align:left;border:1px solid #d1d5de;letter-spacing:.04em;
  text-transform:uppercase;}
.pk-table td{padding:8px 12px;color:#374151;border:1px solid #e5e8ef;
  vertical-align:top;line-height:1.5;}
.pk-table tr:nth-child(even) td{background:#fafbfc;}
.pk-table td b{color:#111827;font-weight:600;}
.pk-ref{font-size:10px;color:#1a4d9e;}
.pk-ref a{color:#1a4d9e;text-decoration:none;}

.pat-table{width:100%;border-collapse:collapse;font-size:12px;}
.pat-table th{background:#f7f2ff;color:#374151;font-size:10px;font-weight:700;
  padding:9px 12px;text-align:left;border:1px solid #d1d5de;letter-spacing:.04em;
  text-transform:uppercase;}
.pat-table td{padding:8px 12px;color:#374151;border:1px solid #e5e8ef;
  vertical-align:top;line-height:1.5;}
.pat-table tr:nth-child(even) td{background:#fdf9ff;}
.pat-table td b{color:#111827;font-weight:600;}
.pat-active{color:#0d6b35;font-weight:600;}
.pat-warn{color:#a05c00;font-weight:600;}

.korea-tbl{width:100%;border-collapse:collapse;font-size:13px;}
.korea-tbl th{background:#f0f2f7;color:#374151;font-size:11px;font-weight:700;
  padding:10px 14px;text-align:left;border:1px solid #d1d5de;}
.korea-tbl td{padding:9px 14px;color:#374151;border:1px solid #e5e8ef;
  vertical-align:top;line-height:1.55;font-size:13px;}
.korea-tbl tr:nth-child(even) td{background:#fafbfc;}
.korea-tbl td b{color:#111827;font-weight:600;}
.s-review{color:#a05c00;font-weight:600;}
.s-pending{color:#b91c1c;font-weight:600;}
.s-launched{color:#0d6b35;font-weight:600;}

.mkt-card{background:#fff;border:1.5px solid #e5e8ef;border-radius:10px;
  padding:18px 20px;margin-bottom:12px;box-shadow:0 1px 4px rgba(0,0,0,0.04);}
.mkt-num{font-size:28px;font-weight:700;color:#111827;line-height:1.1;}
.mkt-unit{font-size:14px;font-weight:500;color:#6b7280;margin-left:4px;}
.mkt-label{font-size:12px;color:#6b7280;margin-top:4px;line-height:1.4;}
.mkt-cagr{font-size:12px;color:#0d6b35;font-weight:600;margin-top:4px;}
.mkt-source{font-size:10px;color:#9098b0;font-style:italic;margin-top:4px;}
.bar-track{background:#e5e8ef;border-radius:4px;height:10px;margin:4px 0 2px 0;overflow:hidden;}
.bar-fill{height:100%;border-radius:4px;}

.tl-row{display:flex;gap:14px;align-items:flex-start;margin-bottom:10px;}
.tl-date{flex-shrink:0;width:90px;font-size:11px;font-weight:700;color:#6b7280;padding-top:3px;}
.tl-dot{flex-shrink:0;width:10px;height:10px;border-radius:50%;margin-top:5px;}
.tl-text{font-size:13px;color:#374151;line-height:1.5;}

.source-note{font-size:11px;color:#9098b0;font-style:italic;}
.page-header{font-size:12px;color:#9098b0;letter-spacing:.06em;text-transform:uppercase;margin-bottom:6px;}
.section-divider{border-top:1.5px solid #e5e8ef;margin:20px 0;}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────
def badge(text, cls):
    return f'<span class="badge {cls}">{text}</span>'

def info_card(title, html):
    return f'<div class="info-card"><div class="info-card-title">{title}</div><div class="info-card-value">{html}</div></div>'

def trial_box(t):
    return (f'<div class="trial-box"><div class="trial-box-title">🔬 {t["name"]}</div>'
            f'<div class="trial-box-body"><b>Citation:</b> {t["citation"]}<br>'
            f'<b>Design:</b> {t["design"]}<br>'
            f'<b>Primary endpoint:</b> {t["primary_endpoint"]}<br>'
            f'<b>Result:</b> {t["result"]}</div></div>')

# ─────────────────────────────────────────────
# DRUG DATA
# ─────────────────────────────────────────────
DRUGS = {
    "VUITY": {
        "brand":"VUITY®","generic":"Pilocarpine hydrochloride ophthalmic solution 1.25%",
        "company":"Allergan / AbbVie","approval_status":"FDA Approved",
        "approval_date":"October 29, 2021","approval_note":"First-ever FDA-approved presbyopia eye drop",
        "nda_number":"NDA 214028","application_type":"NDA — 505(b)(1)","rx_type":"Prescription (Rx only)",
        "active_ingredient":"Pilocarpine hydrochloride","concentration":"1.25% (12.5 mg/mL)",
        "free_base_equivalent":"1.06% (10.6 mg/mL) pilocarpine free-base",
        "iupac":"(3S,4R)-3-ethyl-4-[(1-methyl-1H-imidazol-5-yl)methyl]oxolan-2-one hydrochloride",
        "molecular_formula":"C₁₁H₁₆N₂O₂ · HCl","molecular_weight":"244.72 g/mol",
        "drug_class":"Cholinergic muscarinic M3 receptor agonist (partial)",
        "moa":("Partial M3 muscarinic receptor agonist. Activates M3 on iris sphincter → miosis (pinhole effect). "
               "Simultaneously activates M3 on ciliary muscle → zonule relaxation → lens thickening → accommodation. "
               "Partial-agonist ceiling self-limits spasm risk compared to carbachol."),
        "technology":"pH-buffered low-viscosity isotonic solution; BAK-preserved multi-dose bottle",
        "dosing":"1 drop each eye once daily. Second dose possible 3–6 h after first. Separate from other drops by ≥5 min.",
        "dosage_form":"2.5 mL multi-dose bottle","onset":"As early as 15 min","duration":"Up to 6 hours",
        "storage":"Room temperature 15–25°C","preservative":"BAK 0.0075%","ph_range":"3.5–5.5",
        "excipients":[
            {"name":"Benzalkonium chloride (BAK) 0.0075%","role":"Preservative",
             "function":"Antimicrobial for multi-dose bottle. Disrupts microbial cell membranes. Lowest BAK concentration among BAK-preserved ophthalmic products; risk of chronic corneal epithelial toxicity with long-term daily use."},
            {"name":"Boric acid","role":"Buffer",
             "function":"Maintains pH 3.5–5.5 preventing pilocarpine hydrolysis to inactive isopilocarpine. Mild antimicrobial."},
            {"name":"Sodium citrate dihydrate","role":"Buffer / Chelating",
             "function":"Chelates divalent metal ions (Ca²⁺, Fe²⁺) that catalyze oxidative degradation. Softens acidity sting on instillation."},
            {"name":"Sodium chloride","role":"Tonicity agent",
             "function":"Adjusts osmolality to ~280–320 mOsm/kg. Minimises instillation discomfort."},
            {"name":"Purified water","role":"Vehicle","function":"Aqueous vehicle, USP grade."},
            {"name":"HCl / NaOH","role":"pH adjuster","function":"Titrates final pH to 3.5–5.5 during manufacturing."},
        ],
        "key_trials":[
            {"name":"GEMINI 1 (Phase 3)","citation":"Waring GO et al. JAMA Ophthalmol. 2022;140:363–371",
             "design":"RCT, double-masked, vehicle-controlled, 30 days, n=354",
             "primary_endpoint":"≥3-line mesopic DCNVA gain + <5-letter BCDVA loss",
             "result":"~26% achieved ≥3-line gain vs ~9% vehicle. Onset Day 1. Peak ~1h. Duration up to 6h."},
            {"name":"GEMINI 2 (Phase 3)","citation":"Confirmatory — supported NDA submission",
             "design":"Identical design to GEMINI 1","primary_endpoint":"Same composite endpoint",
             "result":"Confirmed GEMINI 1 results. Both trials supported FDA approval Oct 2021."},
        ],
        "efficacy_summary":"~26% ≥3-line mesopic DCNVA gain vs ~9% vehicle. Onset 15 min, peak ~1h, duration up to 6h. Distance vision preserved.",
        "side_effects":[
            ("Headache / brow ache",">5%","Rapid ciliary muscle contraction (spasm). Most common discontinuation reason."),
            ("Conjunctival hyperemia",">5%","Cholinergic-mediated vasodilation."),
            ("Blurred vision","Common","Transient; shortly after instillation."),
            ("Dim / dark vision","Common","Miosis reduces light entry; worse in low-light settings."),
            ("Myopic shift","Up to −1.75 D","Over-accommodation; temporary distance blurring."),
            ("Retinal detachment / tear","Rare","Case reports post-approval. Higher risk in myopes. Retinal exam recommended before initiating therapy."),
        ],
        "contraindications":"Known hypersensitivity. Caution: iritis, narrow anterior chamber angle, history of retinal disease.",
    },
    "QLOSI": {
        "brand":"QLOSI™","generic":"Pilocarpine hydrochloride ophthalmic solution 0.4%",
        "company":"Orasis Pharmaceuticals / Optus Pharma (Korea)","approval_status":"FDA Approved",
        "approval_date":"October 16, 2023","approval_note":"Second approved; lowest-concentration pilocarpine; PF unit-dose. Korea: license Oct 2025 (₩24B), MFDS NDA not yet filed.",
        "nda_number":"NDA 215962","application_type":"NDA — 505(b)(1)","rx_type":"Prescription (Rx only)",
        "active_ingredient":"Pilocarpine hydrochloride","concentration":"0.4% (4 mg/mL)",
        "free_base_equivalent":"~0.34% pilocarpine free-base",
        "iupac":"(3S,4R)-3-ethyl-4-[(1-methyl-1H-imidazol-5-yl)methyl]oxolan-2-one hydrochloride",
        "molecular_formula":"C₁₁H₁₆N₂O₂ · HCl","molecular_weight":"244.72 g/mol",
        "drug_class":"Cholinergic muscarinic M3 receptor agonist (partial, low-dose)",
        "moa":("Same M3 agonism as Vuity but 0.4% concentration. Sits below the ciliary spasm threshold while above "
               "the miosis efficacy threshold. Polysorbate 80 enhances corneal penetration at this low concentration. "
               "PRN use possible — designed for on-demand dosing."),
        "technology":"Low-dose miotic; PF unit-dose vial; polysorbate 80 penetration enhancer system",
        "dosing":"1 drop each eye once daily or as needed. Single-use vial — discard after use.",
        "dosage_form":"0.3 mL PF unit-dose vials","onset":"Within 30 min","duration":"Up to 8 hours",
        "storage":"Room temperature 15–30°C","preservative":"None (PF)","ph_range":"~5.0–5.5",
        "excipients":[
            {"name":"Polysorbate 80","role":"Solubilizer / Penetration enhancer",
             "function":"Enhances corneal penetration at low pilocarpine concentration by loosening tight junctions and improving drug partitioning into corneal lipid layers. Critical for maintaining efficacy at 0.4%."},
            {"name":"Boric acid","role":"Buffer",
             "function":"Maintains acidic pH (5.0–5.5) stabilising pilocarpine against hydrolysis."},
            {"name":"Mannitol","role":"Tonicity agent / Stabiliser",
             "function":"Provides isotonicity without chloride ions. Avoids chloride-catalysed pilocarpine oxidation. Also mild antioxidant."},
            {"name":"Sodium chloride","role":"Tonicity co-agent","function":"Fine-tunes osmolality to physiological range."},
            {"name":"HCl / NaOH","role":"pH adjuster","function":"Titrates to pH 5.0–5.5."},
            {"name":"Water for injection","role":"Vehicle","function":"USP WFI — highest purity for sterile PF unit-dose."},
        ],
        "key_trials":[
            {"name":"NEAR-1 & NEAR-2 (Phase 3)","citation":"Holland E et al. Clin Ther. 2024;46:104–113",
             "design":"Two multicenter, double-masked, vehicle-controlled trials. Oct 2020–Feb 2022. 35 US sites.",
             "primary_endpoint":"≥3-line mesopic DCNVA + <5-letter BCDVA loss",
             "result":"Both trials met primary and secondary endpoints. Duration up to 8h. Lower brow ache vs 1.25% formulations."},
        ],
        "efficacy_summary":"Both NEAR-1 and NEAR-2 met primary endpoints. Duration up to 8h. Lower side effect burden vs Vuity due to reduced concentration.",
        "side_effects":[
            ("Headache / brow ache","Lower than Vuity","Reduced ciliary spasm at 0.4%."),
            ("Dim vision","Common (class)","Miosis reduces light entry."),
            ("Eye irritation","Mild","Less than BAK-preserved products."),
            ("Myopic shift","Reduced vs Vuity","Less ciliary stimulation."),
            ("Retinal detachment","Rare (class warning)","Retained for all miotics."),
        ],
        "contraindications":"Known hypersensitivity. Caution: iritis, narrow angle, retinal disease.",
    },
    "VIZZ": {
        "brand":"VIZZ™","generic":"Aceclidine ophthalmic solution 1.44%",
        "company":"LENZ Therapeutics (Nasdaq: LENZ)","approval_status":"FDA Approved",
        "approval_date":"July 31, 2025","approval_note":"First FDA-approved aceclidine; first once-daily drop with ≤10h efficacy; new chemical entity (NCE). Korea: Alvogen Korea license May 2025, MFDS NDA filed Dec 2025.",
        "nda_number":"NDA 218585","application_type":"NDA — 505(b)(1) — NCE","rx_type":"Prescription (Rx only)",
        "active_ingredient":"Aceclidine hydrochloride (≡ 1.44% aceclidine)","concentration":"1.75% aceclidine HCl (17.82 mg/mL)",
        "free_base_equivalent":"1.44% aceclidine (14.4 mg/mL)",
        "iupac":"3-Acetoxyquinuclidine hydrochloride (3-Quinuclidinyl Acetate Hydrochloride)",
        "molecular_formula":"C₉H₁₅NO₂ · HCl","molecular_weight":"205.68 g/mol",
        "drug_class":"Iris-selective cholinergic muscarinic M3 agonist (pupil-selective miotic)",
        "moa":("Aceclidine binds M3 receptors with preferential selectivity for iris sphincter over ciliary muscle. "
               "Stronger/longer pupil constriction (sub-2mm) than pilocarpine with markedly less ciliary stimulation. "
               "Hypromellose extends ocular surface residence time → 10h duration. No myopic shift, minimal brow ache."),
        "technology":"Iris-selective NCE; viscous solution with hypromellose for extended contact time; refrigerated PF unit-dose",
        "dosing":"1 drop each eye once daily. Effect within 30 min. Discard single-use vial after use.",
        "dosage_form":"PF unit-dose vials (refrigerated)","onset":"Within 30 min","duration":"Up to 10 hours",
        "storage":"Refrigerated 2–8°C. Do not freeze.","preservative":"None (PF)","ph_range":"4.5–5.5",
        "excipients":[
            {"name":"Polysorbate 80","role":"Solubilizer / Wetting",
             "function":"Solubilises aceclidine HCl, enhances corneal penetration. Wetting agent improving drug-ocular surface contact."},
            {"name":"Mannitol","role":"Tonicity / Stabiliser",
             "function":"Primary tonicity agent (~280–320 mOsm/kg). Lower metal ion-catalysed degradation risk vs NaCl. Mild antioxidant."},
            {"name":"Hypromellose (HPMC)","role":"Viscosity / Bioadhesive",
             "function":"KEY efficacy excipient. Increases viscosity (~15–25 cP), slows nasolacrimal drainage → extended ocular surface residence time → major contributor to 10h duration advantage. Also lubricates."},
            {"name":"Edetate disodium (EDTA·2Na)","role":"Chelating / Penetration aid",
             "function":"Sequesters divalent metals (Ca²⁺, Fe²⁺) preventing oxidative degradation. Chelates Ca²⁺ from tight junctions → increased corneal permeability."},
            {"name":"Sodium citrate dihydrate","role":"Buffer",
             "function":"Citrate buffer maintains pH 4.5–5.5. Better tolerated than phosphate at equivalent molarity."},
            {"name":"HCl / NaOH","role":"pH adjuster","function":"Titrates to 4.5–5.5. Aceclidine (pKa ~9.5) most stable at acidic pH."},
            {"name":"Water for injection","role":"Vehicle","function":"USP WFI for sterile PF unit-dose."},
        ],
        "key_trials":[
            {"name":"CLARITY 1 (Phase 3)","citation":"NCT05656027 · n=466 · 42 days",
             "design":"RCT, double-masked, vehicle-controlled, once daily, multicenter",
             "primary_endpoint":"≥3-line mesopic DCNVA + <5-letter BCDVA loss",
             "result":"Met all primary & secondary endpoints (p<0.0001). 71% gained ≥3 lines at 30 min and 3h. 40% maintained at 10h."},
            {"name":"CLARITY 2 (Phase 3)","citation":"NCT06045299 · n=466 · 42 days",
             "design":"Confirmatory RCT, double-masked, vehicle-controlled",
             "primary_endpoint":"Same composite","result":"All endpoints met. 70–75% pooled ≥3-line vs ~10–15% vehicle. No serious treatment-related AEs in 30,000+ treatment days."},
            {"name":"CLARITY 3 (6-month safety)","citation":"NCT05753189 · n=217",
             "design":"Open-label 6-month safety extension","primary_endpoint":"Long-term safety",
             "result":"Well-tolerated at 6 months. No tachyphylaxis. Sustained efficacy confirmed."},
        ],
        "efficacy_summary":"70–75% ≥3-line DCNVA gain vs ~10–15% vehicle. Onset 30 min. Duration up to 10h — longest approved. No myopic shift. No serious AEs in 30,000+ treatment days.",
        "side_effects":[
            ("Instillation site irritation","~20%","Transient, mild, self-resolving. Related to acidic pH."),
            ("Dim vision","~16%","Miosis reduces light entry; expected class effect."),
            ("Headache","~13%","Significantly lower than pilocarpine; minimal ciliary stimulation."),
            ("Eye redness","Low","Minimal hyperemia."),
            ("Myopic shift","Minimal to none","Iris-selective mechanism avoids significant ciliary stimulation."),
        ],
        "contraindications":"Known hypersensitivity to aceclidine or excipients. Caution: iritis, narrow anterior chamber angle.",
    },
    "YUVEZZI": {
        "brand":"YUVEZZI™","generic":"Carbachol 2.75% / Brimonidine tartrate 0.1% ophthalmic solution",
        "company":"Tenpoint Therapeutics / Kwangdong Pharma (Korea)","approval_status":"FDA Approved",
        "approval_date":"January 28, 2026","approval_note":"First FDA-approved dual-agent FDC for presbyopia. Korea: Kwangdong license Jan 2024, MFDS NDA filed Sep 2025 — first presbyopia NDA in Korea.",
        "nda_number":"NDA 218124","application_type":"NDA — 505(b)(2) — Fixed-dose combination","rx_type":"Prescription (Rx only)",
        "active_ingredient":"Carbachol 2.75% + Brimonidine tartrate 0.1%",
        "concentration":"Carbachol: 27.5 mg/mL (2.75%) | Brimonidine tartrate: 1.0 mg/mL (0.1%)",
        "free_base_equivalent":"N/A (marketed as salts)",
        "iupac":("Carbachol: 2-[(Aminocarbonyl)oxy]-N,N,N-trimethylethanaminium chloride\n"
                 "Brimonidine tartrate: 5-Bromo-N-(4,5-dihydro-1H-imidazol-2-yl)quinoxalin-6-amine L-tartrate"),
        "molecular_formula":"Carbachol: C₆H₁₅ClN₂O₂ (MW 182.65) | Brimonidine tartrate: C₁₁H₁₀BrN₅·C₄H₆O₆ (MW 442.24)",
        "molecular_weight":"Carbachol: 182.65 g/mol | Brimonidine tartrate: 442.24 g/mol",
        "drug_class":"FDC: Full muscarinic+nicotinic agonist (carbachol) + presynaptic α2-adrenergic agonist (brimonidine)",
        "moa":("CARBACHOL (full M3+nicotinic agonist): Directly contracts iris sphincter → strong miosis. Contracts ciliary muscle → accommodation. "
               "Full agonism gives stronger, longer miosis than pilocarpine.\n\n"
               "BRIMONIDINE (presynaptic α2 agonist): Blocks α2 receptors at iris dilator nerve terminals → inhibits NE release → "
               "dilator silenced. Also (1) relaxes tonic ciliary tension → reduces carbachol brow ache, (2) vasoconstricts conjunctiva → "
               "reduces redness (2.8% vs 10.7% carbachol alone), (3) increases cholinergic bioavailability in aqueous ~50%.\n\n"
               "Net: stronger sustained miosis than either drug alone, lower side effects than carbachol monotherapy."),
        "technology":"Dual-pathway FDC; parasympathetic (M3) + sympathetic (α2) simultaneous targeting; PF unit-dose",
        "dosing":"1 drop each eye once daily. Single-use vial — discard after opening.",
        "dosage_form":"0.3 mL PF unit-dose vials","onset":"30–60 min","duration":"Up to 8 hours",
        "storage":"Room temperature 20–25°C. Protect from light.","preservative":"None (PF)","ph_range":"~6.5–7.5",
        "excipients":[
            {"name":"Sodium chloride","role":"Tonicity agent",
             "function":"Adjusts osmolality (~280–320 mOsm/kg). Both APIs are stable in isotonic NaCl solution."},
            {"name":"Sodium phosphate monobasic","role":"Buffer",
             "function":"Maintains pH 6.5–7.5 where both carbachol and brimonidine tartrate are chemically stable. Phosphate buffer well-tolerated ophthalmically."},
            {"name":"HCl / NaOH","role":"pH adjuster","function":"Fine-tunes pH. Carbachol stable at pH 5–8; brimonidine at pH 6–8. pH chosen to satisfy both APIs."},
            {"name":"Water for injection","role":"Vehicle","function":"USP WFI for sterile PF unit-dose."},
        ],
        "key_trials":[
            {"name":"BRIO-I (Phase 3 — combination superiority)","citation":"NCT05270863 · Tenpoint Therapeutics",
             "design":"3-arm RCT: YUVEZZI vs carbachol alone vs brimonidine alone",
             "primary_endpoint":"Combination superiority over each active monotherapy (FDA FDC requirement)",
             "result":"YUVEZZI superior to both individual active components. Met FDA combination superiority requirement."},
            {"name":"BRIO-II (Phase 3 — 12-month safety)","citation":"NCT05270876 · 72,000+ treatment days",
             "design":"Vehicle-controlled, 12-month — longest presbyopia safety study to date",
             "primary_endpoint":"≥3-line BUNVA improvement; 12-month safety",
             "result":"All near vision endpoints met sustained over 8h. Hyperemia 2.8% vs 10.7% carbachol alone. No serious AEs in 72,000+ treatment days."},
        ],
        "efficacy_summary":"Superior to both monotherapies. ≥3-line BUNVA over 8h sustained. Lowest hyperemia (2.8%). 72,000+ treatment-day safety dataset — most extensive in category.",
        "side_effects":[
            ("Ocular hyperemia","2.8% — lowest of all drops","Brimonidine vasoconstriction offsets carbachol hyperemia."),
            ("Brow ache / headache","Reduced vs carbachol alone","Brimonidine dampens carbachol ciliary spasm."),
            ("Dim vision","Common (class)","Expected."),
            ("Myopic shift","Possible, reduced","Brimonidine's ciliary relaxation partially offsets carbachol-driven shift."),
            ("Dry mouth (brimonidine)","Uncommon","α2 effect on salivary glands; low risk at 0.1%."),
            ("CNS / hypotension","Rare at 0.1%","Monitor in elderly or antihypertensive users."),
            ("Young children","CONTRAINDICATED","Brimonidine crosses immature blood-brain barrier → CNS depression."),
        ],
        "contraindications":"Known hypersensitivity. CONTRAINDICATED in young children. Caution: antihypertensives, MAO inhibitors, iritis.",
    },
    "RYZUMVI": {
        "brand":"Ryzumvi®","generic":"Phentolamine mesylate ophthalmic solution 0.75%",
        "company":"Viatris / Opus Genetics","approval_status":"FDA Approved (mydriasis reversal) | Presbyopia: sNDA under review",
        "approval_date":"Sep 25, 2023 (mydriasis) | Presbyopia PDUFA: Oct 17, 2026",
        "approval_note":"Approved for mydriasis reversal (NDA 217064). sNDA for presbyopia accepted Feb 25, 2026 — PDUFA Oct 17, 2026. Same formulation; indication expansion only.",
        "nda_number":"NDA 217064","application_type":"NDA — 505(b)(2) (original); sNDA (presbyopia indication expansion)","rx_type":"Prescription (Rx only)",
        "active_ingredient":"Phentolamine mesylate","concentration":"0.75% (10 mg/mL mesylate ≡ 7.5 mg/mL free base)",
        "free_base_equivalent":"0.75% phentolamine free-base",
        "iupac":"3-[[(4,5-Dihydro-1H-imidazol-2-yl)methyl](4-methylphenyl)amino]phenol methanesulfonate",
        "molecular_formula":"C₁₇H₁₉N₃O · CH₃SO₃H (mesylate) | C₁₇H₁₉N₃O (free base)",
        "molecular_weight":"377.46 g/mol (mesylate) | 281.36 g/mol (free base)",
        "drug_class":"Non-selective α1/α2-adrenergic antagonist (alpha-blocker)",
        "moa":("PRIMARY — α1 postsynaptic blockade at iris dilator: Blocks α1 receptors on iris dilator → dilator cannot contract → "
               "sphincter acts unopposed → passive pupil constriction. NO direct sphincter activation. NO ciliary muscle involvement.\n\n"
               "SECONDARY — α2 blockade at sphincter: Blocks inhibitory α2 on sphincter → releases brake → adds indirect sphincter activation.\n\n"
               "CONSEQUENCE: No brow ache (no ciliary spasm), no myopic shift (no ciliary contraction), no retinal traction risk. "
               "Effect lasts up to 20h from a single EVENING dose."),
        "technology":"α1/α2 antagonist; ultra-minimalist PF formulation with nitrogen overlay to prevent oxidation; evening dosing; refrigerated",
        "dosing":"1 drop each eye once daily IN THE EVENING. 20h duration covers following morning/day. Nasolacrimal duct occlusion recommended.",
        "dosage_form":"0.31 mL PF unit-dose vials (5 per foil pouch, 6 pouches per carton)","onset":"60–90 min after evening instillation","duration":"Up to 20 hours",
        "storage":"Refrigerated 2–8°C. After opening pouch: up to 25°C for 14 days. Do not freeze.","preservative":"None (PF)","ph_range":"4.5–5.5",
        "excipients":[
            {"name":"Mannitol","role":"Tonicity / Antioxidant",
             "function":"Primary tonicity agent. CRITICAL: used instead of NaCl because chloride ions catalyse phentolamine oxidation. Mannitol also acts as mild hydroxyl radical scavenger — secondary antioxidant function preserving potency."},
            {"name":"Sodium acetate trihydrate","role":"Buffer",
             "function":"Acetate buffer maintains pH 4.5–5.5 where phentolamine is most chemically stable. Low-molarity acetate (5–25 mM) minimises instillation sting while providing adequate pH control."},
            {"name":"HCl / NaOH","role":"pH adjuster","function":"Titrates to 4.5–5.5 satisfying acetate buffer range and phentolamine stability simultaneously."},
            {"name":"Water for injection","role":"Vehicle","function":"Metal-ion free USP WFI — critical given phentolamine's metal-catalysed oxidation sensitivity."},
            {"name":"Nitrogen gas (headspace)","role":"Antioxidant atmosphere",
             "function":"UNIQUE FEATURE — vial headspace filled with nitrogen before sealing. Eliminates dissolved oxygen preventing phentolamine air oxidation. Only approved ophthalmic drug with this feature. Explains why unit-dose format is required: once opened, nitrogen atmosphere is lost."},
        ],
        "key_trials":[
            {"name":"VEGA-3 (Phase 3 presbyopia — primary pivotal)","citation":"Viatris/Opus Genetics · n=545 · 40 US sites",
             "design":"RCT, double-masked, placebo-controlled, once-daily EVENING dose, 6-week + 48-week safety follow-up",
             "primary_endpoint":"≥3-line DCNVA + <5-letter BCDVA loss at 12h post-dose, Day 8",
             "result":"MET: 27.2% vs 11.5% placebo (p<0.0001). Secondary: 20.6% vs 6.1% at 1h Day 1 (p=0.0002). Patient-reported outcomes significant at Days 3, 8, Week 6. No serious treatment-related AEs. No tachyphylaxis at 6 weeks."},
            {"name":"VEGA-2 (Phase 3 presbyopia — second pivotal)","citation":"n=333, ages 40–64",
             "design":"Phase 3 with phentolamine ± adjunctive pilocarpine arm","primary_endpoint":"Near VA improvement",
             "result":"Met primary endpoint. Phentolamine alone and with low-dose pilocarpine both significantly improved near VA."},
            {"name":"MIRA-2 + MIRA-3 (Phase 3 — mydriasis reversal, approved)","citation":"n=553 combined, age 12–80",
             "design":"Two pivotal RCTs for mydriasis reversal","primary_endpoint":"Return to baseline pupil at 60 and 90 min",
             "result":"Both met. Supported NDA 217064 approval Sep 2023. Established safety infrastructure for sNDA."},
        ],
        "efficacy_summary":("VEGA-3: 27.2% ≥3-line DCNVA at 12h Day 8 vs 11.5% placebo (p<0.0001). Evening dose provides up to 20h near vision — effect present on waking. No brow ache. No myopic shift. "
                            "NOTE: Presbyopia indication NOT YET APPROVED — PDUFA October 17, 2026."),
        "side_effects":[
            ("Systemic hypotension","Low risk at ophthalmic dose","α-blockade lowers BP; caution with antihypertensives. Nasolacrimal occlusion recommended."),
            ("Dim vision at night","Possible","Miosis reduces light; minimised by evening dosing (patient asleep during peak)."),
            ("Uveitis — CONTRAINDICATED","Absolute","Risk of synechiae in inflamed eyes."),
            ("Reflex tachycardia","Rare","Compensatory HR increase from α-blockade."),
            ("Refrigeration requirement","Compliance concern","Only presbyopia drug requiring cold-chain storage."),
        ],
        "contraindications":"Known hypersensitivity. Active uveitis/iritis. Caution: antihypertensives, cardiac conditions, MAO inhibitors. PRESBYOPIA USE INVESTIGATIONAL — PDUFA Oct 17, 2026.",
    },
}

DRUG_COLORS = {"VUITY":"#534AB7","QLOSI":"#0F6E56","VIZZ":"#BA7517","YUVEZZI":"#185FA5","RYZUMVI":"#A32D2D"}
DRUG_ORDER  = ["VUITY","QLOSI","VIZZ","YUVEZZI","RYZUMVI"]

# ─────────────────────────────────────────────
# NONCLINICAL / CLINICAL PK·PD STUDIES
# ─────────────────────────────────────────────
PKPD_STUDIES = [
    {"drug":"Pilocarpine","study":"28-day GLP ocular toxicology",
     "model":"NZW rabbit · 5–7/sex/group · BID × 28 days",
     "endpoint":"Ocular safety (Draize); histopathology; iris response",
     "result":"NOAEL = 1.0% pilocarpine BID. Slow iris responses observed at NOAEL — non-adverse and reversible. No histopathological findings at any dose.",
     "ref":"https://cdn.clinicaltrials.gov/large-docs/15/NCT02780115/Prot_001.pdf",
     "ref_short":"NCT02780115 Protocol"},
    {"drug":"Pilocarpine","study":"Single-dose ocular PK",
     "model":"Dutch-belted rabbit · Single bilateral dose · Fixed vs unfixed combo",
     "endpoint":"Ocular PK: Cmax, Tmax, AUC in aqueous humor and iris/ciliary body",
     "result":"Comparable ocular PK between fixed-combination and unfixed sequential dosing. Supports safety of 1.5% pilocarpine without hypromellose.",
     "ref":"https://cdn.clinicaltrials.gov/large-docs/15/NCT02780115/Prot_001.pdf",
     "ref_short":"NCT02780115 Protocol"},
    {"drug":"Pilocarpine","study":"Ocular tissue PK",
     "model":"NZW rabbit tolerability + PK arms · Single topical dose",
     "endpoint":"Pilocarpine detectability: aqueous humor, iris, lens; Draize scoring",
     "result":"Pilocarpine detectable in ocular tissues up to 8h post-dose. No corneal, iridial, or conjunctival adverse effects. Tmax ~0.5h in aqueous humor.",
     "ref":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12629135/",
     "ref_short":"PMC12629135"},
    {"drug":"Pilocarpine","study":"Accommodation PD model",
     "model":"Young adult rhesus monkey · Topical 0.5% pilocarpine ± oxymetazoline",
     "endpoint":"Pupil diameter; accommodative amplitude (refractometry); time to peak accommodative response",
     "result":"0.5% pilocarpine caused measurable decrease in pupil size and increase in accommodative amplitude. Co-admin with oxymetazoline delayed time to peak accommodative response.",
     "ref":"https://cdn.clinicaltrials.gov/large-docs/28/NCT02595528/Prot_001.pdf",
     "ref_short":"NCT02595528 Protocol"},
    {"drug":"Pilocarpine","study":"Systemic PK — Vuity NDA (clinical)",
     "model":"Human n=22 presbyopes · 1 drop/eye QD × 30 days",
     "endpoint":"Plasma Cmax, AUC₀₋τ,ss, Tmax, t½ at steady state",
     "result":"Cmax,ss = 1.95 ng/mL; AUC₀₋τ,ss = 4.14 ng·hr/mL; median Tmax = 0.3h; t½ ~3–4h. Systemic exposure very low — not expected to contribute to efficacy or toxicity.",
     "ref":"https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/214028Orig1s003lbl.pdf",
     "ref_short":"FDA Label NDA 214028"},
    {"drug":"Brimonidine","study":"Comparative ocular PK",
     "model":"Albino rabbit + Dutch-belted (pigmented) · Single 35µL drop 0.5% ¹⁴C-brimonidine",
     "endpoint":"Aqueous humor Cmax, Tmax; iris-ciliary body concentration over time; melanin binding",
     "result":"Aqueous Cmax: 2.16 µg/mL (albino) vs 1.52 µg/mL (pigmented) at Tmax 0.67h. Aqueous t½ ~1h (albino). Pigmented iris-ciliary body: peak 20.1 µg-eq/g at 1.5h; terminal t½ = 160h (melanin depot effect).",
     "ref":"https://pubmed.ncbi.nlm.nih.gov/7587958/",
     "ref_short":"PMID 7587958"},
    {"drug":"Brimonidine","study":"Tissue distribution",
     "model":"Monkey, rabbit, rat · Single + multiple doses · 0.2% and 0.5% topical",
     "endpoint":"Drug concentration in cornea, aqueous humor, iris-ciliary body, vitreous, retina/choroid, optic nerve; radioactivity by tissue type",
     "result":"Higher and more prolonged drug levels in pigmented vs non-pigmented tissues across all species. Multiple dosing led to drug accumulation in pigmented tissues. Posterior segment levels adequate to activate α2 receptors without retinal vasoconstriction.",
     "ref":"https://pubmed.ncbi.nlm.nih.gov/11901096/",
     "ref_short":"PMID 11901096"},
    {"drug":"Brimonidine","study":"Selectivity pharmacology — receptor binding",
     "model":"In vitro receptor binding assays (multiple species tissues)",
     "endpoint":"α2 vs α1 binding selectivity ratio; comparison vs clonidine and apraclonidine",
     "result":"Brimonidine is 1,000× more selective for α2 vs α1. 7–12× more α2-selective than clonidine. 23–32× more selective than apraclonidine. Not mydriatic (unlike apraclonidine).",
     "ref":"https://www.sciencedirect.com/science/article/abs/pii/S0039625796820273",
     "ref_short":"ScienceDirect"},
    {"drug":"Brimonidine","study":"Systemic PK — Alphagan P label (clinical)",
     "model":"Human n=14 · Single drop 0.15%/eye",
     "endpoint":"Plasma Cmax, AUC₀₋∞, Tmax after single topical dose",
     "result":"Cmax = 73 ± 19 pg/mL; AUC₀₋∞ = 375 ± 89 pg·hr/mL; Tmax = 1.7 ± 0.7h. ~27× lower systemic exposure than pilocarpine on a mass basis.",
     "ref":"https://www.accessdata.fda.gov/drugsatfda_docs/label/2006/021262s018lbl.pdf",
     "ref_short":"FDA Label NDA 021262"},
    {"drug":"Carbachol + Brimonidine","study":"Nonclinical PK/PD of Brimochol — ARVO 2022",
     "model":"Dutch-belted rabbit · n=4/group · Single unilateral 35µL: Brimochol vs carbachol 2.75% alone vs PBS",
     "endpoint":"Pupil diameter by digital pupillometer under 4 lighting conditions (scotopic, low mesopic, high mesopic, photopic); carbachol concentration in iris/ciliary body",
     "result":"Brimochol sustained pupil reduction for 12h vs shorter duration with carbachol alone. Greater pupil reduction at all 4 lighting levels. Brimonidine increased carbachol concentration in iris/ciliary body (~50% higher AUC) — mechanistically explains enhanced and prolonged PD effect. Ocular tolerance profile also improved vs carbachol alone.",
     "ref":"https://iovs.arvojournals.org/article.aspx?articleid=2780074",
     "ref_short":"ARVO 2022 / IOVS"},
]

# ─────────────────────────────────────────────
# PATENT DATA
# ─────────────────────────────────────────────
PATENTS = [
    {"no":"US8299079","holder":"Visus Therapeutics (now Tenpoint)","status":"Active until 2030",
     "scope":"Method of treating presbyopia using parasympathomimetics (pilocarpine, carbachol) combined with alpha agonist (brimonidine 0.05–3.0%) — broad method-of-use claim.",
     "note":"Tenpoint now holds YUVEZZI + this foundational patent. May license, enforce, or both. Contact required before development.",
     "ref":"https://patents.google.com/patent/US8299079"},
    {"no":"US11857539","holder":"Somerset Therapeutics LLC","status":"Active until 2043",
     "scope":"Gel formulation — pilo >1% + brim 0.05–0.2% with polyethoxylated castor oil",
     "note":"","ref":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11857539"},
    {"no":"US11969410","holder":"Somerset Therapeutics LLC","status":"Active until 2043",
     "scope":"Low pH formulation — pH 3–5.5, pilo 1.15–3% + brim 0.05–0.18%, BAK 0.003–0.02%",
     "note":"","ref":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11969410"},
    {"no":"US12156868","holder":"Somerset Therapeutics LLC","status":"Active until 2043",
     "scope":"Solution formulation — pilo 1.15–2.5% + brim 0.05–0.18%, viscosity enhancer 0.1–1%",
     "note":"","ref":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12156868"},
    {"no":"WO2009/077736","holder":"Unknown","status":"Active until 2027–2028",
     "scope":"Combination of pilocarpine + brimonidine (or iopidine) for presbyopia, myopia, hypermetropia, low night vision. National phase status varies by country including Korea.",
     "note":"Check whether applied in Korean territory. Active time 1–2 years from now — inline with development timeline.",
     "ref":"https://patents.google.com/patent/WO2022103250A1"},
    {"no":"US8455494","holder":"Visus Therapeutics (now Tenpoint)","status":"Active until May 2030",
     "scope":"Brimonidine <0.2%; pilocarpine <0.5% or even <0.1%; also covers phentolamine as alpha antagonist. Continuation of US8299079 detailing chemical concentrations.",
     "note":"Explicit naming of very low pilocarpine concentrations (<0.1%) means Tenpoint IP potentially reaches micro-dose formulations that might otherwise seem safely distant from the claimed range.",
     "ref":"https://patents.google.com/patent/US8455494"},
]

# ─────────────────────────────────────────────
# MARKET DATA  (verified sources cited inline)
# ─────────────────────────────────────────────
MARKET_GLOBAL = {
    "total_treatment_2024": 10.17,   # Straits Research 2024
    "total_treatment_2033": 16.77,
    "total_cagr": 5.5,
    "eye_drops_2024": 1.31,          # Dataintelo 2024
    "eye_drops_2033": 2.86,
    "eye_drops_cagr": 9.2,
    "pharma_fastest_cagr": 12.8,     # Emergen Research
    "global_presbyopes_2024": 1.8,   # WHO / Fricke 2018 Ophthalmology meta-analysis
    "global_presbyopes_2030": 2.1,
    "apac_cagr": 11.2,
    "north_america_share_pct": 42,
    "europe_share_pct": 29,
    "apac_share_pct": 20,
    "row_share_pct": 9,
}

MARKET_KOREA = {
    # Derived from Statistics Korea 2024 population data + WHO presbyopia prevalence
    # Korea population 2024: ~51.7M (Statistics Korea / World Bank)
    # Population ≥40: approximately 58% of total = ~30M (UN World Population Prospects 2024)
    # WHO global presbyopia prevalence in 40+ pop: ~55–80% depending on study; conservative ~55% used
    # → 30M × 0.55 = ~16.5M; rounded to ~16–17M
    # This is a derived estimate — no single Korean epidemiological study has directly counted presbyopia patients
    "est_patients_derived": "~16–17M",
    "est_basis": ("Derived estimate: Korea population ≥40 years ~30M "
                  "(Statistics Korea 2024 / UN World Population Prospects 2024: "
                  "median age 46.2y, ~58% of 51.7M population aged ≥40). "
                  "Applied WHO global presbyopia prevalence ~55% in 40+ population "
                  "(Fricke TR et al. Ophthalmology. 2018;125:1492–1499). "
                  "No single peer-reviewed Korean-specific epidemiological study directly "
                  "reports the national presbyopia patient count as of 2026."),
    "market_2023": 411.7,   # Grand View Research / Horizon Databook (myopia+presbyopia combined)
    "market_2025": 631.63,  # Expert Market Research (EMR) — myopia+presbyopia combined
    "market_2030": 885.9,   # Grand View Research
    "market_2035": 1242.51, # EMR 2025 report
    "cagr_2024_2030": 11.6, # Grand View Research
    "cagr_2025_2035": 7.0,  # EMR
    "note_combined": "Korea market figures are for combined myopia + presbyopia treatment market. Presbyopia-only ophthalmic drop sub-segment is pre-commercial (no approved product as of June 2026).",
    "drivers": [
        "Super-aged society: >20% population ≥65 as of Dec 2024 (Statista 2024) — fastest aging in OECD",
        "Median age 46.2 years (Worldometer 2026) — presbyopia peak demographic",
        "Highest smartphone penetration globally → digital eye strain compounding demand",
        "High disposable income + willingness to spend on premium healthcare",
        "No approved presbyopia drop yet — virgin segment awaiting first MFDS approval",
    ],
    "approved_drops": 0,
    "ndas_under_review": 3,
    "expected_first_approval": "2026",
}

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 💧 Presbyopia Eye Drop\n**Competitive Intelligence**")
    st.caption("Formulation · Clinical · Market · Patent")
    st.markdown("---")
    st.markdown("##### 📋 View")
    view_mode = st.radio("View", [
        "💊 Drug Profile",
        "📊 Comparison Table",
        "🔬 PK/PD Studies",
        "📜 Patent Landscape",
        "🇰🇷 Korea Market",
        "🌍 Global Market",
    ], label_visibility="collapsed")

    if view_mode == "💊 Drug Profile":
        st.markdown("---")
        st.markdown("##### Select Drug")
        selected_drug = st.radio("Drug", DRUG_ORDER,
            label_visibility="collapsed",
            format_func=lambda x: f"{DRUGS[x]['brand'].replace('®','').replace('™','')} — {x}")
    st.markdown("---")
    st.caption("Sources: FDA DailyMed, PubMed, ClinicalTrials.gov, Statistics Korea, EMR, Grand View Research, Straits Research. June 2026.")

# ─────────────────────────────────────────────
# VIEW: DRUG PROFILE
# ─────────────────────────────────────────────
if view_mode == "💊 Drug Profile":
    d = DRUGS[selected_drug]
    color = DRUG_COLORS[selected_drug]
    st.markdown(f'<p class="page-header">Drug Profile · {d["brand"]}</p>', unsafe_allow_html=True)

    if "sNDA" in d["approval_status"]:
        sb = badge("FDA Approved — Mydriasis Reversal","badge-approved")+badge("sNDA Presbyopia — PDUFA Oct 17 2026","badge-pending")+badge(d["rx_type"],"badge-rx")
    elif "Approved" in d["approval_status"]:
        sb = badge("FDA Approved","badge-approved")+badge(d["rx_type"],"badge-rx")
    else:
        sb = badge(d["approval_status"],"badge-pending")+badge(d["rx_type"],"badge-rx")

    st.markdown(f"""
<div class="drug-hero">
  <p class="drug-name" style="color:{color}">{d['brand']}</p>
  <p class="drug-generic">{d['generic']}</p>
  {sb}
  <div style="margin-top:14px;font-size:13px;color:#6b7280;">
    <b style="color:#111827">{d['company']}</b> &nbsp;·&nbsp; NDA: <b style="color:#111827">{d['nda_number']}</b>
    &nbsp;·&nbsp; Type: <b style="color:#111827">{d['application_type']}</b>
    &nbsp;·&nbsp; Approved: <b style="color:#111827">{d['approval_date']}</b>
  </div>
  <div style="margin-top:6px;font-size:12px;color:#9098b0;font-style:italic">{d['approval_note']}</div>
</div>
""", unsafe_allow_html=True)

    t1,t2,t3,t4,t5 = st.tabs(["🧬 API & Chemistry","⚗️ Formulation","💊 Dosing & Regulatory","🔬 Efficacy & Trials","⚠️ Safety"])

    with t1:
        st.markdown("#### Active Ingredient & Chemistry")
        c1,c2 = st.columns([1.2,0.8])
        with c1:
            st.markdown(info_card("IUPAC Name",f"<code style='font-size:12px;color:#1a4d9e;background:#f0f5ff;padding:4px 6px;border-radius:4px;'>{d['iupac'].replace(chr(10),'<br>')}</code>"),unsafe_allow_html=True)
            st.markdown(info_card("Molecular Formula",f"<span style='font-size:16px;font-family:monospace;color:#0d6b35;font-weight:700;'>{d['molecular_formula']}</span>"),unsafe_allow_html=True)
            st.markdown(info_card("Molecular Weight",f"<span style='font-size:16px;font-weight:700;color:#111827;'>{d['molecular_weight']}</span>"),unsafe_allow_html=True)
        with c2:
            st.markdown(info_card("Drug Class",d['drug_class']),unsafe_allow_html=True)
            st.markdown(info_card("Active Concentration",f"<b>{d['concentration']}</b><br><span style='color:#6b7280;font-size:12px;'>{d['free_base_equivalent']}</span>"),unsafe_allow_html=True)
            st.markdown(info_card("Prescription Type",f"<span class='hl'>{d['rx_type']}</span>"),unsafe_allow_html=True)
        st.markdown(info_card("Mechanism of Action",f"<div style='white-space:pre-line;'>{d['moa']}</div>"),unsafe_allow_html=True)
        st.markdown(info_card("Technology / Platform",d["technology"]),unsafe_allow_html=True)

    with t2:
        c1,c2,c3 = st.columns(3)
        with c1:
            st.markdown(info_card("Dosage Form",d["dosage_form"]),unsafe_allow_html=True)
            st.markdown(info_card("Preservative",f"<span class='{'hl' if 'None' in d['preservative'] else 'warn'}'>{d['preservative']}</span>"),unsafe_allow_html=True)
        with c2:
            st.markdown(info_card("pH Range",f"<b>{d['ph_range']}</b>"),unsafe_allow_html=True)
            st.markdown(info_card("Storage",d["storage"]),unsafe_allow_html=True)
        with c3:
            st.markdown(info_card("Active Concentration",f"<b>{d['concentration']}</b>"),unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("#### Excipients — complete list with formulation rationale")
        rows=""
        for i,e in enumerate(d["excipients"]):
            bg="background:#fafbfc;" if i%2==0 else ""
            rows+=f'<tr style="{bg}"><td><b>{e["name"]}</b></td><td><span class="excip-role">{e["role"]}</span></td><td>{e["function"]}</td></tr>'
        st.markdown(f'<div class="info-card"><table class="excip-table"><thead><tr><th style="min-width:200px">Excipient</th><th style="min-width:130px">Role</th><th>Function & Rationale</th></tr></thead><tbody>{rows}</tbody></table></div>',unsafe_allow_html=True)

    with t3:
        c1,c2 = st.columns(2)
        with c1:
            st.markdown(info_card("Dosing",d["dosing"]),unsafe_allow_html=True)
            st.markdown(info_card("Onset",f"<span class='hl'>{d['onset']}</span>"),unsafe_allow_html=True)
            st.markdown(info_card("Duration",f"<span class='hl'>{d['duration']}</span>"),unsafe_allow_html=True)
        with c2:
            st.markdown(info_card("Dosage Form",d["dosage_form"]),unsafe_allow_html=True)
            st.markdown(info_card("Storage",d["storage"]),unsafe_allow_html=True)
            st.markdown(info_card("Status",f"{d['approval_status']}<br><span style='font-size:12px;color:#9098b0;'>{d['approval_note']}</span>"),unsafe_allow_html=True)
        st.markdown("---")
        st.markdown(info_card("Regulatory Filing",f"<b>NDA:</b> {d['nda_number']}<br><b>Type:</b> {d['application_type']}<br><b>Approval:</b> {d['approval_date']}<br><b>Rx class:</b> {d['rx_type']}"),unsafe_allow_html=True)

    with t4:
        st.markdown(info_card("Overall Efficacy",d['efficacy_summary']),unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("#### Key Clinical Trials")
        for t in d["key_trials"]:
            st.markdown(trial_box(t),unsafe_allow_html=True)

    with t5:
        st.markdown("#### Adverse Effects")
        hdr_c = st.columns([1.2,0.6,2.2])
        hdr_c[0].markdown("**Adverse Effect**"); hdr_c[1].markdown("**Incidence**"); hdr_c[2].markdown("**Notes**")
        st.markdown('<div style="border-top:1.5px solid #e5e8ef;margin-bottom:8px"></div>',unsafe_allow_html=True)
        for ae,inc,note in d["side_effects"]:
            r = st.columns([1.2,0.6,2.2])
            r[0].markdown(f"<div style='font-size:13px;color:#111827;font-weight:500;padding:3px 0'>{ae}</div>",unsafe_allow_html=True)
            r[1].markdown(f"<div style='font-size:12px;color:#a05c00;font-weight:600;padding:3px 0'>{inc}</div>",unsafe_allow_html=True)
            r[2].markdown(f"<div style='font-size:12px;color:#5a5f78;padding:3px 0'>{note}</div>",unsafe_allow_html=True)
        st.markdown("---")
        st.markdown(info_card("Contraindications & Warnings",f"<span class='danger'>{d['contraindications']}</span>"),unsafe_allow_html=True)

# ─────────────────────────────────────────────
# VIEW: COMPARISON TABLE
# ─────────────────────────────────────────────
elif view_mode == "📊 Comparison Table":
    st.markdown('<p class="page-header">All 5 Drugs — Side-by-side Comparison</p>',unsafe_allow_html=True)
    st.markdown("## Competitive Comparison")
    rows=[]
    for k in DRUG_ORDER:
        d=DRUGS[k]
        rows.append({"Drug":d["brand"],"Company":d["company"].split("/")[0].strip(),
            "API":d["active_ingredient"].split("\n")[0],"Concentration":d["concentration"].split("\n")[0][:30],
            "Class":d["drug_class"][:45]+"…" if len(d["drug_class"])>45 else d["drug_class"],
            "FDA Status":d["approval_status"].split("|")[0].strip(),
            "Approval":d["approval_date"].split("|")[0].strip()[:20],
            "Dosing":d["dosing"][:55]+"…","Duration":d["duration"],
            "Preservative":d["preservative"],"Storage":d["storage"][:25]})
    st.dataframe(pd.DataFrame(rows).set_index("Drug"),use_container_width=True,height=230)

    st.markdown("---")
    st.markdown("### Molecular Data")
    mol=[]
    for k in DRUG_ORDER:
        d=DRUGS[k]
        mol.append({"Brand":d["brand"],"API":d["active_ingredient"].split("\n")[0],
            "IUPAC (short)":d["iupac"].split("\n")[0][:65]+"…" if len(d["iupac"].split("\n")[0])>65 else d["iupac"].split("\n")[0],
            "Formula":d["molecular_formula"].split("|")[0].strip()[:28],"MW":d["molecular_weight"].split("|")[0].strip()[:18]})
    st.dataframe(pd.DataFrame(mol).set_index("Brand"),use_container_width=True)

    st.markdown("---")
    st.markdown("### Excipient Category Comparison")
    ex=[]
    for k in DRUG_ORDER:
        d=DRUGS[k]
        ex.append({"Brand":d["brand"],
            "Preservative":d["preservative"] if "None" not in d["preservative"] else "PF — None",
            "Buffer":next((e["name"].split(" (")[0] for e in d["excipients"] if "Buffer" in e["role"]),"—"),
            "Tonicity":next((e["name"].split(" ")[0] for e in d["excipients"] if "Tonicity" in e["role"]),"—"),
            "Viscosity Agent":next((e["name"].split(",")[0] for e in d["excipients"] if "Viscosity" in e["role"]),"None"),
            "pH Range":d["ph_range"],
            "Unique Feature":{"VUITY":"BAK 0.0075% (multi-dose)","QLOSI":"Polysorbate 80 penetration enhancer",
                "VIZZ":"HPMC viscosity → 10h duration","YUVEZZI":"Dual-API; minimal 4-excipient matrix","RYZUMVI":"N₂ headspace; mannitol replaces NaCl"}.get(k,"—")})
    st.dataframe(pd.DataFrame(ex).set_index("Brand"),use_container_width=True)

# ─────────────────────────────────────────────
# VIEW: PK/PD STUDIES
# ─────────────────────────────────────────────
elif view_mode == "🔬 PK/PD Studies":
    st.markdown('<p class="page-header">Selected Nonclinical & Clinical PK/PD Studies</p>',unsafe_allow_html=True)
    st.markdown("## PK/PD Evidence Base")
    st.info("Data from your research table (verified). Nonclinical = animal/in vitro. Clinical = human data. All references linked.",icon="📋")

    drug_filter = st.multiselect("Filter by drug",
        options=["Pilocarpine","Brimonidine","Carbachol + Brimonidine"],
        default=["Pilocarpine","Brimonidine","Carbachol + Brimonidine"])

    filtered = [s for s in PKPD_STUDIES if any(f.lower() in s["drug"].lower() for f in drug_filter)]
    study_type = st.radio("Study type",["All","Nonclinical only","Clinical only"],horizontal=True)
    if study_type == "Nonclinical only":
        filtered = [s for s in filtered if "Human" not in s["model"] and "human" not in s["model"]]
    elif study_type == "Clinical only":
        filtered = [s for s in filtered if "Human" in s["model"] or "human" in s["model"]]

    st.markdown(f"**{len(filtered)} studies shown**")
    st.markdown("---")

    rows=""
    for s in filtered:
        is_clinical = "Human" in s["model"] or "human" in s["model"]
        type_badge = ("<span style='background:#e6f9f0;color:#0d6b35;font-size:10px;font-weight:700;padding:2px 8px;border-radius:10px;'>CLINICAL</span>"
                      if is_clinical else
                      "<span style='background:#f0f5ff;color:#1a3d8a;font-size:10px;font-weight:700;padding:2px 8px;border-radius:10px;'>NONCLINICAL</span>")
        drug_col = {"Pilocarpine":"#534AB7","Brimonidine":"#0F6E56","Carbachol + Brimonidine":"#185FA5"}.get(s["drug"],"#888")
        rows += (f'<tr>'
                 f'<td><b style="color:{drug_col}">{s["drug"]}</b></td>'
                 f'<td>{type_badge}<br><span style="font-size:12px;font-weight:600;">{s["study"]}</span></td>'
                 f'<td style="font-size:12px">{s["model"]}</td>'
                 f'<td style="font-size:12px">{s["endpoint"]}</td>'
                 f'<td style="font-size:12px">{s["result"]}</td>'
                 f'<td style="font-size:11px"><a href="{s["ref"]}" target="_blank" style="color:#1a4d9e;">{s["ref_short"]} ↗</a></td>'
                 f'</tr>')

    st.markdown(f'<div style="overflow-x:auto"><table class="pk-table"><thead><tr><th>Drug</th><th>Study / Type</th><th>Animal / Population Model</th><th>PD Endpoint</th><th>Key Result</th><th>Ref</th></tr></thead><tbody>{rows}</tbody></table></div>',unsafe_allow_html=True)
    st.markdown('<p class="source-note" style="margin-top:10px">Data verified from referenced sources. Links open original protocol documents, FDA labels, or PubMed abstracts.</p>',unsafe_allow_html=True)

# ─────────────────────────────────────────────
# VIEW: PATENT LANDSCAPE
# ─────────────────────────────────────────────
elif view_mode == "📜 Patent Landscape":
    st.markdown('<p class="page-header">Patent Landscape · Pilocarpine + Brimonidine Combinations</p>',unsafe_allow_html=True)
    st.markdown("## Patent Landscape — Dual Formulation IP")
    st.warning("All patents listed cover pilocarpine + brimonidine combination formulations for presbyopia. Review with legal counsel before product development.",icon="⚠️")

    rows=""
    for p in PATENTS:
        exp_year = int(p["status"].split("until ")[1].split("-")[0].split(" ")[0][:4])
        is_near = exp_year <= 2030
        status_cls = "pat-warn" if is_near else "pat-active"
        note_html = f'<div style="margin-top:6px;font-size:11px;color:#6b7280;font-style:italic">{p["note"]}</div>' if p["note"] else ""
        rows += (f'<tr>'
                 f'<td><a href="{p["ref"]}" target="_blank" style="color:#1a4d9e;font-weight:700;">{p["no"]} ↗</a></td>'
                 f'<td style="font-size:12px">{p["holder"]}</td>'
                 f'<td class="{status_cls}" style="font-size:12px">{p["status"]}</td>'
                 f'<td style="font-size:12px">{p["scope"]}{note_html}</td>'
                 f'</tr>')

    st.markdown(f'<div style="overflow-x:auto"><table class="pat-table"><thead><tr><th>Patent No</th><th>Holder</th><th>Status</th><th>Scope & Notes</th></tr></thead><tbody>{rows}</tbody></table></div>',unsafe_allow_html=True)

    st.markdown("---")
    c1,c2,c3 = st.columns(3)
    c1.markdown(info_card("Key Originator — Tenpoint (Visus)","US8299079 (2030) + US8455494 (2030) together cover the <b>core method-of-use</b> for pilocarpine/carbachol + brimonidine in presbyopia. Any combination product in this space must either license from Tenpoint or design around these claims."),unsafe_allow_html=True)
    c2.markdown(info_card("Near-expiry window","WO2009/077736 expires 2027–2028 — creating a potential freedom-to-operate window for pilocarpine + brimonidine in some territories. <span class='warn'>Check Korean national phase status.</span>"),unsafe_allow_html=True)
    c3.markdown(info_card("Somerset portfolio (until 2043)","Three patents covering specific gel, low-pH, and solution formulations of pilo + brim combinations. Blocks specific excipient combinations including polyethoxylated castor oil, BAK 0.003–0.02%, and viscosity enhancers 0.1–1%."),unsafe_allow_html=True)

# ─────────────────────────────────────────────
# VIEW: KOREA MARKET
# ─────────────────────────────────────────────
elif view_mode == "🇰🇷 Korea Market":
    st.markdown('<p class="page-header">Korea Market Intelligence</p>',unsafe_allow_html=True)
    st.markdown("## 🇰🇷 Korean Presbyopia Eye Drop Market")
    st.markdown(f"<p style='color:#5a5f78;font-size:14px;margin-bottom:4px;'>As of June 2026, <b>no presbyopia eye drop has received MFDS approval in Korea</b>. The market is pre-commercial, with 3 NDAs under active review. Patient population estimate is derived (see footnote).</p>",unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)
    for col,num,lab,src in [
        (c1,"~16–17M","Estimated presbyopia patients","Derived: Korea pop. ≥40 ~30M × WHO prevalence ~55%"),
        (c2,"0","MFDS-approved presbyopia drops","As of June 2026"),
        (c3,"3","NDAs under active MFDS review","YUVEZZI, VIZZ, QLOSI"),
        (c4,"2026","Expected first MFDS approval year","Based on Sep 2025 NDA filing (Kwangdong)"),
    ]:
        col.markdown(f'<div class="mkt-card" style="text-align:center"><div class="info-card-title">{lab}</div><div class="mkt-num">{num}</div><div class="mkt-source">{src}</div></div>',unsafe_allow_html=True)

    st.caption(f"⚠️ Population estimate note: {MARKET_KOREA['est_basis']}")
    st.markdown("---")

    # Product table
    st.markdown("### Product-by-product breakdown")
    KOREA_DATA=[
        ("Company","광동제약 (Kwangdong)","알보젠코리아 (Alvogen Korea)","옵투스제약 (Optus Pharma)","대우제약 (Daewoo Pharma)"),
        ("Product","유베지 (YUVEZZI)","비즈 (VIZZ)","클로시 (QLOSI)","필로스타 (Pilostar)"),
        ("Active Ingredient","Carbachol 2.75% + Brimonidine 0.1%","Aceclidine 1.44%","Pilocarpine HCl 0.4%","Pilocarpine HCl 1.0%"),
        ("MFDS Status","🟡 NDA under review","🟡 NDA under review","🔴 NDA not yet filed","🟢 Approved (glaucoma) — indication expansion planned"),
        ("Developer","Tenpoint Therapeutics (UK)","LENZ Therapeutics (US)","Orasis Pharmaceuticals (US/Israel)","In-house"),
        ("License Chain","Tenpoint → Zhaoke (HK) → Kwangdong","LENZ → Lotus (Taiwan) → Alvogen Korea","Orasis → Optus Pharma (direct)","N/A — domestic"),
        ("Contract Signed","January 2024","May 2025","October 2025","N/A"),
        ("MFDS NDA Filed","September 2025 ✓ (first in Korea)","December 2025 ✓","Not announced as of 2026","Indication trial planned 2–3 years"),
        ("US FDA Approved","January 28, 2026","July 31, 2025","October 16, 2023","No — domestic only"),
        ("Expected Korea Launch","2026 (regulatory lead)","2026","2026 (pending NDA filing)","~2028–2029"),
        ("Duration","Up to 8 hours","Up to 10 hours","Up to 8 hours","~4–6 hours"),
        ("Preservative","None (PF)","None (PF)","None (PF)","None (PF)"),
        ("Key Differentiator","Only dual-agent FDC; lowest redness (2.8%); 12-month safety","Longest duration (10h); iris-selective; no brow ache; NCE","Lowest pilo conc (0.4%); PRN use; longest US track record","Only Korean-made; existing glaucoma network; off-label ongoing"),
    ]
    hd="".join(f"<th>{h}</th>" for h in ["Parameter","유베지 (YUVEZZI)","비즈 (VIZZ)","클로시 (QLOSI)","필로스타 (Pilostar)"])
    rows=""
    for row in KOREA_DATA:
        cells=f"<td><b>{row[0]}</b></td>"
        for i,v in enumerate(row[1:]):
            css_class=""
            if row[0]=="MFDS Status":
                css_class={"YUVEZZI":"s-review","VIZZ":"s-review","QLOSI":"s-pending","Pilostar":"s-launched"}.get(["YUVEZZI","VIZZ","QLOSI","Pilostar"][i],"")
            cells+=f"<td class='{css_class}'>{v}</td>"
        rows+=f"<tr>{cells}</tr>"
    st.markdown(f'<div style="overflow-x:auto"><table class="korea-tbl"><thead><tr>{hd}</tr></thead><tbody>{rows}</tbody></table></div>',unsafe_allow_html=True)

    st.markdown("---")
    c1,c2 = st.columns(2)
    with c1:
        st.markdown("### Korea Market Size (Myopia + Presbyopia combined)")
        for yr,val,note in [
            ("2023","$411.7M","Grand View Research"),
            ("2025","$631.6M","Expert Market Research"),
            ("2030 (est.)","$885.9M","Grand View Research — CAGR 11.6%"),
            ("2035 (est.)","$1,242.5M","Expert Market Research — CAGR 7.0%"),
        ]:
            pct = {"2023":33,"2025":51,"2030 (est.)":71,"2035 (est.)":100}[yr]
            st.markdown(f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">'
                        f'<div style="width:80px;font-size:12px;font-weight:600;color:#374151;">{yr}</div>'
                        f'<div style="flex:1"><div class="bar-track"><div class="bar-fill" style="width:{pct}%;background:#185FA5;"></div></div></div>'
                        f'<div style="width:90px;font-size:13px;font-weight:700;color:#111827;">{val}</div>'
                        f'<div style="font-size:10px;color:#9098b0;">{note}</div></div>',unsafe_allow_html=True)
        st.caption("⚠️ Combined myopia + presbyopia market. Presbyopia-only drug sub-segment is pre-commercial.")

    with c2:
        st.markdown("### Growth drivers")
        for d in MARKET_KOREA["drivers"]:
            st.markdown(f"- {d}")
        st.markdown("### Strategic dynamics")
        st.markdown("""
- **First-mover premium:** Kwangdong (YUVEZZI) filed first (Sep 2025) — holds regulatory lead
- **Duration battleground:** VIZZ 10h vs YUVEZZI & QLOSI 8h — matters for working-age Korean patients
- **NHI reimbursement unresolved:** If classified as lifestyle drug, OOP pricing limits market
- **Daewoo wildcard:** Only domestic manufacturer — cost & supply chain independence long-term
""")

    st.markdown("---")
    st.markdown("### Korea timeline")
    for date,dot_col,text in [
        ("Jan 2024","#0d6b35","Kwangdong signs Korea exclusive YUVEZZI license from Zhaoke Ophthalmology"),
        ("May 2025","#185FA5","Alvogen Korea signs VIZZ distribution license (LENZ → Lotus → Alvogen)"),
        ("Jul 2025","#185FA5","VIZZ receives US FDA approval — strengthens Korea dossier"),
        ("Sep 2025","#0d6b35","Kwangdong files MFDS NDA for YUVEZZI — first presbyopia NDA in Korea"),
        ("Oct 2025","#a05c00","Optus Pharma signs QLOSI license (₩24B contract)"),
        ("Nov 2025","#185FA5","Alvogen Korea files MFDS NDA for VIZZ"),
        ("Nov 2025","#374151","Daewoo launches Pilostar (glaucoma) + announces presbyopia indication expansion plan"),
        ("Jan 2026","#0d6b35","YUVEZZI receives US FDA approval — reinforces Kwangdong MFDS dossier"),
        ("2026 (est.)","#0d6b35","First MFDS presbyopia approval expected — market opens for first time"),
        ("2028–2029","#374151","Daewoo indication-expansion trial expected to complete — domestic product enters"),
    ]:
        st.markdown(f'<div class="tl-row"><div class="tl-date">{date}</div><div class="tl-dot" style="background:{dot_col}"></div><div class="tl-text">{text}</div></div>',unsafe_allow_html=True)

    st.markdown('<p class="source-note">Sources: Statistics Korea 2024; Worldometer 2026; WHO/Fricke et al. Ophthalmology 2018 (prevalence); Expert Market Research; Grand View Research; company press releases.</p>',unsafe_allow_html=True)

# ─────────────────────────────────────────────
# VIEW: GLOBAL MARKET
# ─────────────────────────────────────────────
elif view_mode == "🌍 Global Market":
    st.markdown('<p class="page-header">Global Presbyopia Market Intelligence</p>',unsafe_allow_html=True)
    st.markdown("## 🌍 Global Presbyopia Treatment Market")

    # Headline stats
    c1,c2,c3,c4 = st.columns(4)
    for col,(num,unit,lab,cagr,src) in zip([c1,c2,c3,c4],[
        ("1.8B","people","Global presbyopes (2024)","→ 2.1B by 2030","WHO / Fricke et al. Ophthalmology 2018"),
        ("$10.2B","USD","Total treatment market (2024)","CAGR 5.5% → $16.8B by 2033","Straits Research 2024"),
        ("$1.31B","USD","Eye drops segment (2024)","CAGR 9.2% → $2.86B by 2033","Dataintelo 2024"),
        ("12.8%","CAGR","Pharmacological drug fastest","Fastest-growing treatment sub-segment","Emergen Research 2025"),
    ]):
        col.markdown(f'<div class="mkt-card"><div class="info-card-title">{lab}</div>'
                     f'<div><span class="mkt-num">{num}</span><span class="mkt-unit">{unit}</span></div>'
                     f'<div class="mkt-cagr">{cagr}</div>'
                     f'<div class="mkt-source">{src}</div></div>',unsafe_allow_html=True)

    st.markdown("---")
    c1,c2 = st.columns([1.2,0.8])
    with c1:
        st.markdown("### Market size trajectory")
        for yr,val,bar,note in [
            ("2023","$8.14B",46,"DataM Intelligence"),
            ("2024","$10.17B",58,"Straits Research"),
            ("2025","$10.91B",62,"Straits Research (est.)"),
            ("2028","~$13B",74,"Interpolated"),
            ("2033","$16.77B",95,"Straits Research forecast"),
        ]:
            st.markdown(f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">'
                        f'<div style="width:50px;font-size:12px;font-weight:600;color:#374151;">{yr}</div>'
                        f'<div style="flex:1"><div class="bar-track"><div class="bar-fill" style="width:{bar}%;background:#534AB7;"></div></div></div>'
                        f'<div style="width:80px;font-size:13px;font-weight:700;color:#111827;">{val}</div>'
                        f'<div style="font-size:10px;color:#9098b0;">{note}</div></div>',unsafe_allow_html=True)

        st.markdown("### Eye drops segment (pharmacological only)")
        for yr,val,bar,note in [
            ("2024","$1.31B",46,"Dataintelo — first year of meaningful commercial market"),
            ("2026","~$1.56B",55,"Estimated — YUVEZZI, VIZZ newly launched"),
            ("2028","~$1.86B",65,"Estimated"),
            ("2033","$2.86B",100,"Dataintelo forecast"),
        ]:
            st.markdown(f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">'
                        f'<div style="width:50px;font-size:12px;font-weight:600;color:#374151;">{yr}</div>'
                        f'<div style="flex:1"><div class="bar-track"><div class="bar-fill" style="width:{bar}%;background:#0F6E56;"></div></div></div>'
                        f'<div style="width:80px;font-size:13px;font-weight:700;color:#111827;">{val}</div>'
                        f'<div style="font-size:10px;color:#9098b0;">{note}</div></div>',unsafe_allow_html=True)

    with c2:
        st.markdown("### Regional eye drop market share (2024)")
        for region,pct,val,cagr,col in [
            ("North America",42,"~$550M","8.5%","#534AB7"),
            ("Europe",29,"~$380M","~6.0%","#185FA5"),
            ("Asia Pacific",20,"~$262M","11.2% — fastest","#0F6E56"),
            ("Rest of World",9,"~$118M","—","#9098b0"),
        ]:
            st.markdown(f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">'
                        f'<div style="width:110px;font-size:12px;color:#374151;">{region}</div>'
                        f'<div style="flex:1"><div class="bar-track"><div class="bar-fill" style="width:{pct}%;background:{col};"></div></div></div>'
                        f'<div style="width:36px;font-size:12px;font-weight:700;color:#111827;">{pct}%</div>'
                        f'<div style="width:55px;font-size:11px;color:#6b7280;">{val}</div>'
                        f'<div style="font-size:10px;color:#0d6b35;font-weight:600;">{cagr}</div></div>',unsafe_allow_html=True)

        st.markdown("### CAGR by segment")
        for seg,cagr,col in [
            ("Eye drops (pharma)","9.2%","#0F6E56"),
            ("Pharmacological drugs","12.8%","#0d6b35"),
            ("Asia Pacific regional","11.2%","#185FA5"),
            ("Total treatment market","5.5%","#534AB7"),
            ("Korea (myopia+presbyopia)","11.6%","#A32D2D"),
        ]:
            pct = int(cagr.replace("%","").replace("~",""))
            st.markdown(f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:7px;">'
                        f'<div style="width:160px;font-size:12px;color:#374151;">{seg}</div>'
                        f'<div style="flex:1"><div class="bar-track"><div class="bar-fill" style="width:{min(pct*6,100)}%;background:{col};"></div></div></div>'
                        f'<div style="font-size:13px;font-weight:700;color:#111827;">{cagr}</div></div>',unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Key demand drivers & market dynamics")
    c1,c2,c3 = st.columns(3)
    c1.markdown(info_card("Demographics","Global population ≥40 years is growing rapidly. WHO: 1.8B presbyopes in 2024 → 2.1B by 2030. Asia Pacific has largest absolute numbers; Western markets have highest per-capita spending."),unsafe_allow_html=True)
    c2.markdown(info_card("Regulatory acceleration","4 FDA-approved drops in 5 years (2021–2026). Phentolamine (5th) PDUFA Oct 2026. Regulatory precedent now established — faster pathways for new entrants. Korea, EU, Japan approval races actively underway."),unsafe_allow_html=True)
    c3.markdown(info_card("Unmet needs driving growth","85%+ of presbyopes still rely on glasses. Pharmacological drops remain <1% of presbyopia management. The gap is the opportunity — but requires patient education and prescriber behaviour change. Reimbursement is the key remaining barrier."),unsafe_allow_html=True)

    st.markdown('<p class="source-note">Market data sources: Straits Research (2024 total market), Dataintelo (eye drops segment), Emergen Research (pharma segment CAGR), Dataintelo (regional breakdown), Grand View Research (Korea), Expert Market Research (Korea 2025–2035). WHO / Fricke TR et al. Ophthalmology. 2018;125:1492–1499 (global prevalence). All figures USD. Last updated June 2026.</p>',unsafe_allow_html=True)

# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown("---")
st.markdown('<p class="source-note">Presbyopia Eye Drop Competitive Intelligence Dashboard · All drug data from FDA DailyMed, accessdata.fda.gov prescribing information, PubMed, ClinicalTrials.gov. Excipients confirmed from official product labels. PK/PD studies from referenced protocols and publications. Patent data from Google Patents / USPTO. Market data from Straits Research, Dataintelo, EMR, Grand View Research. Korea demographic data from Statistics Korea 2024, UN World Population Prospects 2024, Worldometer 2026. Ryzumvi presbyopia indication investigational — sNDA PDUFA Oct 17, 2026. For internal research use only. Last updated June 2026.</p>',unsafe_allow_html=True)
