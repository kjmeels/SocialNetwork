from fastapi import APIRouter

from .api.router import router as api_router
from .social_network.router import router as social_network_router

router = APIRouter()
router.include_router(router=api_router)
router.include_router(router=social_network_router)
