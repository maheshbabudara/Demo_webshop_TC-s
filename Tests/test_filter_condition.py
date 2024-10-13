from POM.filter_conditions import filter

def test_filter_condition(fil_con):
    f=filter(fil_con)
    f.fil()
    assert fil_con.find_element('xpath','//div[@class="selected-price-range"]').is_displayed()
