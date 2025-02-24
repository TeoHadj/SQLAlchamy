import sqlalchemy
import sqlalchemy.orm as orm
import model

engine = sqlalchemy.create_engine('sqlite+pysqlite:///pupils.sqlite', echo=False)

with (orm.Session(engine)) as session:
    pupil_th = model.Pupil(first_name = "Teo", last_name = "Hadjinikolov")
    pupil_rc = model.Pupil(first_name = "Ryan", last_name = "Chan")


    session.add(pupil_th)
    session.add(pupil_rc)

    session.commit()