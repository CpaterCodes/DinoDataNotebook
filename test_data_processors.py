from data_processors import with_lengths, with_periods
from pandas import DataFrame



def test_lengths_become_floats():
    
    length_dataframe = DataFrame.from_dict(
        [{'length': l} for l in ['10.0m', '0.5m', '103.2m']]
    )
    length_m_dataframe = with_lengths(length_dataframe)

    assert('length_m' in length_m_dataframe.columns)
    assert('length' not in length_m_dataframe.columns)
    assert(list(length_m_dataframe['length_m']) == [10.0, 0.5, 103.2])


def test_null_lengths_handled():
    
    length_df_with_nulls = DataFrame.from_dict(
        [{'length': l} for l in ['', '']]
    )
    length_m_df_with_nulls = with_lengths(length_df_with_nulls)

    assert(list(length_m_df_with_nulls['length_m']) == [0.0, 0.0])


def test_time_periods_converted():
    pass

