from sqlalchemy import Column , Integer , String , DateTime
from app.database import Base

class shimpment(Base):

    __tablename__ = "shimpments"

    id = Column(Integer , primary_key = True , index = True)
    source = Column(String , nullable = False)
    destination = Column(String , nullable = False)
    status = Column(String , nullable = False)
    delay_hours = Column(Integer , default=0)

    

