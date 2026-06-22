import math
from dataclasses import dataclass

import numpy as np


@dataclass
class Scenario:
    n0: float
    r: float
    k: float | None = None
    a: float | None = None


def malthus(n0: float, r: float, t: np.ndarray) -> np.ndarray:
    return n0 * np.exp(r * t)


def logistic_continuous(n0: float, r: float, k: float, t: np.ndarray) -> np.ndarray:
    return k / (1 + ((k - n0) / n0) * np.exp(-r * t))


def logistic_discrete(n0: float, r: float, k: float, steps: int) -> np.ndarray:
    out = np.zeros(steps + 1, dtype=float)
    out[0] = n0
    for i in range(steps):
        out[i + 1] = out[i] + r * out[i] * (1 - out[i] / k)
        out[i + 1] = max(out[i + 1], 0.0)
    return out


def ricker(n0: float, r: float, k: float, steps: int) -> np.ndarray:
    out = np.zeros(steps + 1, dtype=float)
    out[0] = n0
    for i in range(steps):
        out[i + 1] = out[i] * math.exp(r * (1 - out[i] / k))
        out[i + 1] = max(out[i + 1], 0.0)
    return out


def beverton_holt(n0: float, r: float, k: float, steps: int) -> np.ndarray:
    out = np.zeros(steps + 1, dtype=float)
    out[0] = n0
    for i in range(steps):
        out[i + 1] = (r * out[i]) / (1 + (r - 1) * out[i] / k)
        out[i + 1] = max(out[i + 1], 0.0)
    return out


def allee_discrete(n0: float, r: float, k: float, a: float, steps: int) -> np.ndarray:
    out = np.zeros(steps + 1, dtype=float)
    out[0] = n0
    for i in range(steps):
        growth = r * out[i] * (1 - out[i] / k) * (out[i] / a - 1)
        out[i + 1] = max(out[i] + growth, 0.0)
    return out


def leslie_matrix_example(years: int = 20):
    leslie = np.array([
        [0.0, 1.15, 1.70],
        [0.55, 0.0, 0.0],
        [0.0, 0.70, 0.35],
    ])
    state = np.array([80.0, 50.0, 20.0])
    history = [state]
    for _ in range(years):
        state = leslie @ state
        history.append(state)
    history = np.array(history)
    return leslie, history


def stochastic_logistic(
    n0: float,
    r: float,
    k: float,
    steps: int,
    sigma: float,
    seed: int = 42,
) -> np.ndarray:
    rng = np.random.default_rng(seed)
    out = np.zeros(steps + 1, dtype=float)
    out[0] = n0
    for i in range(steps):
        noise = rng.normal(0.0, sigma)
        out[i + 1] = out[i] + (r + noise) * out[i] * (1 - out[i] / k)
        out[i + 1] = max(out[i + 1], 0.0)
    return out
