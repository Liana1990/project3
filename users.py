from fastapi import APIRouter

from schemas import UserChangeUsernameSchema
from fastapi import Depends
import main
from security import get_current_user

users_router = APIRouter(tags=["Users"])


@users_router.put("/api/change-username")
def change_username(username_change_data: UserChangeUsernameSchema,token=Depends(get_current_user)): #sa asum e, vor user@ token ta
    user_id = username_change_data.user_id
    new_username = username_change_data.new_username

    main.cursor.execute("""UPDATE users SET name=%s WHERE id=%s""",
                        (new_username, user_id))
    main.conn.commit()

    return "OK"
