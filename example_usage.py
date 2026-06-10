```python
"""
Example usage of the Response Distribution Entropy (RDE) calculator.

This script reads option-level response counts or proportions from example.csv
and calculates RDE and the effective number of options for each item.
"""

import pandas as pd

from rde import calculate_rde, calculate_effective_options


def main():
    input_file = "example.csv"
    output_file = "example_output.csv"

    df = pd.read_csv(input_file)

    option_cols = [col for col in df.columns if col.startswith("option_")]

    results = []

    for _, row in df.iterrows():
        values = row[option_cols].values

        rde = calculate_rde(values)
        effective_options = calculate_effective_options(values)

        results.append(
            {
                "item_id": row["item_id"],
                "n_options": len(option_cols),
                "RDE": rde,
                "effective_number_of_options": effective_options,
            }
        )

    output = pd.DataFrame(results)

    print(output)

    output.to_csv(output_file, index=False)
    print(f"Saved output to {output_file}")


if __name__ == "__main__":
    main()
```
