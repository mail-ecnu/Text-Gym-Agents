from pydantic import BaseModel, Field, validator
from typing import List

class DisActionModel(BaseModel):
    action: int = Field(description="the chosen action to perform")

    @classmethod
    def create_validator(cls, max_action):
        @validator('action', allow_reuse=True)
        def action_is_valid(cls, field):
            if field not in range(1, max_action + 1):
                raise ValueError(f"Action is not valid ([1, {max_action}])!")
            return field
        return action_is_valid

# Generate classes dynamically
def generate_action_class(max_action):
    return type(f"{max_action}Action", (DisActionModel,), {'action_is_valid': DisActionModel.create_validator(max_action)})
    
# Dictionary of parsers with dynamic class generation
DISPARSERS = {num: generate_action_class(num) for num in [2, 3, 4, 6, 9, 18]}

class ContinuousActionBase(BaseModel):
    action: List[float] = Field(description="the chosen continuous actions to perform")

    @classmethod
    def set_expected_length(cls, length):
        cls.expected_length = length

    @validator('action', pre=True)
    def validate_length(cls, action):
        if len(action) != cls.expected_length:
            raise ValueError(f"The action list must have exactly {cls.expected_length} items.")
        return action

    @validator('action', each_item=True)
    def action_is_valid(cls, item):
        if not -1 <= item <= 1:
            raise ValueError("Each action dimension must be in the range [-1, 1]!")
        return item

# Generate classes dynamically
def generate_continuous_action_class(expected_length):
    NewClass = type(
        f"{expected_length}DContinuousAction",
        (ContinuousActionBase,),
        {}
    )
    NewClass.set_expected_length(expected_length)
    return NewClass


# Dictionary of parsers with dynamic class generation
CONPARSERS = {length: generate_continuous_action_class(length) for length in range(1, 17)}
