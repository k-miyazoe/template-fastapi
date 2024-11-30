from fastapi import APIRouter
from db import session
from models import TestUserTable, TestUser

# appの代わりにrouterをインスタンスする
router = APIRouter()

# db接続
#　ユーザー情報一覧取得
@router.get("/test_users")
def get_user_list():
    users = session.query(TestUserTable).all()
    session.close()
    return users


# ユーザー情報取得(id指定)
@router.get("/test_users/{user_id}")
def get_user(user_id: int):
    user = session.query(TestUserTable).\
        filter(TestUserTable.id == user_id).first()
    session.close()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# ユーザ情報登録
@router.post("/test_users")
def post_user(user: TestUser):
    try:
        existing_user = session.query(TestUser).filter(
            (TestUser.name == user.name) | (TestUser.email == user.email)
        ).first()

        if existing_user:
            raise HTTPException(status_code=400, detail="User with same name or email already exists")

        db_test_user = TestUser(name=user.name, email=user.email)
        session.add(db_test_user)
        session.commit()
        return {"message": "User created successfully"}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        session.close()

# ユーザ情報更新
@router.put("/test_users/{user_id}")
def put_users(user: TestUser, user_id: int):
    target_user = session.query(TestUserTable).\
        filter(TestUserTable.id == user_id).first()
    target_user.name = user.name
    target_user.email = user.email
    session.commit()
    session.close()