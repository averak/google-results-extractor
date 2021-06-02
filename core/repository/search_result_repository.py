import os
import csv

from core.model.search_result_model import SearchResultModel
from core.config.data_config import DATA_ROOT_DIR


class SearchResultRepository:
    search_result: list[SearchResultModel] = []

    # 一括保存
    def bulk_insert(self, search_results: list[SearchResultModel], keyword: str) -> None:
        search_results.extend(self.find_all(keyword))
        search_results = sorted(set(search_results), key=search_results.index)

        file_name = f"{DATA_ROOT_DIR}/{keyword}.csv"
        with open(file_name, "w") as f:
            writer = csv.writer(f)

            for search_result in search_results:
                writer.writerow([search_result.title, search_result.url])

    # 全件取得
    def find_all(self, keyword: str) -> list[SearchResultModel]:
        result: list[SearchResultModel] = []

        file_name = f"{DATA_ROOT_DIR}/{keyword}.csv"

        # ファイルが存在しない
        if not os.path.exists(file_name):
            return result
        # ファイルが存在する
        with open(file_name, "r") as f:
            records = csv.reader(f)
            result = [SearchResultModel(title=record[0], url=record[1]) for record in records]

        return result
