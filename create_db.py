import sqlalchemy
import sqlalchemy.orm as orm
import model

engine = sqlalchemy.create_engine('sqlite+pysqlite:///pupils.sqlite')
model.Base.metadata.drop_all(engine)
model.Base.metadata.create_all(engine)