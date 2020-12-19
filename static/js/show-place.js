ymaps.ready(init);

let x = document.getElementById('x').innerHTML
let y = document.getElementById('y').innerHTML
let name = document.getElementById('place-name').innerHTML

function setCoords(x, y) {
    return [x, y]
}

function setName(name) {
    return name;
}

function init() {
    var myMap = new ymaps.Map("map-show-place", {
        center: setCoords(x, y),
        zoom: 15,
        controls: []
    });

    myMap.geoObjects
        .add(new ymaps.Placemark(setCoords(x, y), {
            balloonContent: setName(name)
        }, {
            preset: 'islands#circleIcon',
            iconColor: '#f1027c'
        }));
}