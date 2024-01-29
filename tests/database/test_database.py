import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users) 


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    assert len(orders) == 1

    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'


@pytest.mark.database
def test_customer_insert():
    db = Database()
    db.insert_customer(3, 'Andrii', 'Shevchenko str 3', 'Kyiv', '3020', 'Ukraine')
    db.insert_customer(4, 'Alex', 'Mira str 4', 'Dnipro', '4030', 'Ukraine')
    users = db.get_all_users()

    assert len(users) == 4
    assert users[0][0] != users[1][0] != users[2][0] != users[3][0]
    assert users[0][1] != users[1][1] != users[2][1] != users[3][1]
    


@pytest.mark.database
def test_postalcode():
    db = Database()
    user = db.get_postalcode()
    print(user)
    assert user[0][0] > '0'
    assert user[1][0] > '0'
    assert user[2][0] > '0'
    assert user[3][0] > '0'


@pytest.mark.database
def test_table():
    db = Database()
    db.create_table()




@pytest.mark.database
def test_union():
    db = Database()
    users = db.union_tables('Kyiv')
    print(users)
    assert len(users) == 4


    


    
    