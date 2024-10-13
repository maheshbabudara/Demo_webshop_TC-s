from POM.Buy_product import Buy

def test_Buy_product(Buy_product):
    b=Buy(Buy_product)
    b.order()
    assert Buy_product.find_element('xpath',"//strong[text()='Your order has been successfully processed!']").is_displayed()