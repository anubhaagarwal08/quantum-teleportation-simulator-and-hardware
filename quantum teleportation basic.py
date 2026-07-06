from qiskit import QuantumCircuit ,transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
qc=QuantumCircuit(3,2)
qc.h(1)
qc.cx(1,2)
qc.h(0)
qc.cx(0,1)
qc.h(0)
qc.measure(0,0)
qc.measure(1,1)
print(qc.draw())
qc.draw(output='mpl', filename='quantum teleportation circuit.png')
with qc.if_test((qc.cregs[0],1)):
    qc.x(2)
with qc.if_test((qc.cregs[0],2)):
    qc.z(2)

sim= AerSimulator()
Compiled=transpile(qc,sim)
result=sim.run(Compiled,shots=1024).result()
print(result.get_counts())
counts=result.get_counts()
hist = plot_histogram(counts)

hist.savefig("teleportation_histogram.png")

plt.show()
