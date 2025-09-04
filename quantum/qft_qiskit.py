import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def qft_circuit(n):
    qc = QuantumCircuit(n)
    for j in range(n):
        qc.h(j)
        for k in range(j+1, n):
            qc.cp(2*np.pi/2**(k-j+1), k, j)
    qc.barrier()
    for j in range(n//2):
        qc.swap(j, n-j-1)
    return qc

if __name__ == "__main__":
    qc = qft_circuit(3)
    qc.draw("mpl")
    plt.show()

    sim = Aer.get_backend('aer_simulator_statevector')
    transpiled = transpile(qc, sim)
    result = sim.run(transpiled).result()
    statevector = result.get_statevector()
    print("Statevector after QFT:", statevector)
