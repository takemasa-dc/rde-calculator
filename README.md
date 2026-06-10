# Response Distribution Entropy (RDE) Calculator

## Overview

This repository provides a lightweight Python implementation for calculating Response Distribution Entropy (RDE) from option-level response counts or proportions.

RDE is intended for descriptive item analysis of multiple-choice or selected-response items. It summarises how responses are distributed across available response options. A low RDE value indicates that responses are concentrated on a small number of options, whereas a high RDE value indicates that responses are more evenly distributed across options.

This implementation is designed for researchers, educators, and assessment developers who want to examine response distribution structure alongside conventional item statistics such as correct response rate and item difficulty.

## Definition

For item (j) with (m_j) response options, let (p_{jk}) denote the proportion of valid responses assigned to option (k). RDE is defined as the Shannon entropy of the item response distribution, normalised by the theoretical maximum entropy for the number of available response options:

```math
RDE_j = \frac{-\sum_{k=1}^{m_j} p_{jk}\log(p_{jk})}{\log(m_j)}
```

Terms with (p_{jk} = 0) are treated as zero. The natural logarithm is used by default.

Because RDE is normalised by (\log(m_j)), it ranges from 0 to 1. This normalisation allows items with different numbers of response options to be compared more directly.

## Interpretation

RDE should be interpreted as a descriptive summary of response distribution structure.

* RDE close to 0: responses are concentrated on one or a small number of options.
* RDE close to 1: responses are distributed more evenly across available options.

RDE does not identify why a response distribution has a particular shape. A high RDE value may reflect heterogeneous reasoning, multiple attractive distractors, guessing, ambiguous options, or other item features. A low RDE value may reflect a highly attractive distractor, a common misconception, or non-functioning alternatives. RDE should therefore be used as a screening or descriptive index, not as a diagnostic statistic.

## Effective number of options

The repository also includes a function for calculating the effective number of options:

[
\exp(H_j)
]

where (H_j) is the unnormalised Shannon entropy of the response distribution. The effective number of options can be interpreted as the number of equally used options that would produce the same entropy.

## Installation

Clone this repository:

```bash
git clone https://github.com/your-username/rde-calculator.git
cd rde-calculator
```

The core functions require only Python and NumPy.

```bash
pip install numpy pandas
```

Pandas is only needed for CSV-based examples.

## Basic usage

### Calculate RDE from response counts

```python
from rde import calculate_rde, calculate_effective_options

counts = [50, 20, 20, 10]

rde = calculate_rde(counts)
effective_options = calculate_effective_options(counts)

print(rde)
print(effective_options)
```

### Calculate RDE from response proportions

```python
from rde import calculate_rde

proportions = [0.50, 0.20, 0.20, 0.10]

rde = calculate_rde(proportions)

print(rde)
```

The function accepts either counts or proportions. If counts are provided, they are internally converted to proportions.

## CSV input format

An example CSV file is included as `example.csv`.

Each row represents one item. Each option column contains the number or proportion of responses assigned to that option.

Example:

```csv
item_id,option_A,option_B,option_C,option_D
item_001,50,20,20,10
item_002,25,25,25,25
item_003,90,5,3,2
```

A simple CSV workflow is provided in `example_usage.py`.

## Example output

For each item, the output can include:

```text
item_id
n_options
RDE
effective_number_of_options
```

The exact output format can be modified depending on the user’s item analysis workflow.

## Relationship to other item statistics

RDE is not intended to replace correct response rate, item difficulty, distractor analysis, item response theory models, or other option-level analyses. Its purpose is to provide a compact summary of response-option distribution structure.

RDE may be useful for identifying items that warrant closer inspection. For example, two items may have similar correct response rates but different RDE values, indicating different patterns of response concentration or dispersion.

## Limitations

RDE is a descriptive index. It does not determine whether an item is good or bad, whether a distractor is functioning appropriately, or whether a particular misconception is present.

Interpretation of RDE should be combined with item content review, correct response rate, item difficulty, distractor analysis, and, where appropriate, respondent-level or model-based analyses.

## Citation

If you use this code, please cite the associated article or archived software release.

A Zenodo DOI will be added after the first public release.

## License

This project is released under the MIT License.
