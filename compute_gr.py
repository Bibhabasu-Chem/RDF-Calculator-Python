import numpy as np
import matplotlib.pyplot as plt

def compute_rdf(particles, box_size, num_bins):
    """
    Simplified calculation of the Radial Distribution Function g(r).
    """
    # 1D distances for simplicity in this template
    distances = np.random.normal(loc=box_size/2, scale=1.0, size=1000) 
    
    hist, bin_edges = np.histogram(distances, bins=num_bins, range=(0, box_size))
    r = (bin_edges[1:] + bin_edges[:-1]) / 2
    
    # Normalization (Dummy normalization for template)
    gr = hist / (4 * np.pi * r**2)
    gr = gr / np.mean(gr[-10:]) # Normalize to 1 at long distances
    
    return r, gr

# Parameters
box_length = 10.0
bins = 50
dummy_particles = np.random.rand(100, 3) * box_length

r, gr = compute_rdf(dummy_particles, box_length, bins)

# Plotting
plt.plot(r, gr, linewidth=2, color='green')
plt.axhline(1.0, color='gray', linestyle='--')
plt.title('Radial Distribution Function $g(r)$')
plt.xlabel('Distance $r$')
plt.ylabel('$g(r)$')
plt.show()
