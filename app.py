import streamlit as st
import pandas as pd

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Presbyopia Eye Drop – Competitive Landscape",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
/* ── Font & base ── */
html, body, [class*="css"] { font-family: 'DM Sans', 'Inter', sans-serif; }

/* ── Sidebar ── */
[data-testid="stSidebar"] { background: #f7f8fa; border-right: 1px solid #e5e8ef; }
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 { color: #1a1d27 !important; }

/* ── Drug hero card ── */
.drug-hero {
    background: #ffffff;
    border: 1.5px solid #e5e8ef;
    border-radius: 14px;
    padding: 24px 28px;
    margin-bottom: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.drug-name { font-size: 28px; font-weight: 700; margin: 0 0 4px 0; }
.drug-generic { font-size: 15px; color: #5a5f78; margin: 0 0 16px 0; }

/* ── Badges ── */
.badge {
    display: inline-block;
    font-size: 11px;
    font-weight: 600;
    padding: 4px 12px;
    border-radius: 20px;
    margin-right: 6px;
    margin-bottom: 4px;
    letter-spacing: 0.03em;
}
.badge-approved { background: #e6f9f0; color: #0d6b35; border: 1px solid #b3e6cc; }
.badge-pending  { background: #fff8e6; color: #8a5c00; border: 1px solid #ffd980; }
.badge-rx       { background: #e8f0fb; color: #1a4d9e; border: 1px solid #b3c8f0; }

/* ── Section cards ── */
.info-card {
    background: #f7f8fa;
    border: 1px solid #e5e8ef;
    border-radius: 10px;
    padding: 16px 18px;
    margin-bottom: 12px;
    height: 100%;
}
.info-card-title {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    color: #9098b0;
    margin-bottom: 8px;
}
.info-card-value { font-size: 14px; color: #2c3150; line-height: 1.65; }
.info-card-value b { color: #111827; font-weight: 600; }
.info-card-value .highlight { color: #0d6b35; font-weight: 600; }
.info-card-value .warn { color: #a05c00; font-weight: 600; }
.info-card-value .danger { color: #b91c1c; font-weight: 600; }

/* ── Excipient table ── */
.excip-table { width: 100%; border-collapse: collapse; font-size: 13px; }
.excip-table th {
    background: #f0f2f7;
    color: #6b7280;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    padding: 9px 12px;
    text-align: left;
    border-bottom: 1.5px solid #d1d5de;
}
.excip-table td {
    padding: 9px 12px;
    color: #374151;
    border-bottom: 1px solid #edf0f5;
    vertical-align: top;
    line-height: 1.6;
}
.excip-table tr:nth-child(even) td { background: #fafbfc; }
.excip-table tr:last-child td { border-bottom: none; }
.excip-table td b { color: #111827; }
.excip-role {
    display: inline-block;
    font-size: 10px;
    padding: 2px 8px;
    border-radius: 10px;
    background: #e8f0fb;
    color: #1a4d9e;
    font-weight: 600;
}

/* ── Trial result box ── */
.trial-box {
    background: #f0f5ff;
    border: 1px solid #c7d9f5;
    border-left: 4px solid #3b72d9;
    border-radius: 8px;
    padding: 14px 16px;
    margin-bottom: 10px;
}
.trial-box-title { font-size: 13px; font-weight: 700; color: #1a3d8a; margin-bottom: 6px; }
.trial-box-body  { font-size: 13px; color: #374151; line-height: 1.65; }
.trial-box-stat  { font-size: 22px; font-weight: 700; color: #0d6b35; }
.trial-box-label { font-size: 11px; color: #6b7280; }

/* ── Korea landscape table ── */
.korea-tbl { width: 100%; border-collapse: collapse; font-size: 13px; }
.korea-tbl th {
    background: #f0f2f7;
    color: #374151;
    font-size: 11px;
    font-weight: 700;
    padding: 10px 14px;
    text-align: left;
    border: 1px solid #d1d5de;
}
.korea-tbl td {
    padding: 9px 14px;
    color: #374151;
    border: 1px solid #e5e8ef;
    vertical-align: top;
    line-height: 1.55;
    font-size: 13px;
}
.korea-tbl tr:nth-child(even) td { background: #fafbfc; }
.korea-tbl td b { color: #111827; font-weight: 600; }
.korea-status-review  { color: #a05c00; font-weight: 600; }
.korea-status-pending { color: #b91c1c; font-weight: 600; }
.korea-status-launched { color: #0d6b35; font-weight: 600; }
.korea-section-header {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    color: #9098b0;
    margin: 20px 0 8px 0;
}

/* ── Misc ── */
.divider { border-top: 1.5px solid #e5e8ef; margin: 20px 0; }
.source-note { font-size: 11px; color: #9098b0; font-style: italic; }
.page-header { font-size: 12px; color: #9098b0; letter-spacing: 0.06em; text-transform: uppercase; margin-bottom: 6px; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# DATA — all sourced from FDA prescribing info,
# DailyMed, PubMed, and prior research sessions
# ─────────────────────────────────────────────
DRUGS = {
    "VUITY": {
        "brand": "VUITY®",
        "generic": "Pilocarpine hydrochloride ophthalmic solution 1.25%",
        "company": "Allergan / AbbVie",
        "approval_status": "FDA Approved",
        "approval_date": "October 29, 2021",
        "approval_note": "First-ever FDA-approved presbyopia eye drop",
        "nda_number": "NDA 214028",
        "application_type": "NDA — 505(b)(1)",
        "rx_type": "Prescription (Rx only)",
        "active_ingredient": "Pilocarpine hydrochloride",
        "concentration": "1.25% (12.5 mg/mL)",
        "free_base_equivalent": "1.06% (10.6 mg/mL) pilocarpine free-base",
        "iupac": "(3S,4R)-3-ethyl-4-[(1-methyl-1H-imidazol-5-yl)methyl]oxolan-2-one hydrochloride",
        "molecular_formula": "C₁₁H₁₆N₂O₂ · HCl",
        "molecular_weight": "244.72 g/mol",
        "drug_class": "Cholinergic muscarinic M3 receptor agonist",
        "moa": (
            "Pilocarpine is a partial muscarinic M3 receptor agonist. "
            "It activates M3 receptors on the iris sphincter muscle → pupil constriction (miosis) → "
            "pinhole depth-of-focus effect. Simultaneously activates M3 on the ciliary muscle → "
            "zonule relaxation → lens thickening → accommodation enhancement. "
            "Effect is dose-dependent and self-limiting due to partial agonism."
        ),
        "technology": "Small-molecule cholinergic miotic; pH-buffered low-viscosity aqueous solution; BAK-preserved multi-dose bottle",
        "dosing": "1 drop in each eye once daily. A second dose may be administered 3–6 hours after the first. If using multiple ophthalmic products, separate by ≥5 minutes.",
        "dosage_form": "Ophthalmic solution, 2.5 mL multi-dose bottle",
        "onset": "As early as 15 minutes",
        "duration": "Up to 6 hours (Day 30 data)",
        "storage": "Room temperature 15–25°C (59–77°F)",
        "preservative": "Benzalkonium chloride (BAK) 0.0075%",
        "ph_range": "3.5–5.5",
        "excipients": [
            {"name": "Benzalkonium chloride (BAK) 0.0075%", "role": "Preservative", "function": "Antimicrobial preservative for multi-dose bottle; disrupts microbial cell membranes. Lowest BAK concentration among BAK-preserved ophthalmic products; still carries risk of long-term corneal epithelial toxicity with chronic daily use."},
            {"name": "Boric acid", "role": "Buffer", "function": "Weak acid component of the borate buffer system. Maintains pH in the 3.5–5.5 range required for pilocarpine chemical stability (prevents hydrolysis to inactive isopilocarpine). Also has mild antimicrobial properties."},
            {"name": "Sodium citrate dihydrate", "role": "Buffer / Chelating", "function": "Mild buffer and chelating agent. Sequester calcium and other divalent metal ions that could catalyze pilocarpine oxidative degradation. Also softens the stinging sensation of acidic ophthalmic solutions."},
            {"name": "Sodium chloride", "role": "Tonicity agent", "function": "Adjusts osmolality to near-physiological (~280–320 mOsm/kg). Minimizes ocular discomfort on instillation. Critical for corneal epithelial integrity."},
            {"name": "Purified water", "role": "Solvent / Vehicle", "function": "Aqueous vehicle for all ingredients. Must meet USP Purified Water standards (endotoxin-free)."},
            {"name": "Hydrochloric acid / Sodium hydroxide", "role": "pH adjuster", "function": "Used as needed to titrate final pH to 3.5–5.5. Pilocarpine is most stable and least prone to hydrolysis at acidic pH; alkaline conditions accelerate conversion to inactive isopilocarpine."},
        ],
        "key_trials": [
            {"name": "GEMINI 1 (Phase 3)", "citation": "Waring GO et al. JAMA Ophthalmol. 2022;140:363–371", "design": "Randomized, double-masked, vehicle-controlled, 30 days, n=354", "primary_endpoint": "≥3-line mesopic DCNVA gain with <5-letter BCDVA loss", "result": "Primary endpoint met. ~26% achieved ≥3-line gain vs vehicle. Onset Day 1; effect improved through Day 14 and maintained Day 30."},
            {"name": "GEMINI 2 (Phase 3)", "citation": "Supported NDA submission", "design": "Identical to GEMINI 1, confirmatory study", "primary_endpoint": "Same composite near/distance endpoint", "result": "Confirmed GEMINI 1 results. Supported FDA approval."},
        ],
        "efficacy_summary": "~26% ≥3-line mesopic DCNVA improvement vs ~9% vehicle. Onset Day 1, peak effect ~1 hour, duration up to 6 hours. Distance vision preserved (no ≥5-letter BCDVA loss).",
        "side_effects": [
            ("Headache / brow ache", ">5%", "Caused by rapid ciliary muscle contraction (spasm). Most common reason for discontinuation."),
            ("Conjunctival hyperemia", ">5%", "Cholinergic-mediated vasodilation of conjunctival vessels."),
            ("Blurred vision", "Common", "Transient, particularly shortly after instillation."),
            ("Dim / dark vision", "Common", "Miosis reduces light entry; problematic in low-light conditions."),
            ("Myopic shift", "Up to −1.75 D", "Over-accommodation from ciliary contraction; causes temporary distance blurring."),
            ("Retinal detachment / tear", "Rare", "Rare but serious. Ciliary contraction may exert anterior traction. Higher risk in myopes. Retinal exam recommended before initiating therapy."),
            ("Accommodative spasm", "Uncommon", "Excessive ciliary contraction causing near-blur paradox."),
        ],
        "contraindications": "Known hypersensitivity to pilocarpine or excipients. Caution: iritis, narrow anterior chamber angle, history of retinal disease.",
    },

    "QLOSI": {
        "brand": "QLOSI™",
        "generic": "Pilocarpine hydrochloride ophthalmic solution 0.4%",
        "company": "Orasis Pharmaceuticals / Optus Pharma (Korea licensee)",
        "approval_status": "FDA Approved",
        "approval_date": "October 16, 2023",
        "approval_note": "Second FDA-approved presbyopia drop; lowest-concentration pilocarpine approved; preservative-free unit-dose",
        "nda_number": "NDA 215962",
        "application_type": "NDA — 505(b)(1)",
        "rx_type": "Prescription (Rx only)",
        "active_ingredient": "Pilocarpine hydrochloride",
        "concentration": "0.4% (4 mg/mL)",
        "free_base_equivalent": "~0.34% pilocarpine free-base",
        "iupac": "(3S,4R)-3-ethyl-4-[(1-methyl-1H-imidazol-5-yl)methyl]oxolan-2-one hydrochloride",
        "molecular_formula": "C₁₁H₁₆N₂O₂ · HCl",
        "molecular_weight": "244.72 g/mol",
        "drug_class": "Cholinergic muscarinic M3 receptor agonist",
        "moa": (
            "Same M3 muscarinic receptor agonism as Vuity but at significantly lower concentration (0.4% vs 1.25%). "
            "Lower concentration produces effective miosis for depth-of-focus improvement while reducing ciliary muscle "
            "over-stimulation — the primary cause of brow ache and myopic shift. The lower dose is optimized to sit below "
            "the ciliary spasm threshold while remaining above the miosis efficacy threshold. "
            "Polysorbate 80 in the formulation enhances corneal penetration of pilocarpine at this lower concentration."
        ),
        "technology": "Low-dose cholinergic miotic; preservative-free single-use unit-dose vial; polysorbate 80 solubilizer system for enhanced corneal penetration",
        "dosing": "1 drop in each eye once daily, or as needed (PRN use possible given on-demand design). Unit-dose vial — single use only, discard after use.",
        "dosage_form": "Ophthalmic solution, 0.3 mL single-use unit-dose vial",
        "onset": "Within 30 minutes",
        "duration": "Up to 8 hours",
        "storage": "Room temperature 15–30°C (59–86°F)",
        "preservative": "None (preservative-free)",
        "ph_range": "~5.0–5.5",
        "excipients": [
            {"name": "Polysorbate 80", "role": "Solubilizer / Penetration enhancer", "function": "Non-ionic surfactant. At low pilocarpine concentration (0.4%), polysorbate 80 enhances corneal penetration by temporarily loosening tight junctions in the corneal epithelium and improving drug partitioning into lipid-containing corneal tissues. Critical for maintaining efficacy at the reduced API concentration."},
            {"name": "Boric acid", "role": "Buffer", "function": "Maintains acidic pH (5.0–5.5) to stabilize pilocarpine against hydrolysis to inactive isopilocarpine. Also provides mild antimicrobial activity."},
            {"name": "Mannitol", "role": "Tonicity agent / Stabilizer", "function": "Provides isotonicity (280–320 mOsm/kg) without chloride ions. Preferred over NaCl because chloride can catalyze pilocarpine oxidative degradation. Mannitol also contributes to chemical stability of the formulation and is well-tolerated at the ocular surface."},
            {"name": "Sodium chloride", "role": "Tonicity co-agent", "function": "Secondary tonicity adjustment in combination with mannitol. Fine-tunes osmolality to physiological range."},
            {"name": "Hydrochloric acid / Sodium hydroxide", "role": "pH adjuster", "function": "Titrates final solution to pH 5.0–5.5. Critical for both pilocarpine chemical stability and patient comfort on instillation."},
            {"name": "Water for injection", "role": "Solvent / Vehicle", "function": "USP Water for Injection — highest purity grade aqueous vehicle. Required for sterile unit-dose ophthalmic products to meet endotoxin and particulate matter specifications."},
        ],
        "key_trials": [
            {"name": "NEAR Phase 3 Trials (NEAR-1 & NEAR-2)", "citation": "Holland E et al. Clin Ther. 2024;46:104–113", "design": "Two multicenter, double-masked, vehicle-controlled Phase 3 trials. Oct 2020–Feb 2022. 35 US sites.", "primary_endpoint": "≥3-line mesopic DCNVA improvement with <5-letter BCDVA loss", "result": "Both trials met primary and key secondary endpoints. Significant improvement in near VA demonstrated. Less brow ache and fewer visual disturbances vs Vuity historical data due to lower concentration."},
        ],
        "efficacy_summary": "Significant DCNVA improvement vs vehicle in both NEAR-1 and NEAR-2 pivotal trials. Duration up to 8 hours. Lower side effect burden vs 1.25% formulations due to reduced concentration.",
        "side_effects": [
            ("Headache / brow ache", "Lower than Vuity", "Reduced ciliary spasm at 0.4% concentration vs 1.25%."),
            ("Dim vision", "Common", "Miosis reduces light entry; transient."),
            ("Eye irritation", "Mild", "Instillation discomfort; less than BAK-preserved products."),
            ("Myopic shift", "Reduced vs Vuity", "Less ciliary stimulation → less accommodation-driven myopic shift."),
            ("Retinal detachment", "Rare", "Class effect warning retained for all miotics; lower risk theoretically at reduced concentration."),
        ],
        "contraindications": "Known hypersensitivity to pilocarpine or excipients. Caution: iritis, narrow angle, retinal disease history.",
    },

    "VIZZ": {
        "brand": "VIZZ™",
        "generic": "Aceclidine ophthalmic solution 1.44%",
        "company": "LENZ Therapeutics (Nasdaq: LENZ)",
        "approval_status": "FDA Approved",
        "approval_date": "July 31, 2025",
        "approval_note": "First and only FDA-approved aceclidine-based eye drop; first once-daily drop with up to 10-hour efficacy; new chemical entity in US",
        "nda_number": "NDA 218585",
        "application_type": "NDA — 505(b)(1) (New Chemical Entity)",
        "rx_type": "Prescription (Rx only)",
        "active_ingredient": "Aceclidine hydrochloride (equivalent to 1.44% aceclidine)",
        "concentration": "1.75% aceclidine HCl (17.82 mg/mL) ≡ 1.44% aceclidine free base",
        "free_base_equivalent": "1.44% aceclidine (14.4 mg/mL)",
        "iupac": "3-Acetoxyquinuclidine hydrochloride (also: 3-Quinuclidinyl Acetate Hydrochloride)",
        "molecular_formula": "C₉H₁₅NO₂ · HCl",
        "molecular_weight": "205.68 g/mol",
        "drug_class": "Iris-selective cholinergic muscarinic receptor agonist (pupil-selective miotic)",
        "moa": (
            "Aceclidine is a muscarinic agonist with preferential selectivity for M3 receptors on the iris sphincter "
            "over those on the ciliary muscle. This iris selectivity means aceclidine produces strong, sustained pupil "
            "constriction (miosis < 2 mm at peak) with markedly less ciliary muscle stimulation than pilocarpine or carbachol. "
            "Consequences: (1) deeper pinhole effect → superior depth of focus, (2) minimal myopic shift (no ciliary lens thickening), "
            "(3) significantly less brow ache (no ciliary spasm). Duration advantage over pilocarpine comes from the combination "
            "of tight iris M3 binding and the hypromellose-based viscous formulation extending ocular surface residence time."
        ),
        "technology": "Iris-selective muscarinic M3 agonist (new chemical entity); viscous aqueous solution with hypromellose for extended contact time; preservative-free single-use vials; refrigerated storage",
        "dosing": "1 drop in each eye once daily. Begin to notice improvement within 30 minutes. Single-use vial — discard after use. Do not touch tip to eye.",
        "dosage_form": "Ophthalmic solution, unit-dose single-use vials (0.3 mL); refrigerated",
        "onset": "Within 30 minutes",
        "duration": "Up to 10 hours (longest of all approved presbyopia drops)",
        "storage": "Refrigerated 2–8°C (36–46°F). Do not freeze.",
        "preservative": "None (preservative-free)",
        "ph_range": "4.5–5.5",
        "excipients": [
            {"name": "Polysorbate 80", "role": "Solubilizer / Wetting agent", "function": "Non-ionic surfactant that solubilizes aceclidine HCl and enhances corneal epithelial penetration. Also serves as a wetting agent improving drug-ocular surface contact. Essential for maintaining solution clarity given aceclidine's physical-chemical properties."},
            {"name": "Mannitol", "role": "Tonicity agent / Stabilizer", "function": "Primary tonicity agent for isotonic adjustment (~280–320 mOsm/kg). Preferred over NaCl due to lower risk of metal ion-catalyzed degradation. Mannitol is also a mild antioxidant that contributes to aceclidine chemical stability during storage."},
            {"name": "Hypromellose (HPMC)", "role": "Viscosity agent / Ocular surface bioadhesive", "function": "Cellulosic polymer that increases solution viscosity (~15–25 cP). Extends ocular surface residence time by slowing drainage via the nasolacrimal duct — a key contributor to VIZZ's 10-hour duration advantage vs Vuity. Also lubricates the ocular surface and reduces instillation discomfort. This is a pharmacokinetically important excipient, not merely a comfort agent."},
            {"name": "Edetate disodium dihydrate (EDTA·2Na)", "role": "Chelating agent / Preservative aid", "function": "Sequester divalent metal ions (Ca²⁺, Mg²⁺, Fe²⁺) that could catalyze aceclidine oxidative degradation. Also enhances corneal epithelial permeability by chelating Ca²⁺ from tight junction complexes (Cadherin-Ca²⁺ disruption) → increased drug penetration. Provides additional antimicrobial protection in combination with the formulation design."},
            {"name": "Sodium citrate dihydrate", "role": "Buffer", "function": "Provides the citrate buffer system maintaining pH 4.5–5.5. Citrate buffer is well-tolerated at the ocular surface (lower stinging than phosphate at equivalent molarity). Also a mild chelating agent providing secondary metal ion sequestration."},
            {"name": "Hydrochloric acid / Sodium hydroxide", "role": "pH adjuster", "function": "Titrates final solution to target pH 4.5–5.5. Aceclidine (pKa ~9.5) is fully protonated and most chemically stable in this acidic range. Refrigerated storage at 2–8°C further slows hydrolytic degradation of the ester bond in the aceclidine molecule."},
            {"name": "Water for injection", "role": "Solvent / Vehicle", "function": "USP Water for Injection. Highest purity aqueous vehicle required for sterile unit-dose products. Meets USP bacterial endotoxin and particulate matter limits."},
        ],
        "key_trials": [
            {"name": "CLARITY 1 (Phase 3)", "citation": "NCT05656027 · n=466, 42 days, once daily", "design": "Randomized, double-masked, vehicle-controlled, multicenter, 42 days", "primary_endpoint": "≥3-line mesopic DCNVA gain + <5-letter BCDVA loss", "result": "Primary and all secondary endpoints met (p<0.0001). 71% gained ≥3 lines at 30 min & 3h. 40% maintained ≥3-line improvement at 10 hours."},
            {"name": "CLARITY 2 (Phase 3)", "citation": "NCT06045299 · n=466, 42 days, once daily", "design": "Confirmatory randomized, double-masked, vehicle-controlled", "primary_endpoint": "Same composite endpoint", "result": "All primary and secondary endpoints met. Confirmed CLARITY 1 results. 70–75% pooled ≥3-line improvement vs ~10–15% vehicle. No serious treatment-related AEs over 30,000 treatment days."},
            {"name": "CLARITY 3 (Phase 3 safety extension)", "citation": "NCT05753189 · n=217, 6 months", "design": "Open-label 6-month safety extension", "primary_endpoint": "Long-term safety and tolerability", "result": "Well-tolerated at 6 months. No serious treatment-related AEs. No tachyphylaxis observed. Sustained efficacy confirmed."},
        ],
        "efficacy_summary": "70–75% of VIZZ-treated eyes achieved ≥3-line DCNVA improvement (vs ~10–15% vehicle). Onset within 30 minutes. Duration up to 10 hours — longest of all approved presbyopia drops. No myopic shift. Superior tolerability profile vs pilocarpine.",
        "side_effects": [
            ("Instillation site irritation", "~20%", "Most common AE. Transient, mild, self-resolving. Related to acidic pH."),
            ("Dim vision", "~16%", "Miosis reduces light entry; expected class effect."),
            ("Headache", "~13%", "Significantly lower rate than pilocarpine; minimal ciliary stimulation."),
            ("Eye redness", "Low", "Minimal hyperemia compared to pilocarpine formulations."),
            ("Myopic shift", "Minimal to none", "Iris-selective mechanism avoids significant ciliary stimulation — key differentiator from pilocarpine."),
        ],
        "contraindications": "Known hypersensitivity to aceclidine or excipients. Caution: iritis, narrow anterior chamber angle.",
    },

    "YUVEZZI": {
        "brand": "YUVEZZI™",
        "generic": "Carbachol 2.75% / Brimonidine tartrate 0.1% ophthalmic solution",
        "company": "Tenpoint Therapeutics (formerly Visus Therapeutics) / Kwangdong Pharma (Korea)",
        "approval_status": "FDA Approved",
        "approval_date": "January 28, 2026",
        "approval_note": "First and only FDA-approved dual-agent fixed-dose combination for presbyopia; first carbachol-based presbyopia drop",
        "nda_number": "NDA 218124",
        "application_type": "NDA — 505(b)(2) (Fixed-dose combination of two approved APIs)",
        "rx_type": "Prescription (Rx only)",
        "active_ingredient": "Carbachol 2.75% + Brimonidine tartrate 0.1%",
        "concentration": "Carbachol: 27.5 mg/mL (2.75%) | Brimonidine tartrate: 1.0 mg/mL (0.1%)",
        "free_base_equivalent": "N/A (salts as marketed)",
        "iupac": (
            "Carbachol: 2-[(Aminocarbonyl)oxy]-N,N,N-trimethylethanaminium chloride\n"
            "Brimonidine tartrate: 5-Bromo-N-(4,5-dihydro-1H-imidazol-2-yl)quinoxalin-6-amine L-tartrate"
        ),
        "molecular_formula": "Carbachol: C₆H₁₅ClN₂O₂ (MW 182.65) | Brimonidine tartrate: C₁₁H₁₀BrN₅ · C₄H₆O₆ (MW 442.24)",
        "molecular_weight": "Carbachol: 182.65 g/mol | Brimonidine tartrate: 442.24 g/mol",
        "drug_class": "Fixed-dose combination: muscarinic+nicotinic agonist (carbachol) + α2-adrenergic agonist (brimonidine)",
        "moa": (
            "Dual-pathway mechanism targeting both arms of pupil control:\n\n"
            "CARBACHOL (full agonist at muscarinic M3 + nicotinic receptors): Directly contracts iris sphincter → active pupil "
            "constriction. Simultaneously contracts ciliary muscle → lens thickening → accommodation. As a full agonist "
            "(vs pilocarpine's partial agonism), carbachol achieves stronger, longer-lasting miosis but with greater spasm risk.\n\n"
            "BRIMONIDINE (α2-adrenergic agonist, presynaptic): Binds α2 receptors at iris dilator nerve terminals → inhibits "
            "norepinephrine release → silences iris dilator muscle. Removes the counter-dilation force against carbachol. "
            "Also: (1) relaxes tonic ciliary contraction → reduces carbachol-induced brow ache, (2) constricts conjunctival "
            "vessels → reduces redness (hyperemia rate 2.8% vs 10.7% carbachol alone), (3) increases cholinergic drug "
            "bioavailability in aqueous humor by ~50% (rabbit pharmacokinetic data).\n\n"
            "Net result: stronger and more sustained miosis than either drug alone, with lower side effects than carbachol monotherapy."
        ),
        "technology": "Fixed-dose dual-pathway combination; preservative-free single-use vials; synergistic PD design targeting both parasympathetic (M3) and sympathetic (α2) iris pathways simultaneously",
        "dosing": "1 drop in each eye once daily. Single-use vial — discard after opening.",
        "dosage_form": "Ophthalmic solution, preservative-free single-use unit-dose vials (0.3 mL)",
        "onset": "Within 30–60 minutes",
        "duration": "Up to 8 hours",
        "storage": "Room temperature 20–25°C (68–77°F). Protect from light.",
        "preservative": "None (preservative-free)",
        "ph_range": "~6.5–7.5 (carbachol/brimonidine stability range)",
        "excipients": [
            {"name": "Sodium chloride", "role": "Tonicity agent", "function": "Adjusts osmolality to near-physiological levels (~280–320 mOsm/kg). Both carbachol and brimonidine are stable in isotonic NaCl-based solutions. Critical for minimizing instillation discomfort."},
            {"name": "Sodium phosphate monobasic", "role": "Buffer", "function": "Acid component of the phosphate buffer system. Maintains pH in the 6.5–7.5 range where both carbachol and brimonidine tartrate are chemically stable. Phosphate buffers are well-tolerated in ophthalmic formulations and provide reliable pH control over the shelf-life of the product."},
            {"name": "Hydrochloric acid / Sodium hydroxide", "role": "pH adjuster", "function": "Fine-tunes pH to the target range during manufacturing. Carbachol is stable at pH 5–8 (broader window than pilocarpine); brimonidine tartrate is stable at pH 6–8. The final pH is chosen to simultaneously satisfy both API stability requirements."},
            {"name": "Water for injection", "role": "Solvent / Vehicle", "function": "USP Water for Injection. Highest purity aqueous vehicle. Required for sterile preservative-free unit-dose ophthalmic products. Free of bacterial endotoxins and particulate matter."},
        ],
        "key_trials": [
            {"name": "BRIO-I (Phase 3 Combination Superiority)", "citation": "NCT05270863 · Tenpoint Therapeutics", "design": "3-arm randomized, double-masked, crossover: YUVEZZI vs carbachol alone vs brimonidine alone", "primary_endpoint": "Combination superiority over each active monotherapy (FDA requirement for FDC)", "result": "YUVEZZI demonstrated superior near VA improvement vs both carbachol alone and brimonidine alone. Met FDA's combination superiority requirement for fixed-dose combination NDA approval."},
            {"name": "BRIO-II (Phase 3 Vehicle-Controlled, 12-month Safety)", "citation": "NCT05270876 · n=estimated 400+, 12 months", "design": "Vehicle-controlled, 12-month randomized study — longest presbyopia safety study to date (72,000+ treatment days)", "primary_endpoint": "≥3-line BUNVA improvement + distance VA preservation; 12-month safety", "result": "All primary near vision endpoints met and sustained over 8 hours with once-daily dosing. Ocular hyperemia: 2.8% (YUVEZZI) vs 10.7% (carbachol alone). No serious treatment-related AEs over 72,000+ treatment days. No loss of ≥1 line distance VA."},
        ],
        "efficacy_summary": "Superior to carbachol and brimonidine monotherapy. ≥3-line BUNVA improvement sustained over 8 hours. Lowest hyperemia rate of any approved presbyopia drop (2.8%). 12 months / 72,000+ treatment-days safety data — most extensive safety dataset in the category.",
        "side_effects": [
            ("Ocular hyperemia (redness)", "2.8%", "Lowest of all approved drops; brimonidine's vasoconstriction offsets carbachol's hyperemia."),
            ("Brow ache / headache", "Reduced vs carbachol alone", "Brimonidine's ciliary relaxation effect dampens carbachol-induced ciliary spasm."),
            ("Dim vision", "Common (class effect)", "Miosis reduces light entry; expected."),
            ("Myopic shift", "Possible", "Carbachol-driven ciliary contraction can cause some myopic shift; reduced by brimonidine's tonic ciliary relaxation."),
            ("Dry mouth (brimonidine component)", "Systemic — uncommon", "α2-adrenergic effect on salivary glands. Low risk at 0.1% concentration."),
            ("Drowsiness / fatigue (brimonidine)", "Rare", "CNS α2 penetration. More relevant at glaucoma concentrations (0.15–0.2%); low risk at 0.1%."),
            ("Contraindicated in young children (brimonidine)", "Absolute", "Brimonidine crosses immature blood-brain barrier → CNS depression risk. Do not use in young children."),
        ],
        "contraindications": "Known hypersensitivity to carbachol, brimonidine, or any excipient. CONTRAINDICATED in young children (brimonidine CNS depression risk). Caution: antihypertensive medications (brimonidine systemic hypotension risk), MAO inhibitors.",
    },

    "RYZUMVI": {
        "brand": "Ryzumvi®",
        "generic": "Phentolamine mesylate ophthalmic solution 0.75%",
        "company": "Viatris / Opus Genetics (formerly Ocuphire Pharma)",
        "approval_status": "FDA Approved (mydriasis reversal) | Presbyopia: sNDA under review",
        "approval_date": "September 25, 2023 (mydriasis reversal) | Presbyopia PDUFA: October 17, 2026",
        "approval_note": "FDA-approved for reversal of pharmacologically induced mydriasis. Supplemental NDA (sNDA) for presbyopia accepted Feb 25, 2026 — PDUFA Oct 17, 2026. Same formulation; indication expansion only.",
        "nda_number": "NDA 217064",
        "application_type": "NDA — 505(b)(2) (original); sNDA (supplemental — presbyopia)",
        "rx_type": "Prescription (Rx only)",
        "active_ingredient": "Phentolamine mesylate",
        "concentration": "0.75% (7.5 mg/mL phentolamine free-base equivalent; 10 mg/mL phentolamine mesylate)",
        "free_base_equivalent": "0.75% phentolamine free-base",
        "iupac": "3-[[(4,5-Dihydro-1H-imidazol-2-yl)methyl](4-methylphenyl)amino]phenol methanesulfonate",
        "molecular_formula": "C₁₇H₁₉N₃O · CH₃SO₃H (mesylate salt) | C₁₇H₁₉N₃O (free base)",
        "molecular_weight": "377.46 g/mol (mesylate) | 281.36 g/mol (free base)",
        "drug_class": "Non-selective α1/α2-adrenergic antagonist (alpha-blocker)",
        "moa": (
            "Phentolamine is a non-selective alpha-adrenergic antagonist with a fundamentally different mechanism from all "
            "other presbyopia drops:\n\n"
            "PRIMARY (α1 postsynaptic blockade at iris dilator): Competitively blocks α1 receptors on the iris dilator muscle "
            "→ dilator cannot contract in response to norepinephrine → dilator force is removed → iris sphincter acts unopposed "
            "→ passive pupil constriction (miosis). NO direct sphincter activation — no ciliary muscle involvement.\n\n"
            "SECONDARY (α2 blockade at iris sphincter): Also blocks α2 receptors on the iris sphincter (which normally inhibit "
            "sphincter tone) → releases the inhibitory brake → adds indirect sphincter activation component.\n\n"
            "CRITICAL CONSEQUENCE — NO CILIARY MUSCLE ACTIVITY: Since phentolamine does not activate M3 receptors on the "
            "ciliary body, there is (1) no accommodation enhancement (depth of focus only), (2) no brow ache, (3) no myopic "
            "shift, (4) no anterior lens migration → no retinal traction risk. The miotic effect lasts up to 20 hours from "
            "a single evening dose, through into the following day."
        ),
        "technology": "Alpha-adrenergic antagonist (sympatholytic); ultra-minimalist PF formulation with nitrogen overlay to prevent oxidation; evening dosing for next-day near vision; refrigerated storage",
        "dosing": "1 drop in each eye once daily in the evening. Single-use vial — discard immediately after use. Nasolacrimal duct occlusion recommended to reduce systemic absorption.",
        "dosage_form": "Ophthalmic solution, 0.31 mL single-use unit-dose vial (5 vials per foil pouch; 6 pouches per carton)",
        "onset": "Within 60–90 minutes of evening instillation",
        "duration": "Up to 20 hours — longest duration of any presbyopia drop; effect present on waking next morning",
        "storage": "Refrigerated 2–8°C (36–46°F). Do not freeze. After opening foil pouch: store up to 25°C for up to 14 days.",
        "preservative": "None (preservative-free)",
        "ph_range": "4.5–5.5",
        "excipients": [
            {"name": "Mannitol", "role": "Tonicity agent / Antioxidant / Stabilizer", "function": "Primary tonicity agent providing isotonicity (~280–320 mOsm/kg). Preferred over NaCl specifically because chloride ions can catalyze phentolamine oxidation — a critical consideration given phentolamine's susceptibility to air and metal-catalyzed oxidative degradation. Mannitol also acts as a mild hydroxyl radical scavenger (antioxidant function), providing a secondary layer of chemical stability."},
            {"name": "Sodium acetate trihydrate", "role": "Buffer", "function": "Acetate buffer system maintains pH 4.5–5.5 where phentolamine is maximally chemically stable and least prone to hydrolytic and oxidative degradation. Acetate buffer is chosen over phosphate or citrate because it provides a gentle, physiologically compatible acidic environment with minimal potential for metal ion interactions. The low-molarity acetate system (typically 5–25 mM) minimizes instillation sting while providing adequate pH control."},
            {"name": "Hydrochloric acid / Sodium hydroxide", "role": "pH adjuster", "function": "Titrates the final solution to the target pH range 4.5–5.5 during manufacturing. Ensures both the acetate buffer range and the phentolamine chemical stability window are satisfied simultaneously."},
            {"name": "Water for injection", "role": "Solvent / Vehicle", "function": "USP Water for Injection. Highest purity aqueous vehicle. Metal-ion free (important given phentolamine's metal-catalyzed oxidation sensitivity). Endotoxin and particulate matter compliant for sterile ophthalmic use."},
            {"name": "Nitrogen (headspace)", "role": "Antioxidant / Inert atmosphere", "function": "The solution is overlaid with nitrogen gas in the unit-dose vial before sealing. This eliminates dissolved oxygen and prevents air oxidation of phentolamine — a unique feature not present in any other approved ophthalmic drug. Oxygen exposure at any point in manufacturing, filling, or storage would accelerate phentolamine degradation, reducing potency and potentially generating harmful oxidation products. The nitrogen overlay is the key reason for the unit-dose format: once opened, the nitrogen atmosphere is lost, making multi-dose packaging unsuitable for this formulation."},
        ],
        "key_trials": [
            {"name": "VEGA-3 (Phase 3 Presbyopia — Primary Pivotal)", "citation": "NCT — Viatris/Opus Genetics, n=545, 40 US sites", "design": "Randomized, double-masked, placebo-controlled, once-daily evening dosing, 6-week treatment + 48-week long-term safety follow-up", "primary_endpoint": "≥3-line DCNVA gain + <5-letter BCDVA loss at 12h post-dose, Day 8", "result": "PRIMARY ENDPOINT MET: 27.2% vs 11.5% placebo (p<0.0001). Secondary: 20.6% vs 6.1% at 1h Day 1 (p=0.0002). Patient-reported satisfaction significant at Days 3, 8, Week 6. No serious treatment-related AEs. No tachyphylaxis at 6 weeks."},
            {"name": "VEGA-2 (Phase 3 Presbyopia — Second Pivotal)", "citation": "n=333, ages 40–64, phentolamine ± adjunctive pilocarpine", "design": "Multicenter Phase 3 with pilocarpine adjunct arm", "primary_endpoint": "Near VA improvement", "result": "Met primary endpoint. Phentolamine alone and with low-dose pilocarpine both showed significant near VA improvement. Data contributes to sNDA submission."},
            {"name": "MIRA-2 + MIRA-3 (Phase 3 Mydriasis Reversal — Approved)", "citation": "n=553 combined, age 12–80", "design": "Two randomized, double-masked, placebo-controlled pivotal trials for mydriasis reversal", "primary_endpoint": "Return to baseline pupil diameter at 60 and 90 minutes", "result": "Both trials met primary endpoints. Supported FDA approval (NDA 217064) in September 2023. The approval provides existing safety/regulatory infrastructure for the sNDA."},
        ],
        "efficacy_summary": (
            "VEGA-3: 27.2% achieved ≥3-line DCNVA improvement at 12h Day 8 vs 11.5% placebo (p<0.0001). "
            "Evening dosing provides up to 20 hours of near vision improvement — effect present on waking. "
            "No brow ache. No myopic shift. No retinal detachment risk (no ciliary involvement). "
            "NOTE: Presbyopia indication NOT YET APPROVED — sNDA PDUFA October 17, 2026."
        ),
        "side_effects": [
            ("Systemic hypotension", "Low risk at ophthalmic dose", "α-adrenergic blockade can lower BP systemically. Caution with antihypertensive medications. Risk is minimal at 0.75% ophthalmic dose but nasolacrimal occlusion is recommended."),
            ("Dim vision at night", "Possible", "Miosis reduces light entry — effect during sleep minimized by evening dosing strategy."),
            ("Uveitis risk", "Rare — contraindicated active uveitis", "Risk of posterior synechiae (iris-lens adhesion) in inflamed eyes. Contraindicated in active iritis/uveitis."),
            ("Reflex tachycardia", "Rare", "Systemic α-blockade can cause compensatory heart rate increase. Uncommon at ophthalmic doses."),
            ("Refrigeration requirement", "Compliance concern", "Only approved presbyopia product requiring refrigerated storage — potential daily adherence issue."),
        ],
        "contraindications": (
            "Known hypersensitivity to phentolamine or excipients. Active uveitis/iritis. "
            "Caution: antihypertensive medications, cardiac conditions, MAO inhibitors. "
            "NOTE: Presbyopia use is investigational — sNDA PDUFA October 17, 2026. "
            "Current approved indication: reversal of pharmacologically induced mydriasis."
        ),
    },
}

DRUG_COLORS = {
    "VUITY":   "#534AB7",
    "QLOSI":   "#0F6E56",
    "VIZZ":    "#BA7517",
    "YUVEZZI": "#185FA5",
    "RYZUMVI": "#A32D2D",
}

DRUG_ORDER = ["VUITY", "QLOSI", "VIZZ", "YUVEZZI", "RYZUMVI"]

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
def badge(text, badge_class):
    return f'<span class="badge {badge_class}">{text}</span>'

def info_card(title, content_html):
    return f"""
<div class="info-card">
  <div class="info-card-title">{title}</div>
  <div class="info-card-value">{content_html}</div>
</div>
"""

def trial_box(trial):
    return f"""
<div class="trial-box">
  <div class="trial-box-title">🔬 {trial['name']}</div>
  <div class="trial-box-body">
    <b>Citation:</b> {trial['citation']}<br>
    <b>Design:</b> {trial['design']}<br>
    <b>Primary endpoint:</b> {trial['primary_endpoint']}<br>
    <b>Result:</b> {trial['result']}
  </div>
</div>
"""

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 💧 Presbyopia Eye Drop\n**Competitive Intelligence**")
    st.markdown("---")
    st.markdown("##### Select Drug")
    selected_drug = st.radio(
        label="Drug",
        options=DRUG_ORDER,
        label_visibility="collapsed",
        format_func=lambda x: f"{DRUGS[x]['brand'].replace('®','').replace('™','')}  —  {x}",
    )
    st.markdown("---")
    st.markdown("##### View Mode")
    view_mode = st.radio(
        "View", ["Drug Profile", "Comparison Table", "🇰🇷 Korea Landscape"],
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.markdown(
        '<p style="font-size:10px;color:#444860;">Data sources: FDA prescribing information (DailyMed), '
        'PubMed, ClinicalTrials.gov, PharmKorea. Last updated June 2026.</p>',
        unsafe_allow_html=True
    )

# ─────────────────────────────────────────────
# COMPARISON TABLE VIEW
# ─────────────────────────────────────────────
if view_mode == "Comparison Table":
    st.markdown('<p class="page-header">Presbyopia Eye Drop · Competitive Intelligence</p>', unsafe_allow_html=True)
    st.markdown("## Competitive Comparison — All 5 Drugs")
    st.markdown("---")

    rows = []
    for k in DRUG_ORDER:
        d = DRUGS[k]
        rows.append({
            "Drug": d["brand"],
            "Company": d["company"].split("/")[0].strip(),
            "API": d["active_ingredient"].split("\n")[0],
            "Concentration": d["concentration"].split("\n")[0],
            "Drug Class": d["drug_class"][:50] + "…" if len(d["drug_class"]) > 50 else d["drug_class"],
            "FDA Status": d["approval_status"].split("|")[0].strip(),
            "Approval Date": d["approval_date"].split("|")[0].strip()[:20],
            "Dosing": d["dosing"][:60] + "…",
            "Duration": d["duration"],
            "Preservative": d["preservative"],
            "Storage": d["storage"][:25],
            "Rx Type": d["rx_type"],
        })

    df = pd.DataFrame(rows).set_index("Drug")
    st.dataframe(df, use_container_width=True, height=260)

    st.markdown("---")
    st.markdown("### Molecular Data")
    mol_rows = []
    for k in DRUG_ORDER:
        d = DRUGS[k]
        apis = d["active_ingredient"].split("\n")
        for api in apis:
            mol_rows.append({
                "Brand": d["brand"],
                "API": api.strip(),
                "IUPAC Name": d["iupac"].split("\n")[0][:70] + "…" if len(d["iupac"].split("\n")[0]) > 70 else d["iupac"].split("\n")[0],
                "Molecular Formula": d["molecular_formula"].split("|")[0].strip()[:30],
                "MW (g/mol)": d["molecular_weight"].split("|")[0].strip()[:20],
            })
    df_mol = pd.DataFrame(mol_rows).set_index("Brand")
    st.dataframe(df_mol, use_container_width=True)

    st.markdown("---")
    st.markdown("### Formulation Comparison — Excipient Categories")
    excip_summary = []
    for k in DRUG_ORDER:
        d = DRUGS[k]
        roles = set(e["role"].split("/")[0].strip() for e in d["excipients"])
        excip_summary.append({
            "Brand": d["brand"],
            "API Count": len(d["active_ingredient"].split("+")),
            "Preservative": d["preservative"] if d["preservative"] != "None (preservative-free)" else "PF — None",
            "Buffer": next((e["name"].split(" (")[0] for e in d["excipients"] if "Buffer" in e["role"]), "—"),
            "Tonicity": next((e["name"].split(" ")[0] for e in d["excipients"] if "Tonicity" in e["role"]), "—"),
            "Viscosity Agent": next((e["name"].split(",")[0] for e in d["excipients"] if "Viscosity" in e["role"]), "None"),
            "pH Range": d["ph_range"],
            "Unique Feature": {
                "VUITY": "BAK preserved (0.0075%)",
                "QLOSI": "Polysorbate 80 penetration enhancer",
                "VIZZ": "Hypromellose viscosity + EDTA chelation",
                "YUVEZZI": "Dual-API; minimal excipient matrix",
                "RYZUMVI": "N₂ headspace; mannitol antioxidant role",
            }.get(k, "—")
        })
    df_excip = pd.DataFrame(excip_summary).set_index("Brand")
    st.dataframe(df_excip, use_container_width=True)

    st.stop()

# ─────────────────────────────────────────────
# KOREA LANDSCAPE VIEW
# ─────────────────────────────────────────────
if view_mode == "🇰🇷 Korea Landscape":
    st.markdown('<p class="page-header">Presbyopia Eye Drop · Korea Market Intelligence</p>', unsafe_allow_html=True)
    st.markdown("## 🇰🇷 Korean Presbyopia Eye Drop Market")
    st.markdown(
        "<p style='color:#5a5f78;font-size:14px;margin-bottom:8px;'>"
        "Current landscape of presbyopia eye drops entering the Korean market — "
        "MFDS approval status, license chains, and expected launch timeline. "
        "As of June 2026, <b>no presbyopia eye drop has received MFDS approval yet</b>. "
        "The market is a virgin territory with an estimated <b>17 million presbyopia patients</b>."
        "</p>", unsafe_allow_html=True
    )

    # ── Key market stats ──────────────────────────
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    for col, num, label in [
        (col1, "17M", "Estimated presbyopia patients in Korea"),
        (col2, "0",   "Currently MFDS-approved presbyopia drops"),
        (col3, "3",   "NDAs under active MFDS review"),
        (col4, "2026","Expected year of first approval"),
    ]:
        col.markdown(f"""
<div class="info-card" style="text-align:center;">
  <div class="info-card-title">{label}</div>
  <div style="font-size:30px;font-weight:700;color:#111827;">{num}</div>
</div>""", unsafe_allow_html=True)

    # ── Main comparison table ─────────────────────
    st.markdown("---")
    st.markdown("### Product-by-product breakdown")

    KOREA_DATA = [
        {
            "field": "Company",
            "YUVEZZI": "광동제약 (Kwangdong Pharma)",
            "VIZZ": "알보젠코리아 (Alvogen Korea)",
            "QLOSI": "옵투스제약 (Optus Pharma)",
            "Pilostar": "대우제약 (Daewoo Pharma)",
        },
        {
            "field": "Product",
            "YUVEZZI": "유베지 (YUVEZZI)",
            "VIZZ": "비즈 (VIZZ)",
            "QLOSI": "클로시 (QLOSI)",
            "Pilostar": "필로스타 (Pilostar)",
        },
        {
            "field": "Active Ingredient",
            "YUVEZZI": "Carbachol 2.75% + Brimonidine Tartrate 0.1%",
            "VIZZ": "Aceclidine 1.44%",
            "QLOSI": "Pilocarpine HCl 0.4%",
            "Pilostar": "Pilocarpine HCl 1.0%",
        },
        {
            "field": "MFDS Status",
            "YUVEZZI": "🟡 NDA under review",
            "VIZZ": "🟡 NDA under review",
            "QLOSI": "🔴 NDA not yet filed",
            "Pilostar": "🟢 Approved (glaucoma) — indication expansion planned",
        },
        {
            "field": "Developer (Originator)",
            "YUVEZZI": "Tenpoint Therapeutics (UK)",
            "VIZZ": "LENZ Therapeutics (US)",
            "QLOSI": "Orasis Pharmaceuticals (US / Israel)",
            "Pilostar": "In-house (domestic)",
        },
        {
            "field": "License Chain",
            "YUVEZZI": "Tenpoint → Zhaoke Ophthalmology (HK) → Kwangdong (Korea exclusive)",
            "VIZZ": "LENZ → Lotus Pharmaceutical (Taiwan) → Alvogen Korea (distribution)",
            "QLOSI": "Orasis → Optus Pharma (direct Korea license)",
            "Pilostar": "N/A — domestic manufacturer",
        },
        {
            "field": "Contract Signed",
            "YUVEZZI": "January 2024",
            "VIZZ": "May 2025",
            "QLOSI": "October 2025",
            "Pilostar": "N/A",
        },
        {
            "field": "MFDS NDA Filed",
            "YUVEZZI": "September 2025 ✓ (first NDA in Korea for presbyopia)",
            "VIZZ": "December 2025 ✓",
            "QLOSI": "Not yet announced as of early 2026",
            "Pilostar": "Trial planned for indication expansion (2–3 years)",
        },
        {
            "field": "US FDA Approved",
            "YUVEZZI": "January 28, 2026",
            "VIZZ": "July 31, 2025",
            "QLOSI": "October 16, 2023",
            "Pilostar": "No — domestic product only",
        },
        {
            "field": "Expected Korea Launch",
            "YUVEZZI": "2026 (earliest — first NDA filed)",
            "VIZZ": "2026",
            "QLOSI": "2026 (pending NDA filing)",
            "Pilostar": "N/A (indication approval ~2028–2029)",
        },
        {
            "field": "Duration",
            "YUVEZZI": "Up to 8 hours",
            "VIZZ": "Up to 10 hours",
            "QLOSI": "Up to 8 hours",
            "Pilostar": "~4–6 hours",
        },
        {
            "field": "Preservative",
            "YUVEZZI": "None (PF unit-dose)",
            "VIZZ": "None (PF unit-dose)",
            "QLOSI": "None (PF unit-dose)",
            "Pilostar": "None (PF unit-dose)",
        },
        {
            "field": "Key Differentiator",
            "YUVEZZI": "Only dual-agent (carbachol + brimonidine); lowest redness rate (2.8%); 12-month safety data",
            "VIZZ": "Longest duration (10 h); iris-selective miotic; no brow ache; new chemical entity",
            "QLOSI": "Lowest pilocarpine concentration (0.4%); PRN use possible; well-established FDA safety record",
            "Pilostar": "Only Korean-made product; existing glaucoma distribution; off-label presbyopia use ongoing",
        },
    ]

    # Build HTML table
    headers = ["Parameter", "유베지 (YUVEZZI)", "비즈 (VIZZ)", "클로시 (QLOSI)", "필로스타 (Pilostar)"]
    header_html = "".join(f"<th>{h}</th>" for h in headers)

    rows_html = ""
    status_map = {
        "YUVEZZI": "korea-status-review",
        "VIZZ": "korea-status-review",
        "QLOSI": "korea-status-pending",
        "Pilostar": "korea-status-launched",
    }

    for row in KOREA_DATA:
        cells = f"<td><b>{row['field']}</b></td>"
        for col_key in ["YUVEZZI", "VIZZ", "QLOSI", "Pilostar"]:
            val = row.get(col_key, "—")
            css_class = status_map[col_key] if row["field"] == "MFDS Status" else ""
            cells += f"<td class='{css_class}'>{val}</td>"
        rows_html += f"<tr>{cells}</tr>"

    st.markdown(f"""
<div style="overflow-x:auto;">
<table class="korea-tbl">
  <thead><tr>{header_html}</tr></thead>
  <tbody>{rows_html}</tbody>
</table>
</div>
""", unsafe_allow_html=True)

    # ── Strategic notes ───────────────────────────
    st.markdown("---")
    st.markdown("### Strategic context")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
<div class="info-card">
  <div class="info-card-title">🏁 The MFDS approval race</div>
  <div class="info-card-value">
    <b>Kwangdong (YUVEZZI)</b> filed first (Sep 2025) and holds the regulatory lead.<br><br>
    <b>Alvogen Korea (VIZZ)</b> filed second (Dec 2025) — 3 months behind.<br><br>
    <b>Optus Pharma (QLOSI)</b> has not yet filed — could be 6–12 months behind the leaders.<br><br>
    <b>Daewoo (Pilostar)</b> is on a completely separate timeline — a domestic clinical trial for indication expansion
    will take 2–3 years, with approval expected ~2028–2029 at the earliest.<br><br>
    <span class="warn">First-mover advantage is real — the first MFDS-approved presbyopia drop will
    establish prescriber habits and pharmacy relationships before competitors enter.</span>
  </div>
</div>
""", unsafe_allow_html=True)

    with col2:
        st.markdown("""
<div class="info-card">
  <div class="info-card-title">💡 Key market dynamics</div>
  <div class="info-card-value">
    <b>Duration is the main battleground:</b> VIZZ's 10 h vs YUVEZZI's 8 h vs QLOSI's 8 h.
    For working-age Korean patients (heavy screen use), duration matters for compliance.<br><br>
    <b>Side effect profile drives switches:</b> YUVEZZI → lowest redness; VIZZ → least brow ache;
    QLOSI → lowest pilocarpine dose.<br><br>
    <b>Reimbursement unresolved:</b> None of the products has been considered for NHI listing yet.
    If classified as lifestyle/cosmetic, coverage may be limited — significantly affecting market size.<br><br>
    <b>Daewoo wildcard:</b> Long-term, if the domestic trial succeeds, a Korean-made pilocarpine
    presbyopia drop can offer lower cost and domestic supply chain independence.
  </div>
</div>
""", unsafe_allow_html=True)

    # ── Timeline ──────────────────────────────────
    st.markdown("---")
    st.markdown("### Korea market timeline")

    timeline_events = [
        ("Jan 2024",  "#0d6b35", "Kwangdong signs Korea exclusive license for YUVEZZI from Zhaoke Ophthalmology"),
        ("May 2025",  "#1a4d9e", "Alvogen Korea signs distribution license for VIZZ (LENZ → Lotus → Alvogen)"),
        ("Jul 2025",  "#1a4d9e", "VIZZ receives US FDA approval — strengthens Korea dossier"),
        ("Sep 2025",  "#0d6b35", "Kwangdong files MFDS NDA for YUVEZZI — first presbyopia NDA in Korea"),
        ("Oct 2025",  "#a05c00", "Optus Pharma signs license for QLOSI (₩24B contract)"),
        ("Nov 2025",  "#1a4d9e", "VIZZ MFDS NDA filed by Alvogen Korea"),
        ("Nov 2025",  "#374151", "Daewoo launches Pilostar as glaucoma treatment; announces presbyopia indication-expansion plan"),
        ("Jan 2026",  "#0d6b35", "YUVEZZI receives US FDA approval — reinforces Kwangdong MFDS dossier"),
        ("2026 (est.)","#0d6b35","First MFDS presbyopia approval expected — market opens for the first time"),
        ("2026–2027", "#1a4d9e", "QLOSI MFDS filing and approval expected — 3-way commercial competition begins"),
        ("2028–2029", "#374151", "Daewoo indication-expansion trial expected to complete — domestic product enters market"),
    ]

    for date, color_dot, text in timeline_events:
        st.markdown(f"""
<div style="display:flex;gap:14px;align-items:flex-start;margin-bottom:10px;">
  <div style="flex-shrink:0;width:90px;font-size:11px;font-weight:700;color:#6b7280;padding-top:3px;">{date}</div>
  <div style="flex-shrink:0;width:10px;height:10px;border-radius:50%;background:{color_dot};margin-top:5px;"></div>
  <div style="font-size:13px;color:#374151;line-height:1.5;">{text}</div>
</div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(
        '<p class="source-note">Korea market data sourced from: Korean MFDS (식품의약품안전처) press releases, '
        'company announcements, PharmKorea (약학정보원), Kwangdong/Alvogen/Optus investor communications, '
        'and internal research. As of June 2026.</p>',
        unsafe_allow_html=True
    )
    st.stop()

# ─────────────────────────────────────────────
# SINGLE DRUG PROFILE VIEW
# ─────────────────────────────────────────────
d = DRUGS[selected_drug]
color = DRUG_COLORS[selected_drug]

st.markdown('<p class="page-header">Presbyopia Eye Drop · Competitive Intelligence · Drug Profile</p>', unsafe_allow_html=True)

# ── Hero card ──────────────────────────────
status_class = "badge-approved" if "Approved" in d["approval_status"] and "sNDA" not in d["approval_status"] else "badge-pending"
if "sNDA" in d["approval_status"]:
    status_badges = (
        badge("FDA Approved — Mydriasis Reversal", "badge-approved") +
        badge("sNDA Under Review — Presbyopia", "badge-pending") +
        badge(d["rx_type"], "badge-rx")
    )
elif "Approved" in d["approval_status"]:
    status_badges = badge("FDA Approved", "badge-approved") + badge(d["rx_type"], "badge-rx")
else:
    status_badges = badge(d["approval_status"], "badge-pending") + badge(d["rx_type"], "badge-rx")

st.markdown(f"""
<div class="drug-hero">
  <p class="drug-name" style="color:{color}">{d['brand']}</p>
  <p class="drug-generic">{d['generic']}</p>
  {status_badges}
  <div style="margin-top:14px;font-size:13px;color:#6b7280;">
    <b style="color:#111827">{d['company']}</b> &nbsp;·&nbsp;
    NDA: <b style="color:#111827">{d['nda_number']}</b> &nbsp;·&nbsp;
    Type: <b style="color:#111827">{d['application_type']}</b> &nbsp;·&nbsp;
    Approved: <b style="color:#111827">{d['approval_date']}</b>
  </div>
  <div style="margin-top:8px;font-size:12px;color:#9098b0;font-style:italic">{d['approval_note']}</div>
</div>
""", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🧬 API & Chemistry",
    "⚗️ Formulation & Excipients",
    "💊 Dosing & Clinical",
    "🔬 Efficacy & Trials",
    "⚠️ Safety Profile",
])

# ════════ TAB 1: API & CHEMISTRY ════════
with tab1:
    st.markdown("#### Active Ingredient(s) & Chemical Data")

    col1, col2 = st.columns([1.2, 0.8])
    with col1:
        st.markdown(info_card("IUPAC Name", f"<code style='font-size:12px;color:#1a4d9e;background:#f0f5ff;padding:4px 6px;border-radius:4px;'>{d['iupac'].replace(chr(10), '<br>')}</code>"), unsafe_allow_html=True)
        st.markdown(info_card("Molecular Formula",
            f"<span style='font-size:16px;font-family:monospace;color:#0d6b35;font-weight:700;'>{d['molecular_formula']}</span>"), unsafe_allow_html=True)
        st.markdown(info_card("Molecular Weight",
            f"<span style='font-size:16px;font-weight:700;color:#111827;'>{d['molecular_weight']}</span>"), unsafe_allow_html=True)

    with col2:
        st.markdown(info_card("Drug Class", d['drug_class']), unsafe_allow_html=True)
        st.markdown(info_card("Active Concentration",
            f"<b>{d['concentration']}</b><br><span style='color:#6b7280;font-size:12px;'>{d['free_base_equivalent']}</span>"), unsafe_allow_html=True)
        st.markdown(info_card("Prescription Type",
            f"<span class='highlight'>{d['rx_type']}</span>"), unsafe_allow_html=True)

    st.markdown("#### Mechanism of Action")
    st.markdown(f"""
<div class="info-card">
  <div class="info-card-title">Mechanism of Action (MOA)</div>
  <div class="info-card-value" style="white-space:pre-line;">{d['moa']}</div>
</div>
""", unsafe_allow_html=True)

    st.markdown(info_card("Technology / Platform", d["technology"]), unsafe_allow_html=True)

# ════════ TAB 2: FORMULATION ════════
with tab2:
    st.markdown("#### Formulation Details")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(info_card("Dosage Form", d["dosage_form"]), unsafe_allow_html=True)
        st.markdown(info_card("Preservative",
            f"<span class='{'highlight' if 'None' in d['preservative'] else 'warn'}'>{d['preservative']}</span>"), unsafe_allow_html=True)
    with col2:
        st.markdown(info_card("pH Range", f"<b>{d['ph_range']}</b>"), unsafe_allow_html=True)
        st.markdown(info_card("Storage", d["storage"]), unsafe_allow_html=True)
    with col3:
        st.markdown(info_card("Active Ingredient Concentration",
            f"<b>{d['concentration']}</b>"), unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### Complete Excipient List with Functions")
    st.markdown("*Each excipient sourced from official FDA prescribing information / DailyMed*", unsafe_allow_html=False)

    rows_html = ""
    for i, exc in enumerate(d["excipients"]):
        bg = "background:rgba(255,255,255,0.015);" if i % 2 == 0 else ""
        rows_html += f"""
<tr style="{bg}">
  <td><b>{exc['name']}</b></td>
  <td><span class="excip-role">{exc['role']}</span></td>
  <td>{exc['function']}</td>
</tr>"""

    st.markdown(f"""
<div class="info-card">
<table class="excip-table">
  <thead><tr>
    <th style="min-width:200px">Excipient</th>
    <th style="min-width:140px">Role / Category</th>
    <th>Function & Rationale</th>
  </tr></thead>
  <tbody>{rows_html}</tbody>
</table>
</div>
""", unsafe_allow_html=True)

# ════════ TAB 3: DOSING & CLINICAL ════════
with tab3:
    st.markdown("#### Dosing Information")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(info_card("Recommended Dosing", d["dosing"]), unsafe_allow_html=True)
        st.markdown(info_card("Onset of Action",
            f"<span class='highlight'>{d['onset']}</span>"), unsafe_allow_html=True)
        st.markdown(info_card("Duration of Effect",
            f"<span class='highlight'>{d['duration']}</span>"), unsafe_allow_html=True)
    with col2:
        st.markdown(info_card("Dosage Form", d["dosage_form"]), unsafe_allow_html=True)
        st.markdown(info_card("Storage Conditions", d["storage"]), unsafe_allow_html=True)
        st.markdown(info_card("Approval / Regulatory Status",
            f"{d['approval_status']}<br><span style='font-size:12px;color:#9098b0;'>{d['approval_note']}</span>"), unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### Regulatory Details")
    reg_html = f"""
<b>NDA Number:</b> {d['nda_number']}<br>
<b>Application Type:</b> {d['application_type']}<br>
<b>Approval Date:</b> {d['approval_date']}<br>
<b>Prescription Classification:</b> {d['rx_type']}
"""
    st.markdown(info_card("Regulatory Filing Information", reg_html), unsafe_allow_html=True)

# ════════ TAB 4: EFFICACY & TRIALS ════════
with tab4:
    st.markdown("#### Efficacy Summary")
    st.markdown(f"""
<div class="info-card">
  <div class="info-card-title">Overall Efficacy Profile</div>
  <div class="info-card-value">{d['efficacy_summary']}</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### Key Clinical Trials")
    for trial in d["key_trials"]:
        st.markdown(trial_box(trial), unsafe_allow_html=True)

# ════════ TAB 5: SAFETY ════════
with tab5:
    st.markdown("#### Adverse Effects")
    cols = st.columns([1.2, 0.6, 2.2])
    cols[0].markdown("**Adverse Effect**")
    cols[1].markdown("**Incidence**")
    cols[2].markdown("**Notes**")
    st.markdown('<div style="border-top:1.5px solid #e5e8ef;margin-bottom:10px"></div>', unsafe_allow_html=True)

    for ae, incidence, note in d["side_effects"]:
        c1, c2, c3 = st.columns([1.2, 0.6, 2.2])
        c1.markdown(f"<div style='font-size:13px;color:#111827;font-weight:500;padding:4px 0;'>{ae}</div>", unsafe_allow_html=True)
        c2.markdown(f"<div style='font-size:12px;color:#a05c00;font-weight:600;padding:4px 0;'>{incidence}</div>", unsafe_allow_html=True)
        c3.markdown(f"<div style='font-size:12px;color:#5a5f78;padding:4px 0;'>{note}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### Contraindications & Warnings")
    st.markdown(f"""
<div class="info-card">
  <div class="info-card-title">Contraindications & Important Warnings</div>
  <div class="info-card-value danger">{d['contraindications']}</div>
</div>
""", unsafe_allow_html=True)

# ── Footer ────────────────────────────────
st.markdown("---")
st.markdown(
    '<p class="source-note">Data sourced from: FDA DailyMed, accessdata.fda.gov prescribing information, PubMed, ClinicalTrials.gov, '
    'Drugs.com, and internal research sessions. All excipient data confirmed from official product labels. '
    'RYZUMVI presbyopia indication is investigational — sNDA PDUFA October 17, 2026. Last updated June 2026.</p>',
    unsafe_allow_html=True
)
