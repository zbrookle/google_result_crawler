from .application import app
from celery import chain
from .web_search import get_search_results, parse_results

terms = ["test term", "test term2", "test term3", "test term4"]


@app.task
def retrieve_search_page(term: str):
    return get_search_results(f"http://www.google.com/search?q={term}")


@app.task
def parse(result_html: str):
    return parse_results(result_html)


@app.task
def count_results(result_urls: list):
    return len(result_urls)


for term in terms:
    chain(retrieve_search_page.s(term) | parse.s()).delay()
