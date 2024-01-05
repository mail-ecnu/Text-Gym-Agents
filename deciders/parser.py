from pydantic import BaseModel, Field, validator

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
PARSERS = {num: generate_action_class(num) for num in [2, 3, 4, 6, 9, 18]}

# class ContinuousAction(BaseModel):
#     action: float = Field(description="the choosed action to perform")
#     # You can add custom validation logic easily with Pydantic.
#     @validator('action')
#     def action_is_valid(cls, field):
#         if not (field >= -1 and field <= 1):
#             raise ValueError("Action is not valid ([-1,1])!")
#         return field
    
# PARSERS = {1:ContinuousAction, 2: TwoAction, 3: ThreeAction, 4: FourAction, 6: SixAction, 9:NineAction, 18: FullAtariAction}
