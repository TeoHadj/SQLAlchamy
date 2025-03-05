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
    house_id: orm.Mapped[int]=orm.mapped_column(sqlalchemy.ForeignKey('house.house_id'), init=False, repr=False)
    house: orm.Mapped['House'] = orm.relationship(default=None, back_populates='pupils')
    subjects:orm.Mapped[list['Subject']] = orm.relationship(repr=False,default = None,back_populates='pupils', secondary='subject_pupil')

class House(Base):
    __tablename__ = 'house'

    house_id: orm.Mapped[int] = orm.mapped_column(init=False, primary_key=True, repr = False)
    name: orm.Mapped[str] = orm.mapped_column()

    pupils: orm.Mapped[list['Pupil']] = orm.relationship(repr = False, default_factory=list, back_populates='house')

class Subject(Base):
    __tablename__ = 'subject'

    subject_id: orm.Mapped[int] = orm.mapped_column(repr= False, init=False, primary_key=True)
    name: orm.Mapped[str] = orm.mapped_column()
    pupils: orm.Mapped[list['Pupil']] = orm.relationship(repr= False, default_factory=list, back_populates='subjects', secondary='subject_pupil')

class SubjectPupil(Base):
    __tablename__ = 'subject_pupil'
    pupil_id: orm.Mapped[int] = orm.mapped_column(sqlalchemy.ForeignKey('pupil.pupil_id'), init=False, repr=False, primary_key=True)
    subject_id: orm.Mapped[int] = orm.mapped_column(sqlalchemy.ForeignKey('subject.subject_id'), init=False, repr=False,primary_key=True)
