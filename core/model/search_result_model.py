from pydantic import BaseModel


class SearchResultModel(BaseModel):
    title: str
    url: str

    def __eq__(self, other):
        return self.url == other.url

    def __hash__(self):
        return hash(self.url)
