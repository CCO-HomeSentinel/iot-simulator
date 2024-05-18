from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from .base import Base


class Telefone(Base):
    __tablename__ = "telefone"
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey("cliente.id"), nullable=False)
    codigo_discagem = Column(String(4), nullable=False)
    codigo_area = Column(String(2), nullable=False)
    numero = Column(String(9), nullable=False, unique=True)
    habilitado = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint("numero", name="numero_UNIQUE"),
        {"extend_existing": True},
    )
