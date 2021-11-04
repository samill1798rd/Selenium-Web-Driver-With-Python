
import pytest
from pages import search
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

@pytest.mark.parametrize('phrase',['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "panda"

    #Given the DuckDuckGo home page is deplayed
    search_page.load()    

    #When the user searches for "panda"
    search_page.search(PHRASE)

    #And then search result query is "panda"
    assert PHRASE == result_page.search_input_value()

    #And the result links pertain to "panda"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if PHRASE.lower() in t.lower()]
    assert len(matches) > 0

    #Then the search resul title contains "panda"
    assert PHRASE in result_page.title()    

def  test_search():
    assert True
     