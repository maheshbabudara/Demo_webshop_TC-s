import pytest

from POM.Advance_search import advance
from time import sleep



@pytest.mark.advancesearch
def test_search(advancesearch):
    s=advance(advancesearch)
    s.advance_search_call('shoe')
    assert advancesearch.find_element('xpath','//a[contains(text(),"Running Shoe")]').is_displayed()
    # driver.close()

@pytest.mark.advancesearch
def test_search_computers(advance_invalid):
    s=advance(advance_invalid)
    s.advance_search_computer('shoe')
    assert advance_invalid.find_element('xpath','//strong[@class="result"]').is_displayed()


