# Quantum Teleportation using Qiskit

This repository demonstrates the implementation of the Quantum Teleportation protocol using IBM Qiskit. The project includes both a simulator-based implementation using Qiskit Aer and an execution on real IBM Quantum hardware using IBM Quantum Runtime.

---

## Project Overview

Quantum Teleportation is a fundamental quantum communication protocol that transfers the quantum state of one qubit to another distant qubit without physically transmitting the qubit itself.

The protocol relies on:

- Quantum Entanglement
- Bell State Preparation
- Quantum Measurement
- Classical Communication
- Conditional Quantum Operations

This project illustrates the complete teleportation workflow and compares execution on an ideal simulator with execution on a real quantum processor.

---

## Files

### `quantum_teleportation_basic.py`

- Implements the Quantum Teleportation protocol using the Qiskit Aer Simulator.
- Executes the circuit locally.
- Displays measurement counts after execution.

### `quantum_teleportation_hardware.py`

- Executes the same Quantum Teleportation circuit on IBM Quantum hardware.
- Uses IBM Quantum Runtime (SamplerV2).
- Demonstrates real quantum computation on IBM Quantum processors.

---

## Technologies Used

- Python
- Qiskit
- Qiskit Aer
- IBM Quantum Runtime
- IBM Quantum Platform

---

## Requirements

Install the required packages:

```bash
pip install qiskit
pip install qiskit-aer
pip install qiskit-ibm-runtime
pip install pylatexenc
```

---

## How to Run

### Simulator

```bash
python quantum_teleportation_basic.py
```

### IBM Quantum Hardware

Configure your IBM Quantum API key first.

Then run:

```bash
python quantum_teleportation_hardware.py
```

---

## Learning Outcomes

Through this project I learned:

- Building multi-qubit quantum circuits
- Creating entangled Bell pairs
- Implementing the Quantum Teleportation protocol
- Performing quantum measurements
- Using conditional quantum operations
- Running circuits on the Qiskit Aer Simulator
- Executing quantum programs on IBM Quantum hardware
- Retrieving and interpreting quantum measurement results
- Understanding the practical differences between simulator and real hardware execution

---

## Future Improvements

- Circuit visualization
- Histogram plotting of measurement counts
- Fidelity comparison between simulator and hardware
- Noise analysis of IBM Quantum devices

---

## Author

**Anubha Agarwal**

GitHub: https://github.com/anubhaagarwal08git add .
