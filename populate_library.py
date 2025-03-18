import sqlalchemy
import sqlalchemy.orm as orm
import model

engine = sqlalchemy.create_engine('sqlite:///library.sqlite', echo=False)

with (orm.Session(engine)) as session:
    p1 = model.Publisher(name='Penguin')
    p2 = model.Publisher(name='RandomHouse')
    p3 = model.Publisher(name='Puffin')

    session.add(p1)
    session.add(p2)
    session.add(p3)

    a1 = model.Author(first_name='Roald', last_name='Dahl')
    a2 = model.Author(first_name='Michael', last_name='Mopurgo')
    a3 = model.Author(first_name='Stephen', last_name='King')
    a4 = model.Author(first_name='William', last_name='Shakespeare')
    a5 = model.Author(first_name='JK', last_name='Rowling')
    session.add_all([a1, a2, a3, a4, a5])

    b1 = model.Book(name = "Hamlet", publisher=p1, author = [a4])
    b2 = model.Book(name = "Harry Potter", publisher=p2, author = [a3, a5])