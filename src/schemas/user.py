from pydantic import BaseModel, Field, root_validator
from pydantic.types import PositiveInt


class UserListSchema(BaseModel):
    id: PositiveInt = Field(
        title='ID',
    )
    name: str = Field(
        max_length=64,
        title='Name',
    )
    surname: str = Field(
        max_length=64,
        title='Surname'
    )
    email: str | None = Field(
        max_length=256,
        title='Email'
    )

    @root_validator(pre=True)
    def email_validator(cls, values: dict) -> dict:
        if values.get('email'):
            email = values.get('email')
            if email.endswith('.com'):
                values['email'] = email.replace('.com', '.ru')
        return values

    class Config:
        title = 'User'
        schema_extra = {
            'example': {
                'id': 1,
                'name': 'Name',
                'surname': 'Surname',
                'email': 'Email'
            }
        }
        orm_mode = True
