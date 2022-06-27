from pydantic import BaseModel


class Writer(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class Book(BaseModel):
    id: int
    author_id: int
    name: str

    class Config:
        orm_mode = True


class DisplayBook(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class OutputSchema(BaseModel):
    id: int
    name: str
    books: list[DisplayBook] = []

    class Config:
        orm_mode = True
