from pathlib import Path
from eda_eso_tic.data_utils import load_raw, clean_ine_43698

def main():
    raw = Path('data/raw/Dataset_INE_Graduados_ESO_43698.csv')
    out = Path('data/processed/ine_43698_clean.csv')
    df = load_raw(raw)
    dfc = clean_ine_43698(df)
    out.parent.mkdir(parents=True, exist_ok=True)
    dfc.to_csv(out, index=False)
    print(f'Guardado: {out} ({len(dfc):,} filas)')

if __name__ == '__main__':
    main()

