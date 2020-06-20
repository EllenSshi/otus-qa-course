*** Settings ***
Resource  opencart_keywords.robot
Library  SeleniumLibrary

*** Test Cases ***
User can open Opencart in Chrome
    Открыть пользовательскую часть опенкарт
    Закрыть браузер

Verify featured block is not empty (main page)
    Открыть пользовательскую часть опенкарт
    Проверить что блок Featured не пустой
    Закрыть браузер

Add product to cart (product page)
    Открыть страницу товара   41
    Добавить товар в корзину
    Проверить что в корзине есть этот товар   41
    Закрыть браузер

Add product to comparison (product page)
    Открыть страницу товара   31
    Добавить товар в сравнение товаров
    Перейти на страницу сравнения товаров
    Проверить что товар добавлен на страницу сравнения товаров   31
    Закрыть браузер

Verify search (main page)
    Открыть пользовательскую часть опенкарт
    Ввести текст в строку поиска и нажать Enter   iphone
    Проверить что заголовок страницы результатов поиска содержит строку поиска   iphone
    Закрыть браузер