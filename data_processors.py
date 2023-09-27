from pandas import DataFrame


def with_lengths(df: DataFrame) -> DataFrame:
    df['length_m'] = df["length"].apply(convert_length)
    return df.drop(columns=['length'])


def convert_length(length: str) -> float:
    try:
        return float(str(length)[:-1])
    except:
        return 0.0


def with_epochs(df: DataFrame) -> DataFrame:
    df[['epoch', 'mya_lower', 'mya_upper']] = df['period'].str.extract(
        r'(\w+\s\w+)\s(\d+)-(\d+)\smillion\syears\sago', expand=True
    )
    df['mya_lower'] = df['mya_lower'].apply(convert_mya)
    df['mya_upper'] = df['mya_upper'].apply(convert_mya)
    return df.drop(columns=['period'])


def convert_mya(mya: str) -> int:
    try:
        return int(mya)
    except:
        return 0