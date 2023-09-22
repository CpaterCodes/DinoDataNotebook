from pandas import DataFrame


def with_lengths(df: DataFrame) -> DataFrame:
    df['length_m'] = df["length"].apply(convert_length)
    return df.drop(columns=['length'])


def convert_length(length: str) -> float:
    try:
        return float(str(length)[:-1])
    except:
        return 0.0


def with_periods(df: DataFrame) -> DataFrame:
    df[['epoch', 'period', 'mya_lower_bound', 'mya_upper_bound']] = df['period'].str.extract(
        '(\w+)\s(\w+)\s(\d+)-(\d+)\smillion\syears\sago', expand=True
    )
    df['mya_lower_bound'] = df['mya_lower_bound'].apply(convert_mya)
    df['mya_upper_bound'] = df['mya_upper_bound'].apply(convert_mya)
    return df


def convert_mya(mya: str) -> int:
    try:
        return int(mya)
    except:
        return 0