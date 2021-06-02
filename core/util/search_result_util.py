from pycrawl import PyCrawl

from core.model.search_result_model import SearchResultModel


# pycrawlオブジェクトを検索結果モデルに変換するビルダー
def search_result_builder(col: PyCrawl):
    return SearchResultModel(
        title=col.css("h3").inner_text(),
        url=col.css("a").attr("href"),
    )
