# US_Data_scrape_morgenroutine
Dieses Programm dient dazu Daaten aus dem Netz auszulesen oder diese runter zu laden und daraus Markt relevante Daten abzuleiten oder einfach zu berechnen. 

Level 1 14.01.26 grobe struktur bilden

SYSTEM REQUIREMENTS
- 8–16 GB RAM
- SSD empfohlen
- 50–200 GB Speicherplatz
- Linux oder macOS bevorzugt, Windows mit WSL2 möglich

SOFTWARE REQUIREMENTS
- Python 3.11+
- Virtuelle Umgebung (venv oder uv)

PYTHON LIBRARIES
- polars
- pyarrow
- requests
- fastapi
- uvicorn
- pydantic
- tqdm
- python-dotenv

DATENQUELLEN (US-MARKT)
- Stooq Bulk Download (us.zip) für komplette US-Aktienhistorie
- NASDAQ Official Symbol Directory
- NYSE Official Symbol List
- AMEX Symbol List
- Optional: EODData (kostenlos, Registrierung nötig)

ARCHITEKTUR-MODULE
1. Loader Layer
   - Bulk Loader (Initial Load)
   - Daily Update Loader (inkrementelle Updates)

2. Storage Layer
   - Parquet-Dateien
   - Ordnerstruktur pro Börse und Symbol

3. Compute Layer
   - NH/NL Berechnung (252 Handelstage, Penny-Filter, pro Börse)
   - Breadth (Advance/Decline)
   - Volume-Breadth
   - AD-Lines
   - Regime-Module

4. API Layer
   - FastAPI Endpunkte für fertige Module

5. Config Layer
   - .env
   - Settings (Pfade, Parameter)

6. Optional: Orchestrierung
   - Cronjob oder Prefect

LOGISCHE REQUIREMENTS
- NH/NL: 252 Handelstage, Close > 1 USD Filter, pro Börse getrennt
- Breadth: Advancing, Declining, Unchanged
- Volume-Breadth: UpVolume, DownVolume, Ratio
- Delistings optional einbeziehen
- ETFs, ETNs, Preferreds, Warrants, SPACs herausfiltern

ORDNERSTRUKTUR
project/
  data/
    raw/
      us/
        nyse/
        nasdaq/
        amex/
    processed/
      nhnl/
      breadth/
      volume/
  loaders/
    bulk_loader.py
    daily_loader.py
  modules/
    nhnl.py
    breadth.py
    volume.py
    regime.py
  api/
    main.py
  config/
    settings.py
    .env
  utils/
    filters.py
    symbols.py
