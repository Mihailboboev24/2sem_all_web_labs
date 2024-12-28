from flask import Blueprint, render_template, request, abort, jsonify


lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')
films = [
    {
        "title": "Inception",
        "title_ru": "Начало",
        "year": 2010,
        "description": "Дом Кобб – талантливый вор, лучший из лучших в опасном искусстве извлечения: он крадет ценные секреты из глубин подсознания во время сна, когда человеческий разум наиболее уязвим. Но теперь ему предстоит не украсть идею, а внедрить её. Если он преуспеет, это станет идеальным преступлением."
    },
    {
        "title": "The Grand Budapest Hotel",
        "title_ru": "Отель «Гранд Будапешт»",
        "year": 2014,
        "description": "Фильм рассказывает об увлекательных приключениях легендарного консьержа отеля «Гранд Будапешт» и его юного помощника, которые становятся обладателями бесценного произведения искусства и оказываются в центре заговора, связанного с огромным состоянием семьи."
    },
    {
        "title": "Interstellar",
        "title_ru": "Интерстеллар",
        "year": 2014,
        "description": "Когда засуха приводит человечество к продовольственному кризису, команда исследователей и учёных отправляется сквозь червоточину (которая предположительно соединяет области пространства-времени через большое расстояние) в путешествие, чтобы превзойти прежние ограничения для космических путешествий человека и найти планету с подходящими для человечества условиями."
    },
    {
        "title": "The Dark Knight",
        "title_ru": "Тёмный рыцарь",
        "year": 2008,
        "description": "Бэтмен поднимает ставки в своей войне с преступностью. С помощью лейтенанта Джима Гордона и прокурора Харви Дента он намерен очистить улицы Готэма от преступности. Но всё усложняется с появлением нового преступника – Джокера, который сеет хаос и ставит под угрозу планы Бэтмена."
    },
    {
        "title": "La La Land",
        "title_ru": "Ла-Ла Ленд",
        "year": 2016,
        "description": "Джазовый музыкант и начинающая актриса встречаются и влюбляются друг в друга в Лос-Анджелесе, городе, где мечты часто разбиваются о суровую реальность. Их любовь и стремление к успеху сталкиваются с трудностями, которые испытывают их отношения."
    },
]
@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return films
@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if 0 <= id < len(films):
        return films[id]
    else:
        abort(404)

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if 0 <= id < len(films):
        del films[id]
        return '', 204
    else:
        abort(404)

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    if 0 <= id < len(films):
        film = request.get_json()
        films[id] = film
        return films[id]
    else:
        abort(404)

@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    film = request.get_json()
    if not film or not isinstance(film, dict):
        abort(400)
    films.append(film)
    new_index = len(films) - 1
    return jsonify({"id": new_index}), 201
