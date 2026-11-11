
from sqlalchemy.orm import Session
from . import models, schemas


def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def get_customers(db: Session):
    return db.query(models.Customer).all()


def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(
        models.Customer.id == customer_id
    ).first()


def get_customer_by_email(db: Session, email: str):
    return db.query(models.Customer).filter(
        models.Customer.email == email
    ).first()


def update_customer(db: Session, customer_id: int, customer: schemas.CustomerUpdate):
    db_customer = get_customer(db, customer_id)

    if not db_customer:
        return None

    for key, value in customer.model_dump().items():
        setattr(db_customer, key, value)

    db.commit()
    db.refresh(db_customer)
    return db_customer


def delete_customer(db: Session, customer_id: int):
    db_customer = get_customer(db, customer_id)

    if not db_customer:
        return False

    db.delete(db_customer)
    db.commit()
    return True
