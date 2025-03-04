import sqlalchemy
import sqlalchemy.orm as orm
import model

engine = sqlalchemy.create_engine('sqlite+pysqlite:///pupils.sqlite')

with (orm.Session(engine)) as session:

    print("All the pupils")

    pupils = session.query(model.Pupil).all()
    print(pupils)

    for pupil in pupils:
        print(pupil.first_name, pupil.last_name)

    houses = session.query(model.House).all()
    for house in houses:
        print(house.name, house.pupils)