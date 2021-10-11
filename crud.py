from sqlalchemy.orm import Session

from . import models, schemas


def get_request(db: Session, order_id: int):
    return db.query(models.Request).filter(models.Request.order_id == order_id).first()


def create_request(db: Session, item: schemas.RequestItem):
    db_item = models.Request(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

