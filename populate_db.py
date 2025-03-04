import sqlalchemy
import sqlalchemy.orm as orm
import model

engine = sqlalchemy.create_engine('sqlite+pysqlite:///pupils.sqlite', echo=False)

with (orm.Session(engine)) as session:
    h1 = model.House(name="Southgate")
    h2 = model.House(name="Northgate")
    h3 = model.House(name="Queensgate")
    session.add(h1)
    session.add(h2)
    session.add(h3)

    pupil_th = model.Pupil(first_name = "Teo", last_name = "Hadjinikolov", house=h2)
    pupil_rc = model.Pupil(first_name = "Ryan", last_name = "Chan", house=h1)
    pupil_ah = model.Pupil(first_name = "Arthur", last_name = "Hassabis", house = h3)



    session.add(pupil_th)
    session.add(pupil_rc)
    session.add(pupil_ah)


    session.commit()