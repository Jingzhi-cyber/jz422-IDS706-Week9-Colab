from lib import read_dataset, summary_statistics


def test_read_dataset():
    df = read_dataset("hurricanes.csv")
    assert df is not None


def test_summary_statistics():
    df = read_dataset("hurricanes.csv")
    stats = summary_statistics(df)
    assert "mean" in stats
    assert "median" in stats
    assert "std_dev" in stats
