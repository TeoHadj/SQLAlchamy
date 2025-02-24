import sqlalchemy
import sqlalchemy.orm as orm
import model

engine = sqlalchemy.create_engine('sqlite+pysqlite:///pupils.sqlite')

with (orm.Session(engine)) as session:

    print("All the pupils")

    pupils = session.query(model.Pupil).all()
    print(pupils)