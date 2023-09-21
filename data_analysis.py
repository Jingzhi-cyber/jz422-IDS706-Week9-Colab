import lib

if __name__ == "__main__":
    # Replace this path with the path to your own CSV file
    file_path = "hurricanes.csv"

    df = lib.read_dataset(file_path)

    # Calculate summary statistics for the "Average" column
    stats = lib.summary_statistics(df[["Average"]])
    mean = stats["mean"]
    median = stats["median"]
    std_dev = stats["std_dev"]

    print("Mean:", mean)
    print("Median:", median)
    print("Standard Deviation:", std_dev)

    # Visualize the "Average" column
    lib.data_visualization_save(df, "Average")

    # Generate summary report
    with open("summary_report.md", "w", encoding="utf-8") as f:
        f.write("# Summary Report\n")
        f.write("## Descriptive Statistics\n")
        f.write(f"### Mean:\n{mean}\n")
        f.write(f"### Median:\n{median}\n")
        f.write(f"### Standard Deviation:\n{std_dev}\n")
