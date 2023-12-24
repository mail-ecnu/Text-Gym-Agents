from pydantic import BaseModel, Field, validator

# Define your desired data structure.
class TwoAction(BaseModel):
    action: int = Field(description="the choosed action to perform")
    
    # You can add custom validation logic easily with Pydantic.
    @validator('action')
    def action_is_valid(cls, field):
        if field not in [1, 2]:
            raise ValueError("Action is not valid ([1, 2])!")
        return field
    
class ThreeAction(BaseModel):
    action: int = Field(description="the choosed action to perform")
    
    # You can add custom validation logic easily with Pydantic.
    @validator('action')
    def action_is_valid(cls, field):
        if field not in [1, 2, 3]:
            raise ValueError("Action is not valid ([1, 2, 3])!")
        return field
    
class FourAction(BaseModel):
    action: int = Field(description="the choosed action to perform")
    
    # You can add custom validation logic easily with Pydantic.
    @validator('action')
    def action_is_valid(cls, field):
        if field not in [1, 2, 3, 4]:
            raise ValueError("Action is not valid ([1, 2, 3, 4])!")
        return field
    
class SixAction(BaseModel):
    action: int = Field(description="the choosed action to perform")
    
    # You can add custom validation logic easily with Pydantic.
    @validator('action')
    def action_is_valid(cls, field):
        if field not in [1, 2, 3, 4, 5, 6]:
            raise ValueError("Action is not valid ([1, 2, 3, 4, 5, 6])!")
        return field


class NineAction(BaseModel):
    action: int = Field(description="the choosed action to perform")

    # You can add custom validation logic easily with Pydantic.
    @validator('action')
    def action_is_valid(cls, field):
        if field not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            raise ValueError("Action is not valid ([1, 2, 3, 4, 5, 6, 7, 8, 9])!")
        return field

class FullAtariAction(BaseModel):
    action: int = Field(description="the choosed action to perform")
    @validator('action')
    def action_is_valid(cls, info):
        if info not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
            raise ValueError("Action is not valid ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])!")
        return info
    
class ContinuousAction(BaseModel):
    action: float = Field(description="the choosed action to perform")
    # You can add custom validation logic easily with Pydantic.
    @validator('action')
    def action_is_valid(cls, field):
        if not (field >= -1 and field <= 1):
            raise ValueError("Action is not valid ([-1,1])!")
        return field
    
PARSERS = {1:ContinuousAction, 2: TwoAction, 3: ThreeAction, 4: FourAction, 6: SixAction, 9:NineAction, 18: FullAtariAction}
