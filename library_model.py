import sqlalchemy
import sqlalchemy.orm as orm

class Base(orm.DeclarativeBase, orm.MappedAsDataclass):
    pass

class Author(Base):
    __tablename__ = 'author'

    author_id: orm.Mapped[int] = orm.mapped_column(init=False, primary_key=True)
    first_name: orm.Mapped[str] = orm.mapped_column()
    last_name: orm.Mapped[str] = orm.mapped_column()
    # pupil_house_id: orm.Mapped[int] = orm.mapped_column()
    publisher_id: orm.Mapped[int]=orm.mapped_column(sqlalchemy.ForeignKey('publisher.publisher_id'), init=False, repr=False)
    publisher: orm.Mapped['Publisher'] = orm.relationship(default=None, back_populates='authors')

    books:orm.Mapped[list['Book']] = orm.relationship(repr=False,default = None,back_populates='authors', secondary='book_author')



class Publisher(Base):
    __tablename__ = 'publisher'

    publisher_id: orm.Mapped[int] = orm.mapped_column(init=False, primary_key=True, repr = False)
    name: orm.Mapped[str] = orm.mapped_column()

    authors: orm.Mapped[list['Author']] = orm.relationship(repr = False, default_factory=list, back_populates='publisher')
    books: orm.Mapped[list['Book']] = orm.relationship(repr=False, default_factory=list, back_populates='publisher')

class Book(Base):
    __tablename__ = 'book'

    book_id: orm.Mapped[int] = orm.mapped_column(repr= False, init=False, primary_key=True)
    name: orm.Mapped[str] = orm.mapped_column()
    authors: orm.Mapped[list['Author']] = orm.relationship(repr= False, default_factory=list, back_populates='books', secondary='book_author')
    publisher_id: orm.Mapped[int] = orm.mapped_column(sqlalchemy.ForeignKey('publisher.publisher_id'), init=False,
                                                      repr=False)
    publisher: orm.Mapped['Publisher'] = orm.relationship(default=None, back_populates='books')

class BookAuthor(Base):
    __tablename__ = 'book_author'
    author_id: orm.Mapped[int] = orm.mapped_column(sqlalchemy.ForeignKey('author.author_id'), init=False, repr=False, primary_key=True)
    book_id: orm.Mapped[int] = orm.mapped_column(sqlalchemy.ForeignKey('book.book_id'), init=False, repr=False,primary_key=True)
