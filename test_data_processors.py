from data_processors import with_lengths, with_epochs
from pandas import DataFrame



def test_lengths_become_floats():
    
    length_dataframe = DataFrame({'length': ['10.0m', '0.5m', '103.2m']})
    
    length_m_dataframe = with_lengths(length_dataframe)

    assert('length_m' in length_m_dataframe.columns)
    assert('length' not in length_m_dataframe.columns)
    assert(list(length_m_dataframe['length_m']) == [10.0, 0.5, 103.2])


def test_null_lengths_handled():
    
    length_df_with_nulls = DataFrame({'length': ['', '']})
    length_m_df_with_nulls = with_lengths(length_df_with_nulls)

    assert(list(length_m_df_with_nulls['length_m']) == [0.0, 0.0])


def test_time_periods_converted():
    df_with_periods = DataFrame(
        {"period": [
            "Mid Jurassic 190-180 million years ago", 
            "Late Cretaceous 70-66 million years ago"
        ]}
    )
    df_with_epochs = with_epochs(df_with_periods)
    
    assert(list(df_with_epochs['epoch']) == ['Mid Jurassic', 'Late Cretaceous'])
    assert(list(df_with_epochs['mya_upper']) == [180, 66])
    assert(list(df_with_epochs['mya_lower']) == [190, 70])

def test_null_handling_for_time_periods():
    df_with_period_nulls = DataFrame(
        {"period": [
            "Mid Jurassic 170 million years ago",
            "Early Cretaceous",
            "USA",
            ""
        ]}
    )
    df_with_epoch_nulls = with_epochs(df_with_period_nulls)
    
    epochs, uppers, lowers = [list(df_with_epoch_nulls[col]) for col in ['epoch', 'mya_upper', 'mya_lower']]
    assert(epochs == ["Mid Jurassic", "Early Cretaceous", "", ""])
    assert(uppers == [170, 0, 0, 0])
    assert(lowers == [170, 0, 0, 0])
    