import numpy as np
import matplotlib.pyplot as plt

from pop_model_code import (
    malthus,
    logistic_continuous,
    ricker,
    beverton_holt,
    stochastic_logistic,
    allee_discrete,
    leslie_matrix_example,
)


T = np.linspace(0, 25, 500)
exp_curve = malthus(50, 0.22, T)
log_curve = logistic_continuous(50, 0.22, 1000, T)

plt.figure()
plt.plot(T, exp_curve, label="Мальтус")
plt.plot(T, log_curve, label="Ферхюльст, K=1000")
plt.legend()
plt.xlabel("t")
plt.ylabel("N(t)")
plt.title("Порівняння експоненційної та логістичної моделей")
plt.savefig("fig31.png", dpi=200)

capacity_values = [300, 600, 1000, 1500]
plt.figure()
for k in capacity_values:
    plt.plot(T, logistic_continuous(50, 0.22, k, T), label=f"K={k}")
plt.legend()
plt.xlabel("t")
plt.ylabel("N(t)")
plt.title("Вплив місткості середовища K")
plt.savefig("fig32.png", dpi=200)

r_values = [0.10, 0.18, 0.28, 0.40]
plt.figure()
for r in r_values:
    plt.plot(T, logistic_continuous(50, r, 1000, T), label=f"r={r}")
plt.legend()
plt.xlabel("t")
plt.ylabel("N(t)")
plt.title("Вплив коефіцієнта росту r")
plt.savefig("fig33.png", dpi=200)

steps = np.arange(41)
plt.figure()
plt.plot(steps, ricker(30, 1.8, 100, 40), label="Рікер")
plt.plot(steps, beverton_holt(30, 2.2, 100, 40), label="Бевертон-Голт")
plt.legend()
plt.xlabel("k")
plt.ylabel("N_k")
plt.title("Порівняння моделей Рікера та Бевертона–Голта")
plt.savefig("fig34.png", dpi=200)

plt.figure()
for r in [1.2, 1.8, 2.4, 3.0]:
    plt.plot(steps, ricker(30, r, 100, 40), label=f"r={r}")
plt.legend()
plt.xlabel("k")
plt.ylabel("N_k")
plt.title("Зміна режимів у моделі Рікера")
plt.savefig("fig35.png", dpi=200)

leslie_matrix, leslie_history = leslie_matrix_example(15)
plt.figure()
plt.plot(leslie_history[:, 0], label="молодь")
plt.plot(leslie_history[:, 1], label="репродуктивна група")
plt.plot(leslie_history[:, 2], label="старші особини")
plt.plot(leslie_history.sum(axis=1), label="усього")
plt.legend()
plt.xlabel("k")
plt.ylabel("чисельність")
plt.title("Динаміка вікової структури за моделлю Леслі")
plt.savefig("fig36.png", dpi=200)

plt.figure()
for seed in [1, 2, 3, 4, 5, 6, 7]:
    plt.plot(stochastic_logistic(40, 0.22, 900, 80, 0.06, seed))
plt.xlabel("k")
plt.ylabel("N_k")
plt.title("Стохастичні траєкторії логістичної моделі")
plt.savefig("fig37.png", dpi=200)

plt.figure()
for n0 in [30, 60, 90, 150]:
    plt.plot(allee_discrete(n0, 1.4, 800, 80, 60), label=f"N0={n0}")
plt.legend()
plt.xlabel("k")
plt.ylabel("N_k")
plt.title("Пороговий ефект Аллі")
plt.savefig("fig38.png", dpi=200)
