# 01

Flask — микрофреймворк Python. Армин Ронахер создал его в 2010

## Установка в виртуальное окружение

```bash
python3 -m venv .venv
cd .venv
.venv/bin/activate
pip install Flask
```

### Устанавливаемые зависимости

- Werkzeug - сервер WSGI, отвечает за обработку HTTP-запросов и ответов, роутинг, дебагер и релоудер
- Jinja2 - шаблонизатор
- click - консольная команда flask
- itsdangerous - утилита для защиты от уязвимостей
- markupsafe - утилита для защиты от уязвимостей

### Веб-приложение

[Hello world](lesson_1/app_01.py)

Создаем экземпляр класса `Flask` по имени `app`, которому передаем имя текущего модуля

```python
app = Flask(__name__)
```

Декоратор `app.route` позволяет определить маршрут, при вводе которого будет выполняться функция `hello_world`

```python
@app.route('/')
def hello_world():
    return 'Hello, World!'
```

Функция может возвращать в том числе и строковые значения.

Функция app.run() отвечает за запуск веб-сервера с переданными ей параметрами

```python
app.run(host='0.0.0.0', port=5500)
```

## Запуск веб-приложения

Запустить приложение flask можно несколькими способами

1. Через IDE: с помощью кнопки "Run" в верхнем правом углу VSC
2. Классическим способом: `python3 module_name.py` 
3. С помощью пакета click: `flask --app module_name.py run` 
4. С помощью скрипта wsgi.py: `flask run`

### wsgi.py

При выполнении команды `flask run` ищется файл `wsgi.py` в текущей директории и в случае его наличия запускается веб-сервер.

wsgi.py файл содержит строку, которая импортирует приложение из нужной директории и условие запуска веб-сервера с необходимыми параметрами:

```python
from package.module_name import app

if __name__ == "__main__":
    app.run(debug=True)
```

## View функция

Или функция-представление

Декоратор `@app.route()` используется для привязки роутинга `hello` к функции-представлению `hello()`:

```python
@app.route('/hello/')
def hello():
    return 'Hello, World!'
```

При отрытии в браузере http://127.0.0.1:5500/hello/ выводится строка `Hello, World!`

**Важно** не забывать ставить слеш в конце роутинга, который передаётся в route().

Одна функция-представление может быть привязана к нескольким декораторам:

```python
@app.route('/Фёдор/')
@app.route('/Fedor/')
@app.route('/Федя/')
def fedor():
    return 'Привет, Феодор!'
```

## Переменные

Через роутинг можно передать переменную в функцию-представление:

```python
@app.route('/<name>/')
def hello(name):
    return f'Hello, {name}!'
```

где `<name>` переменная передаваемая через строку браузера, т.е. является частью адреса url, в функции-представлении переменная используется без треугольных кавычек.

### Типы переменных

- [string](lesson_1/app_02.py) (по умолчанию), строка без слешей
- int целые положительные числа
- [float](lesson_1/app_03.py) вещественные числа
- [path](lesson_1/app_04.py) путь к файлу, т.е. строка включая слэши
- uuid уникальный идентификатор

При передаче другого типа данных вызовет ошибку 404

## Вывод HTML

### Многострочный текст

[Используя тройные кавычки](lesson_1/app_05.py)

### Рендеринг HTML файла

Чтобы отрисовать файл [index.html](lesson_1/templates/index.html) в браузере:

1. html-файл нужно поместить в папку `templates`, расположенной на одном уровне с запускаемым веб-приложением.
2. в приложении пайтона нужно подключить функцию отрисовки шаблона из библиотеки Flask:

```python
from flask import render_template
```

3. в функции-представлении нужно вернуть функцию отрисовки с указанием html-файла в качестве аргумента:

```python
@app.route('/index/')
def html_index():
    return render_template('index.html')
```

[Полный код рендеринга файла html](lesson_1/app_06.py)

## Шаблонизатор Jinja

Отрисовкой html файлов занимается библиотека Jinja, она превращает статические html-страницы в шаблоны для формирования переиспользуемого контента


### Проброс контекста из функции-представления в шаблон

Функция render_template после имени шаблона может принимать неограниченное число именованных аргументов и пробрасывать их в шаблон

```python
return render_template('index.html', name='Харитон')
```

В шаблоне заменим имя владельца на вывод переменной из шаблона внутри двойных фигурных скобок:

```html
<h1 class="text-monospace">Привет, меня зовут {{ name }}</h1>
```

Для компактности переменные объединяют в один словарь, передают его в рендерящую функции и там же его распаковывают:

```python
@app.route('/index/')
def index():
    context = {
        'title': 'Личный блог',
        'name': 'Харитон',
    }
    return render_template('index.html', **context)
```

При написании переменных внутри шаблона рекомендуют имя и скобки отделять пробелом:

```html
<title>{{ title }}</title>
```

### Условный оператор в шаблоне

Если в шаблон передали переменную user, то будет выведен абзац текста, иначе ничего.

```html
{% if user %}
    <p>Вы вошли под именем {{ user }}</p>
{% endif %}
```

Поддерживаются более сложные условия. Например можно добиться правильного окончания в предложении:

```html
<p>К прочтению предлагается {{ number }}
    {% if number == 1 %}
        пост
    {% elif 2 <= number <= 4 %}
        поста
    {% else %}
        постов
    {% endif %}
</p>
```

### Цикл в шаблоне

[Поэма в виде списка предложений](lesson_1/app_09.py)

Используя цикл в шаблоне можно вывести все элементы списка, т.е. всю поэму:

```python
{% for item in item_list %}
    {{ item }}
{% endfor %}
```

[Вывод поэмы в шаблоне html](lesson_1/templates/show_for.html)

### Вывод сложных структур в цикле шаблона

С помощью цикла в шаблоне можно отображать сложные структуры, например [список словарей](lesson_1/app_10.py), используя точечную нотацию для доступа к вложенными элементам структуры:

```html
<body>
    <div class="row">
        <h1 class="col-12 text-monospace text-center">Список пользователей из БД</h1>
        {% for user in users %}
            <div class="col-12 col-md-6 col-lg-4">
                <h2>{{ user.name }}</h2>
                <p>{{ user.mail }}</p>
                <p>{{ user.phone }}</p>
            </div>
        {% endfor %}
    </div>
</body>
```

### Наследование шаблонов

Применяя наследование шаблонов соблюдается принцип DRY (Don't Repeat Yourself)

Например, имеем два html файла:

- [main.html](lesson_1/templates/main.html) - 45 строк кода
- [data.html](lesson_1/templates/data.html) - 28 строк кода

В результате 73 строк рендерется с помощью [скрипта пайтона](lesson_1/app_11.py)

Можно сократить количество информации за счет оптимизации дублирования, для этого создадим базовый  и дочерний шаблоны.


1. Всю одинаковую информацию поместим в [базовый шаблон](lesson_1/templates/base.html) - 30 строк

Уникальную информацию поместим в дочерние шаблоны:

2. [new_main.html](lesson_1/templates/new_main.html) - 10 строк

3. [new_data.html](lesson_1/templates/new_data.html) 27 строк

В итоге 67 строк рендерятся [обновленным скриптом](lesson_1/app_11_update.py). Разница в количестве информации будет заметнее при большем количестве разделов сайта.

Использование переменной {{ super() }} в дочерних шаблонах позволяет выводить содержимое родительского блока, а не заменять его!
Сохранять текстовую информацию в data.html нелогично, ее нужно хранить в БД, тогда шаблон будет получать её через контекст и выводить в цикле.

# 02

## Экранирование или защита данных

Если не использовать экранирование данных в скрипте, то при вводе в браузере адреса типа:

```
http://127.0.0.1:5500/<script>alert(1)</script>/ 
```

Так можно выполнить любую команду.

Чтобы обезопаситься от взлома [скрипта](lesson_2/app_01.py), используем функцию экранирования из библиотеки markupsafe:

```python
from markupsafe import escape

@app.route('/<path:file>/')
def get_file(file):
    return escape(file)
```

### url_for()

Функция url_for() позволяет генерировать url-путь внутри шаблонов на основе функции-представления и множества параметров, позволяя адресную строку делать динамической в зависимости от ввода пользователя.

[Имея скрипт с url_for()](lesson_2/app_02.py), передав ему адрес, типа:

```
http://127.0.0.1:5500/test_url_for/7/
```

Получим вывод:

```html
В num лежит 7
Функция url_for("test_url", num=num) = '/test_url_for/7/'
Функция url_for("test_url", num=num, data="new_data") = '/test_url_for/7/?data=new_data'
Функция url_for("test_url", num=num, data="new_data", pi=3.14515) = '/test_url_for/7/?data=new_data&pi=3.14515'
```

url_for() можно использовать внутри html-шаблонов, тогда в качестве базового url (первый аргумент) будет использоваться имя одноименной функции-представления.

```html
<img src="{{ url_for('static', filename='image/foto.jpg') }}" alt="Моё фото">
```

### HTTP-запросы

Для работы с [HTTP-запросами](https://developer.mozilla.org/ru/docs/Web/HTTP/Methods) используются объект `request` из библиотеки `flask`.

Данный объект содержит:

- метод запроса
- заголовки
- параметры
- данные

Эти данные хранятся в словаре `args` и получить данные можно классическим способом через метод get() по ключу.

#### GET-запросы

Имеются недостатки: 

- можно передавать только текстовые данные
- длина адресной строки ограничена
- безопасность

Запустив [скрипт](lesson_2/app_04.py) и введя в браузере адрес:

```
http://192.168.1.11:5500/get/?name=alex&level=80
```

Получим вывод:

```html
Похоже ты опытный игрок, раз имеешь уровень 80
ImmutableMultiDict([('name', 'alex'), ('level', '80')])
```

#### POST-запросы

С html-тегом `form` часто используют атрибут`method="post"`
Внутри [скрипта](lesson_2/app_05.py) используют request.form.get() для получения на сервер данных из формы.

При указании в декораторе роутинга methods=['GET', 'POST'] будут работать два вида запросов

#### Mетоды get() и post()

Новый [скрипт](lesson_2/app_06.py) вместо одного метода route использует два:

- get() - отрисовка формы
- post() - передача данных из формы

### Загрузка файлов

При указании параметров в атрибуте `enctype=multipart/form-data` можно выгружать файлы на сервер.

[Скрипт](lesson_2/app_07.py) с помощью post получает файл, сохраняет его в переменной file, т.е. в оперативной памяти или во временном каталоге, если файл очень большой. 
Чтобы избежать проблем с плохими именами используем функцию secure_filename из модуля werkzeug.utils.
Переменная file имеет метод save(), с помощью него сохраняется файл из оперативки на диск.

## Декоратор errorhandler

Можно заменить стандартные страницы ошибок своими.

### 404

Дополним [скрипт сайта с меню](lesson_2/app_08.py) из прошлого урока обработчиком ошибки 404. 

На основе [базового шаблона](lesson_2/templates/base.html) создадим собственную страницу [ошибки 404](lesson_2/templates/404.html)

Теперь при переходе по несуществующему адресу выведется наша страница с возможностью выйти на главный экран сайта:

```html
Мы не нашли страницу: «http://localhost:5500/news/sdf».
Попробуйте вернуться на главную
```

### abort()

Во Flask функция abort() используется для преднамеренного вызова ошибки с указанием кода ошибки:

```python
if result is None:
    abort(404)
```

В [данном коде](lesson_2/app_09.py) в случае отсутствия нужного блога происходит преднамеренный сброс на ошибку 404, т.к. страница для нее была определена ранее, то отображается стилизованное сообщение на фоне нашего сайта.

#### Коды ошибок

- 400: Неверный запрос
- 401: Не авторизован
- 403: Доступ запрещен
- 404: Страница не найдена
- 500: Внутренняя ошибка сервера

##### 500

[Симулируем в коде](lesson_2/app_10.py) ошибку, отключив импорт функции get_blog(), тогда приложение не зная откуда брать ее выдаст 500. Но, мы определили декоратор перехвата ошибки 500 и пользователю вернется стилизованная страница, а не скучное сообщение "Internal Server Error".

Внимание! Для того, чтобы возвращалась ошибка 500, нужно отключить режим отладки

```python
app.run(debug=True, host='0.0.0.0', port=5500)
```

## redirect()

Она принимает URL-адрес, на который нужно перенаправить пользователя, и возвращает объект ответа, который перенаправляет пользователя на указанный адрес.

[Редирект](lesson_2/app_11.py) на внутренний адрес с использованием ulr_for()

```python
@app.route('/internal/')
def internal():
    return redirect(url_for('main'))
```

Редирект на внешне адреса не использует url_for(), но обязательно указание префикса https://

```python
@app.route('/external/')
def external():
    return redirect(('https://google.com'))
```

Возможен [редирект](lesson_2/app_12.py) с параметрами, предаем в качестве аргумента имя, которое будет передано в другой роут

```python
@app.route('/hello/<name>')
    def hello(name):
    return f'Привет, {name}!'

@app.route('/redirect/<name>')
    def redirect_to_hello(name):
    return redirect(url_for('hello', name=name))
```

## flash()

Flash-сообщения в Flask это способ передачи информации между python-скриптом и html-щаблоном
Функция flash() в скрипте принимает сообщение и его категорию, сохраняя во временном хранилище (сессионный cookie) в оперативке.
Flash-сообщение можно визуализировать внутри html-шаблона с помощью функции get_flashed_messages(), после прочтения куки удаляется.

### secrets

Для шифрования и подписи сообщений необходимо сгенерировать секретный ключ, например с помощью консоли python:

```python
>>> import secrets
>>> secrets.token_hex()
```

При формировании сообщения на сервере с помощью скрипта оно будет подписано и при необходимости зашифровано, после чего передано в браузер пользователя.
При необходимости извлечения и отображения данного сообщения в соответствии с логикой веб-приложения, как правило в момент визуализации html-шаблона, сообщение извлекается из куков, передается на сервер в скрипт c Flask, где происходит проверка и расшифровка с помощью секретного ключа и наконец куки удаляется.

### Код c flash()

Сгенерированный секретный ключ поместим в переменную app.secret_key [в нашем коде](lesson_2/app_13.py). Далее, импортируем функцию flash из библиотеки flask.

Для передачи сообщения внутри функции передаем два аргумента: сообщение и категорию

```python
flash('Форма успешно отправлена!', 'success')
```

### Шаблон с flash-сообщением

В случае обычного get-запроса загрузиться пустая форма из [html-шаблона](lesson_2/templates/flash_form.html), если вписать что-то в форму и нажать кнопку сформируется post-запрос включая сообщение, данный пост-запрос передастся тому-же html-шаблону:

```html
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        {% for category, message in messages %}
            <div class="alert alert-{{ category }}">
                {{ message }}
            </div>
        {% endfor %}
    {% endif %}
{% endwith %}
```

В данном блоке оператор with шаблонизатора jinja создает список messages, помещая туда все полученное сообщения и их категории (with_categories=true) с помощью функции get_flashed_messages().
Далее, условный оператор проверяет, есть ли хоть одно flash-сообщение в переменной messages. Если сообщение есть, то выполняется цикл, в котором из каждого элемента списка распаковывается кортеж, в первую переменную помещается категория, во вторую само сообщение.

### bootstrap с flash

Категорию используем для генерации имени класса блока, сообщение помещаем в текстовую часть блока.
Благодаря bootstrap и использованию в именах классов категории, можно добиться разной окраски блоков с сообщениями:

- success - зеленый цвет
- warning - желтый цвет
- danger - красный

## Хранилища данных на стороне клиента

Из-за ограничений по безопасности на стороне клиента существует ограниченное количество хранилищ данных в браузере:

1. Cookies (Куки) — это небольшие фрагменты данных, которые веб-сервер отправляет и хранятся на устройстве пользователя.
2. Local Storage (локальное хранилище) предоставляет способ хранения данных в виде пар «ключ-значение» в браузере и доступно даже после закрытия браузера.
3. Session Storage (сессионное хранилище) - работает по принципу «ключ-значение» и предназначено для хранения данных в рамках текущей сессии браузера. Данные удаляются, когда пользователь закрывает вкладку или окно.
4. IndexedDB - подходит для хранения больших объёмов данных и позволяет сохранять более сложные структуры данных по сравнению с Local и Session Storage.
5. Cache Storage (кэш) - используется в основном для кэширования ресурсов при работе с Service Workers и Progressive Web Apps (PWA).
6. Web SQL — это устаревший API, который позволяет использовать SQL для управления хранилищем данных на стороне клиента. 

### Cookie

1. Сессионные куки (Session Cookies). Хранятся в памяти браузера и удаляются, когда пользователь закрывает браузер. Используются для отслеживания состояния сессии пользователя (например, вход в систему или корзина покупок).
2. Постоянные куки (Persistent Cookies).Хранятся на диске пользователя на определённый срок (от нескольких секунд до нескольких лет). Используются для хранения информации, такой как логин пользователя, предпочтения и настройки.
3. Безопасные куки (Secure Cookies). Передаются только через защищённые HTTPS-соединения, что помогает защитить данные от прослушивания при передаче по сети.
4. HttpOnly куки. Доступны только через HTTP(S) протокол, что предотвращает доступ к ним с помощью JavaScript (это может помочь защитить от атак типа XSS).
5. Куки с указанием срока действия (Expiry Cookies). Куки, которые имеют установленное время жизни, после которого они становятся недействительными. Это управляется с помощью атрибута Expires или Max-Age.
6. Сторонние куки (Third-party Cookies). Создаются доменами, отличными от домена, посещаемого пользователем. Данные могут использоваться для отслеживания пользователей между различными сайтами. Часто используются рекламными сетями для мониторинга поведения пользователей на разных ресурсах.
7. Параметризированные куки (SameSite Cookies). Используются для указания, при каких условиях куки должны отправляться с кросс-доменными запросами. Можно установить значения Lax, Strict или None. 

С куками позволяет работать библиотека request:

1. С помощью функции make_response() создаем объект типа response и передаем ему любой описательный текст в качестве аргумента 
2. С помощью метода set_cookie() устанавливаем куки
3. С помощью метода get_cookie() получаем куки
4. С помощью метода delete_cookie() удаляем куки

#### make_response()

Ранее мы через функцию-представление возвращали текст, страницу полученную с помощью render_template() или редирект. Но,каждый раз Flask неявно формировал из информации выше объект ответа - response. С помощью make_response() мы можем не только самостоятельно формировать response, но и изменять его.

Создадим простой шаблон [main.html](lesson_2/templates/main.html) в нем отобразим имя, переданное из [скрипта](lesson_2/app_14.py). В скрипте мы генерируем страницу на основе шаблона и записываем это в объект response.
И самое главное в объекте response 

Добавляем заголовки (хедеры, не путать с head) в объект response, которые будут в заголовке ответного http-пакета, их можно посмотреть с помощью F12

```python
response.headers['new_head'] = 'New value'
```

В хедерах html-ответа будет также заголовок Set-Cookie, который мы задали в коде

```python
response.set_cookie('username', context['name'])
```

#### set_cookie()

С помощью данного метода объекта response мы можем создать куку и в качестве аргументов передать:

- 'key': Имя куки или ключ.
- 'value': Значение, которое будет храниться в куке.
- 'max_age': Максимальный возраст куки в секундах. Это позволит сделать куку постоянной, если указано значение, отличное от None.
- 'expires': Временная метка или дата, после которой кука истечёт. Это также позволяет сделать куку постоянной.
- 'path': Путь, для которого кука доступна. По умолчанию используется '/', что означает, что кука будет доступна для всех URL на данном домене.
- 'domain': Домен, для которого кука должна быть доступна.
- 'secure': Если True, кука будет передаваться только через HTTPS соединения.
- 'httponly': Если True, кука не будет доступна через JavaScript (то есть, не будет доступна через document.cookie), что помогает защитить куку от атак типа XSS (межсайтовый скриптинг).
- 'samesite': Этот атрибут помогает предотвратить атаки CSRF (межсайтовая подделка запроса). Возможные значения: 'Lax', 'Strict' или 'None'.

Минимально можем задать все два аргумента: 'key' и 'value'. В данном случае создастся временный сессионный куки.

В [более сложном скрипте](app_15.py) при его запуске и обращении через браузер по адресу http://localhost:5500/ будет выведена форма, через которую можно задать имя пользователя и при отправке имя сохранится в сессионном куке.
Далее, при обращении по адресу http://localhost:5500/get/ будет выведено имя из сессионного куки. Данный куки можно изменить вручную через F12 - раздел хранилище, тогда при обращении по адресу http://localhost:5500/get/ будет выведено имя из изменённого куки.

#### session

Сессии используют серверное хранилище для хранения данных, обычно в виде словаря в памяти сервера или записей в базе данных, и идентификатор сеанса передается пользователю через куку (обычно с помощью куки с именем session).
Данные в сессии могут быть более сложными и содержать различные типы данных.
Сессии по умолчанию живут один месяц.
Необходимо создавать секретный ключ

[Шаблон использующий сессии](lesson_2/templates/username_form.html)

[Скрипт использующий сессии](lesson_2/app_16.py), определяем в нем три маршрута:

1. '/' для вывода имени пользователя
2. '/login' для авторизации
3. '/logout' для выхода.

При отправке формы на странице /login происходит запись имени пользователя в сессию. Если имя пользователя уже есть в сессии, то оно выводится на странице '/'.
Чтобы удалить данные из сессии используем страницу /logout.

Т.к. сессия это словарь до добавлять и удалять сессии можно аналогично:

```python
session['name'] = 'John'
session.pop('name')
```

## Примеры 02

[Семинар 02](seminar_2/app.py)

# 03

Для работы с СУБД можно использовать встроенные в python библиотеки:

[Пример работы с SQLite](lesson_3/sqlite.py)

Нативные библиотеки, т.е. разработанные компаниями производящими СУБД:

Сначала установить нативную библиотеку

```bash
pip install mysql-connector-python
```

[Пример с MySql](lesson_3/mysql_script.py)

Но, есть универсальный инструмент ORM SQLAlchemy.

ORM (Object-Relational Mapping) - это паттерн программирования, который позволяет работать с базами данных, представляя данные в виде объектов и классов, а не в виде SQL-запросов.


## Flask-SQLAlchemy

Библиотека расширяющая flask, для облегчения работы с СУБД.

### Установки и настройка

```bash
pip install Flask-SQLAlchemy
```

Импорт в проект

```python
from flask_sqlalchemy import SQLAlchemy
```

### Подключение к ДБ

Для подключения SQLite используем:

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)
```

Создали объект db на базе класса SQLAlchemy, который далее и буде эксплуатироваться

[Скрипт с кодом выше](lesson_3/app_01.py)

При старте этого скрипта, создастся папка instance в директории запуска, в ней обычно располагается файл БД.

С помощью SQLAlchemy можно подключаться к MySQL

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@hostname/database_name'
```

Или к PostgreSQL

```python
postgresql+psycopg2://username:password@hostname/database_name
```

### Модель

Модель алхимии - это класс, который описывает структуру таблицы в базе данных.

Обычно, служебный код моделей, т.е. структура таблиц базы, выносится в отдельные компоненты models.

```python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
```

Следовательно в [основном скрипте](lesson_3/app_02.py) мы не импортируем и не создаем объект класса алхимии.

Вместо этого импортируем объект из компонента моделей (models) и инициализируем созданный объект алхимии:

```python
from lesson_3.models_02 import db
db.init_app(app)
```

Для описания модели используют следующие типы данных:

- Integer — целое число
- String — строка
- Text — текстовое поле
- Boolean — булево значение
- DateTime — дата и время
- Float — число с плавающей точкой
- Decimal — десятичное число (для денег)
- Enum — перечисление значений
- ForeignKey — внешний ключ к другой таблице

### Создание моделей БД

Предположим, что мы делаем базу данных социальной сети, в которой три таблицы:

- пользователи
- статьи
- комментарии

ORM предполагает наличие еще одного уровня абстракции с помощью моделей на основе классовой реализации.
Создадим 3 класса моделей:

1. User() - управляет таблицей пользователей в СУБД 
2. Post() - управляет таблицей статей
3. Comment() - управляет таблице комментариев

#### User()

В [компоненте моделей](lesson_3/models_03.py) создадим 4 поля для работы с таблицей пользователей БД с помощью класса User:

```python
id = db.Column(db.Integer, primary_key=True)
username = db.Column(db.String(80), unique=True, nullable=False)
email = db.Column(db.String(120), unique=True, nullable=False)
created_at = db.Column(db.DateTime, default=datetime.utcnow)
posts = db.relationship('Post', backref='author', lazy=True)
```

5 полей модели User():

1. id - целочисленное поле, является первичным ключом таблицы, автоматически генерируется при добавлении записи
2. username - строка до 80 символов с ограничением на уникальность и обязательностью заполнения
3. email - строка до 120 символов с ограничением на уникальность и обязательностью заполнения
4. created_at - дата и время создания записи, автоматически заполняется текущей датой и временем при добавлении записи
5. posts - взаимосвязь, где первый аргумент указывает на связанную модель Post

Пятое поле класса `posts` не связано с одноименной колонкой БД, является фишкой алхимии, ускоряющей работу программы python.
Образует связь с моделью Post, backref - обратное отношение, lazy - загрузка данных по мере необходимости.

#### Post()

Добавим в [компоненте моделей](lesson_3/models_04.py) еще таблицу статей с помощью класса Post:

```python
id = db.Column(db.Integer, primary_key=True)
title = db.Column(db.String(80), nullable=False)
content = db.Column(db.Text, nullable=False)
author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

5 полей модели Post():

1. id - целочисленное поле, первичный ключ таблицы статей
2. title - строковое обязательное поле до 80 символов, не уникальное, т.к. заголовки могут повторяться
3. content - текстовое обязательное поле
4. author_id - целочисленное поле, внешний ключ к полю id таблицы пользователей
5. created_at - дата и время создания записи и автоматически заполняется текущей датой и временем при добавлении записи

#### Comment()

Добавим третью модель в [компоненте моделей](lesson_3/models_05.py), связав таблицу комментариев БД с помощью класса Comment:

```python
id = db.Column(db.Integer, primary_key=True)
content = db.Column(db.Text, nullable=False)
post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

5 полей модели Comment:

1. id
2. content - обязательное для заполнения
3. post_id - обязательное для заполнения, внешний ключ к полю id таблицы статей
4. author_id - внешний ключ к полю id таблицы пользователей
5. created_at - дата и время создания записи, автоматически заполняется текущей датой и временем при добавлении записи

### Создание таблиц БД

В [компонент моделей](lesson_3/models_05.py), можно поместить следующий код для инициализации БД с помощью командной строки:

```python
@app.cli.command('init-db')
def create_db():
    db.create_all()
    print('db created')
```

Далее выполнить команду в консоли:

```bash
flask --app models_05.py init-db
```

В текущей директории появится папка instance с файлом SQLite базы `mydatabase.db`.
Код для командной строки можно положить в любой файл: главный компонент, компонент модели или wsgi.py главное правильные импорты.

### Работа с БД

CRUD:

1. Create
2. Read (filter)
3. Update
4. Delete

#### 1. Create

Создадим новый объект на основе модели класса User

```python
@app.cli.command("add-john")
def add_user():
    user = User(username='john', email='john@example.com')
    db.session.add(user)
    db.session.commit()
    print('John add in DB!')
```

Метод commit() обязателен для применения изменений. Необходимо запустить в консоли терминала [компонент моделей](lesson_3/models_06.py):

```bash
flask --app models_06.py add-john
```

### 2. Read

При создании классов моделей ранее, был задан метод `__repr__`, которая сработает в случае вывода на печать:

```python
def __repr__(self):
    return f'User({self.username}, {self.email})'
```

Поэтому при чтении из БД, и для простого вывода ее содержимого в консоль, можно ограничится функцией print():

```python
...
@app.cli.command("read-db")
def read_db():
    users = User.query.all()
    print(users)
```

После выполнения команды в терминале:

```bash
flask --app models_06.py read-db
```

Получим вывод содержимого из таблицы пользователей в консоль:

```bash
[User(user1, user1@mail.ru), User(user2, user2@mail.ru), User(user3, user3@mail.ru), User(user4, user4@mail.ru), User(user5, user5@mail.ru)]
```

### 3. Update

Поменяем почту у первого найденного пользователя:

```python
@app.cli.command("edit-john")
def edit_user():
    user = User.query.filter_by(username='john').first()
    user.email = 'new_email@example.com'
    db.session.commit()
    print('Edit John mail in DB!')
```

.first() - метод останавливает на первой найденной записи

Запуск на изменение через консоль:

```bash
flask --app models_06.py edit-john
```

### 4. Delete

Удалим первую найденную запись:

```python
@app.cli.command("del-john")
def del_user():
    user = User.query.filter_by(username='john').first()
    db.session.delete(user)
    db.session.commit()
    print('Delete John from DB!')
```

Запуск скрипта на удаление первой найденной записи:

```bash
flask --app models_06.py del-john
```

### Наполним БД случайными данными

```python
@app.cli.command("fill-db")
def fill_tables():
    count = 5
    # Добавляем пользователей
    for user in range(1, count + 1):
        new_user = User(username=f'user{user}',
        email=f'user{user}@mail.ru')
        db.session.add(new_user)
        db.session.commit()
    # Добавляем статьи
    for post in range(1, count ** 2):
        author = User.query.filter_by(username=f'user{post % count + 1}').first()
        new_post = Post(title=f'Post title {post}',
        content=f'Post content {post}', author=author)
        db.session.add(new_post)
    db.session.commit()
```

Запуск скрипта на наполнение БД:

```bash
flask --app models_06.py fill-db
```

### Вывод данных в браузере

В основном компоненте flask-приложения импортируем нужные классы из моделей и добавим маршрут /users/:

```python
from models_06 import app, User

@app.route('/users/')
def all_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)
```

В папке templates создадим шаблон [users.html](lesson_3/templates/users.html), расширяющий [базовый шаблон](lesson_3/templates/base.html), с помощью цикла jinja выводим весь контент в браузер:

```html
{%block content%}
    <div class="row">
        {% for user in users %}
        <p class="col-12 col-md-6">Username: {{ user.username }}<br>Email: {{ user.email }}</p>
        {% endfor %}
    </div>
{% endblock %}
```

### Фильтрация данных

#### Фильтрация из User()

Метод filter() принимает параметры фильтрации в качестве аргументов. Создадим новый динамический маршрут в [главном компоненте](lesson_3/app_07.py):

```python
@app.route('/users/<username>/')
def users_by_username(username):
    users = User.query.filter(User.username == username).all()
    context = {'users': users}
    return render_template('users.html', **context)
```

При вводе адреса в браузере http://localhost:5500/users/user1 отобразится информация только по заданному пользователю.

#### Фильтрация из Post()

Изменим [главный компонент](lesson_3/app_08.py), чтобы иметь возможность фильтровать данные из таблицы статей, для этого импортируем jsonify и класс модели Post и добавим маршрут:

```python
from flask import jsonify
from models_06 import Post

@app.route('/posts/author/<int:user_id>/')
def get_posts_by_author(user_id):
    posts = Post.query.filter_by(author_id=user_id).all()
    if posts:
        return jsonify([{'id': post.id, 'title': post.title, 'content': post.content, 'created_at': post.created_at} for post in posts])
    else:
        return jsonify({'error': 'Posts not found'})
```

В результате ввода в адресной строке http://localhost:5500/posts/author/1/ получим JSON-ответ:

```json
[
  {
    "content": "Post content 5",
    "created_at": "Thu, 09 Jan 2025 22:08:24 GMT",
    "id": 5,
    "title": "Post title 5"
  },
  {
    "content": "Post content 10",
    "created_at": "Thu, 09 Jan 2025 22:08:25 GMT",
    "id": 10,
    "title": "Post title 10"
  },
  {
    "content": "Post content 15",
    "created_at": "Thu, 09 Jan 2025 22:08:26 GMT",
    "id": 15,
    "title": "Post title 15"
  },
  {
    "content": "Post content 20",
    "created_at": "Thu, 09 Jan 2025 22:08:27 GMT",
    "id": 20,
    "title": "Post title 20"
  }
]
```

#### Фильтрация по дате

Добавим импорт библиотеки для работы с датой и добавим маршрут для фильтрации статей за прошлую неделю:

```python
from datetime import datetime, timedelt

@app.route('/posts/last-week/')
def get_posts_last_week():
    date = datetime.utcnow() - timedelta(days=7)
    posts = Post.query.filter(Post.created_at >= date).all()
    if posts:
        return jsonify([{'id': post.id, 'title': post.title, 'content': post.content, 'created_at': post.created_at} for post in posts])
    else:
        return jsonify({'error': 'Posts not found'})
```

При вводе в браузере http://localhost:5500/posts/last-week/ отобразится JSON-ответ содержащий все посты за неделю.

## Flask-WTForm

Это модуль Flask для работы с формами веб-приложений на Python. Он позволяет легко
создавать и обрабатывать формы, валидировать данные, защищать приложение от атак CSRF (межсайтовой подделки
запросов).

Для установки Flask-WTF выполним в консоли:

```bash
pip install Flask-WTF
```

Импортировать в проект:

```python
from flask_wtf import FlaskForm
```

### Защита от CSRF-атак

Необходимо импортировать модуль CSRFProtect и установить секретный ключ приложения:

```python
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dac238ac08a088965ebd9d0741c816571b357bcf67c5f1a2ae9a070900995a65'
csrf = CSRFProtect(app)
```

Отключение защиты осуществляется с помощью декоратора @csrf.exempt.

Напоминаю как с помощью python-консоли быстро сгенерить ключ:

```bash
>>> import secrets
>>> secrets.token_hex()
'dac238ac08a088965ebd9d0741c816571b357bcf67c5f1a2ae9a070900995a65'
```

### Типы полей WTF-форм

1. StringField — строковое поле для ввода текста;
2. IntegerField — числовое поле для ввода целочисленных значений;
3. FloatField — числовое поле для ввода дробных значений;
4. BooleanField — чекбокс;
5. SelectField — выпадающий список;
6. DateField — поле для ввода даты;
7. FileField — поле для загрузки файла.

### Создание WTF-форм

В [компоненты форм](lesson_3/forms_10.py) определим класс формы:

```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
```
В импортах берем из библиотеки WTF-forms функции: StringField, PasswordField и валидацию DataRequired.

В классе определены два поля: 

1. username - обязательное строковое поле
2. password - обязательное поле ввода пароля

validators - атрибут принимающий список проверок, в нашем случае указан параметр DataRequired, т.е. обязательный


В [компоненте форм](lesson_3/forms_11.py) добавлена более сложная форма RegisterForm:

```python
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Мужчина'), ('female', 'Женщина')])
```

RegisterForm() определяет три поля: 

1. name - обязательное строковое
2. age - обязательное целое
3. gender - выпадающий список

SelectField() вторым параметром choice принимает значения для выпадающего списка

### Валидация данных wtf-forms

Можно создавать свои валидаторы, но существуют готовые валидаторы: DataRequired, Email, Length и другие.

```python
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
```

В [коде](lesson_3/forms_12.py) функции типов полей форм в параметр validators принимают список валидирующих функций.

Функции валидации:

- DataRequired() - обязательный параметр
- Email() - данные должны быть электронной почтой
- Length() - принимает параметры минимальной и максимальной длины
- EqualTo() - принимает строку, с которой поле должно совпадать, например при повторе пароля

Для того чтобы валидатор электронной почты заработал необходимо установить библиотеку:

```python
pip install email-validator
```

### Визуализация форм в html-приложении

В [главном компоненте](lesson_3/app_13.py) добавим новый маршрут /login/:

```python
@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        pass
    return render_template('login.html', form=form)
```

1. При переходе по маршруту /login/ создается объект form из класса [LoginForm()](lesson_3/forms_13.py) 
2. Проверка какой вид запроса был отправлен на сервер GET или POST
3. Если GET-запрос, то отрисовка шаблона из login.html с передачей в переменной form одноименного объекта
4. Если же POST-запрос, то с помощью оператора and происходит запуск функций валидации каждого поля объекта.

[Шаблон login](lesson_3/templates/login.html):

```html
{% extends "base.html" %}
{% block content %}
<h1>Login</h1>
<form method="POST" action="{{ url_for('login') }}">
    {{ form.csrf_token }}
    <p>
        {{ form.username.label }}<br>
        {{ form.username(size=32) }}
    </p>
    <p>
        {{ form.password.label }}<br>
        {{ form.password(size=32) }}
    </p>
    <p>
        <input type="submit" value="Login">
    </p>
</form>
{% endblock %}
```

В шаблоне следующий порядок выполнения:

1. Шаблон берет за основу base.html и подставляет свои данные
2. В блоке контента, в теге form, параметр action формируется ссылка на маршрута /login/
3. Внутрь формы передается csrf-токен, это позволят избежать прямого обращения к форме миную браузер.
4. Далее визуализируются поля формы:

    - Метка (название) поля username
    - Поле username размером 32 символа
    - Метка поля password
    - Поле password размером 32 символа

### Обработка данных из формы

В [основном компоненте](lesson_3/app_14.py) определим маршрут /route/

```python
@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        email = form.email.data
        password = form.password.data
        print(email, password)
    ...
    return render_template('register.html', form=form)
```

Похоже на предыдущую форма, но с помощью свойства data мы можем получать данные из полей формы

[Шаблон register.html](lesson_3/templates/register.html) похож на login.html, но мы не указываем поля явно:

```html
{% extends "base.html" %}
{% block content %}
<h1>Login</h1>
<form method="POST" action="{{ url_for('register') }}">
    {{ form.csrf_token }}
    {% for field in form if field.name != 'csrf_token' %}
    <p>
        {{ field.label }}<br>
        {{ field }}
        {% if field.errors %}
    <ul class="alert alert-danger">
        {% for error in field.errors %}
        <li>{{ error }}</li>
        {% endfor %}
    </ul>
    {% endif %}
    </p>
    {% endfor %}
    <p>
        <input type="submit" value="Register">
    </p>
</form>
{% endblock %}
```

Чтобы не писать каждый раз имени поля формы в шаблоне используется цикл:

```html
{% for field in form if field.name != 'csrf_token' %}
```

Цикл выводит все поля кроме нашего токена, который был выведен ранее. Вложенный цикл проводит валидацию на ошибки и если ошибки были, то они будут выведены пользователю в браузер, под нужным полем формы.
Также в консоль будет выведен текст введенный в форму, включая пароль, который был спрятан за точками. Это говорит о том что пароль может быть виден на сервере открытым текстом.

