class FeedLocators:
    ORDER_CARD = '//li[contains(@class,"OrderHistory_orderHistory__")]'
    ORDER_MODAL = '//div[contains(@class,"Modal_modal__")]'
    TOTAL_DONE = '//p[text()="Выполнено за все время:"]/following-sibling::p'
    TODAY_DONE = '//p[text()="Выполнено за сегодня:"]/following-sibling::p'