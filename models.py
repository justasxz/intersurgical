from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Darbuotojas(Base):
    __tablename__ = "Darbuotojai"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    vardas: Mapped[str] = mapped_column(nullable=False)
    pavarde: Mapped[str] = mapped_column(nullable=False)
    alga: Mapped[float] = mapped_column(nullable=False)
    metai: Mapped[int] = mapped_column(nullable=False, default=0)