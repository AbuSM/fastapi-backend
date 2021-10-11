from sqlalchemy.orm import Session

import models
import schemas
from utils import generate_string


def get_request(db: Session, order_id: int):
    return db.query(models.Request).filter(models.Request.order_id == order_id).first()


def create_request(db: Session, item: schemas.RequestItem):
    link_id = generate_string(10)
    db_item = models.Request(link_id=link_id, **item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

