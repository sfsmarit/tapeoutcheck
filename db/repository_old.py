from sqlalchemy.orm import Session, declarative_base


Base = declarative_base()

def add_user(session: Session, name: str, age: int) -> User:
    new_user = User(name=name, age=age)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

def get_all_users(session: Session) -> list[User]:
    return session.query(User).all()

def get_user_by_id(session: Session, user_id: int) -> User | None:
    return session.query(User).filter(User.id == user_id).first()

def update_user(session: Session, user_id: int, name: str = None, age: int = None) -> User | None:
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        if name is not None:
            user.name = name
        if age is not None:
            user.age = age
        session.commit()
        session.refresh(user)
    return user

def delete_user(session: Session, user_id: int) -> bool:
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
        return True
    return False