#  Copyright (c) 2022. Hexagoon. Criador: Fabricio Gatto Lourençone. Todos os direitos reservados.

from typing import Optional

from pydantic import BaseModel


class RoleOut(BaseModel):
    id: int
    sigla: str
    descricao: str

    class Config:
        title = 'roles'
        orm_mode = True


class RoleIn(BaseModel):
    sigla: Optional[str]
    descricao: Optional[str]
    id: Optional[int]
