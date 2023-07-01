from fastapi.routing import APIRouter

from food_order_system.web.api.routes import monitoring, user

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(user.router)
