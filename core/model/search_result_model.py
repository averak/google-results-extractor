from pydantic import BaseModel


class SearchResultModel(BaseModel):
    title: str
    url: str
