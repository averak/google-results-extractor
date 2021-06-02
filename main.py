#!/usr/bin/env python

from core.service.search_result_service import SearchResultService

search_result_service = SearchResultService()


keywords = [
    "医師監修",
    "医師執筆",
    "記事監修",
]

for keyword in keywords:
    print(keyword)
    search_results = search_result_service.fetch_search_results(f"site;{keyword}")
    search_result_service.export_search_results(search_results, keyword)
