# hybrid solver test with 10 edges, 4 vertices
import dimod
from dwave.system import LeapHybridSampler
import numpy as np

h = np.loadtxt('h.txt')
J = np.loadtxt('J.txt')

sampler = LeapHybridSampler()
results = sampler.sample_ising(h,J, num_reads = 100)

out = open('Outputs.txt', 'w')
for campione in results.record:
	for Nple in campione:
		out.write(str(Nple)+"\t")
	out.write("\n")
out.close()

print(results.first)