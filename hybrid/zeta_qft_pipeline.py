import numpy as np
from classical.riemann_siegel import riemann_siegel
from quantum.qft_numpy import apply_qft

def hybrid_zeta(t, n=8):
    # Classical preprocessing: weights
    terms = int(np.sqrt(t/(2*np.pi)))
    coeffs = np.array([1/np.sqrt(k) for k in range(1, terms+1)])
    
    # Quantum simulation: encode coefficients as state
    state = np.zeros(2**n, dtype=complex)
    state[:len(coeffs)] = coeffs
    state /= np.linalg.norm(state)
    
    # Apply QFT (simulated with NumPy)
    qft_state = apply_qft(state)
    
    # Postprocessing: simple sum of amplitudes
    return np.sum(np.abs(qft_state)**2)

if __name__ == "__main__":
    t = 1e4
    classical_val = riemann_siegel(t)
    quantum_val = hybrid_zeta(t)
    print(f"Classical Z({t}) ≈ {classical_val}")
    print(f"Hybrid Quantum Z({t}) ≈ {quantum_val}")
