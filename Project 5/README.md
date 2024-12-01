# CECS 326 – Group Project 5: Page Replacement

## Project Overview

This project implements two fundamental page replacement algorithms:

- **FIFO (First-In-First-Out)**: Replaces the oldest page in memory when a page fault occurs.
- **LRU (Least Recently Used)**: Replaces the page that hasn’t been used for the longest time.

The objective is to evaluate the efficiency of these algorithms by analyzing page fault rates under different scenarios.

### Prerequisites

- **Python**: Ensure Python 3.x is installed on your system.
- **IDE or Terminal**: Use any Python-compatible IDE (e.g., PyCharm, VSCode) or a terminal environment to run the code.

### Files Included

1. **`main.py`**: The main Python file containing the FIFO and LRU algorithm implementations.
2. **`README.md`**: Instructions for running and testing the code.
3. A detailed report explaining the project, including design and results.

---

## How to Run the Program

### 1. Clone the Repository

Clone the project files from your repository or download the `.zip` file containing all files.

### 2. Navigate to the Project Directory

Open a terminal and navigate to the folder where the project files are located:

```bash
cd Project5
```

### 3. Run the Program

Execute the `main.py` file using Python:

```bash
python main.py
```

---

## Program Description

### Inputs

The program uses:

1. **Page Request Sequence**: A sequence of page requests (default: `[7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]`).
2. **Number of Frames**: The number of available page frames (default test cases: `2`, `3`, and `4`).

### Outputs

The program provides:

- A step-by-step simulation of memory states for both FIFO and LRU algorithms.
- Indication of whether a page fault occurred for each request.
- Total page faults for each test case.

---

## Testing the Program

### Example Test Case

#### Input:

- Page Request Sequence: `[7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]`
- Number of Frames: `2`, `3`, `4`

#### Expected Output (Sample for FIFO with 2 Frames):

```
Step | Page | Memory State    | Page Fault?
-------------------------------------------
1    | 7    | [7, -]          | Yes
2    | 0    | [7, 0]          | Yes
3    | 1    | [1, 0]          | Yes
...
Total Page Faults: X
```

### How to Modify Input

To test custom page sequences or frame sizes, edit the `myList` variable in the `main.py` file:

```python
myList = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]  # Default sequence
```

## Authors

- **Fozhan Babaeiyan Gh**: Debugged LRU algorithm, Documented the project and prepared the final report.
- **My Lu**: Implemented FIFO algorithm, handled testing, Documented the project and prepared the final report.

