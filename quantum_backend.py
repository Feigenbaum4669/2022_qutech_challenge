from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, BasicAer
from quantuminspire.qiskit import QI


def get_QI_backend(backend_type="QX single-node simulator"):
    """
    Returns the backend needed for Qiskit QuantumCircuit execution.
    Reads a file named 'cred.txt' containing your Quantum-Inspire email and password for authentication.

    Parameter
    ---------
        backend_type: str
            Valid inputs are 'Spin-2', 'Starmon-5', 'QX-34-L', 'QX single-node simulator'. Run QI.backends() to check the list.

    Return
    ------
        qi_backend: quantuminspire.qiskit.backend_qx.QuantumInspireBackend
            Object to be used to specify the backend when executing a Qiskit QuantumCircuit object.
    """
    with open('cred.txt', 'r') as f:
        creds = f.readlines()
    QI.set_authentication_details(creds[0].rstrip(), creds[1].rstrip())
    qi_backend = QI.get_backend(backend_type)
    return qi_backend


# To-Do keep track of used inputs.
def generate_QuantumCircuit(input_str: str) -> QuantumCircuit:
    """
    Returns a QuantumCircuit given an input string containing the information about the data qubit error.

    Parameter
    ---------
        input_str: str
            Input string specifying the type of error on the set of 5 data qubits. In this case it is limited to the set of single-qubit Pauli errors.

    Return
    ------
        qc: qiskit.circuit.quantumcircuit.QuantumCircuit
            A QuantumCircuit object representing the [[5,1,3]] circuit with artificially injected single-qubit error.
    """
    input_str = input_str.upper()  # Normalise the input string to always be uppercase.
    valid_inputs = ["I", "X0", "Y0", "Z0", "X1", "Y1", "Z1", "X2", "Y2", "Z2", "X3", "Y3", "Z3", "X4", "Y4", "Z4"]

    assert input_str in valid_inputs, "Please enter a valid input!"

    # Initialising the quantum circuit.
    ancilla_qubits = QuantumRegister(4, name='a')
    data_qubits = QuantumRegister(5, name='d')
    creg = ClassicalRegister(4)
    qc = QuantumCircuit(ancilla_qubits, data_qubits, creg)

    # Encoding the 5 data qubits into 1 logical qubit.
    qc.h(data_qubits)
    qc.cz(data_qubits[0], data_qubits[1])
    qc.cz(data_qubits[2], data_qubits[3])
    qc.cz(data_qubits[1], data_qubits[2])
    qc.cz(data_qubits[3], data_qubits[4])
    qc.cz(data_qubits[0], data_qubits[4])
    qc.barrier()

    if len(input_str) != 1:  # elso do nothing. (I.e., the input was "I", which is the identity).
        if input_str[0] == "X":
            qc.x(data_qubits[int(input_str[1])])
        if input_str[0] == "Y":
            qc.y(data_qubits[int(input_str[1])])
        if input_str[0] == "Z":
            qc.z(data_qubits[int(input_str[1])])
        qc.barrier()

    # Stabiliser operations.
    qc.h(ancilla_qubits)
    qc.barrier()
    qc.cx(ancilla_qubits[0], data_qubits[0])
    qc.cz(ancilla_qubits[0], data_qubits[1])
    qc.cz(ancilla_qubits[0], data_qubits[2])
    qc.cx(ancilla_qubits[0], data_qubits[3])
    qc.barrier()
    qc.cx(ancilla_qubits[1], data_qubits[1])
    qc.cz(ancilla_qubits[1], data_qubits[2])
    qc.cz(ancilla_qubits[1], data_qubits[3])
    qc.cx(ancilla_qubits[1], data_qubits[4])
    qc.barrier()
    qc.cx(ancilla_qubits[2], data_qubits[0])
    qc.cx(ancilla_qubits[2], data_qubits[2])
    qc.cz(ancilla_qubits[2], data_qubits[3])
    qc.cz(ancilla_qubits[2], data_qubits[4])
    qc.barrier()
    qc.cz(ancilla_qubits[3], data_qubits[0])
    qc.cx(ancilla_qubits[3], data_qubits[1])
    qc.cx(ancilla_qubits[3], data_qubits[3])
    qc.cz(ancilla_qubits[3], data_qubits[4])
    qc.barrier()
    qc.h(ancilla_qubits)
    qc.barrier()

    # Add the measurements into the circuit
    qc.measure(ancilla_qubits, creg)
    return qc


def execute_QuantumCircuit(input_str, backend, shots=512):
    """
    Creates and executes the five-qubit code quantum circuit using the Quantum-Inspire backend.

    Parameter
    ---------
        input_str: str
            Input string specifying the type of error on the set of 5 data qubits. In this case it is limited to the set of single-qubit Pauli errors.

        backend: quantuminspire.qiskit.backend_qx.QuantumInspireBackend
            Object to be used to specify the backend when executing a Qiskit QuantumCircuit object.

        shots: int
            Number of shots to execute.

    Return
    ------
        qc_job: quantuminspire.qiskit.qi_job.QIJob
            Qiskit job object which contain the execution and measurement results.
    """
    qc = generate_QuantumCircuit(input_str)
    qc_job = execute(qc, backend=backend, shots=shots)
    return qc_job
