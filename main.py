from sqlalchemy import create_engine
from sqlalchemy.sql import functions
from sqlalchemy.engine import URL
from models import Base, Providers
from sqlalchemy.orm import sessionmaker
from data import *

url = URL.create(
    drivername="postgresql",
    username="postgres",
    host="localhost",
    database="test"
)


def main():
    engine = create_engine(url)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add_all([Providers1, Providers2, Providers3, Providers4, Providers5])
    session.commit()
    session.add_all([Supply1, Supply2, Supply3, Supply4, Supply5])
    session.commit()
    session.add_all([Product1, Product2, Product3, Product4, Product5])
    session.commit()
    session.add_all([Client1, Client2, Client3, Client4, Client5])
    session.commit()
    session.add_all([Employee1, Employee2, Employee3, Employee4, Employee5])
    session.commit()
    session.add_all([Order1, Order2, Order3, Order4, Order5])
    session.commit()

    # print(str(session.query(Clients).filter(Clients.Код == 2))) #Посмтотреть запрос
    result = session.query(Clients.Код, Clients.ФИО, Clients.Адрес).filter(Clients.Код == 2).all()
    for client in result:
        print(client)
    print('****************************************************************')

    result = session.query(Supplys.КодПоставки, Supplys.Дата, Providers.НазваниеПоставщика).join(Providers)
    for supply in result:
        print(supply)
    print('****************************************************************')

    session.query(Clients).filter(Clients.Код == 1).update(
        {'ФИО': 'Быков Дмитрий Алексеевич', 'Телефон': '+375295413866'})
    session.commit()
    result = session.query(Clients).filter(Clients.Код == 1)
    for client in result:
        print(client.__dict__)
    print('****************************************************************')

    result = session.query(Products.КодТовара, Products.НаименованиеТовара, Products.СтоимостьЗакупки).order_by(
        Products.СтоимостьЗакупки)
    for product in result:
        print(product)
    print('****************************************************************')

    result = session.query(Products.КодТовара, Products.НаименованиеТовара, functions.sum(Products.СтоимостьЗакупки * Products.Количество)).group_by(Products.КодТовара).order_by(Products.КодТовара)
    for product in result:
        print(product)
    print('****************************************************************')

    session.query(Providers).filter(Providers.КодПоставщика == 1).delete(synchronize_session='evaluate')
    session.query(Providers).filter(Providers.КодПоставщика == 2).delete(synchronize_session='evaluate')

    result = session.query(Providers.КодПоставщика, Providers.НазваниеПоставщика)
    for provider in result:
        print(provider)
    print('****************************************************************')


if __name__ == '__main__':
    main()
