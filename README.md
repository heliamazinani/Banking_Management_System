# Banking Management System

A simple console-based banking management system built in C to demonstrate core banking operations such as account creation, balance inquiry, deposit, and withdrawal.

---

## Features

This system provides the following functionalities:
1. **Create New Account**: Add a new customer to the banking system.
2. Deposit Funds: Add money to an existing account.
3. Withdraw Funds: Deduct money from an account if sufficient balance exists.
4. Check Balance: View the current balance of a specific account.
5. Exit System: Safely exit the application.

---

## Project Structure

The project consists of the following key files:
- `main.c`: Contains the main function and the logic for user interaction and menu navigation.
- `banking_operations.c`: Implements the core banking functionalities.
- `banking_operations.h`: Header file defining functions and data structures used across the project.
- `data_storage.txt`: Used to persist account information between sessions.

## Race Condition :
To prevent race conditions, we implement a locking mechanism for each account, where each account is essentially represented by a JSON file stored on the core.
This lock ensures that only one process can access or modify the file at any given time. Before making any changes to these files, it is necessary to first check whether the lock is free.
If the lock is not free, the process must wait until it becomes available to avoid any potential conflicts or data inconsistencies.

## Deadlock :

To prevent deadlocks, we have implemented a recovery mechanism. During fund transfers, we check the locks in a non-blocking manner. If both the source and destination account locks are free, the transaction proceeds.
However, if either or both locks are not free, we release both locks to avoid potential deadlock scenarios.
To further manage the operation, we have set a maximum retry limit and a timeout value for each transaction, ensuring that the process does not run indefinitely and remains efficient.

---

## Getting Started

### Prerequisites
- A C compiler (e.g., GCC)
- Text editor or IDE (e.g., Visual Studio Code, Code::Blocks)
- A terminal or command-line interface

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/heliamazinani/Banking_Management_System.git

 2. Navigate to the project directory:

cd Banking_Management_System

Usage
 1. Compile the Code:

gcc main.c banking_operations.c -o banking_system


 2. Run the Program:

./banking_system


 3. Follow the on-screen menu to perform various banking operations.

Sample Workflow

Welcome to the Banking Management System!

1. Create New Account
2. Deposit Funds
3. Withdraw Funds
4. Check Balance
5. Exit

Enter your choice: 

For example:
 • Choose 1 to create a new account, enter the required details, and a new account will be added.
 • Choose 4 to check the balance of an existing account by providing the account number.

Data Persistence
 • The application uses the file data_storage.txt to store account information.
 • Ensure that this file is present in the project directory to retain data between sessions.

Limitations
 • No advanced user authentication is implemented.
 • Data is stored in plain text, which may not be secure for real-world applications.
 • Concurrency and multi-user access are not supported.

Future Enhancements

Potential future improvements to the system:
 1. Implementing user authentication (e.g., usernames and passwords).
 2. Adding support for data encryption for secure storage.
 3. Enhancing the UI with a graphical interface.
 4. Supporting multiple currencies and internationalization.
