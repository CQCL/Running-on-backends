import numpy as np
from matplotlib import pyplot as plt


def plot_bars(counts, label, **kwargs):
    fig, ax = plt.subplots(figsize=(4, 3))

    # x_vals = kwargs.get("x_vals", None)
    x_ticks = range(len(counts))
    ax.bar(x_ticks, counts.values())
    # if x_vals is None:
    #     x_vals = [rf"$|{x[0]}{x[1]}\rangle$" for x in counts.keys()]

    # If yim given, set it

    x_tick_labels = kwargs.get("x_tick_labels", None)
    if x_tick_labels is None:
        x_tick_labels = [tuple_to_ket(x) for x in counts.keys()]

    x_tick_labels = [x_tick_labels[0]] + [""] * len(x_tick_labels[1:-1]) + [x_tick_labels[-1]]

    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_tick_labels, rotation=45, ha="center")

    ylim = kwargs.get("ylim", None)
    if ylim is not None:
        ax.set_ylim(ylim)

    ax.set_title(f"{label}")
    plt.tight_layout()

    return fig, ax


def plot_multiple_bars(all_counts, labels):
    n_qubits = len(list(all_counts[0].keys())[0])

    ideal_counts = all_counts[0]
    noisy_counts = all_counts[1]
    mitigated_counts = all_counts[2]

    # Fill in so every bitstring has a values, even if it's 0
    all_tuples = gen_tuples(n_qubits)
    all_ideal_counts = {k: ideal_counts.get(k, 0) for k in all_tuples}
    all_noisy_counts = {k: noisy_counts.get(k, 0) for k in all_tuples}
    all_mitigated_counts = {k: mitigated_counts.get(k, 0) for k in all_tuples}
    # Plot counts as bars next to each other

    from matplotlib import pyplot as plt
    import numpy as np

    fig, ax = plt.subplots()

    xs = np.arange(2**n_qubits)
    width = 0.25

    xs_plus = xs + width
    xs_plus2 = xs + 2 * width

    ax.bar(xs, all_ideal_counts.values(), width, label=labels[0])
    ax.bar(xs_plus, all_noisy_counts.values(), width, label=labels[1])
    ax.bar(xs_plus2, all_mitigated_counts.values(), width, label=labels[2])

    ax.set_ylabel("Counts")
    plt.legend()

    ax.set_xticks(xs)

    all_tick_labels = [tuple_to_ket(x) for x in all_noisy_counts.keys()]
    clean_tick_labels = (
        [all_tick_labels[0]] + [""] * len(all_tick_labels[1:-1]) + [all_tick_labels[-1]]
    )
    ax.set_xticklabels(clean_tick_labels, rotation=45)
    plt.show()


def tuple_to_ket(t):
    numbers = "".join(map(str, t))
    return rf"$|{numbers}\rangle$"


def gen_tuples(n_wires):
    """Generate all 2^N bitstrings for N wires as tuples"""
    return [
        tuple(int(x) for x in bin(i)[2:].zfill(n_wires)) for i in range(2**n_wires)
    ]
