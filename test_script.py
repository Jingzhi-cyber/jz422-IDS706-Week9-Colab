import data_analysis


def test_read_dataset():
    df = data_analysis.read_dataset("hurricanes.csv")
    assert df is not None


def test_summary_statistics():
    df = data_analysis.read_dataset("hurricanes.csv")
    stats = data_analysis.summary_statistics(df)
    assert "mean" in stats
    assert "median" in stats
    assert "std_dev" in stats
