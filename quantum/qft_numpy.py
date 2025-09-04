import numpy as np

def qft_matrix(n):
    """Returns the QFT matrix of size n x n"""
    omega = np.exp(2j * np.pi / n)
    return np.array([[omega ** (j*k) / np.sqrt(n) for k in range(n)] for j in range(n)])

def apply_qft(state):
    n = len(state)
    QFT = qft_matrix(n)
    return QFT @ state

if __name__ == "__main__":
    state = np.array([1,0,0,0], dtype=complex)  # |0⟩ state
    print("Input state:", state)
    print("After QFT:", apply_qft(state))
