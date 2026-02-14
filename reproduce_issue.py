from pydantic import BaseModel, ValidationError

try:
    class IterativeRagState(BaseModel):
        attempts: str  # The error suggests this is str

    # This should raise the exact ValidationError seen
    print("Attempting to instantiate IterativeRagState with attempts=0")
    state = IterativeRagState(attempts=0)
except ValidationError as e:
    print("\nCaught expected ValidationError:")
    print(e)
except Exception as e:
    print(f"\nCaught unexpected exception: {e}")
