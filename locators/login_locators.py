class LoginLocators:
    EMAIL_INPUT = '//input[@name="name" or @name="email"]'
    PASSWORD_INPUT = '//input[@type="password"]'
    SUBMIT_BUTTON = '//button[text()="Войти"]'
    SHOW_PASSWORD_ICON = '//div[contains(@class,"input__icon-action")]/..'
    RESTORE_PASSWORD_LINK = '//a[text()="Восстановить пароль"]'
    RESTORE_EMAIL_INPUT = '//input[@name="email"]'
    RESTORE_BUTTON = '//button[text()="Восстановить"]'
