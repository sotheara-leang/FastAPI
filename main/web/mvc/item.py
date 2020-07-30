from fastapi import APIRouter, Request

from main.web import templates

router = APIRouter()


@router.get("/{id}")
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item/index.html", {"request": request, "id": id})
