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

if admin_mode and admin_password == "Berserker":
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
st.info("""ℹ️ **Wichtig:** Dieser Test dient **nicht zur Bewertung**! Es geht nicht darum, alles richtig zu haben. 
Wir möchten nur einschätzen, von welchem Grundwissen wir für die Schulung ausgehen können. 
Bitte antworte ehrlich und **ohne Google oder KI-Hilfe** – nur so können wir die Schulung optimal auf dich abstimmen!""")

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
        "Weiß ich nicht",
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
        "Weiß ich nicht",
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
        "Weiß ich nicht",
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
        "Weiß ich nicht",
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
        "Weiß ich nicht",
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
        "Weiß ich nicht",
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
        "Weiß ich nicht",
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
        "Weiß ich nicht",
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
        "Weiß ich nicht",
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
        "Weiß ich nicht",
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
        "Weiß ich nicht",
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
        "Weiß ich nicht",
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
        "Weiß ich nicht",
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
        "Weiß ich nicht",
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
        "Weiß ich nicht",
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
        "Weiß ich nicht",
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
        "Weiß ich nicht",
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
        "Weiß ich nicht",
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

st.markdown("---")
st.info("✨ **Jetzt kommen wir vom fachlichen Teil zur Lernstil-Analyse!** Beantworte die folgenden Fragen spontan aus dem Bauch heraus, ohne lange nachzudenken.")
st.header("🎨 Lernstil‑Analyse")

# Frage 1
ls1 = st.radio(
    "1. Wie gehst du an neue Themen heran?",
    [
        "Bitte auswählen...",
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
if ls1 != "Bitte auswählen...":
    lernstil_punkte[mapping1[ls1]] += 1

# Frage 2
ls2 = st.radio(
    "2. Was motiviert dich beim Lernen?",
    [
        "Bitte auswählen...",
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
if ls2 != "Bitte auswählen...":
    lernstil_punkte[mapping2[ls2]] += 1

# Frage 3
ls3 = st.radio(
    "3. Wie gehst du mit schwierigen Aufgaben um?",
    [
        "Bitte auswählen...",
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
if ls3 != "Bitte auswählen...":
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

# =========================================================
# PROFESSIONELLE TEXTBAUSTEINE FÜR AUSWERTUNGEN
# =========================================================

def get_it_level_text(prozent, punkte, gesamt):
    """Generiert professionelle IT-Auswertung basierend auf Punktzahl"""
    
    if prozent >= 90:
        level = "Experte"
        farbe = "success"
        beschreibung = f"""
        **Glückwunsch!** Mit {punkte} von {gesamt} Punkten ({prozent}%) zeigst du ein **ausgezeichnetes IT-Grundwissen**. 
        
        Du verfügst über ein fundiertes Verständnis von Netzwerkinfrastrukturen, Serverdiensten und 
        IT-Sicherheitskonzepten. Begriffe wie DHCP, DNS, Active Directory und Virtualisierung sind dir 
        vertraut und du kennst deren praktische Anwendung.
        
        **Deine Stärken:**
        - Sehr gutes Verständnis von Netzwerkprotokollen und -diensten
        - Fundiertes Wissen über Serverinfrastruktur und Verwaltung
        - Ausgeprägtes Bewusstsein für IT-Sicherheit
        - Solides Hardwareverständnis
        
        **Empfehlung für die Schulung:**
        Du bist optimal vorbereitet und kannst direkt mit fortgeschrittenen Themen starten. Die Schulung 
        wird für dich vor allem eine Vertiefung und praktische Anwendung sein. Du kannst als Multiplikator 
        für andere Teilnehmende fungieren und von komplexeren Szenarien profitieren.
        """
    elif prozent >= 75:
        level = "Fortgeschritten Plus"
        farbe = "success"
        beschreibung = f"""
        **Sehr gut!** Mit {punkte} von {gesamt} Punkten ({prozent}%) verfügst du über **solides IT-Grundwissen**.
        
        Du hast ein gutes Verständnis für die wichtigsten IT-Konzepte und kannst mit vielen Fachbegriffen 
        bereits etwas anfangen. Dein Wissen bildet eine hervorragende Grundlage für die kommende Schulung.
        
        **Deine Stärken:**
        - Gutes Verständnis grundlegender Netzwerkkonzepte
        - Solide Kenntnisse über gängige IT-Infrastruktur
        - Grundlegendes Sicherheitsbewusstsein vorhanden
        
        **Entwicklungspotenzial:**
        - Vertiefung einzelner Spezialthemen (z.B. Virtualisierung, Cloud-Services)
        - Praktische Anwendung des theoretischen Wissens
        - Erweiterte Sicherheitskonzepte
        
        **Empfehlung für die Schulung:**
        Du bist gut vorbereitet! In der Schulung können wir auf deinem Wissen aufbauen und direkt in die 
        praktische Anwendung einsteigen. Kleine Wissenslücken schließen wir gemeinsam.
        """
    elif prozent >= 60:
        level = "Fortgeschritten"
        farbe = "info"
        beschreibung = f"""
        **Gut gemacht!** Mit {punkte} von {gesamt} Punkten ({prozent}%) zeigst du **ordentliches IT-Basiswissen**.
        
        Du verfügst über grundlegende IT-Kenntnisse und bist mit einigen wichtigen Konzepten bereits vertraut. 
        Das ist eine gute Ausgangsbasis, auf der wir in der Schulung aufbauen können.
        
        **Deine Stärken:**
        - Grundverständnis wichtiger IT-Konzepte vorhanden
        - Erste Erfahrungen mit Netzwerk- und Serverumgebungen
        - Motivation zur Weiterentwicklung erkennbar
        
        **Entwicklungsbereiche:**
        - Vertiefung des Netzwerkverständnisses (Protokolle, Dienste)
        - Erweiterte Kenntnisse über Serverinfrastruktur
        - Stärkung des IT-Sicherheitsbewusstseins
        - Praktische Anwendung theoretischer Konzepte
        
        **Empfehlung für die Schulung:**
        Du bringst eine solide Basis mit! Wir werden gemeinsam deine Kenntnisse systematisch erweitern und 
        durch viele praktische Übungen vertiefen. Konzentriere dich besonders auf die Vernetzung der einzelnen 
        Themen und deren praktische Anwendung.
        """
    elif prozent >= 45:
        level = "Basis Plus"
        farbe = "info"
        beschreibung = f"""
        Mit {punkte} von {gesamt} Punkten ({prozent}%) verfügst du über **grundlegende IT-Kenntnisse**.
        
        Du hast bereits erste Berührungspunkte mit IT-Themen gehabt und kennst einige Grundkonzepte. 
        Das ist ein guter Anfang! In der Schulung werden wir diese Basis systematisch ausbauen.
        
        **Deine bisherigen Kenntnisse:**
        - Erste Grundkenntnisse in IT-Bereichen vorhanden
        - Einige Fachbegriffe sind bereits bekannt
        - Interesse an IT-Themen ist erkennbar
        
        **Lernfelder für die Schulung:**
        - Systematischer Aufbau von Netzwerkgrundlagen
        - Verständnis für Serverinfrastruktur und -dienste
        - IT-Sicherheitskonzepte und Best Practices
        - Hardware-Komponenten und deren Zusammenspiel
        - Praktische Übungen zur Festigung
        
        **Empfehlung für die Schulung:**
        Keine Sorge – die Schulung ist genau für deinen Kenntnisstand konzipiert! Wir starten mit den 
        Grundlagen und bauen systematisch darauf auf. Stelle aktiv Fragen und nutze die praktischen Übungen, 
        um dein Verständnis zu vertiefen. Tipp: Bereite dich vor, indem du dich mit grundlegenden Begriffen 
        wie IP-Adresse, DNS und Firewall vertraut machst.
        """
    elif prozent >= 30:
        level = "Einsteiger Plus"
        farbe = "warning"
        beschreibung = f"""
        Mit {punkte} von {gesamt} Punkten ({prozent}%) startest du mit **grundlegenden Einstiegskenntnissen**.
        
        Viele IT-Konzepte sind dir noch neu – das ist völlig in Ordnung! Die Schulung ist darauf ausgelegt, 
        auch ohne große Vorkenntnisse den Einstieg zu ermöglichen.
        
        **Dein aktueller Stand:**
        - Einzelne IT-Begriffe sind bekannt
        - Alltagserfahrung mit Computern und Internet vorhanden
        - Bereitschaft, Neues zu lernen
        
        **Deine Lernziele für die Schulung:**
        - Grundverständnis für Netzwerke entwickeln (Was ist eine IP-Adresse? Wie funktioniert das Internet?)
        - Wichtige Serverdienste kennenlernen (DNS, DHCP, Active Directory)
        - IT-Sicherheit verstehen (Firewall, HTTPS, sichere Passwörter)
        - Hardware-Grundlagen erfassen (CPU, RAM, Speicher)
        - Praktische Kompetenzen durch Übungen aufbauen
        
        **Empfehlung für die Schulung:**
        Du erhältst in der Schulung eine umfassende Einführung in alle relevanten Themen. Plane etwas mehr 
        Zeit für Vor- und Nachbereitung ein. Nutze zusätzliche Lernmaterialien und scheue dich nicht, Fragen 
        zu stellen – es gibt keine dummen Fragen! 
        
        **Tipp:** Schaue dir vor Schulungsbeginn YouTube-Videos zu Grundthemen an (z.B. "Was ist eine IP-Adresse?", 
        "Wie funktioniert das Internet?") – das erleichtert dir den Einstieg erheblich.
        """
    else:  # < 30%
        level = "Einsteiger"
        farbe = "warning"
        beschreibung = f"""
        Mit {punkte} von {gesamt} Punkten ({prozent}%) beginnst du als **IT-Einsteiger**.
        
        Die IT-Welt ist für dich größtenteils Neuland – aber genau deshalb bist du hier! Jeder Experte hat 
        einmal als Einsteiger begonnen. Die Schulung wird dich Schritt für Schritt an die Themen heranführen.
        
        **Deine Ausgangssituation:**
        - IT-Fachbegriffe sind weitgehend neu
        - Bisher wenig Berührung mit technischen IT-Themen
        - Motivation, die IT-Welt kennenzulernen
        
        **Das wirst du in der Schulung lernen:**
        - IT-Grundlagen von Grund auf verstehen
        - Netzwerkkonzepte einfach erklärt bekommen
        - Praktische Übungen mit intensiver Betreuung
        - Serverdienste und deren Bedeutung kennenlernen
        - IT-Sicherheit im Alltag anwenden können
        
        **Wichtige Empfehlungen:**
        1. **Vorbereitung ist alles:** Nutze die Zeit vor der Schulung, um dich mit Grundbegriffen vertraut zu machen
        2. **Zusätzliche Ressourcen:** Schaue dir Einführungsvideos auf YouTube an (z.B. "IT für Anfänger")
        3. **Fragen stellen:** Es gibt keine dummen Fragen – nur wer fragt, lernt!
        4. **Praktisch üben:** Nutze jede Gelegenheit für Hands-on-Erfahrungen
        5. **Zeit einplanen:** Rechne mit etwas mehr Lern- und Übungszeit
        6. **Lernpartner suchen:** Tausche dich mit anderen Teilnehmenden aus
        
        **Unser Versprechen:** Die Schulung ist so konzipiert, dass auch Einsteiger alle Inhalte verstehen 
        können. Du erhältst bei Bedarf zusätzliche Unterstützung und Übungsmaterial. Mit Engagement und 
        Durchhaltevermögen wirst du am Ende einen großen Sprung gemacht haben!
        """
    
    return level, farbe, beschreibung


def get_lernstil_text(dominant, zweit, punkte_dict):
    """Generiert professionelle Lernstil-Auswertung"""
    
    # Detaillierte Beschreibungen für jeden Lernstil
    lernstil_beschreibungen = {
        "praktisch": {
            "titel": "🔧 Praktisch-Haptischer Lerntyp",
            "profil": """
            Du bist ein **praktisch orientierter Lerner** – Learning by Doing ist dein Motto! 
            Du verstehst Konzepte am besten, wenn du sie selbst ausprobieren und anfassen kannst.
            """,
            "staerken": [
                "Lernt besonders effektiv durch praktische Übungen und Experimente",
                "Behält Inhalte durch eigenes Ausprobieren am besten",
                "Liebt Hands-on-Labs und direkte Anwendung",
                "Versteht komplexe Zusammenhänge durch praktisches Tun",
                "Motiviert durch sichtbare Erfolgserlebnisse"
            ],
            "lernmethoden": [
                "**Labor-Übungen:** Nutze jede Gelegenheit für praktische Übungen",
                "**Trial and Error:** Probiere Dinge aus, auch wenn du noch nicht alles verstehst",
                "**Eigene Projekte:** Setze Gelerntes sofort in eigenen kleinen Projekten um",
                "**Simulationen:** Nutze virtuelle Umgebungen zum Experimentieren",
                "**Hands-on-Sessions:** Bevorzuge Schulungen mit hohem Praxisanteil"
            ],
            "tipps": [
                "Fordere praktische Übungen ein – dein Lernerfolg steht und fällt damit",
                "Richte dir eine Testumgebung ein, wo du gefahrlos experimentieren kannst",
                "Dokumentiere deine praktischen Erfahrungen als Lerntagebuch",
                "Suche nach YouTube-Tutorials, die zum Mitmachen anregen"
            ]
        },
        "analytisch": {
            "titel": "🧠 Analytisch-Logischer Lerntyp",
            "profil": """
            Du bist ein **analytischer Denker** – du willst verstehen, WARUM etwas funktioniert, 
            nicht nur WIE. Zusammenhänge und Hintergrundwissen sind dir wichtig.
            """,
            "staerken": [
                "Versteht komplexe Konzepte durch logische Analyse",
                "Erfasst Zusammenhänge und Systematiken besonders gut",
                "Lernt gerne durch Erklärungen und Hintergrundwissen",
                "Kann Gelerntes gut strukturieren und kategorisieren",
                "Hinterfragt kritisch und will Dinge tiefgehend verstehen"
            ],
            "lernmethoden": [
                "**Konzepte verstehen:** Vertiefe dich in theoretische Grundlagen",
                "**Mind Maps:** Erstelle Strukturdiagramme und Zusammenhangskarten",
                "**Systematische Notizen:** Schreibe ausführliche, strukturierte Mitschriften",
                "**Fachbücher:** Nutze Lehrbücher und technische Dokumentationen",
                "**Analyse-Sessions:** Nimm dir Zeit, Konzepte zu durchdenken und zu hinterfragen"
            ],
            "tipps": [
                "Fordere Erklärungen für das 'Warum' hinter den Konzepten",
                "Erstelle eigene Zusammenfassungen und Konzeptdiagramme",
                "Suche nach wissenschaftlichen Artikeln und technischen White Papers",
                "Plane Denkzeit ein – Reflexion ist für dich essentiell"
            ]
        },
        "visuell": {
            "titel": "👁️ Visuell-Grafischer Lerntyp",
            "profil": """
            Du bist ein **visueller Lerner** – ein Bild sagt mehr als tausend Worte! 
            Du merkst dir Inhalte am besten über Bilder, Diagramme und grafische Darstellungen.
            """,
            "staerken": [
                "Verarbeitet Informationen besonders gut über visuelle Kanäle",
                "Behält Diagramme, Grafiken und Bilder ausgezeichnet",
                "Kann komplexe Zusammenhänge durch Visualisierung erfassen",
                "Profitiert stark von Farbcodierung und grafischer Strukturierung",
                "Erstellt gerne eigene Skizzen und visuelle Notizen"
            ],
            "lernmethoden": [
                "**Diagramme zeichnen:** Erstelle eigene Netzwerkdiagramme und Infografiken",
                "**Video-Tutorials:** Nutze YouTube und Videoplattformen als Hauptlernquelle",
                "**Mind Maps:** Arbeite mit visuellen Strukturierungstechniken",
                "**Farbcodierung:** Nutze Farben zum Kategorisieren und Merken",
                "**Screenshots:** Dokumentiere Arbeitsschritte visuell"
            ],
            "tipps": [
                "Zeichne Netzwerkstrukturen und IT-Architekturen selbst auf",
                "Nutze Tools wie draw.io oder Lucidchart für Diagramme",
                "Arbeite mit Post-its und visuellen Kanban-Boards",
                "Erstelle Infografiken zu komplexen Themen"
            ]
        },
        "sozial": {
            "titel": "👥 Sozial-Kommunikativer Lerntyp",
            "profil": """
            Du bist ein **sozialer Lerner** – der Austausch mit anderen ist dein Lernturbo! 
            Durch Diskussionen, Erklären und gemeinsames Lernen festigst du dein Wissen.
            """,
            "staerken": [
                "Lernt besonders effektiv im Austausch mit anderen",
                "Versteht Konzepte gut durch Diskussionen und Erklären",
                "Profitiert stark von Gruppenarbeit und Teamlearning",
                "Kann andere motivieren und mitreißen",
                "Lernt durch Lehren – erklärt gerne anderen"
            ],
            "lernmethoden": [
                "**Lerngruppen:** Schließe dich mit anderen Teilnehmenden zusammen",
                "**Peer-Teaching:** Erkläre anderen, was du gelernt hast",
                "**Diskussionsforen:** Nutze Online-Communities und Foren aktiv",
                "**Pair Programming:** Arbeite in der IT mit einem Partner zusammen",
                "**Study Buddies:** Suche dir einen festen Lernpartner"
            ],
            "tipps": [
                "Gründe eine Lerngruppe oder tritt einer bei",
                "Nutze Discord, Slack oder Teams für kontinuierlichen Austausch",
                "Erkläre Konzepte anderen – dadurch festigst du dein eigenes Wissen",
                "Suche aktiv das Gespräch mit Trainern und erfahrenen IT-lern"
            ]
        },
        "strukturiert": {
            "titel": "📋 Strukturiert-Systematischer Lerntyp",
            "profil": """
            Du bist ein **strukturierter Lerner** – klare Pläne, Schritt-für-Schritt-Anleitungen 
            und systematischer Aufbau sind dir wichtig. Du liebst Ordnung und Übersichtlichkeit.
            """,
            "staerken": [
                "Lernt am besten mit klaren Lernplänen und Zielvorgaben",
                "Profitiert von strukturierten Schritt-für-Schritt-Anleitungen",
                "Kann gut nach Checklisten und Prozessen arbeiten",
                "Behält strukturierte Inhalte besonders gut",
                "Organisiert Lernmaterial systematisch und übersichtlich"
            ],
            "lernmethoden": [
                "**Lernpläne erstellen:** Plane deine Lerneinheiten detailliert vor",
                "**Checklisten:** Arbeite mit To-Do-Listen und Fortschrittsmarkern",
                "**Strukturierte Notizen:** Nutze Gliederungen und Nummerierungen",
                "**Standard Operating Procedures:** Erstelle SOPs für wiederkehrende Aufgaben",
                "**Zeitmanagement:** Plane feste Lernzeiten mit klaren Zielen ein"
            ],
            "tipps": [
                "Erstelle dir einen detaillierten Schulungs- und Lernplan",
                "Nutze Tools wie Notion, OneNote oder Trello zur Organisation",
                "Arbeite Kapitel für Kapitel systematisch durch",
                "Definiere klare Meilensteine und Erfolgskriterien"
            ]
        },
        "flexibel": {
            "titel": "🎨 Flexibel-Kreativer Lerntyp",
            "profil": """
            Du bist ein **flexibler Lerner** – du liebst Abwechslung und lernst gut in offenen, 
            kreativen Situationen. Spontanität und verschiedene Herangehensweisen motivieren dich.
            """,
            "staerken": [
                "Lernt gut in offenen, explorativen Situationen",
                "Profitiert von Abwechslung und verschiedenen Lernmethoden",
                "Kann sich schnell auf neue Situationen einstellen",
                "Findet kreative Lösungswege",
                "Motiviert durch Vielfalt und Spontanität"
            ],
            "lernmethoden": [
                "**Methodenmix:** Kombiniere verschiedene Lernformen (Videos, Texte, Übungen)",
                "**Freies Experimentieren:** Erlaube dir, eigene Wege zu gehen",
                "**Projekbasiertes Lernen:** Arbeite an eigenen, freien Projekten",
                "**Gamification:** Nutze spielerische Lernansätze",
                "**Spontane Sessions:** Lerne dann, wenn die Motivation da ist"
            ],
            "tipps": [
                "Variiere deine Lernmethoden regelmäßig, um Motivation aufrechtzuerhalten",
                "Setze dir flexible Lernziele, die Raum für Kreativität lassen",
                "Nutze verschiedene Plattformen und Ressourcen parallel",
                "Erlaube dir, auch mal 'Umwege' zu gehen – sie führen oft zu tieferem Verständnis"
            ]
        }
    }
    
    dominant_info = lernstil_beschreibungen[dominant]
    zweit_info = lernstil_beschreibungen[zweit]
    
    # Kombinationsanalyse
    kombination_text = f"""
    ### 🔄 Deine Lernstil-Kombination: {dominant.capitalize()} + {zweit.capitalize()}
    
    Deine Kombination aus **{dominant}** (dominant) und **{zweit}** (sekundär) ist besonders interessant:
    
    Du lernst hauptsächlich {dominant}, nutzt aber auch Elemente des {zweit}en Lernens. 
    Diese Kombination macht dich vielseitig und anpassungsfähig. Nutze beide Stile aktiv, 
    um deinen Lernerfolg zu maximieren!
    
    **Empfohlene Lernstrategie:** 
    Starte mit {dominant}en Methoden (hier fühlst du dich am wohlsten), ergänze dann mit 
    {zweit}en Elementen für zusätzliche Perspektiven und Vertiefung.
    """
    
    return dominant_info, zweit_info, kombination_text


if st.button("📊 Gesamtauswertung anzeigen"):
    st.header("📈 Deine Professionelle Auswertung")

    # -----------------------------------------------------
    # IT‑AUSWERTUNG MIT TEXTBAUSTEINEN
    # -----------------------------------------------------
    st.subheader("🧠 IT‑Vorwissen – Detaillierte Analyse")

    gesamt_it = 18  # Anzahl deiner IT‑Fragen
    prozent = round((it_punkte / gesamt_it) * 100)

    # Professionelle Auswertung generieren
    level, farbe, beschreibung = get_it_level_text(prozent, it_punkte, gesamt_it)
    
    # Anzeige
    st.metric(label="Erreichte Punktzahl", value=f"{it_punkte} / {gesamt_it}", delta=f"{prozent}%")
    
    if farbe == "success":
        st.success(f"**Level: {level}**")
    elif farbe == "info":
        st.info(f"**Level: {level}**")
    elif farbe == "warning":
        st.warning(f"**Level: {level}**")
    
    st.markdown(beschreibung)

    st.markdown("---")

    # -----------------------------------------------------
    # LERNSTIL‑AUSWERTUNG MIT TEXTBAUSTEINEN
    # -----------------------------------------------------
    st.subheader("🎨 Lernstil‑Profil – Detaillierte Analyse")

    # Dominanter und sekundärer Lernstil ermitteln
    dominant = max(lernstil_punkte, key=lernstil_punkte.get)
    sorted_styles = sorted(lernstil_punkte.items(), key=lambda x: x[1], reverse=True)
    zweit = sorted_styles[1][0]

    # Professionelle Auswertung generieren
    dominant_info, zweit_info, kombination_text = get_lernstil_text(dominant, zweit, lernstil_punkte)
    
    # Übersicht der Punkteverteilung
    st.markdown("#### 📊 Deine Lernstil-Verteilung:")
    col1, col2, col3 = st.columns(3)
    
    sorted_punkte = sorted(lernstil_punkte.items(), key=lambda x: x[1], reverse=True)
    for idx, (stil, wert) in enumerate(sorted_punkte):
        col = [col1, col2, col3][idx % 3]
        with col:
            emoji = {"praktisch": "🔧", "analytisch": "🧠", "visuell": "👁️", 
                     "sozial": "👥", "strukturiert": "📋", "flexibel": "🎨"}[stil]
            st.metric(label=f"{emoji} {stil.capitalize()}", value=f"{wert} Punkte")
    
    st.markdown("---")
    
    # Dominanter Lernstil - ausführlich
    st.markdown(f"## {dominant_info['titel']}")
    st.success(f"**Dies ist dein dominanter Lernstil!**")
    st.markdown(dominant_info['profil'])
    
    with st.expander("💪 Deine Stärken", expanded=True):
        for staerke in dominant_info['staerken']:
            st.markdown(f"- {staerke}")
    
    with st.expander("📚 Optimale Lernmethoden für dich", expanded=True):
        for methode in dominant_info['lernmethoden']:
            st.markdown(f"- {methode}")
    
    with st.expander("💡 Praktische Tipps", expanded=True):
        for tipp in dominant_info['tipps']:
            st.markdown(f"- {tipp}")
    
    st.markdown("---")
    
    # Sekundärer Lernstil - kompakt
    st.markdown(f"### {zweit_info['titel']}")
    st.info(f"**Dies ist dein sekundärer Lernstil**")
    st.markdown(f"{zweit_info['profil']}")
    
    with st.expander(f"Zusätzliche {zweit.capitalize()}e Methoden"):
        st.markdown("**Ergänzende Lernmethoden:**")
        for methode in zweit_info['lernmethoden'][:3]:
            st.markdown(f"- {methode}")
    
    st.markdown("---")
    
    # Kombinations-Analyse
    st.markdown(kombination_text)

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
    # ZUSAMMENFASSUNG FÜR TRAINER:INNEN (KOMPAKT)
    # -----------------------------------------------------
    st.subheader("📘 Zusammenfassung für Trainer:innen")
    
    st.markdown(f"""
    ### Teilnehmer-Profil
    
    **IT-Kompetenz:**
    - **Level:** {level} ({prozent}%)
    - **Punktzahl:** {it_punkte} von {gesamt_it}
    
    **Lernstil-Profil:**
    - **Primär:** {dominant.capitalize()} ({lernstil_punkte[dominant]} Punkte)
    - **Sekundär:** {zweit.capitalize()} ({lernstil_punkte[zweit]} Punkte)
    
    **Didaktische Empfehlungen:**
    """)
    
    # Spezifische Trainer-Tipps basierend auf Lernstil
    trainer_tipps = {
        "praktisch": "Maximale Praxisanteile einplanen, Hands-on-Labs bevorzugen, weniger Theorie-Blöcke",
        "analytisch": "Konzeptionelle Erklärungen vertiefen, 'Warum'-Fragen zulassen, Zusammenhänge betonen",
        "visuell": "Diagramme und Visualisierungen nutzen, Whiteboard-Sessions, grafische Dokumentation",
        "sozial": "Gruppenarbeiten fördern, Peer-Learning ermöglichen, Diskussionsrunden einbauen",
        "strukturiert": "Klare Agenda kommunizieren, Schritt-für-Schritt vorgehen, Checklisten bereitstellen",
        "flexibel": "Methodenmix anbieten, explorative Aufgaben stellen, kreative Freiräume schaffen"
    }
    
    st.markdown(f"- **Für {dominant} Lernende:** {trainer_tipps[dominant]}")
    st.markdown(f"- **Ergänzend ({zweit}):** {trainer_tipps[zweit]}")
    
    if prozent < 45:
        st.warning("⚠️ **Hinweis:** Dieser TN benötigt voraussichtlich zusätzliche Unterstützung bei IT-Grundlagen.")
    
    st.success("✅ Auswertung abgeschlossen. Ergebnisse wurden gespeichert.")
    
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
    # PDF EXPORT MIT PROFESSIONELLEN TEXTBAUSTEINEN
    # ---------------------------------------------------------
    from fpdf import FPDF

    def create_pdf_report(it_score, it_total, lernstil_dict, dominant, zweit, name, prozent_val, level_text):
        pdf = FPDF()
        pdf.add_page()
        
        # Titel
        pdf.set_font("Arial", "B", 18)
        pdf.cell(0, 12, txt="Professionelle Auswertung", ln=True, align="C")
        pdf.cell(0, 8, txt="IT-Vorwissen & Lernstil-Analyse", ln=True, align="C")
        pdf.ln(8)
        
        # Name des Teilnehmers
        if name:
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 8, txt=f"Teilnehmer:in: {name}", ln=True)
            pdf.set_font("Arial", "", 10)
            pdf.cell(0, 6, txt=f"Datum: {datetime.now().strftime('%d.%m.%Y')}", ln=True)
            pdf.ln(5)

        # IT-VORWISSEN SEKTION
        pdf.set_font("Arial", "B", 14)
        pdf.set_fill_color(70, 130, 180)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, 10, txt="IT-Vorwissen", ln=True, fill=True)
        pdf.set_text_color(0, 0, 0)
        pdf.ln(3)
        
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 8, txt=f"Ergebnis: {it_score} von {it_total} Punkten ({prozent_val}%)", ln=True)
        pdf.cell(0, 8, txt=f"Level: {level_text}", ln=True)
        pdf.ln(3)
        
        # IT-Level Beschreibung (gekürzt für PDF)
        pdf.set_font("Arial", "", 10)
        if prozent_val >= 90:
            text = "Ausgezeichnetes IT-Grundwissen. Sehr gutes Verstaendnis von Netzwerk-infrastrukturen, Serverdiensten und IT-Sicherheit. Optimal vorbereitet fuer die Schulung."
        elif prozent_val >= 75:
            text = "Solides IT-Grundwissen. Gutes Verstaendnis der wichtigsten IT-Konzepte. Hervorragende Grundlage fuer die Schulung."
        elif prozent_val >= 60:
            text = "Ordentliches IT-Basiswissen. Grundverstaendnis wichtiger Konzepte vorhanden. Gute Ausgangsbasis fuer die Schulung."
        elif prozent_val >= 45:
            text = "Grundlegende IT-Kenntnisse. Erste Beruehrungspunkte mit IT-Themen vorhanden. Die Schulung wird diese Basis systematisch ausbauen."
        elif prozent_val >= 30:
            text = "Grundlegende Einstiegskenntnisse. Viele Konzepte sind noch neu. Die Schulung ist darauf ausgelegt, auch ohne grosse Vorkenntnisse den Einstieg zu ermoeglichen."
        else:
            text = "IT-Einsteiger. Die IT-Welt ist groesstenteils Neuland. Die Schulung fuehrt Schritt fuer Schritt an die Themen heran."
        
        pdf.multi_cell(0, 6, txt=text)
        pdf.ln(8)

        # LERNSTIL SEKTION
        pdf.set_font("Arial", "B", 14)
        pdf.set_fill_color(255, 140, 0)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, 10, txt="Lernstil-Profil", ln=True, fill=True)
        pdf.set_text_color(0, 0, 0)
        pdf.ln(3)

        # Lernstil-Punkte
        pdf.set_font("Arial", "", 10)
        for stil, wert in sorted(lernstil_dict.items(), key=lambda x: x[1], reverse=True):
            marker = " (Dominant)" if stil == dominant else " (Sekundaer)" if stil == zweit else ""
            pdf.cell(0, 6, txt=f"  {stil.capitalize()}: {wert} Punkte{marker}", ln=True)
        
        pdf.ln(5)
        pdf.set_font("Arial", "B", 11)
        pdf.cell(0, 7, txt=f"Dominanter Lernstil: {dominant.capitalize()}", ln=True)
        pdf.cell(0, 7, txt=f"Sekundaerer Lernstil: {zweit.capitalize()}", ln=True)
        pdf.ln(3)

        # Lernstil-Beschreibungen (kompakt für PDF)
        lernstil_pdf_texte = {
            "praktisch": "Praktisch-Haptischer Lerntyp: Lernt am besten durch Ausprobieren und praktische Uebungen. Learning by Doing ist das Motto. Profitiert von Hands-on-Labs, eigenen Projekten und direkter Anwendung.",
            "analytisch": "Analytisch-Logischer Lerntyp: Versteht durch logische Analyse und moechte das 'Warum' verstehen. Profitiert von Erklaerungen, Konzepten und systematischem Hintergrundwissen.",
            "visuell": "Visuell-Grafischer Lerntyp: Merkt sich Inhalte besonders gut ueber Bilder, Diagramme und grafische Darstellungen. Profitiert von Visualisierungen, Videos und Mind Maps.",
            "sozial": "Sozial-Kommunikativer Lerntyp: Der Austausch mit anderen ist der Lernturbo. Lernt besonders effektiv durch Diskussionen, Gruppenarbeit und das Erklaeren an andere.",
            "strukturiert": "Strukturiert-Systematischer Lerntyp: Klare Plaene und Schritt-fuer-Schritt-Anleitungen sind wichtig. Profitiert von Lernplaenen, Checklisten und systematischem Aufbau.",
            "flexibel": "Flexibel-Kreativer Lerntyp: Liebt Abwechslung und lernt gut in offenen, kreativen Situationen. Profitiert von Methodenmix, freiem Experimentieren und Vielfalt."
        }
        
        pdf.set_font("Arial", "", 10)
        pdf.multi_cell(0, 6, txt=lernstil_pdf_texte[dominant])
        pdf.ln(3)
        
        # Neue Seite für Empfehlungen
        pdf.add_page()
        
        pdf.set_font("Arial", "B", 14)
        pdf.set_fill_color(60, 179, 113)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, 10, txt="Empfehlungen & Lernstrategien", ln=True, fill=True)
        pdf.set_text_color(0, 0, 0)
        pdf.ln(5)
        
        # Lernmethoden-Empfehlungen
        lernmethoden_empfehlungen = {
            "praktisch": [
                "Nutze jede Gelegenheit fuer praktische Uebungen und Hands-on-Labs",
                "Richte dir eine Testumgebung ein zum gefahrlosen Experimentieren",
                "Setze Gelerntes sofort in eigenen kleinen Projekten um",
                "Dokumentiere praktische Erfahrungen als Lerntagebuch"
            ],
            "analytisch": [
                "Vertiefe dich in theoretische Grundlagen und Konzepte",
                "Erstelle Mind Maps und Strukturdiagramme",
                "Schreibe ausfuehrliche, strukturierte Mitschriften",
                "Fordere Erklaerungen fuer das 'Warum' hinter Konzepten"
            ],
            "visuell": [
                "Zeichne Netzwerkstrukturen und IT-Architekturen selbst auf",
                "Nutze Video-Tutorials als Hauptlernquelle",
                "Arbeite mit Farbcodierung und visuellen Strukturen",
                "Erstelle eigene Infografiken zu komplexen Themen"
            ],
            "sozial": [
                "Gruende oder tritt einer Lerngruppe bei",
                "Erklaere anderen, was du gelernt hast (Peer-Teaching)",
                "Nutze Discord, Slack oder Teams fuer kontinuierlichen Austausch",
                "Suche aktiv das Gespraech mit Trainern und erfahrenen IT-lern"
            ],
            "strukturiert": [
                "Erstelle einen detaillierten Schulungs- und Lernplan",
                "Nutze Tools wie Notion oder Trello zur Organisation",
                "Arbeite Kapitel fuer Kapitel systematisch durch",
                "Definiere klare Meilensteine und Erfolgskriterien"
            ],
            "flexibel": [
                "Variiere deine Lernmethoden regelmaessig",
                "Setze flexible Lernziele mit Raum fuer Kreativitaet",
                "Nutze verschiedene Plattformen und Ressourcen parallel",
                "Erlaube dir, auch mal 'Umwege' zu gehen"
            ]
        }
        
        pdf.set_font("Arial", "B", 11)
        pdf.cell(0, 7, txt=f"Optimale Lernmethoden fuer {dominant} Lernende:", ln=True)
        pdf.set_font("Arial", "", 10)
        for methode in lernmethoden_empfehlungen[dominant]:
            pdf.multi_cell(0, 6, txt=f"  - {methode}")
        
        pdf.ln(5)
        pdf.set_font("Arial", "B", 11)
        pdf.cell(0, 7, txt=f"Ergaenzende {zweit} Methoden:", ln=True)
        pdf.set_font("Arial", "", 10)
        for methode in lernmethoden_empfehlungen[zweit][:2]:
            pdf.multi_cell(0, 6, txt=f"  - {methode}")
        
        pdf.ln(8)
        
        # Fazit
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 8, txt="Fazit", ln=True)
        pdf.set_font("Arial", "", 10)
        pdf.multi_cell(0, 6, txt=f"Diese Auswertung zeigt dein individuelles IT-Niveau und deinen persoenlichen Lernstil. Nutze die Empfehlungen, um deinen Lernprozess optimal zu gestalten. Deine Kombination aus {dominant}em und {zweit}em Lernen macht dich vielseitig - nutze beide Stile aktiv!")
        
        return bytes(pdf.output(dest="S"))

    # PDF-Download Button
    st.markdown("---")
    pdf_bytes = create_pdf_report(
        it_score=it_punkte,
        it_total=gesamt_it,
        lernstil_dict=lernstil_punkte,
        dominant=dominant,
        zweit=zweit,
        name=teilnehmer_name,
        prozent_val=prozent,
        level_text=level
    )

    st.download_button(
        label="📄 Professionelle Auswertung als PDF herunterladen",
        data=pdf_bytes,
        file_name=f"IT_Lernstil_Auswertung_{teilnehmer_name if teilnehmer_name else 'Teilnehmer'}_{datetime.now().strftime('%Y%m%d')}.pdf",
        mime="application/pdf"
    )
