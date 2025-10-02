from sqlalchemy.orm import Session, declarative_base


class Respository:
    def __init__(self, session: Session, model_class) -> None:
        self.session = session
        self.model_class = model_class

    def get_by_id(self, id: int):
        return self.session.query(self.model_class).filter(self.model_class.id == id).first()

    def get_by_fields(self, **kwargs):
        query = self.session.query(self.model_class)
        for key, value in kwargs.items():
            if hasattr(self.model_class, key):
                query = query.filter(getattr(self.model_class, key) == value)
        return query.first()

    def get_all(self):
        return self.session.query(self.model_class).all()

    def get_all_by_fields(self, **kwargs):
        query = self.session.query(self.model_class)
        for key, value in kwargs.items():
            if hasattr(self.model_class, key):
                query = query.filter(getattr(self.model_class, key) == value)
        return query.all()

    def get_id_by_fields(self, **kwargs) -> int | None:
        query = self.session.query(self.model_class.id)
        for key, value in kwargs.items():
            if hasattr(self.model_class, key):
                query = query.filter(getattr(self.model_class, key) == value)
        result = query.first()
        return result[0] if result else None
    
    def add(self, **kwargs):
        obj = self.model_class(**kwargs)
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    def update(self, id: int, **kwargs):
        obj = self.get_by_id(id)
        if obj:
            for key, value in kwargs.items():
                if hasattr(obj, key):
                    setattr(obj, key, value)
            self.session.commit()
            self.session.refresh(obj)
        return obj

    def delete(self, id: int):
        obj = self.get_by_id(id)
        if obj:
            self.session.delete(obj)
            self.session.commit()
