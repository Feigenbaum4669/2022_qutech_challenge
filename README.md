# iQuHACK22 QuTech Quantum Error Correction Challenge

# Project : QEC Bingo Game

## Team members and experience
* [Abhay Kamble](https://github.com/abzsd), CS Undergrad @BITS Goa
* [Bernard Wo](https://github.com/bernwo) MSc Applied Physics @ Delft University of Technology,
* [Oskar Słowik](https://github.com/Feigenbaum4669) PhD candidate @ Center for Theoretical Physics PAS,
* [Wridhdhisom Karar](https://github.com/wridhdhi) PhD @ University of Glasgow,
* [Fatma Türkü Tatar](https://github.com/turkutatar), Electrical Engineering Undergraduate @ Cankaya University

Experience - *Our team is highly diverse in terms of nationalities and education levels. We created a supportive and hard working environment together and everyone did their part as perfect as it can be within 24 hours. Despite being in this extraordinary times where hackathons are conducted **remotely** with participants all over the globe with different timezones, we still managed to have had productive and insightful discussion together. We are glad we hacked together :)*

## Demo

![something](https://github.com/Feigenbaum4669/2022_qutech_challenge/blob/main/Assets/running_code.gif?raw=true)
Also see the section [*How to run the code to play the game?*](https://github.com/Feigenbaum4669/2022_qutech_challenge#how-to-run-the-code-to-play-the-game) below.

## Documentation
* Presentation [Slides](https://docs.google.com/presentation/d/1AlDr8H5LY_8CyQQnUTHNoNZCA1F4KANMGV6-wCRXGGM/edit?usp=sharing)
* Original repository [here](https://github.com/turkutatar/iQuHACK22/tree/QEC-Bingo) - for all files/commits
* Jupyter Notebook about a probability distribution of the error syndromes [here](https://github.com/Feigenbaum4669/2022_qutech_challenge/blob/main/Syndrome_Heatmap.ipynb)

## Technologies Used

* [`QX single-node simulator`](https://www.quantum-inspire.com/backends/qx-simulator/) - A [*Quantum-Inspire*](https://www.quantum-inspire.com/) classical simulator backend capable of simulating ~20~30 qubits.
* [`Qiskit`](https://qiskit.org/) - IBM's Quantum computing SDK.
* [`Python`](https://python.org/) - Programming language.
* [`Git`](https://git-scm.com/) - Version control.

## QEC Preliminaries 
The [`[[5,1,3]]` code](https://en.wikipedia.org/wiki/Five-qubit_error_correcting_code) is a five qubit quantum error correction code (QECC) which uses 9 qubits in total: 5 physical qubits and 4 ancilla qubits. This code encodes one logical qubit and can correct an arbitrary single qubit error, e.g., Pauli-X/Y/Z error on any one of physical qubits.

Below, we see the 1-to-1 mapping of the single-qubit errors to the ancilla syndromes. *Image source: [Wikipedia](https://en.wikipedia.org/wiki/Five-qubit_error_correcting_code).*

![ex_table](https://github.com/Feigenbaum4669/2022_qutech_challenge/blob/main/Assets/correction_table.png)

## Layout 
The basic layout of the game is a 4x4 grid which contains numbers ranging from 0 to 15, i.e., 0000 to 1111 in binary. Those numbers correspond to all possible error syndromes. In the beginning the grid is randomly generated, and each player has a separate grid.

![ex_grid](https://user-images.githubusercontent.com/73556839/151690729-09667da5-074a-458c-b45c-01ee4809add7.png)

At each turn, a player gives an input, which can be no error (I) or any of the single-qubit Pauli errors (X, Y, Z). The syndrome of a chosen input triggers the cells in the player's respective grid. If the full diagonal or a straight line has been triggered, that player wins. **Example below**:

![ex_grid](https://github.com/Feigenbaum4669/2022_qutech_challenge/blob/main/Assets/labelled_grid.png)

## Implementation 
We can implement this code and use [*Quantum-Inspire*](https://www.quantum-inspire.com/)'s classical simulator since our idea uses 9 qubits.

## How to play the game?
Player A gives input *i* in the form of a string.
Input gets processed and a quantum circuit is constructed with qiskit.
The quantum circuit is then sent to quantum-inspire.
Quantum-Inspire returns the syndrome, and Player A and B mark their corresponding cell based on the returned syndrome.
The above steps are repeated between the Player A and B, until one wins.

## What is quantum about this game?
The players are introducing quantum errors whose syndromes are detected by stabiliser generators of a QEC code running on a quantum computer. In this case, we are classically simulating the quantum computer via [`QX single-node simulator`](https://www.quantum-inspire.com/backends/qx-simulator/).

## How to run the code to play the game?
Clone the repository via `git clone https://github.com/Feigenbaum4669/2022_qutech_challenge.git`, and edit the `cred.txt` to include your own Quantum-Inspire credentials. Then, in the root folder, execute the following command in your terminal to run the game:

```bash
py main.py
```

### Different variants of the game

It is straightforward to modify the gambe by choosing other single-qubit gates, e.g. containing the Hadamard gate. This way the syndromes can be made probabilistic changing the game expierience.

### Probability heatmap of the syndromes

Separate from the Bingo game, we also visualised the probability heatmap of the 16 possible syndromes using the **custom error model** outlined in the [Jupyter notebook (`Syndrome_Heatmap.ipynb`)](https://github.com/Feigenbaum4669/2022_qutech_challenge/blob/main/Syndrome_Heatmap.ipynb). Such a heatmap is shown below and also in the notebook. 

We can possibly leverage this heatmap as a means to improve the bot's performance and thereby increasing the game's difficulty, or perhaps even come up with a brand new game idea surrounding this error model.

![example_heatmap](https://github.com/Feigenbaum4669/2022_qutech_challenge/blob/main/Assets/example_heatmap.png)





