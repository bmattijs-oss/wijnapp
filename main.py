import streamlit as st
import pandas as pd

# ==========================================
# 1. DE DATABASES
# ==========================================

druiven_profielen = {
    # WIT
    "sauvignon blanc": {"type": "wit", "body": 2, "zuur": 5, "tannine": 1, "zoet": 1},
    "chardonnay":      {"type": "wit", "body": 5, "zuur": 2, "tannine": 1, "zoet": 1},
    "verdejo":         {"type": "wit", "body": 3, "zuur": 4, "tannine": 1, "zoet": 1},
    "pinot grigio":    {"type": "wit", "body": 2, "zuur": 3, "tannine": 1, "zoet": 1},
    "viognier":        {"type": "wit", "body": 4, "zuur": 2, "tannine": 1, "zoet": 1},
    "riesling":        {"type": "wit", "body": 2, "zuur": 5, "tannine": 1, "zoet": 2},
    "grüner veltliner":{"type": "wit", "body": 3, "zuur": 4, "tannine": 1, "zoet": 1},
    "chenin blanc":    {"type": "wit", "body": 4, "zuur": 4, "tannine": 1, "zoet": 1},
    "muscat":          {"type": "wit", "body": 3, "zuur": 2, "tannine": 1, "zoet": 4},
    "gewürztraminer":  {"type": "wit", "body": 4, "zuur": 2, "tannine": 1, "zoet": 3},
    "airén":           {"type": "wit", "body": 2, "zuur": 2, "tannine": 1, "zoet": 1},
    "trebbiano":       {"type": "wit", "body": 2, "zuur": 3, "tannine": 1, "zoet": 1},
    "pecorino":        {"type": "wit", "body": 3, "zuur": 4, "tannine": 1, "zoet": 1},
    
    # ROOD
    "merlot":          {"type": "rood", "body": 3, "zuur": 2, "tannine": 2, "zoet": 1},
    "cabernet sauvignon":{"type": "rood", "body": 5, "zuur": 3, "tannine": 5, "zoet": 1},
    "shiraz":          {"type": "rood", "body": 5, "zuur": 2, "tannine": 4, "zoet": 1},
    "syrah":           {"type": "rood", "body": 5, "zuur": 2, "tannine": 4, "zoet": 1},
    "pinot noir":      {"type": "rood", "body": 2, "zuur": 4, "tannine": 2, "zoet": 1},
    "primitivo":       {"type": "rood", "body": 5, "zuur": 2, "tannine": 3, "zoet": 2},
    "tempranillo":     {"type": "rood", "body": 4, "zuur": 3, "tannine": 4, "zoet": 1},
    "sangiovese":      {"type": "rood", "body": 4, "zuur": 5, "tannine": 4, "zoet": 1},
    "malbec":          {"type": "rood", "body": 5, "zuur": 3, "tannine": 4, "zoet": 1},
    "grenache":        {"type": "rood", "body": 4, "zuur": 2, "tannine": 2, "zoet": 1},
    "montepulciano":   {"type": "rood", "body": 4, "zuur": 3, "tannine": 3, "zoet": 1},
    "corvina":         {"type": "rood", "body": 3, "zuur": 4, "tannine": 2, "zoet": 1},
    "nero d'avola":    {"type": "rood", "body": 4, "zuur": 3, "tannine": 3, "zoet": 1},
    "gamay":           {"type": "rood", "body": 2, "zuur": 4, "tannine": 1, "zoet": 1},
    
    # BLENDS & OVERIG
    "blend":           {"type": "rood", "body": 3, "zuur": 3, "tannine": 3, "zoet": 1},
    "vruchtenwijn":    {"type": "wit", "body": 3, "zuur": 2, "tannine": 1, "zoet": 5},
}

eten_db = {
    "Zalm":      {"gewicht": 3, "vet": 4, "kleur": "wit"},
    "Biefstuk":  {"gewicht": 5, "vet": 3, "kleur": "rood"},
    "Kip":       {"gewicht": 2, "vet": 2, "kleur": "geen"},
    "Mosselen":  {"gewicht": 1, "vet": 1, "kleur": "wit"},
    "Pasta Rood":{"gewicht": 3, "vet": 2, "kleur": "rood"},
    "Salade":    {"gewicht": 1, "vet": 1, "kleur": "wit"},
}

saus_db = {
    "Geen":        {"gew_mod": 0, "vet_mod": 0, "effect": "neutraal"},
    "Roomsaus":    {"gew_mod": 2, "vet_mod": 2, "effect": "romig"},
    "Pepersaus":   {"gew_mod": 2, "vet_mod": 2, "effect": "kruidig"},
    "Kerriesaus":  {"gew_mod": 2, "vet_mod": 1, "effect": "pittig"},
    "Tomatensaus": {"gew_mod": 1, "vet_mod": 0, "effect": "fris"},
    "Citroen":     {"gew_mod": 0, "vet_mod": 0, "effect": "zuur"},
}

# ==========================================
# 2. DE FUNCTIES
# ==========================================

@st.cache_data
def laad_assortiment():
    # Let op: bestandsnamen moeten EXACT kloppen met wat je uploadt naar GitHub
    try:
        df_wit = pd.read_excel("AH - witte wijnen.xlsx")
        df_rood = pd.read_excel("AH_Rode_Wijnen_Met_Producenten.xlsx")
        df_rose = pd.read_excel("AH_Rose_Wijnen_Met_Producenten.xlsx")
    except FileNotFoundError:
        return pd.DataFrame()

    df_wit = df_wit.rename(columns={'Druif': 'druif_raw', 'Naam': 'naam', 'Prijs': 'prijs'})
    df_rood = df_rood.rename(columns={'Druivensoort': 'druif_raw', 'Naam': 'naam', 'Prijs': 'prijs'})
    df_rose = df_rose.rename(columns={'Druivensoort': 'druif_raw', 'Naam': 'naam', 'Prijs': 'prijs'})

    df_totaal = pd.concat([df_wit, df_rood, df_rose], ignore_index=True)
    df_totaal['druif_clean'] = df_totaal['druif_raw'].astype(str).str.lower().str.strip()
    
    return df_totaal

def vind_beste_wijn(gerecht, saus, df_input):
    eten_info = eten_db.get(gerecht)
    saus_info = saus_db.get(saus)
    
    if not eten_info: return []
    
    doel_gewicht = eten_info['gewicht'] + saus_info['gew_mod']
    doel_vet = eten_info['vet'] + saus_info['vet_mod']
    doel_kleur = eten_info['kleur']
    
    doel_zoet = 1
    if saus_info['effect'] == 'pittig': doel_zoet = 3
    
    resultaten = []
    
    for index, row in df_input.iterrows():
        druif_tekst = row['druif_clean']
        
        profiel = None
        for bekende_druif, p in druiven_profielen.items():
            if bekende_druif in druif_tekst:
                profiel = p
                break 
        
        if not profiel:
            continue 
            
        if doel_kleur != "geen" and profiel['type'] != doel_kleur:
            continue 
            
        strafpunten = abs(profiel['body'] - doel_gewicht) + \
                      abs(profiel['zuur'] - doel_vet) + \
                      abs(profiel['zoet'] - doel_zoet)
        
        resultaten.append({
            "naam": row['naam'],
            "prijs": row['prijs'],
            "druif": row['druif_raw'],
            "score": strafpunten
        })
        
    resultaten.sort(key=lambda x: x['score'])
    return resultaten[:5]

# ==========================================
# 3. DE APP
# ==========================================

def main():
    st.title("🍷 De Wijn-Scanner")
    st.write("Wat eten we vandaag?")

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Het Hoofdingrediënt")
        keuze_gerecht = st.selectbox("Kies gerecht:", list(eten_db.keys()))
        
    with col2:
        st.subheader("2. De Saus / Bereiding")
        keuze_saus = st.selectbox("Kies saus:", list(saus_db.keys()))

    st.write("") 
    zoek_knop = st.button("🔍 Vind de perfecte wijn", type="primary")

    if zoek_knop:
        df = laad_assortiment()
        
        if df.empty:
            st.error("⚠️ Kan de Excel-bestanden niet vinden! Zorg dat ze geüpload zijn naar GitHub.")
        else:
            matches = vind_beste_wijn(keuze_gerecht, keuze_saus, df)

            if not matches:
                st.warning("Geen exacte match gevonden. Probeer een ander gerecht.")
            else:
                st.success(f"Gevonden! Top 3 wijnen voor {keuze_gerecht} met {keuze_saus}:")
                
                for i, wijn in enumerate(matches[:3], 1):
                    with st.container():
                        st.markdown(f"### #{i}: {wijn['naam']}")
                        col_a, col_b = st.columns([1, 3])
                        with col_a:
                            st.image("https://cdn-icons-png.flaticon.com/512/2405/2405451.png", width=80)
                        with col_b:
                            st.markdown(f"**Druif:** {wijn['druif']}")
                            st.markdown(f"**Prijs:** €{wijn['prijs']}")
                            st.caption(f"Match Score: {wijn['score']} (Lager is beter)")
                    st.divider()

if __name__ == "__main__":
    main()