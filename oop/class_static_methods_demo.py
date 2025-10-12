class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Performs addition without referencing the class or instance."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Performs multiplication and shows class-level context."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
