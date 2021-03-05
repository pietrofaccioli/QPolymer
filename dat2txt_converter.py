import numpy as np

# defining variable that tracks lattice dimension <=> number of DOF

dim_h = 0
dim_J = 0
h0 = 0

# open .dat file containing parameters and count

params = open('fields_and_couplings_L3_nb6_ns7_cross0_Tjunct0_4loop0.dat')

for row in params:
	if '#' not in row:
		row = np.array(str(row).split(' '))
		if len(row) == 2:
			dim_h += 1
		if len(row) == 3:
			dim_J += 1		


# filling variables with h0, h, J

h = np.zeros(dim_h)
J = np.zeros((dim_h,dim_h))

params = open('fields_and_couplings_L3_nb6_ns7_cross0_Tjunct0_4loop0.dat')
for row in params:
	if '#' not in row:
		row = np.array(str(row).split(' '))
		if len(row) == 1:
			h0 = row[0]
		if len(row) == 2:
			h[int(row[0])] = row[1]
		if len(row) == 3:
			J[int(row[0]),int(row[1])] = row[2]
			J[int(row[1]),int(row[0])] = row[2]

# saving parameters as txt so to be in the proper form for dwave

with open("h0.txt", "w") as output:
    output.write(str(h0))

np.savetxt('h.txt',h)
np.savetxt('J.txt',J)