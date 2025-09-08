
from __future__ import annotations
import pandas as pd
import re

def load_raw(csv_path: str) -> pd.DataFrame:
    """Carga el CSV del INE (TPX 43698). Está separado por ';'.
    Devuelve el DataFrame tal cual.
    """
    return pd.read_csv(csv_path, sep=';', encoding='utf-8-sig')

def clean_ine_43698(df: pd.DataFrame) -> pd.DataFrame:
    """Limpieza y enriquecimiento del dataset:
    - Rellena CCAA faltante con '00 España' para los registros nacionales.
    - Elimina la col. 'Total Nacional' (no aporta variabilidad).
    - Separa código y nombre de CCAA en 'ccaa_cod' (int) y 'ccaa' (str).
    - Renombra 'Total' a 'valor' y calcula 'persons' con **escala dinámica por grupo**
      para evitar inconsistencias de unidad (ver notas).
    - Define categorías ordenadas para 'Sexo', 'Tipo de centro' y 'Habilidades TIC'.
    Notas sobre unidades:
      * En los ficheros JAXI de esta operación, los totales aparecen con formato tipo '64.118' y
        las categorías pueden mostrarse con valores que, empíricamente, son coherentes si
        consideramos que el total está en **miles de personas**, mientras que las categorías
        'No usuario de las TIC' y 'No consta' están en **personas**. Además, en CCAA de menor tamaño,
        las categorías principales pueden venir ya en **personas**.
      * Para robustez, elegimos automáticamente la escala (1 o 1000) que hace que la suma de
        ['Usuario experto','Usuario de nivel avanzado','Usuario de nivel básico'] se aproxime más
        al 'Total' del grupo. 'No usuario' y 'No consta' se tratan como personas.
    """
    df = df.copy()
    df['Comunidades y Ciudades Autónomas'] = df['Comunidades y Ciudades Autónomas'].fillna('00 España')
    df = df.drop(columns=['Total Nacional'])
    # Separar código y nombre de CCAA
    def split_ccaa(x: str):
        if x.startswith('00'):
            return (0, 'España')
        m = re.match(r'^(\d{2})\s+(.+)$', x)
        if m:
            return (int(m.group(1)), m.group(2))
        return (None, x)
    tmp = df['Comunidades y Ciudades Autónomas'].apply(split_ccaa)
    df['ccaa_cod'] = [t[0] for t in tmp]
    df['ccaa'] = [t[1] for t in tmp]

    df = df.rename(columns={'Total':'valor'})

    cats_main = ['Usuario experto','Usuario de nivel avanzado','Usuario de nivel básico']

    personas = []
    for keys, sub in df.groupby(['Comunidades y Ciudades Autónomas','Sexo','Tipo de centro'], sort=False):
        total_val = float(sub[sub['Habilidades TIC']=='Total']['valor'].iloc[0]) * 1000.0
        vals = sub[sub['Habilidades TIC'].isin(cats_main)]['valor'].astype(float).values
        sum_k1 = vals.sum()
        sum_k1000 = (vals*1000.0).sum()
        k = 1.0 if abs(sum_k1 - total_val) < abs(sum_k1000 - total_val) else 1000.0
        for _, row in sub.iterrows():
            cat = row['Habilidades TIC']
            v = float(row['valor'])
            if cat == 'Total':
                personas.append(total_val)
            elif cat in cats_main:
                personas.append(v * k)
            else:  # 'No usuario' / 'No consta' -> personas
                personas.append(v)

    df['personas'] = pd.Series(personas, index=df.index).round(0).astype('Int64')

    # Categóricas ordenadas
    sexo_cat = pd.CategoricalDtype(categories=['Ambos sexos','Hombres','Mujeres'], ordered=True)
    centro_cat = pd.CategoricalDtype(categories=['Total','Centro Público','Centro Privado'], ordered=True)
    hab_cat = pd.CategoricalDtype(categories=['Total','Usuario experto','Usuario de nivel avanzado','Usuario de nivel básico','No usuario de las TIC','No consta'], ordered=True)
    df['Sexo'] = df['Sexo'].astype(sexo_cat)
    df['Tipo de centro'] = df['Tipo de centro'].astype(centro_cat)
    df['Habilidades TIC'] = df['Habilidades TIC'].astype(hab_cat)

    df = df[['ccaa_cod','ccaa','Sexo','Tipo de centro','Habilidades TIC','valor','personas']]
    return df

def pivot_percentages(df: pd.DataFrame, filtro_sexo='Ambos sexos', filtro_centro='Total') -> pd.DataFrame:
    """Calcula porcentajes por CCAA para cada categoría de habilidad, normalizando por el valor de 'Total' del mismo grupo.
    Nota: los porcentajes pueden no sumar 100% si se incluye 'No consta'.
    """
    base = df[(df['Sexo']==filtro_sexo) & (df['Tipo de centro']==filtro_centro)]
    totales = base[base['Habilidades TIC']=='Total'][['ccaa_cod','ccaa','personas']].rename(columns={'personas':'personas_total'})
    partes = base[base['Habilidades TIC']!='Total'][['ccaa_cod','ccaa','Habilidades TIC','personas']]
    merged = partes.merge(totales, on=['ccaa_cod','ccaa'])
    merged['pct'] = 100 * (merged['personas'] / merged['personas_total'])
    tabla = merged.pivot_table(index=['ccaa_cod','ccaa'], columns='Habilidades TIC', values='pct', aggfunc='sum').reset_index().sort_values('ccaa_cod')
    return tabla
