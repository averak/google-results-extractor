import time
from pycrawl import PyCrawl

from core.model.search_result_model import SearchResultModel
from core.repository.search_result_repository import SearchResultRepository
from core.config.crawler_config import USER_AGENT, DELAY, DEPTH_LIMIT


class SearchResultService:
    search_result_repository = SearchResultRepository()

    # 検索結果一覧を取得
    def fetch_search_results(self, keyword: str) -> list[SearchResultModel]:
        result: list[SearchResultModel] = []

        number_of_page: int = 10
        page_index: int = 0
        while True:
            start_index: int = page_index * number_of_page
            doc = PyCrawl(
                f"https://www.google.com/search?&filter=0&q={keyword}&start={start_index}",
                user_agent=USER_AGENT,
            )
            print(f"ACCESS({page_index}): {doc.url}")

            # pycrawlオブジェクトを検索結果モデルに変換
            def search_result_builder(col):
                return SearchResultModel(
                    title=col.css("h3").inner_text(),
                    url=col.css("a").attr("href"),
                )

            columns = doc.css("#res").css(".yuRUbf")
            result.extend([search_result_builder(col) for col in columns])

            # 存在する場合は次のページへ
            if doc.css("#pnnext") == []:
                break
            else:
                page_index += 1

                # クロールする上限
                if page_index >= DEPTH_LIMIT:
                    break

                time.sleep(DELAY)

        return result

    # 検索結果をエクスポート
    def export_search_results(self, search_results: list[SearchResultModel]) -> None:
        self.search_result_repository.bulk_insert(search_results)
