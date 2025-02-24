import sqlalchemy
import sqlalchemy.orm as orm

class Base(orm.DeclarativeBase, orm.MappedAsDataclass):
    pass

class Pupil(Base):
    __tablename__ = 'pupil'

    pupil_id: orm.Mapped[int] = orm.mapped_column(init=False, primary_key=True)
    first_name: orm.Mapped[str] = orm.mapped_column()
    last_name: orm.Mapped[str] = orm.mapped_column()
    # pupil_house_id: orm.Mapped[int] = orm.mapped_column()

class House(Base):
    __tablename__ = 'house'

    house_id: orm.Mapped[int] = orm.mapped_column(init=False, primary_key=True)
    name: orm.Mapped[str] = orm.mapped_column()
