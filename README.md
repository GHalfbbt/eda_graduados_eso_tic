# 📊 **EDA: Graduados en ESO según habilidades TIC**

## **Análisis de Habilidades TIC en España (INE, API 43698)**

🎓 Proyecto Académico: Brecha Digital Educativa

🏛️ **Fuente**: Instituto Nacional de Estadística (INE):

INE / INEbase — *Encuesta de Transición Educativa-Formativa e Inserción Laboral*  
**Catálogo**: <https://datos.gob.es/es/catalogo/ea0010587-graduados-en-eso-segun-sus-habilidades-tic-por-sexo-ccaa-de-estudio-y-tipo-de-centro-identificador-api-43698>  

Descargas directas: CSV ';' <https://www.ine.es/jaxi/files/tpx/csv_bdsc/43698.csv>

📅 Fecha: 2024

---

Este repositorio contiene un ejemplo de **Análisis Exploratorio de Datos (EDA)** pensado como guía para instalar dependencias con uv, cargar los datos de un dataset, abrir el proyecto en JupyterLab y ejecutar el notebook paso a paso.

Se busca también la práctica de análisis y limpieza de datos, estadísticas descriptivas y visualización con Python, pandas, matplotlib y seaborn, principalmente, además de el flujo de trabajo con uv y JupyterLab. Los resultados son demostrativos y con fines estrictamente educativos.

NOTA: Dentro del código del notebook de esta guía, se pueden ver algunas de las herramientas estadísticas usadas en este código con fines académicos.

---

> Objetivo: limpiar y analizar el dataset de *Graduados en ESO según sus habilidades TIC* por **sexo**, **CCAA** y **tipo de centro**, y producir insights accionable para un público ejecutivo.

## Entregables
- **Informe ejecutivo (Markdown):** `reports/executive_report.md`
- **Informe ejecutivo (STORYTELLING: Los datos hablan):** `reports/Informe_Ejecutivo_EDA_INE43698.pdf`
- **Informe ejecutivo automático (PDF con portada + índice + comentarios):** `reports/executive_report.pdf`
- **Mapas:** `reports/maps/`
- **Figuras:** `reports/figures/`
- **Dashboards:** `reports/plotly/`

> Abre el PDF aquí: [reports/Informe_Ejecutivo_EDA_INE43698.pdf](reports/Informe_Ejecutivo_EDA_INE43698.pdf)

---

## **Qué vas a encontrar en este notebook**

- Gestión de CSV.
- Diccionario de datos y chequeos de calidad (duplicados, tipos, nulos).
- Limpieza (estandarización de nombres, tratamiento de `Total` y `No consta`).
- Estadística descriptiva (univariado/bivariado/multivariado).
- Detección de outliers (IQR) y justificación.
- Visualizaciones con `pandas`, `matplotlib`, `seaborn` y `plotly`.
- Mapa coroplético por CCAA (base OpenStreetMap) con `folium` + `geopandas`.
- Hypothesis testing (chi-cuadrado, test de proporciones).
- Storytelling + **generación automática** de un *executive report* en `reports/executive_report.md`.

**CONTEXTO DEL PROYECTO:**
==========================
Este análisis exploratorio examina las habilidades TIC de graduados en ESO en España, analizando las diferencias por género, comunidad autónoma y tipo de centro educativo.

OBJETIVO:
- Identificar brechas digitales en educación
- Proporcionar insights para políticas educativas
- Analizar diferencias territoriales y de género
- Generar recomendaciones estratégicas

METODOLOGÍA:
1. Carga y exploración inicial de datos
2. Limpieza y preprocesamiento
3. Análisis exploratorio (univariado, bivariado, multivariado)
4. Pruebas de hipótesis estadísticas
5. Visualizaciones avanzadas
6. Storytelling y conclusiones

---

## 1) Requisitos

- **Python 3.9+** (recomendado >= 3.10–3.12).
- **uv** instalado y accesible en tu PATH. Comprueba:
  ```bash
  uv --version
  ```
- **Git Bash** (y opcional VS Code).
- **Datos del INE** (CSV ;) en: data/raw/Dataset_INE_Graduados_ESO_43698.csv

Descarga del INE: https://www.ine.es/jaxi/files/tpx/csv_bdsc/43698.csv
Luego muévelo a (después de haber creado la estructura del proyecto): 
```bash
mkdir -p data/raw
mv /ruta/descarga/43698.csv data/raw/Dataset_INE_Graduados_ESO_43698.csv
```

---

## 2) Clonación del proyecto

```bash
  git clone https://github.com/TU_USUARIO/eda_graduados_eso_tic.git
  cd eda_graduados_eso_tic
```

---

## 3) Instalación de dependencias

Con uv (recomendado):

  ### Opción A — Proyecto con `pyproject.toml` 
  Si este repositorio ya trae un `pyproject.toml`, simplemente:
  
  - Crea el entorno
    ```bash
    uv venv .venv
    ```

  - Instala dependencias declaradas en el TOML
  ```bash
  uv sync
  ```
  > Si **no** existe `pyproject.toml` y quieres crearlo con uv:
  > ```bash
  > uv init --name eda_graduados_eso_tic
  > uv add pandas numpy matplotlib seaborn plotly folium scipy scikit-learn reportlab jupyterlab ipykernel 
  > uv sync
  > ```

  ### Opción B — `requirements.txt` (alternativa clásica)
  Si prefieres gestionar deps con `requirements.txt`:

  ```bash
  uv venv .venv
  source .venv/Scripts/activate
  uv pip install -r requirements.txt
  ```
  ```bash
  uv venv .venv
  uv sync
  ```

  > Alternativa (pip):
  > ```bash
  > uvpython -m venv .venv && source .venv/Scripts/activate && pip install -r requirements.txt
  > ```

## 4) Opciones de ejecución

### Opción A — Notebook en JupyterLab
```bash
# activar entorno (si no usas uv run)
source .venv/Scripts/activate

# lanzar jupyter
uv run jupyter lab
# abre: notebooks/eda_graduados_eso_tic.ipynb
```

- Si no ves el kernel, créalo una vez:
```bash
uv run python -m ipykernel install --user --name=eda-eso-tic --display-name "Python (eda-eso-tic)"
```

· En el menú: Kernel → Change Kernel… → "Python (eda-eso-tic)"
· Run → Run All Cells para ejecutar todo el flujo y generar:
  - CSV limpio en data/processed/ine_43698_clean.csv
  - Figuras/Mapas/Dashboards en reports/**
  - Informe en reports/executive_report.pdf


### Opción B — Ejecutar todo el Notebook por terminal
```bash
uv run --active python scripts/run_notebook.py
```

Esto:
· Crea las carpetas necesarias (reports/**, data/processed)
· Ejecuta el notebook y guarda una copia en reports/notebooks/*.executed.ipynb
· Genera salidas en reports/**


### Opción C — Solo limpieza rápida del CSV
```bash
# Git Bash / cmd:
PYTHONPATH=src uv run python -m eda_eso_tic.main

# PowerShell:
$env:PYTHONPATH="src"; uv run python -m eda_eso_tic.main
```
Salida esperada: data/processed/ine_43698_clean.csv

Los gráficos aparecen **inline** (debajo de cada celda). Los CSV limpios se guardan en la carpeta del proyecto (p. ej. `../reports/tables/t_genero_datos.csv`, `../reports/plotly/brecha_genero_ccaa.html`).

---

## 5) Estructura recomendada del proyecto

```
eda_graduados_eso_tic/
├─ data/
│  ├─ raw/                      # Dataset original (no tocar)
│  │  └─ Dataset_INE_Graduados_ESO_43698.csv
│  └─ processed/
│     └─ ine_43698_clean.csv    # Dataset limpio generado
├─ notebooks/
│  └─ eda_graduados_eso_tic.ipynb   #notebook principal
│  └─ eda_graduados_eso_tic.py      #notebook si exportamos a .py
├─ reports/
│  ├─ figures/                  # Figuras PNG para el PDF
│  ├─ maps/                     # Folium HTML
│  ├─ plotly/                   # Dashboards HTML
│  ├─ executive_report.md
│  └─ executive_report.pdf
│  └─ Informe_Ejecutivo_EDA_INE43698.pdf # Informe Ejecutivo Storytelling
├─ src/
│  └─ eda_eso_tic/
│     ├─ __init__.py
│     ├─ main.py                # CLI para limpieza rápida
│     ├─ data_utils.py
│     └─ paths.py
├─ .venv/                       # (si usas venv local)
├─ .gitignore
├─ pyproject.toml               # (si usas uv)  ← opcional
├─ requirements.txt             # (si usas pip)
└─ README.md
```

---

**.gitignore** sugerido:
```bash
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class
*.pyo
*.pyd
*.egg-info/
.dist-info/
build/
dist/


# --- Python / Virtual entornos ---
.venv/
.uv/

# --- Jupyter / VSCode / OS ---
.ipynb_checkpoints/
.notebook_cache/
notebooks/.ipynb_checkpoints/
.vscode/
.DS_Store
Thumbs.db

# -------- Data --------
# Ignora todo lo generado y externo
data/processed/**
data/external/**


# Mantener sólo el CSV origina del INE (ajusta si usas otro nombre)
!data/raw/
data/raw/**
!data/raw/Dataset_INE_Graduados_ESO_43698.csv

# mantener directorios vacíos con .gitkeep
!data/processed/.gitkeep
!data/external/.gitkeep

# -------- Reports (generados)--------
# Ignora todo en reports por defecto..
reports/**
# ...pero permite el informe ejecutivo y su versión en Markdown
!reports/
!reports/executive_report.pdf
!reports/executive_report.md
!reports/Informe_Ejecutivo_EDA_INE43698.pdf
# ...y los directorios de tablas, figuras, mapas y plotly
!reports/tables/.gitkeep
!reports/figures/.gitkeep
!reports/maps/.gitkeep
!reports/plotly/.gitkeep

# Mantenemos fuera los artefactos pesados/volátiles
reports/figures/**
reports/maps/**
reports/plotly/**
reports/tables/**
reports/notebooks/**

# -------- Notebooks --------
notebooks/**
!notebooks/
!notebooks/eda_graduados_eso_tic.ipynb

# -------- Scripts --------
scripts/**
!scripts/
!scripts/.gitkeep

# -------- Src --------
src/**/__pycache__/

# --- Logs / temporales ---
*.log
*.tmp
*.cache/
```

> Si no quieres subir los CSV, ni ficheros generados, añade `data/` completo al `.gitignore` y no los incluyas en `git add`.

---

## 6) ¿Necesito guardar imágenes en `../reports/...` `reports/figures/` `reports/maps/`?

**No es obligatorio.** Las salidas de las celdas (gráficas incluidas) quedan **embebidas** dentro del `.ipynb`, por lo que **GitHub** las muestra al visualizar el notebook.  
Solo guarda PNGs en `figures/` si:
- Quieres reutilizarlos (README, informes externos).
- Te preocupa el tamaño del `.ipynb` o su render en GitHub en notebooks muy pesados.
- Prefieres versionar imágenes sueltas.


Puedes insertar un PNG guardado en una **celda Markdown** y hacer la referencia al PNG generado en el propio README.md con:
```markdown
![Informe_ejecutivo](../reports/Informe_Ejecutivo_EDA_INE43698.pdf)
```