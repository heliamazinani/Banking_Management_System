class AtomicTransaction:
    def __init__(self):
        self.operations = []
        self.rollback_operations = []
        self.success = True

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
            
            for op in self.operations:
                op()  

            print("Transaction committed successfully.")

        except Exception as e:
            print(f"Error occurred: {e}. Rolling back...")
            self.rollback() 
            self.success = False

    def rollback(self):
        """Rollback all operations if something fails"""
        
        for undo in reversed(self.rollback_operations):
            undo() 

        print("Transaction rolled back.")

