from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.common.database import Base


class CreateUserDTO:
    def __init__(self, username: str, email: str, password: str, name: str):
        self.username = username
        self.password = password
        self.email = email
        self.name = name


# class User(Base):
#     # __tablename__ = 'Users'
#     # id: Mapped[int] = mapped_column('UserID', primary_key=True)

#     username: Mapped[str] = mapped_column()
#     email: Mapped[str] = mapped_column()
#     confirmed: Mapped[bool] = mapped_column()

#     def __init__(self, createdUser: CreateUserDTO):
#         self.username = createdUser.username
#         self.email = createdUser.email
#         self.name = createdUser.name
#         self.confirmed = True
