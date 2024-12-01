# CPU Scheduler Project

This project implements three classic CPU scheduling algorithms: First-Come, First-Served (FCFS), Priority Scheduling, and Round Robin (RR). Each algorithm is implemented as a separate scheduler and executes tasks based on different scheduling rules.

## Table of Contents

- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
- [Code Documentation](#code-documentation)
  - [driver.c](#driverc)
  - [schedule_fcfs.c](#schedule_fcfsc)
  - [schedule_priority.c](#schedule_priorityc)
  - [schedule_rr.c](#schedule_rrc)
- [Contributing](#contributing)

## Installation Instructions

To install and run this project on a Unix-like system (e.g., Linux, WSL):

1. Clone the repository and navigate to the project directory:

   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```

   Ensure make and gcc are installed on your system. If not, install them:

```bash
sudo apt update
sudo apt install build-essential
```

Compile the code using the provided Makefile:

For FCFS scheduling:
`   make fcfs
  `

For Priority scheduling:
`   make priority
  `
For Round Robin scheduling:
`   make rr
  `

## Usage

After compiling, you can run each scheduler with the appropriate task file.

Example:
`   ./fcfs schedule.txt   # Run FCFS scheduler
    ./priority pri-schedule.txt   # Run Priority scheduler
    ./rr rr-schedule.txt  # Run Round Robin scheduler
  `

## Code Documentation

### driver.c

Purpose: The main driver file reads tasks from an input file and passes them to the selected scheduling algorithm.
Key Functions:
main(): Reads the schedule file, parses task attributes (name, priority, burst), and invokes the scheduler.

### schedule_fcfs.c

Purpose: Implements First-Come, First-Served scheduling where tasks are executed in the order of arrival.
Key Functions:
add(): Adds a new task to the list.
schedule(): Executes tasks in the order they were added.

### schedule_priority.c

Purpose: Implements Priority scheduling where tasks are selected based on their priority values.
Key Functions:
add(): Adds a new task to the list.
pickNextTask(): Selects the highest-priority task from the list.
schedule(): Executes tasks in descending order of priority.

### schedule_rr.c

Purpose: Implements Round Robin scheduling with a fixed time quantum (10 milliseconds).
Key Functions:
add(): Adds a new task to the list.
schedule(): Executes tasks in a round-robin fashion, giving each task up to 10 milliseconds per cycle.

## Contributing

CECS 326 - PROJECT REPORT 4

My Lu

Fozhan Babaeiyan Ghamsari
