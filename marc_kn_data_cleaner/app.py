import os
from pathlib import Path
import logging
import pandas as pd
import streamlit as st
from cleaned.cleaner import clean_data  # Deine eigene Reinigungsfunktion

# Arbeitsverzeichnis setzen
os.chdir(Path(__file__).parent)

# Logging einrichten
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)
logging.basicConfig(
    filename=log_dir / "data_cleaning.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    # Streamlit-Seiteneinstellungen
    st.set_page_config(page_title="CSV Data Cleaner", layout="wide")
    st.title(" CSV Data Cleaner")
    st.markdown(" **Lade deine CSV-Datei hoch, um die Daten zu bereinigen und zu exportieren.**")

    # CSV-Datei hochladen
    uploaded_file = st.file_uploader(" Wähle eine CSV-Datei", type="csv")

    if uploaded_file is not None:
        st.subheader(" Datenvorschau")

        # CSV-Datei lesen mit Fehlerbehandlung
        try:
            df = pd.read_csv(uploaded_file, encoding='utf-8')
        except UnicodeDecodeError:
            try:
                df = pd.read_csv(uploaded_file, encoding='latin1')
            except Exception as e:
                st.error(" Fehler beim Lesen der Datei.")
                logging.error(f"Fehler beim Lesen der CSV-Datei: {e}")
                return

        st.success(" Datei erfolgreich geladen.")
        st.write(" Spaltenübersicht:", df.columns.tolist())
        st.dataframe(df)

        # Datentyp-Auswahl pro Spalte
        st.subheader(" Spaltentypen festlegen")
        dtype_options = {'int': 'int64', 'float': 'float64', 'string': 'object'}
        column_types = {}

        for column in df.columns:
            selected_type = st.selectbox(
                f" Datentyp für Spalte '{column}'",
                options=list(dtype_options.keys()),
                key=column
            )
            column_types[column] = dtype_options[selected_type]

        # Bereinigung starten
        if st.button("🧹 Daten bereinigen"):
            try:
                cleaned_df = clean_data(df, column_types, remove_duplicates=True, remove_na=True)
                st.success(" Daten wurden erfolgreich bereinigt.")
                st.dataframe(cleaned_df)

                # Bereinigte Datei speichern
                output_dir = Path("cleaned")
                output_dir.mkdir(exist_ok=True)
                cleaned_file = output_dir / "cleaned_data.csv"
                cleaned_df.to_csv(cleaned_file, index=False)

                # Download-Link
                with open(cleaned_file, "rb") as f:
                    st.download_button(
                        label=" Bereinigte CSV herunterladen",
                        data=f.read(),
                        file_name="bereinigte_datei.csv",
                        mime="text/csv"
                    )

                logging.info("Datenbereinigung erfolgreich durchgeführt.")

            except Exception as e:
                st.error(" Fehler bei der Datenbereinigung.")
                logging.error(f"Fehler bei clean_data(): {e}")

if __name__ == "__main__":
    main()
