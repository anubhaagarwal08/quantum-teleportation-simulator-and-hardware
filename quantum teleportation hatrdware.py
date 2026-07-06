from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

# -----------------------------
# Connect to IBM Quantum
# -----------------------------
service = QiskitRuntimeService()

backends = service.backend("ibm_fez")






# -----------------------------
# Create circuit
# -----------------------------
qc = QuantumCircuit(3, 2)

qc.h(1)
qc.cx(1,2)

qc.h(0)
qc.cx(0,1)
qc.h(0)

qc.measure(0,0)
qc.measure(1,1)

with qc.if_test((qc.cregs[0],1)):
    qc.x(2)

with qc.if_test((qc.cregs[0],2)):
    qc.z(2)

with qc.if_test((qc.cregs[0],3)):
    qc.x(2)
    qc.z(2)

# -----------------------------
# Optimize circuit
# -----------------------------
pm = generate_preset_pass_manager(
    backend=backends,
    optimization_level=1
)

isa_circuit = pm.run(qc)

# -----------------------------
# Run on hardware
# -----------------------------
sampler = Sampler(mode=backends)

job = sampler.run([isa_circuit], shots=1024)

print("Job ID:", job.job_id())

result = job.result()[0]

print(result.data)
