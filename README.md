# otus-qa-course
This repository is for learning QA course by OTUS

# dz9
Запустить все тесты: $pytest -v tests/*

# dz8
Запустить тест: $pytest tests/test_opencart.py [--browser] [--base_url]

По-умолчанию --browser=chrome, --base_url="http://192.168.56.101/"

Опция --browser принимает одно из трех значений: chrome, firefox, safari

----------------------------

# Моя пирамида тестирования:
О проекте: проект написан на Django, REST API, количество пользователей - около 100, разработчики - 2 бэк, 1 фронт;
т.к. система является госзаказом, разработка новых фич начинается после заключения контракта,
любые признаки scrum отсутствуют, релизы как правило объемные и редкие, но с 2020 года решили выкатывать обновления
более мелкими релизами и чаще. Также с нового года планируется разработка с использованием
фича-бранчей (до этого все разработчики работали с одной веткой).

1. UI-тесты
    - ручные: ~500 тест-кейсов, регресс идет 2 дня в 2 человека
    - автоматизированные (на тестируемом проекте): месяца два назад начали создавать тестовый фреймворк
    (используем Django + pytest + selenium + allure), пока написано только 6 автотестов и найден 1 баг с помощью них :)
2. Интеграционные тесты
    - можно сказать, что отсутствуют (есть коллекция в Postman для тестирования API, но там только по одному позитивному
     тесту на каждый endpoint)
    - во время регресса отдельно API не тестируется
    - нагрузочное тестирование не проводится
3. Unit-тесты
    - пишут как бэк-разработчики (много), так и фронт (мало, только критичные моменты).
    - измеряли покрытие python-кода в проекте средствами pycharm-а,
    показало в разных модулях 90-98% покрытия
    
Преимущества: преимуществом считаю добросовестный подход разработчиков к написанию unit-тестов

Недостатки: недостатком считаю полное отсутствие тестирования API, документация к API появилась только месяц назад,
хотя проекту уже больше года (разработать документацию было моей идеей). Когда подняла вопрос о необходимости 
тестирования API, например, в Postman, аналитики сказали, что если есть баги, которые пользователи не смогут повторить 
через UI, то они нас не интересуют, предложили заниматься тестированием API в фоновом режиме, когда нет других задач :)

Сама не знаю, как правильно поступить в такой ситуации, но считаю, что в случае изменения поведения на фронте 
(что случается не редко) могут всплывать баги бэка, которые мы могли исправить ранее, если бы тестировали API.