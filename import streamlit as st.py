import streamlit as st
from PIL import Image
import csv
from datetime import datetime

st.set_page_config(page_title="Kompletter Test", layout="centered")

# Logo anzeigen
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(current_dir, "Zukunftsmotor_logo.png")

if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.image(logo, width=300)
else:
    st.error(f"Logo nicht gefunden: {logo_path}")

st.title("IT‑Vorwissen & Lernstil – Gesamttest")

# Admin-Modus Toggle in Sidebar
with st.sidebar:
    st.header("⚙️ Einstellungen")
    admin_mode = st.checkbox("Admin-Ansicht", value=False)
    if admin_mode:
        admin_password = st.text_input("Admin-Passwort:", type="password")
        if admin_password == "Berserker":  # Ändern Sie dieses Passwort!
            st.success("Admin-Modus aktiviert")
        else:
            st.error("Falsches Passwort")
            admin_mode = False

if admin_mode and admin_password == "admin123":
    # ADMIN-BEREICH
    st.header("📊 Admin-Bereich - Alle Ergebnisse")
    
    csv_file = os.path.join(current_dir, "teilnehmer_ergebnisse.csv")
    
    if os.path.exists(csv_file):
        import pandas as pd
        df = pd.read_csv(csv_file)
        st.dataframe(df, use_container_width=True)
        
        st.download_button(
            label="📥 Alle Ergebnisse als CSV herunterladen",
            data=df.to_csv(index=False).encode('utf-8'),
            file_name=f"alle_ergebnisse_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
        
        if st.button("🗑️ Alle Daten löschen"):
            os.remove(csv_file)
            st.success("Alle Daten wurden gelöscht!")
            st.rerun()
    else:
        st.info("Noch keine Teilnehmer-Daten vorhanden.")
    
    st.stop()

# NORMALER TEILNEHMER-MODUS
st.write("Beantworte alle Fragen. Am Ende erhältst du eine vollständige Auswertung.")

# ---------------------------------------------------------
# TEILNEHMER NAME
# ---------------------------------------------------------

teilnehmer_name = st.text_input("👤 Dein Name:", placeholder="Max Mustermann")

st.markdown("---")

# ---------------------------------------------------------
# PUNKTE-SPEICHER
# ---------------------------------------------------------

it_punkte = 0

lernstil_punkte = {
    "praktisch": 0,
    "analytisch": 0,
    "visuell": 0,
    "sozial": 0,
    "strukturiert": 0,
    "flexibel": 0
}

# ---------------------------------------------------------
# IT‑VORWISSEN TEST
# ---------------------------------------------------------

st.header("🧠 IT‑Vorwissen")

# Frage 1
f1 = st.radio(
    "1. Welche Funktion erfüllt ein DHCP‑Server?",
    [
        "Bitte auswählen...",
        "Er vergibt IP‑Adressen automatisch an Geräte.",
        "Er speichert alle Netzwerkdaten.",
        "Er verschlüsselt die Kommunikation.",
        "Er schützt das Netzwerk vor Viren."
    ]
)
if f1 == "Er vergibt IP‑Adressen automatisch an Geräte.":
    it_punkte += 1

# Frage 2
f2 = st.radio(
    "2. Was beschreibt Active Directory?",
    [
        "Bitte auswählen...",
        "Verwaltung von Benutzern, Gruppen und Ressourcen.",
        "Ein Cloud‑Speicher.",
        "Ein Virenschutzprogramm.",
        "Ein Tool zur Bildbearbeitung."
    ]
)
if f2 == "Verwaltung von Benutzern, Gruppen und Ressourcen.":
    it_punkte += 1

# Frage 3
f3 = st.radio(
    "3. Wofür steht Port 443?",
    [
        "Bitte auswählen...",
        "HTTPS‑verschlüsselter Webverkehr.",
        "DNS‑Anfragen.",
        "Remote Desktop.",
        "Unverschlüsseltes FTP."
    ]
)
if f3 == "HTTPS‑verschlüsselter Webverkehr.":
    it_punkte += 1

# Frage 4
f4 = st.radio(
    "4. Wofür wird ein DNS‑Server benötigt?",
    [
        "Bitte auswählen...",
        "Er übersetzt Domainnamen in IP‑Adressen.",
        "Er speichert Passwörter.",
        "Er überwacht den Netzwerkverkehr.",
        "Er erstellt Backups."
    ]
)
if f4 == "Er übersetzt Domainnamen in IP‑Adressen.":
    it_punkte += 1

# Frage 5
f5 = st.radio(
    "5. Welche Aufgabe hat ein Switch?",
    [
        "Bitte auswählen...",
        "Er verbindet Geräte innerhalb eines LANs.",
        "Er stellt Internetzugang bereit.",
        "Er speichert Dateien zentral.",
        "Er verschlüsselt WLAN."
    ]
)
if f5 == "Er verbindet Geräte innerhalb eines LANs.":
    it_punkte += 1

# Frage 6
f6 = st.radio(
    "6. Wofür steht HTTPS?",
    [
        "Bitte auswählen...",
        "Verschlüsselter Webverkehr.",
        "Unverschlüsselter Webverkehr.",
        "Ein Backup‑Protokoll.",
        "Ein WLAN‑Standard."
    ]
)
if f6 == "Verschlüsselter Webverkehr.":
    it_punkte += 1

# Frage 7
f7 = st.radio(
    "7. Was macht eine Firewall?",
    [
        "Bitte auswählen...",
        "Sie filtert Netzwerkverkehr.",
        "Sie speichert Daten.",
        "Sie vergibt IP‑Adressen.",
        "Sie ersetzt den Router."
    ]
)
if f7 == "Sie filtert Netzwerkverkehr.":
    it_punkte += 1

# Frage 8
f8 = st.radio(
    "8. Was ist ein Vorteil der Virtualisierung?",
    [
        "Bitte auswählen...",
        "Mehrere Betriebssysteme auf einem Host.",
        "Sie verhindert alle Cyberangriffe.",
        "Sie macht Computer automatisch schneller.",
        "Sie ersetzt Firewalls."
    ]
)
if f8 == "Mehrere Betriebssysteme auf einem Host.":
    it_punkte += 1

f9 = st.radio(
    "9. Was ist ein Betriebssystem?",
    [
        "Bitte auswählen...",
        "Eine Software, die Hardware verwaltet und Programme ausführt.",
        "Ein Programm zur Bildbearbeitung.",
        "Ein Gerät zur Netzwerküberwachung.",
        "Ein Cloud‑Dienst."
    ]
)
if f9 == "Eine Software, die Hardware verwaltet und Programme ausführt.":
    it_punkte += 1

f10 = st.radio(
    "10. Was ist eine SSD?",
    [
        "Bitte auswählen...",
        "Ein schneller, nicht‑mechanischer Datenspeicher.",
        "Ein Prozessor.",
        "Ein Netzwerkkabel.",
        "Ein Backup‑System."
    ]
)
if f10 == "Ein schneller, nicht‑mechanischer Datenspeicher.":
    it_punkte += 1

f11 = st.radio(
    "11. Wofür steht CPU?",
    [
        "Bitte auswählen...",
        "Central Processing Unit.",
        "Computer Power Unit.",
        "Central Program Utility.",
        "Core Performance Upgrade."
    ]
)
if f11 == "Central Processing Unit.":
    it_punkte += 1

f12 = st.radio(
    "12. Was macht ein Proxy‑Server?",
    [
        "Bitte auswählen...",
        "Er vermittelt Anfragen zwischen Client und Internet.",
        "Er ersetzt den Router.",
        "Er speichert alle Dateien.",
        "Er verschlüsselt WLAN."
    ]
)
if f12 == "Er vermittelt Anfragen zwischen Client und Internet.":
    it_punkte += 1

f13 = st.radio(
    "13. Was ist ein Backup?",
    [
        "Bitte auswählen...",
        "Eine Sicherungskopie wichtiger Daten.",
        "Ein Netzwerkprotokoll.",
        "Ein Virenschutz.",
        "Ein Router."
    ]
)
if f13 == "Eine Sicherungskopie wichtiger Daten.":
    it_punkte += 1

f14 = st.radio(
    "14. Was ist ein Router?",
    [
        "Bitte auswählen...",
        "Ein Gerät, das Netzwerke verbindet.",
        "Ein Gerät zur Datenspeicherung.",
        "Ein Gerät zur Bildbearbeitung.",
        "Ein Gerät zur Virtualisierung."
    ]
)
if f14 == "Ein Gerät, das Netzwerke verbindet.":
    it_punkte += 1

f15 = st.radio(
    "15. Was ist ein Patch?",
    [
        "Bitte auswählen...",
        "Ein Update zur Fehlerbehebung.",
        "Ein Backup.",
        "Ein Hardware‑Upgrade.",
        "Ein Netzwerkgerät."
    ]
)
if f15 == "Ein Update zur Fehlerbehebung.":
    it_punkte += 1

f16 = st.radio(
    "16. Was ist ein VPN?",
    [
        "Bitte auswählen...",
        "Ein verschlüsselter Tunnel für sichere Verbindungen.",
        "Ein WLAN‑Standard.",
        "Ein Backup‑System.",
        "Ein Router."
    ]
)
if f16 == "Ein verschlüsselter Tunnel für sichere Verbindungen.":
    it_punkte += 1

f17 = st.radio(
    "17. Was ist RAM?",
    [
        "Bitte auswählen...",
        "Ein schneller Arbeitsspeicher für laufende Prozesse.",
        "Ein Datenspeicher für Backups.",
        "Ein Netzwerkprotokoll.",
        "Ein Grafikchip."
    ]
)
if f17 == "Ein schneller Arbeitsspeicher für laufende Prozesse.":
    it_punkte += 1

f18 = st.radio(
    "18. Was ist ein Hypervisor?",
    [
        "Bitte auswählen...",
        "Eine Software, die virtuelle Maschinen verwaltet.",
        "Ein Router.",
        "Ein Backup‑System.",
        "Ein Firewall‑Modul."
    ]
)
if f18 == "Eine Software, die virtuelle Maschinen verwaltet.":
    it_punkte += 1


# ---------------------------------------------------------
# LERNSTIL‑TEST
# ---------------------------------------------------------

st.header("🎨 Lernstil‑Analyse")

# Frage 1
ls1 = st.radio(
    "1. Wie gehst du an neue Themen heran?",
    [
        "Ich probiere Dinge direkt aus.",
        "Ich lese zuerst nach.",
        "Ich schaue Videos oder Erklärungen.",
        "Ich lasse es mir erklären."
    ]
)
mapping1 = {
    "Ich probiere Dinge direkt aus.": "praktisch",
    "Ich lese zuerst nach.": "analytisch",
    "Ich schaue Videos oder Erklärungen.": "visuell",
    "Ich lasse es mir erklären.": "sozial"
}
lernstil_punkte[mapping1[ls1]] += 1

# Frage 2
ls2 = st.radio(
    "2. Was motiviert dich beim Lernen?",
    [
        "Klare Ziele und Struktur.",
        "Eigene Neugier.",
        "Teamarbeit.",
        "Druck oder Deadlines."
    ]
)
mapping2 = {
    "Klare Ziele und Struktur.": "strukturiert",
    "Eigene Neugier.": "flexibel",
    "Teamarbeit.": "sozial",
    "Druck oder Deadlines.": "strukturiert"
}
lernstil_punkte[mapping2[ls2]] += 1

# Frage 3
ls3 = st.radio(
    "3. Wie gehst du mit schwierigen Aufgaben um?",
    [
        "Ich zerlege sie in Schritte.",
        "Ich probiere verschiedene Wege.",
        "Ich suche Praxisbeispiele.",
        "Ich bespreche es mit anderen."
    ]
)
mapping3 = {
    "Ich zerlege sie in Schritte.": "strukturiert",
    "Ich probiere verschiedene Wege.": "flexibel",
    "Ich suche Praxisbeispiele.": "praktisch",
    "Ich bespreche es mit anderen.": "sozial"
}
lernstil_punkte[mapping3[ls3]] += 1

ls4 = st.radio(
    "4. Wie behältst du Informationen am besten?",
    [
        "Bitte auswählen...",
        "Durch Schreiben oder Mitschriften.",
        "Durch Zuhören.",
        "Durch Bilder oder Videos.",
        "Durch Anwenden in der Praxis."
    ]
)

mapping4 = {
    "Durch Schreiben oder Mitschriften.": "praktisch",
    "Durch Zuhören.": "sozial",
    "Durch Bilder oder Videos.": "visuell",
    "Durch Anwenden in der Praxis.": "praktisch"
}

if ls4 != "Bitte auswählen...":
    lernstil_punkte[mapping4[ls4]] += 1

ls5 = st.radio(
    "5. Wie gehst du mit Fehlern um?",
    [
        "Bitte auswählen...",
        "Ich analysiere sie.",
        "Ich probiere erneut.",
        "Ich hole mir Feedback.",
        "Ich mache eine Pause."
    ]
)

mapping5 = {
    "Ich analysiere sie.": "analytisch",
    "Ich probiere erneut.": "praktisch",
    "Ich hole mir Feedback.": "sozial",
    "Ich mache eine Pause.": "flexibel"
}

if ls5 != "Bitte auswählen...":
    lernstil_punkte[mapping5[ls5]] += 1

ls6 = st.radio(
    "6. Welche Lernumgebung bevorzugst du?",
    [
        "Bitte auswählen...",
        "Ruhig und strukturiert.",
        "Flexibel und frei.",
        "Mit anderen zusammen.",
        "Unter leichtem Zeitdruck."
    ]
)

mapping6 = {
    "Ruhig und strukturiert.": "strukturiert",
    "Flexibel und frei.": "flexibel",
    "Mit anderen zusammen.": "sozial",
    "Unter leichtem Zeitdruck.": "strukturiert"
}

if ls6 != "Bitte auswählen...":
    lernstil_punkte[mapping6[ls6]] += 1

ls7 = st.radio(
    "7. Wie startest du ein neues Projekt?",
    [
        "Bitte auswählen...",
        "Ich plane alles im Voraus.",
        "Ich lege einfach los.",
        "Ich suche Inspiration.",
        "Ich bespreche es mit anderen."
    ]
)

mapping7 = {
    "Ich plane alles im Voraus.": "strukturiert",
    "Ich lege einfach los.": "praktisch",
    "Ich suche Inspiration.": "visuell",
    "Ich bespreche es mit anderen.": "sozial"
}

if ls7 != "Bitte auswählen...":
    lernstil_punkte[mapping7[ls7]] += 1

ls8 = st.radio(
    "8. Wie gehst du mit komplexen Themen um?",
    [
        "Bitte auswählen...",
        "Ich zerlege sie in kleine Teile.",
        "Ich suche Praxisbeispiele.",
        "Ich probiere herum.",
        "Ich bespreche sie mit anderen."
    ]
)

mapping8 = {
    "Ich zerlege sie in kleine Teile.": "analytisch",
    "Ich suche Praxisbeispiele.": "praktisch",
    "Ich probiere herum.": "flexibel",
    "Ich bespreche sie mit anderen.": "sozial"
}

if ls8 != "Bitte auswählen...":
    lernstil_punkte[mapping8[ls8]] += 1

ls9 = st.radio(
    "9. Wie organisierst du dein Lernen?",
    [
        "Bitte auswählen...",
        "Mit klaren Plänen.",
        "Mit kreativen Methoden.",
        "Mit visuellen Hilfen.",
        "Mit anderen zusammen."
    ]
)

mapping9 = {
    "Mit klaren Plänen.": "strukturiert",
    "Mit kreativen Methoden.": "flexibel",
    "Mit visuellen Hilfen.": "visuell",
    "Mit anderen zusammen.": "sozial"
}

if ls9 != "Bitte auswählen...":
    lernstil_punkte[mapping9[ls9]] += 1



# ---------------------------------------------------------
# AUSWERTUNG
# ---------------------------------------------------------

import matplotlib.pyplot as plt

if st.button("📊 Gesamtauswertung anzeigen"):
    st.header("📈 Deine Ergebnisse")

    # -----------------------------------------------------
    # IT‑AUSWERTUNG
    # -----------------------------------------------------
    st.subheader("🧠 IT‑Vorwissen – Analyse")

    gesamt_it = 18  # Anzahl deiner IT‑Fragen
    prozent = round((it_punkte / gesamt_it) * 100)

    st.write(f"Du hast **{it_punkte} von {gesamt_it} Punkten** erreicht.")
    st.write(f"Das entspricht **{prozent}%**.")

    if prozent >= 85:
        st.success("🔹 **Level: Profi** – Sehr starkes IT‑Grundwissen, du bist bestens vorbereitet.")
    elif prozent >= 60:
        st.info("🔹 **Level: Fortgeschritten** – Gute Basis, einzelne Themen können vertieft werden.")
    elif prozent >= 40:
        st.warning("🔹 **Level: Basis** – Grundkenntnisse vorhanden, aber es gibt Lücken.")
    else:
        st.error("🔹 **Level: Einsteiger** – Du wirst im Kurs zusätzliche Unterstützung erhalten.")

    st.markdown("---")

    # -----------------------------------------------------
    # LERNSTIL‑AUSWERTUNG
    # -----------------------------------------------------
    st.subheader("🎨 Lernstil‑Profil")

    # Punkte anzeigen
    for stil, wert in lernstil_punkte.items():
        st.write(f"- **{stil.capitalize()}**: {wert} Punkte")

    # Dominanter Lernstil
    dominant = max(lernstil_punkte, key=lernstil_punkte.get)

    # Zweitstärkster Lernstil
    sorted_styles = sorted(lernstil_punkte.items(), key=lambda x: x[1], reverse=True)
    zweit = sorted_styles[1][0]

    st.success(f"Dein dominanter Lernstil ist: **{dominant.capitalize()}**")
    st.info(f"Dein sekundärer Lernstil ist: **{zweit.capitalize()}**")

    # Empfehlungstexte
    empfehlungen = {
        "praktisch": "Du lernst am besten durch Ausprobieren, Übungen und reale Aufgaben.",
        "analytisch": "Du profitierst von Erklärungen, Konzepten und Hintergrundwissen.",
        "visuell": "Du merkst dir Inhalte besonders gut über Bilder, Diagramme und Videos.",
        "sozial": "Du lernst stark im Austausch mit anderen.",
        "strukturiert": "Du brauchst klare Ziele, Pläne und Schritt‑für‑Schritt‑Anleitungen.",
        "flexibel": "Du lernst gut in offenen, kreativen Situationen."
    }

    st.markdown("### 📌 Empfehlung für deinen Lernstil")
    st.write(empfehlungen[dominant])

    st.markdown("---")

    # -----------------------------------------------------
    # BALKENDIAGRAMM – LERNSTILE
    # -----------------------------------------------------
    st.subheader("📊 Lernstil‑Diagramm")

    fig, ax = plt.subplots()
    ax.bar(lernstil_punkte.keys(), lernstil_punkte.values(), color=["#4e79a7", "#f28e2b", "#e15759", "#76b7b2", "#59a14f", "#edc949"])
    ax.set_xlabel("Lernstil")
    ax.set_ylabel("Punkte")
    ax.set_title("Lernstil‑Verteilung")
    plt.xticks(rotation=45)

    st.pyplot(fig)

    st.markdown("---")

    # -----------------------------------------------------
    # ZUSAMMENFASSUNG FÜR TRAINER:INNEN
    # -----------------------------------------------------
    st.subheader("📘 Zusammenfassung für Trainer:innen")

    st.write(f"""
    **IT‑Level:** {prozent}%  
    **Dominanter Lernstil:** {dominant.capitalize()}  
    **Sekundärer Lernstil:** {zweit.capitalize()}  

    **Interpretation:**  
    - Lernende mit einem *{dominant}*‑Profil profitieren besonders von:  
      → {empfehlungen[dominant]}  
    - Zweitstarke Ausprägung *{zweit}* unterstützt den Lernprozess zusätzlich.
    """)

    st.success("Die Auswertung ist abgeschlossen.")
    
    # -----------------------------------------------------
    # DATEN SPEICHERN FÜR ADMIN
    # -----------------------------------------------------
    csv_file = os.path.join(current_dir, "teilnehmer_ergebnisse.csv")
    
    # Daten vorbereiten
    ergebnis_daten = {
        "Zeitstempel": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Name": teilnehmer_name if teilnehmer_name else "Anonym",
        "IT-Punkte": it_punkte,
        "IT-Prozent": prozent,
        "Praktisch": lernstil_punkte["praktisch"],
        "Analytisch": lernstil_punkte["analytisch"],
        "Visuell": lernstil_punkte["visuell"],
        "Sozial": lernstil_punkte["sozial"],
        "Strukturiert": lernstil_punkte["strukturiert"],
        "Flexibel": lernstil_punkte["flexibel"],
        "Dominanter Lernstil": dominant.capitalize(),
        "Sekundaerer Lernstil": zweit.capitalize()
    }
    
    # CSV-Datei erstellen oder erweitern
    file_exists = os.path.exists(csv_file)
    with open(csv_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=ergebnis_daten.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(ergebnis_daten)
    
    st.info("✅ Deine Ergebnisse wurden gespeichert!")

    # ---------------------------------------------------------
    # PDF EXPORT
    # ---------------------------------------------------------
    from fpdf import FPDF

    def create_pdf_report(it_score, it_total, lernstil_dict, dominant, zweit, name):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Titel
        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, txt="Auswertung - IT & Lernstil", ln=True, align="C")
        pdf.ln(5)
        
        # Name des Teilnehmers
        if name:
            pdf.set_font("Arial", "B", 12)
            pdf.cell(200, 8, txt=f"Teilnehmer: {name}", ln=True)
            pdf.ln(3)

        # IT-Teil
        pdf.set_font("Arial", "B", 14)
        pdf.cell(200, 10, txt="IT-Vorwissen", ln=True)
        pdf.set_font("Arial", size=12)
        prozent_pdf = round((it_score / it_total) * 100)
        pdf.cell(200, 8, txt=f"Punkte: {it_score} von {it_total} ({prozent_pdf}%)", ln=True)

        # Lernstil-Teil
        pdf.ln(5)
        pdf.set_font("Arial", "B", 14)
        pdf.cell(200, 10, txt="Lernstil-Profil", ln=True)
        pdf.set_font("Arial", size=12)

        for stil, wert in lernstil_dict.items():
            pdf.cell(200, 8, txt=f"{stil.capitalize()}: {wert} Punkte", ln=True)

        pdf.ln(3)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 8, txt=f"Dominanter Lernstil: {dominant.capitalize()}", ln=True)
        pdf.cell(200, 8, txt=f"Sekundaerer Lernstil: {zweit.capitalize()}", ln=True)

        # Empfehlung
        empfehlungen_pdf = {
            "praktisch": "Lernt am besten durch Ausprobieren und praktische Uebungen.",
            "analytisch": "Profitiert von Erklaerungen, Konzepten und Hintergrundwissen.",
            "visuell": "Merkt sich Inhalte besonders gut ueber Bilder und Videos.",
            "sozial": "Lernt stark im Austausch mit anderen.",
            "strukturiert": "Braucht klare Ziele, Plaene und Schritt-fuer-Schritt-Anleitungen.",
            "flexibel": "Lernt gut in offenen, kreativen Situationen."
        }

        pdf.ln(5)
        pdf.set_font("Arial", "B", 14)
        pdf.cell(200, 10, txt="Empfehlung", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 8, empfehlungen_pdf[dominant])

        return bytes(pdf.output(dest="S"))

    # PDF-Download Button
    st.markdown("---")
    pdf_bytes = create_pdf_report(
        it_score=it_punkte,
        it_total=18,
        lernstil_dict=lernstil_punkte,
        dominant=dominant,
        zweit=zweit,
        name=teilnehmer_name
    )

    st.download_button(
        label="📄 PDF herunterladen",
        data=pdf_bytes,
        file_name="Auswertung_IT_Lernstil.pdf",
        mime="application/pdf"
    )
