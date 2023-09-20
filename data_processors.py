
def convert_length(length: str) -> float:
    try:
        return float(str(length)[:-1])
    except:
        return 0.0