#!/usr/bin/env python

from core.service.search_result_service import SearchResultService

search_result_service = SearchResultService()
search_result_service.fetch_search_results("site;医師監修")
