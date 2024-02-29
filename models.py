from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Numeric, Boolean
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()


class Providers(Base):
    __tablename__ = 'Поставщик'
    КодПоставщика = Column(Integer(), primary_key=True)
    НазваниеПоставщика = Column(String(100), nullable=False)
    ПредставительПоставщика = Column(String(100), nullable=False)
    Обращаться = Column(String(100), nullable=False)
    КонтактныйТелефон = Column(String(15), nullable=False)
    Адрес = Column(String(100), nullable=False)


class Supplys(Base):
    __tablename__ = 'Поставка'
    КодПоставки = Column(Integer(), primary_key=True)
    КодПоставщика = Column(Integer(), ForeignKey('Поставщик.КодПоставщика', ondelete='CASCADE'), nullable=False)
    Дата = Column(DateTime(), default=datetime.now)


class Products(Base):
    __tablename__ = 'Товары'
    КодТовара = Column(Integer(), primary_key=True)
    КодПоставки = Column(Integer(), ForeignKey('Поставка.КодПоставки', ondelete='CASCADE'), nullable=False)
    НаименованиеТовара = Column(String(), nullable=False)
    ТехническиеХарактеристики = Column(String(), nullable=False)
    Описание = Column(Text(), nullable=False)
    Изображение = Column(String(), nullable=False)
    СтоимостьЗакупки = Column(Numeric(18, 2), nullable=False)
    Наличие = Column(Boolean(), nullable=False)
    Количество = Column(Integer(), nullable=False)
    СтоимостьПродажи = Column(Numeric(18, 2), nullable=False)


class Clients(Base):
    __tablename__ = 'Клиенты'
    Код = Column(Integer(), primary_key=True)
    ФИО = Column(String(100), nullable=False)
    Адрес = Column(String(50), nullable=False)
    Телефон = Column(String(15), nullable=False)


class Employees(Base):
    __tablename__ = 'Сотрудники'
    КодСотрудника = Column(Integer(), primary_key=True)
    Фамилия = Column(String(30), nullable=False)
    Имя = Column(String(30), nullable=False)
    Отчество = Column(String(30), nullable=False)
    Должность = Column(String(15), nullable=False)
    Адрес = Column(String(100), nullable=False)
    ДомашнийТелефон = Column(String(15), nullable=False)
    ДатаРождения = Column(DateTime(), nullable=False)


class Orders(Base):
    __tablename__ = 'Заказы'
    КодЗаказа = Column(Integer(), primary_key=True)
    КодСотрудника = Column(Integer(), ForeignKey('Сотрудники.КодСотрудника'), nullable=False)
    КодТовара = Column(Integer(), ForeignKey('Товары.КодТовара', ondelete='CASCADE'), nullable=False)
    ДатаРазмещения = Column(DateTime(), nullable=False)
    ДатаИсполнения = Column(DateTime(), nullable=False)
    КодКлиента = Column(Integer(), ForeignKey('Клиенты.Код'), nullable=False)
