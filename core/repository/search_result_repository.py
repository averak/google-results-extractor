from core.model.search_result_model import SearchResultModel


class SearchResultRepository:
    search_result: list[SearchResultModel] = []

    # 一括保存
    def bulk_insert(self, search_results: list[SearchResultModel]) -> None:
        self.search_result.extend(search_results)

    # 全件取得
    def find_all(self) -> list[SearchResultModel]:
        return self.search_result
