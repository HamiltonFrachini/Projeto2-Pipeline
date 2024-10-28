from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "Prod1"
    produto2 = "Prod2"
    produto3 = "Prod3"

class Vendas(BaseModel):

    email: EmailStr # zeh =! zeh@gmail.com
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum

    #   """
    #Modelo de dados para as vendas.

    #Args:
    #    email (EmailStr): email do comprador
    #    data (datetime): data da compra
    #    valor (PositiveFloat): valor da compra
    #    produto (PositiveInt): nome do produto
    #    quantidade (PositiveInt): quantidade de produtos
    #    produto (ProdutoEnum): categoria do produto
    #"""