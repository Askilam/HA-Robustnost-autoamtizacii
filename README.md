# HA-Robustnost-automatizacii

Bakalárska práca  
**Home Assistant: Nástroj na zlepšenie spoľahlivosti automatizácií**  
*(Work in Progress)*

---

## Popis

Tento projekt implementuje nástroj na analýzu Home Assistant automatizácií.
Cieľom je identifikovať sémantické chyby a potenciálne problémy, ktoré môžu viesť
k nespoľahlivému správaniu automatizácií v inteligentnej domácnosti.

Nástroj spracúva YAML konfigurácie, prevádza ich do interného modelu (IR) a
vykonáva množinu sémantických kontrol na základe definovaných pravidiel.

---

## Požiadavky

- Python **3.10+** (testované na 3.10 a 3.12)
- Virtuálne prostredie (odporúčané)
- Operačný systém: Linux / Windows / macOS

---

## Inštalácia

### 1. Vytvorenie virtuálneho prostredia
``` bash
python -m venv venv
```

### 2. Aktivácia virtuálneho prostredia

#### Linux 
```bash
source venv/bin/activate
```

#### Windows
``` bash
venv\Scripts\activate
```

### 3. Inštalácia závislostí
```bash
pip install -r requirements.txt
```

### 4. Spustenie nástroja

#### Na spustenie analýzy automatizácie použite:
``` bash
python main.py
```

#### Predvolený vstupný súbor:
```
automatizacia.yaml
```

#### Výsledok analýzy sa uloží do súboru:
```
parsed_output.txt
```
### 5. Spustenie testov:
```bash
pytest -v
```


