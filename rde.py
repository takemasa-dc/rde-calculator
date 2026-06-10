from __future__ import annotations

import math
from typing import Iterable

import numpy as np


def _to_probabilities(values: Iterable[float]) -> np.ndarray:
    """
    Convert response counts or proportions to a probability vector.

    Parameters
    ----------
    values : Iterable[float]
        Response counts or response proportions for each option.

    Returns
    -------
    np.ndarray
        Probability vector summing to 1.

    Raises
    ------
    ValueError
        If values are empty, contain negative values, or sum to zero.
    """
    arr = np.asarray(list(values), dtype=float)

    if arr.size == 0:
        raise ValueError("Input values must not be empty.")

    if np.any(arr < 0):
        raise ValueError("Input values must not contain negative values.")

    total = arr.sum()

    if total <= 0:
        raise ValueError("Input values must sum to a positive value.")

    return arr / total


def calculate_entropy(values: Iterable[float]) -> float:
    """
    Calculate unnormalised Shannon entropy.

    Parameters
    ----------
    values : Iterable[float]
        Response counts or response proportions for each option.

    Returns
    -------
    float
        Shannon entropy using the natural logarithm.
    """
    p = _to_probabilities(values)
    p_nonzero = p[p > 0]

    return float(-np.sum(p_nonzero * np.log(p_nonzero)))


def calculate_rde(values: Iterable[float]) -> float:
    """
    Calculate Response Distribution Entropy (RDE).

    RDE is Shannon entropy normalised by the theoretical maximum entropy
    for the number of available response options.

    Parameters
    ----------
    values : Iterable[float]
        Response counts or response proportions for each option.

    Returns
    -------
    float
        Normalised RDE ranging from 0 to 1.

    Raises
    ------
    ValueError
        If fewer than two response options are provided.
    """
    p = _to_probabilities(values)
    n_options = p.size

    if n_options < 2:
        raise ValueError("RDE requires at least two response options.")

    entropy = calculate_entropy(p)
    max_entropy = math.log(n_options)

    return float(entropy / max_entropy)


def calculate_effective_options(values: Iterable[float]) -> float:
    """
    Calculate the effective number of response options.

    The effective number of options is exp(H), where H is the unnormalised
    Shannon entropy.

    Parameters
    ----------
    values : Iterable[float]
        Response counts or response proportions for each option.

    Returns
    -------
    float
        Effective number of response options.
    """
    entropy = calculate_entropy(values)

    return float(math.exp(entropy))
