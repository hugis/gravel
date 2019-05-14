import os

from sqlalchemy import Boolean, Column, ForeignKey, Float, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://localhost:5432/gravel", echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Device(Base):
    __tablename__ = "tbl_devices"

    id = Column("dev_id", Integer, primary_key=True)
    description = Column("dev_description", String(50))
    street = Column("dev_street", String(100))
    city = Column("dev_city", String(100))
    zip_code = Column("dev_zip_code", String(20))

    def __repr__(self):
        return (
            f"<Device(id={self.id}, description='{self.description}', "
            f"street='{self.street}', city='{self.city}', zip_code='{self.zip_code}')>"
        )


class Value(Base):
    __tablename__ = "tbl_values"

    id = Column("val_id", Integer, primary_key=True)
    dev_id = Column("val_dev_id", Integer, ForeignKey("tbl_devices.dev_id"))
    timestamp = Column("val_timestamp", DateTime)
    frequency = Column("val_frequency", Float)
    u_1 = Column("val_u_1", Float)
    i_1 = Column("val_i_1", Float)
    fi_1 = Column("val_fi_1", Float)
    p_1 = Column("val_p_1", Float)
    q_1 = Column("val_q_1", Float)
    u_2 = Column("val_u_2", Float)
    i_2 = Column("val_i_2", Float)
    fi_2 = Column("val_fi_2", Float)
    p_2 = Column("val_p_2", Float)
    q_2 = Column("val_q_2", Float)
    u_3 = Column("val_u_3", Float)
    i_3 = Column("val_i_3", Float)
    fi_3 = Column("val_fi_3", Float)
    p_3 = Column("val_p_3", Float)
    q_3 = Column("val_q_3", Float)
    prev_id = Column("val_prev_id", Integer)
    export = Column("val_export", Boolean)

    def __repr__(self):
        return (
            f"<Value(id={self.id}, dev_id={self.dev_id}, timestamp='{self.timestamp}', "
            f"frequency={self.frequency}), "
            f"u_1={self.u_1}, i_1={self.i_1}, fi_1={self.fi_1}, p_1={self.p_1}, q_1={self.q_1}, "
            f"u_2={self.u_2}, i_2={self.i_2}, fi_2={self.fi_2}, p_2={self.p_2}, q_2={self.q_2}, "
            f"u_3={self.u_3}, i_3={self.i_3}, fi_3={self.fi_3}, p_3={self.p_3}, q_3={self.q_3}, "
            f"prev_id={self.prev_id}, export={self.export}>"
        )
