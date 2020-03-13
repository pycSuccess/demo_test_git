#coding:utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, UniqueConstraint, ForeignKeyConstraint, Index
from sqlalchemy.orm import sessionmaker

egine = create_engine('mysql+pymysql://root@127.0.0.1:3306/db1?charset=utf8', max_overflow=5)
Base = declarative_base()

# 单个服务
class Business(Base):
    __tablename__ ='business'
    id = Column(Integer, primary_key=True, autoincrement=True)
    bname = Column(String(32), nullable=False, index=True)


# 一对多
class Service(Base):
    __tablename__ = 'service'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sname = Column(String(32), nullable=False, index=True)
    ip = Column(String(15), nullable=False)
    port = Column(Integer, nullable=False)

    business_id = Column(Integer, ForeignKey('business.id'))
    __table_args__ = (
        UniqueConstraint(ip, port, name = 'uix_ip_port'),
        Index('ix_id_sname', id, sname)
    )


#一对一
class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True, autoincrement=True)
    rname = Column(String(32), nullable=False, index=True)
    priv = Column(String(64), nullable=False)

    business_id = Column(Integer, ForeignKey('business_id'), unique=True)


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(String(32), nullable=False, index=True)


class User2Role(Base):
    __tablename__ = 'users2role'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, ForeignKey('users.id'))
    rid = Column(Integer, ForeignKey('role.id'))

    __table_args__=(
        UniqueConstraint(uid,rid, name='uix_uid_rid')
    )