# Round Robin Scheduling Algorithm 🚀

Welcome to the Round Robin Scheduling Algorithm!
This project implements one of the most popular CPU scheduling algorithms, offering fairness and simplicity in process management. Whether you're a student, a developer, or just curious about operating systems, this project is for you! 🎉

## Project Overview 📚

The Round Robin Scheduling Algorithm is a preemptive CPU scheduling technique where each process gets executed for a fixed time quantum (2 units in our implementation) in a cyclic order. This ensures that no single process can monopolize the CPU, providing a balanced and efficient scheduling strategy.

**Key functionalities include:**

* Fair allocation of CPU time among processes.
* Calculation of key performance metrics: Waiting Time and Turnaround Time.
* Robust input validation for seamless user experience.

## Team Members👪

**Project Leader:** Amr Yasser  
**Assistants:**  
Youssef Mahmoud  
Mohamed Waleed  
Sama El-Fishawy  
Youssef El-Sayed  
Mohamed Hareth  
Mariam Mohamed

## How to Use 📖

### 1. User Input

Enter the number of processes to schedule.  
For each process, provide:

* **Arrival Time:** When the process enters the ready queue.  
* **Burst Time:** Total execution time required by the process.  
  *Ensure all inputs are non-negative integers.*

### 2. Execution

The algorithm simulates process scheduling using Round Robin with a time quantum of 2 units.  
As the program runs, it:

* Handles process execution dynamically.  
* Calculates Waiting Time and Turnaround Time for each process.  
* Updates and validates states to avoid any logical errors.

### 3. Output

Displays:

* Individual metrics for all processes.  
* Averages for Waiting Time and Turnaround Time.

## Features ✨

* **Preemptive Scheduling:** Uses a fixed time slice (2 units) to ensure fairness.  
* **Performance Metrics:** Displays Waiting Time and Turnaround Time for each process along with averages.  
* **Dynamic Input Validation:** Ensures no invalid or negative inputs are processed.  
* **Detailed Execution Flow:** Tracks and manages process states dynamically for better visualization.

## Example Output 🖥️

Here’s what you can expect when you run the program:

\`\`\`
Enter the number of processes: 3  
Enter the arrival time of process  0: 0  
Enter the burst time of process  0: 4  
Enter the arrival time of process  1: 1  
Enter the burst time of process  1: 5  
Enter the arrival time of process  2: 2  
Enter the burst time of process  2: 2  
[8, 10, 4] 7.333333333333333  
[4, 5, 2] 3.6666666666666665
\`\`\`

## Contributions 🤝

This project was developed through the collaborative efforts of:

* Youssef Mahmoud  
* Youssef El-Sayed

**Special thanks to all contributors and team members:**

* Sama El-Fishawy  
* Mohamed Harith  
* Mariam Mohamed  
* Mohamed Walid

We welcome your suggestions and contributions!  
Feel free to submit an issue or pull request. 🚀

## Acknowledgments 🎉

We extend our gratitude to all contributors, reviewers, and enthusiasts who made this project possible.

Special thanks to the countless hours of effort from the team.🌟
