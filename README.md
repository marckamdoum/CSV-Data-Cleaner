# CSV-Data-Cleaner
Ein interaktives Tool zur Bereinigung, Typanpassung und Export von CSV-Daten mit moderner Benutzeroberfläche in Streamlit. Nutzer:innen können eine CSV-Datei hochladen, den Datentyp für jede Spalte festlegen, Dubletten und fehlende Werte entfernen – und anschließend die bereinigte Datei als CSV herunterladen.
# Feature
📤 CSV-Upload über Web-GUI

📊 Vorschau und Analyse der hochgeladenen Daten

⚙️ Auswahl von Datentypen pro Spalte (int, float, string)

🧹 Automatische Bereinigung (Duplikate entfernen, NaNs filtern)

📥 Export der bereinigten Datei als CSV

📄 Logging zur Nachverfolgung des Prozesses

#🛠️ Verwendete Technologien
Streamlit – für die GUI

Pandas – für Datenanalyse

Python Logging – zur Protokollierung

clean_data()-Funktion in eigener Datei für Wiederverwendbarkeit

# Start 
pip install -r requirements.txt
streamlit run app.py

# Screen-shot App
<img width="1782" height="520" alt="image_cleaner" src="https://github.com/user-attachments/assets/4ddccb6c-6af2-41e9-892f-043094615757" />
<img width="1787" height="672" alt="image1_cleaner" src="https://github.com/user-attachments/assets/33143242-e88e-426e-a803-8c5a3d6afa6c" />
<img width="1811" height="887" alt="image3_cleaner" src="https://github.com/user-attachments/assets/666b9988-5c30-45d8-a003-ece01062cd8f" />
<img width="440" height="323" alt="image4_cleaner" src="https://github.com/user-attachments/assets/a0c12164-bc8d-4b2a-9738-3c497342d0c2" />





