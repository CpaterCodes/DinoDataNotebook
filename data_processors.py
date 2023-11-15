from pandas import DataFrame
from re import findall


def with_lengths(df: DataFrame) -> DataFrame:
    df['length_m'] = df["length"].apply(convert_length)
    return df.drop(columns=['length'])


def convert_length(length: str) -> float:
    try:
        return float(str(length)[:-1])
    except:
        return 0.0


def with_epochs(df: DataFrame) -> DataFrame:
    df[['epoch', 'mya_lower', 'mya_upper']] = df['period'].apply(
        period_data
    ).to_list()
    df['mya_lower'] = df['mya_lower'].apply(convert_mya)
    df['mya_upper'] = df['mya_upper'].apply(convert_mya)
    return df.drop(columns=['period'])


def with_epoch_nums(df: DataFrame, epochs: list[str]) -> DataFrame:
    return df


EPOCH_SET = [
    f"{lateness} {period}"
    for lateness in ["Early", "Mid", "Late"]
    for period in ["Triassic", "Jurassic", "Cretaceous"]
] 


def period_data(period: str) -> tuple:
    period = str(period)
    epoch, lower, upper = "N/A", 0, 0

    for epoch_option in EPOCH_SET:
        if epoch_option in period: epoch = epoch_option
    
    bounds = findall(r'\d+', period)
    if bounds != []:
        lower = bounds[0]
        upper = bounds[-1]

    return epoch, lower, upper


def convert_mya(mya: str) -> int:
    try:
        return int(mya)
    except:
        return 0
