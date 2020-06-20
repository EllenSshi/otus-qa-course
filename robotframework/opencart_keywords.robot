*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${URL}   http://demo-opencart.ru/index.php
${ADMIN_URL}   http://demo-opencart.ru/admin/index.php

*** Keywords ***
Открыть пользовательскую часть опенкарт
    Open Browser      ${URL}   Chrome
    Title should be   Your Store

Открыть административную часть опенкарт
    Open Browser      ${ADMIN_URL}   Chrome
    Title should be   Авторизация

Авторизоваться в административной части опенкарт
    [arguments]       ${LOGIN}  ${PASSWORD}
    Input Text        css:input#input-username   ${LOGIN}
    Input Text        css:input#input-password   ${PASSWORD}
    Click element     css:button[type=submit]

Проверить что администратор авторизован
    Title should be   Панель состояния

Проверить что авторизации в административную часть не произошло
    Element should be visible   xpath://div[contains(text(), ' Такой логин и/или пароль не существует!')]

Перейти в список заказов
    Click element     css:a[href='#collapse26']
    Click element     css:#collapse26 a[href*='sale/order']
    Element Text Should Be     css:h1   Заказы

Поиск по номеру заказа
    [arguments]       ${ORDER_ID}
    Input text        css:#input-order-id   ${ORDER_ID}
    Click element     css:#button-filter

Проверить что заказ с таким номером нашелся
    [arguments]       ${ORDER_ID}
    Element Text Should Be     css:#form-order tbody>tr>td:nth-child(2)   ${ORDER_ID}

Перейти в список производителей
    Set browser implicit wait   3 seconds
    Click element     css:a[href='#collapse1']
    Click element     css:#collapse1 a[href*='catalog/manufacturer']
    Element Text Should Be    css:h1   Производители

Добавить производителя
    [arguments]       ${NAME}
    Click element     css:a[data-original-title='Добавить']
    Input text        css:#input-name   ${NAME}
    Click element     css:button[data-original-title='Сохранить']

Проверить что у пользователя нет прав на добавление производителя
    Element Should Be Visible     css:.alert-danger

Проверить что блок Featured не пустой
    Element should be visible   class:image

Открыть страницу товара
    [arguments]       ${PRODUCT_ID}
    Open browser      ${URL}?route=product/product&product_id=${PRODUCT_ID}   Chrome

Добавить товар в корзину
    Click element     css:button#button-cart

Проверить что в корзине есть этот товар
    [arguments]       ${PRODUCT_ID}
    Set browser implicit wait   3 seconds
    Click element     css:.btn-inverse
    Element should be visible   css:tr>*:nth-child(2)>a[href*='product_id=${PRODUCT_ID}']

Добавить товар в сравнение товаров
    Click element     css:button[data-original-title="Compare this Product"]

Перейти на страницу сравнения товаров
    Set browser implicit wait   3 seconds
    Click element     partial link:product comparison

Проверить что товар добавлен на страницу сравнения товаров
    [arguments]       ${PRODUCT_ID}
    Element should be visible   css:tr>*:nth-child(2)>a[href*='product_id=${PRODUCT_ID}']

Ввести текст в строку поиска и нажать Enter
    [arguments]       ${TEXT}
    Input Text        css:#search>input[name=search]   ${TEXT}
    Press Keys        css:#search>input[name=search]   RETURN

Проверить что заголовок страницы результатов поиска содержит строку поиска
    [arguments]       ${TEXT}
    Element Text Should Be    css:#content>h1   Search - ${TEXT}

Разлогиниться
    Click element     css:a[href*='common/logout']

Проверить что администратор не авторизован
    Element text should be    css:h1    Введите логин и пароль

Закрыть браузер
    Close Browser