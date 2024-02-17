# Starting
------------
In Python, matrix and vector computations can be performed using the  **array**  class from the  **NumPy**  library (which includes many additional components for numerical computation).
```
from numpy import array
ket0 = array([1, 0])
ket1 = array([0, 1])
print(ket0 / 2 + ket1 / 2)
```
Matrix multiplication (including matrix-vector multiplication as a special case) can be performed using the **matmul**  function from  **NumPy** Copy to clipboard.
```
from numpy import matmul

display(matmul(M1, ket1))
display(matmul(M1, M2))
display(matmul(M2, M1))
```
_Qiskit includes several classes that allow for states, measurements, and operations to be easily created and manipulated_
_Qiskit's  Statevector  class provides functionality for defining and manipulating quantum state vectors. The following code cell imports the  Statevector  class and defines a few vectors using it. (Note that we need the sqrt  function from the  NumPy  library to compute the square roots for the vector  u  .)_
```
from qiskit.quantum_info import Statevector
from numpy import sqrt

u = Statevector([1 / sqrt(2), 1 / sqrt(2)])
v = Statevector([(1 + 2.0j) / 3, -2 / 3])
w = Statevector([1 / 3, 2 / 3])

print("State vectors u, v, and w have been defined.")
```
The statevector is like a special map that tells you all the possible combinations of on and off for all the qubits in your system, along with their likelihood of being in each state.

So, when we talk about a quantum state represented by a statevector, we're essentially talking about a way to describe all the possible combinations of on and off for all the qubits in our quantum system, along with the probabilities of each combination.


Next we will see one way that measurements of quantum states can be simulated in Qiskit, using the  measure method from the  Statevector  class.

First, we create a qubit state vector  v  and then display it
```
v = Statevector([(1 + 2.0j) / 3, -2 / 3])
v.draw("latex")
```
The  Statevector  class also includes the  is_valid  method, which checks to see if a given vector is a valid quantum state vector (i.e., that it has Euclidean norm equal to 1):
```
display(u.is_valid())
display(w.is_valid())
```
Next we will see one way that measurements of quantum states can be simulated in Qiskit, using the  measure method from the  Statevector  class.

First, we create a qubit state vector  v  and then display it.
```
v = Statevector([(1 + 2.0j) / 3, -2 / 3])
v.draw("latex")
v.measure()
```


```
from qiskit.quantum_info import Operator

X = Operator([[0, 1], [1, 0]])
Y = Operator([[0, -1.0j], [1.0j, 0]])
Z = Operator([[1, 0], [0, -1]])
H = Operator([[1 / sqrt(2), 1 / sqrt(2)], [1 / sqrt(2), -1 / sqrt(2)]])
S = Operator([[1, 0], [0, 1.0j]])
T = Operator([[1, 0], [0, (1 + 1.0j) / sqrt(2)]])

v = Statevector([1, 0])

v = v.evolve(H)
v = v.evolve(T)
v = v.evolve(H)
v = v.evolve(T)
v = v.evolve(Z)

v.draw("text")
```
we can nevertheless experiment with composing qubit unitary operations using Qiskit's  QuantumCircuit  class.
```
from qiskit import QuantumCircuit

circuit = QuantumCircuit(1)

circuit.h(0)
circuit.t(0)
circuit.h(0)
circuit.t(0)
circuit.z(0)

circuit.draw()
```
The operations are applied sequentially, starting on the left and ending on the right in the figure. Let us first initialize a starting quantum state vector and then evolve that state according to the sequence of operations.
```
ket0 = Statevector([1, 0])
v = ket0.evolve(circuit)
v.draw("text")
```
Finally, let's simulate the result of running this experiment (i.e., preparing the state,
∣0⟩, applying the sequence of operations represented by the circuit, and measuring) 4000 times.
```
statistics = v.sample_counts(4000)
plot_histogram(statistics)
```












