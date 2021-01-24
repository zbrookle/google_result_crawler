from project.application import app
from project.web_search import get_search_results, parse_results
from typing import Callable, List
import random

terms = ["test term", "test term2", "test term3", "test term4"]


def fail_chance_decorator(function: Callable):
    num = random.randint(1, 10)
    if num <= 2:

        def retfunc(*args, **kwargs):
            raise Exception("Failure!")

        return retfunc
    return function


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    for term in terms:
        sender.add_periodic_task(10.0, chained_process.s(term))


@app.task(bind=True, name="chained_process", track_started=True)
def chained_process(self, term: str):
    chain_sig = retrieve_search_page.s(term) | parse.s() | count_results.s()
    chain_sig()


@app.task(bind=True)
def retrieve_search_page(self, term: str):
    return get_search_results(f"http://www.google.com/search?q={term}")


@app.task(bind=True)
def parse(self, result_html: str):
    return parse_results(result_html)


@app.task(bind=True)
def count_results(self, result_urls: List[str]):
    return len(result_urls)
