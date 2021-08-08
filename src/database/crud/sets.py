from sqlalchemy.orm import Session

from src.models.crud.sets import Sets
from src.database import schemas


def create_set(db: Session, set: Sets):
    newSet = schemas.Set(reps=set.reps, weight=set.weight,
                         exercise_id=set.exerciseId)
    db.add(newSet)
    db.commit()
    db.refresh(newSet)
    return newSet


def get_set(db: Session):
    pass


def update_set(db: Session, setId, updateSet):
    updated = db.query(schemas.Set).filter(
        schemas.Set.id == setId).update(updateSet.dict())
    db.commit()
    return updated


def delete_set(db: Session):
    pass
