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
- **Informe ejecutivo (PDF con portada + índice + comentarios):** `reports/executive_report.pdf`
- **Mapas:** `reports/maps/`
- **Figuras:** `reports/figures/`
- **Dashboards:** `reports/plotly/`

> Abre el PDF aquí: [reports/executive_report.pdf](reports/executive_report.pdf)

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

- **Git Bash** (puedes usar VS Code si quieres).
- **uv** instalado y accesible en tu PATH. Comprueba:
  ```bash
  uv --version
  ```
- **Python 3.9+** (recomendado >= 3.10–3.12).
- **JupyterLab** (se instala como dependencia).
- **Descarga directa** de los datos fomato **CSV ';'** en ubicación local relative_path="../raw/" del INE ó datos.gob.es serie; (INE, API 43698)

## 2) Instalación de dependencias

### Opción A — Proyecto con `pyproject.toml` (recomendada con uv)
Si este repositorio ya trae un `pyproject.toml`, simplemente:

```bash
# 1) Clona el repo
git clone https://github.com/TU_USUARIO/eda_graduados_eso_tic.git
cd eda_graduados_eso_tic

# 2) Crea el entorno
uv venv .venv

# 3) Instala dependencias declaradas en el TOML
uv sync
```

> Si **no** existe `pyproject.toml` y quieres crearlo con uv:
> ```bash
> uv init --name eda_graduados_eso_tic
> uv add pandas matplotlib seaborn scipy scikit-learn jupyterlab ipykernel kaggle
> uv sync
> ```

### Opción B — `requirements.txt` (alternativa clásica)
Si prefieres gestionar deps con `requirements.txt`:

```bash
uv venv .venv
source .venv/Scripts/activate
uv pip install -r requirements.txt
```

### Opción C — pip
```bash
python -m venv .venv
source .venv/Scripts/activate    # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install jupyterlab
```

> **No mezcles** A y B en el mismo proyecto. Elige un método y quédate con él.

## 3) Datos de Carga (descarga y preparación)
1) **Descarga directa** de los datos fomato **CSV ';'** en ubicación local relative_path="../data/raw/" del **INE** ó **datos.gob.es**:
- **Fuente:**
    ```bash 
    <https://www.ine.es/jaxi/files/tpx/csv_bdsc/43698.csv>** (para descargar los CSV). 
    
    ó bien:
    https://datos.gob.es/es/catalogo/ea0010587-graduados-en-eso-segun-sus-habilidades-tic-por-sexo-ccaa-de-estudio-y-tipo-de-centro-identificador-api-43698
    ```

2) Colocar en (../data/raw/Dataset_INE_Graduados_ESO_43698.csv):
   ```bash
   mkdir -p ../data/raw/
   mv /c/Users/USUARIO/Downloads/43698.csv ../data/raw/Dataset_INE_Graduados_ESO_43698.csv

   chmod 600 ./data/raw/Dataset_INE_Graduados_ESO_43698.csv  # No siempre es necesario
   ```
    - **Descarga directa** de los datos fomato **CSV ';'** en ubicación local relative_path="../raw/" del INE ó datos.gob.es


## 4) Ejecutar el proyecto:

- **Notebook** en JupyterLab

```bash
# Lanza JupyterLab
# (Con venv activado:)
source .venv/Scripts/activate
jupyter-lab
# (O sin activar el venv:)
# uv run jupyter lab

# abre: notebooks/eda_graduados_eso_tic.ipynb
```

En JupyterLab:
1. Abre el notebook: `notebooks/eda_graduados_eso_tic.ipynb`.
2. Selecciona el **kernel** del entorno (menú **Kernel → Change Kernel…**).  
   - Si no aparece, créalo una vez:
     ```bash
     python -m ipykernel install --user --name=eda-eso-tic --display-name "Python (eda-eso-tic)"
     ```
     Cierra y vuelve a abrir JupyterLab.
3. Ejecuta todo: **Run → Run All Cells** (o usa `Shift+Enter` por celda).

Los gráficos aparecen **inline** (debajo de cada celda). Los CSV limpios se guardan en la carpeta del proyecto (p. ej. `../reports/tables/t_genero_datos.csv`, `../reports/plotly/brecha_genero_ccaa.html`).

- **CLI (limpieza rápida) del dataset**
```bash
# desde la raíz del repo
PYTHONPATH=src python -m eda_eso_tic.main
```

---

## 5) Estructura recomendada del proyecto

```
eda_graduados_eso_tic/
├─ data/
│  ├─ raw/                      # Dataset original (no tocar)
│  │  └─ Dataset_INE_Graduados_ESO_43698.csv
│  └─ processed/
│     └─ ine_43698_clean.csv    # Dataset limpio
├─ notebooks/
│  └─ eda_graduados_eso_tic.ipynb   #notebook principal
├─ reports/
│  ├─ figures/                  # Figuras PNG para el PDF
│  ├─ maps/                     # Folium HTML
│  ├─ plotly/                   # Dashboards HTML
│  ├─ executive_report.md
│  └─ executive_report.pdf
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
```
.venv/
.uv/
__pycache__/
.ipynb_checkpoints/

# dejamos que se suba el fichero informe_ejecutivo.pdf
!reports/nforme_ejecutivo.pdf.pdf
reports/*.pdf
reports/plotly/*.html
reports/maps/*.html
data/processed/*.csv
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
![Informe_ejecutivo](../reports/executive_report.pdf)
```