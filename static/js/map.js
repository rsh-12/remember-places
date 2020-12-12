ymaps.ready(init);
var myMap;

function getCoords(x, y) {
    document.getElementById('id_latitude').value=x
    document.getElementById('id_longitude').value=y
}


function init() {
    myMap = new ymaps.Map("map", {
        center: [56.83507546894007, 60.59762278832995], // Екб
        zoom: 13
    }, {
        balloonMaxWidth: 200,
        searchControlProvider: 'yandex#search'
    });

    // Обработка события, возникающего при щелчке
    // левой кнопкой мыши в любой точке карты.
    // При возникновении такого события откроем балун.
    myMap.events.add('click', function (e) {
        if (!myMap.balloon.isOpen()) {
            var coords = e.get('coords')
            myMap.balloon.open(coords, {
                contentHeader: 'Расскажите об этом месте!',
                contentBody: '<p>Что тут произошло?</p>' +
                    '<p>Координаты щелчка: ' + [
                        coords[0].toPrecision(6),
                        coords[1].toPrecision(6)
                    ].join(', ') + '</p>',
                contentFooter: '<sup>Щелкните еще раз</sup>'
            });

            getCoords(coords[0], coords[1])
        } else {
            myMap.balloon.close();
        }
    });

    // Обработка события, возникающего при щелчке
    // правой кнопки мыши в любой точке карты.
    // При возникновении такого события покажем всплывающую подсказку
    // в точке щелчка.

    // Скрываем хинт при открытии балуна.
    myMap.events.add('balloonopen', function (e) {
        myMap.hint.close();
    });

}