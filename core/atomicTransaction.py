class AtomicTransaction:
    def __init__(self):
        self.operations = []  # List of operations to be executed
        self.rollback_operations = []  # Store the rollback actions
        self.success = True  # Initially, assume the transaction will succeed

    def add_operation(self, action, undo_action):
        """
        Add an operation to the transaction.
        `action` is the function to be executed.
        `undo_action` is the function that will undo the operation if there's an error.
        """
        self.operations.append(action)
        self.rollback_operations.append(undo_action)

    def commit(self):
        """
        Execute all operations in the transaction.
        If all succeed, commit changes.
        If any operation fails, rollback changes.
        """
        try:
            # Execute all operations
            for op in self.operations:
                op()  # Execute each operation

            print("Transaction committed successfully.")

        except Exception as e:
            print(f"Error occurred: {e}. Rolling back...")
            self.rollback()  # Rollback if any operation fails
            self.success = False

    def rollback(self):
        """Rollback all operations if something fails"""
        # Undo each operation in reverse order
        for undo in reversed(self.rollback_operations):
            undo()  # Execute undo action

        print("Transaction rolled back.")

