# goit_python_web_hw_10
GoIT, Python WEB, Homework number 10. Django. PostgreSQL. Docker. MongoDB. 

# Домашнє завдання #10

У минулій домашній роботі ви виконували скрапінг сайту http://quotes.toscrape.com.

Вам необхідно самостійно реалізувати аналог такого сайту на Django.

1. Реалізуйте можливість реєстрації на сайті та вхід на сайт.
2. Можливість додавання нового автора на сайт лише для зареєстрованого користувача.
3. Можливість додавання нової цитати на сайт із зазначенням автора тільки для зареєстрованого користувача.
4. Виконайте міграцію бази даних із MongoDB, яка у вас є, у Postgres для вашого сайту. Можна реалізувати кастомним скриптом. (За бажанням можете залишити та працювати з цитатами та авторами в MongoDB, а з користувачами у Postgres)
5. Можна зайти на сторінку кожного автора без автентифікації користувача
6. Усі цитати доступні для перегляду без автентифікації користувача

## Додаткова частина

1. Реалізуйте пошук цитат за тегами. При натисканні на тег, виводиться список цитат з цим тегом.
2. Реалізуйте блок "Top Ten tags" та виведення найпопулярніших тегів.
3. Реалізуйте пагінацію. Це кнопки next та previous
4. Замість перенесення даних з бази даних MongoDB, реалізуйте можливість скрапінгу даних прямо з вашого сайту по натисканню певної кнопки на формі та наповнення бази даних сайту.


# RESULT

1. User SignUP / Login
    ![user-signup-01](doc/user-signup-01.png)

    ![user-signup-02](doc/user-signup-02.png)

    ![user-signup-03](doc/user-signup-03.png)

    ![user-signup-04](doc/user-signup-04.png)

    ![user-signup-05](doc/user-signup-05.png)

    ![user-logged-01](doc/user-logged-01.png)

2. Add Authors only Auth
    ![user-signup-01](doc/add_author_01.png)

    ![user-signup-02](doc/add_author_02.png)
- Add Tag only Auth
    ![add-tag-01](doc/add_tag_01.png)

    ![add-tag-02](doc/add_tag_02.png)

3. Add Quote only Auth
    ![add-quote-01](doc/add_quote_01.png)

    ![add-quote-02](doc/add_quote_02.png)

    ![add-quote-03](doc/add_quote_03.png)

    ![add-quote-04](doc/add_quote_04.png)

    ![add-quote-05](doc/add_quote_05.png)





4. MongoDB -> PostgresSQL

    python -m utils.migration

    `scripts\mongo2pg.cmd`

    MongoDB (cloud):
    ![migration-mongo](doc/migration-mongo-01.png)
    PostgreSQL (docker):
    ![migration-pg](doc/migration-pg-01.png)


5. Author
   ![Author](doc/author_01.png)
6. Quotes
    ![quotes_list_01](doc/quotes_list_01.png)

## Додаткова частина

1. Quotes by tags
    ![quote_bytag](doc/quote_bytag_list_01.png)

3. Pagination
    ![quotes_list_01](doc/quotes_list_01.png)
    ![quotes_list_02](doc/quotes_list_02.png)



## Addon HW 13
### PASSWORD RESET
Added email filed:
![](doc/signup-01.png)

![](doc/password-reset-06.png)

![](doc/password-reset-05.png)

![](doc/password-reset-01.png)

![](doc/password-reset-02.png)

![](doc/password-reset-03.png)

![](doc/password-reset-04.png)


### PROFILE
![](doc/profile-01.png)

![](doc/profile-02-meida.png)

![](doc/user-delete-01.png)


