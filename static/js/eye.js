var iris = $('#iris'),
	pupil = $('#pupil'),
	hotspot = $('#hotspot'),
	cx = iris.attr('cx') * 1,
	cy = iris.attr('cy') * 1;

document.onmousemove = function (event) {
	var m = {
			x: event.clientX,
			y: event.clientY
		},

		win = {
			x: document.body.clientWidth,
			y: document.body.clientHeight
		},
		x = (m.x - cx) / (win.x) ,
		y = (m.y - cy) / (win.y) ;

	iris.attr('cx', x + cx);
	iris.attr('cy', y + cy);
	pupil.attr('cx', x * 1.5 + cx);
	pupil.attr('cy', y * 1.5 + cy);
	hotspot.attr('cx', cx + x / 2);
	hotspot.attr('cy', cy + y / 2);

};

function random(i, j) {
	if (j) {
		return Math.round(i + Math.random() * (j - i))
	}
	if (i) {
		return Math.round(Math.random() * i)
	} else return Math.round(1 - Math.random() * 2)
};

function irisRadiusAnimation(e) {
	var s = Number (iris.attr('r'));
	if (s > e) {
		loop = setInterval(function () {
			if (s < e) clearInterval(loop);
			iris.attr('r', s);
			pupil.attr('r', s/1.5);
			s = s - 0.5;
		}, 30);
		return a = 'Bolshe';
	};

	if (s < e) {
		loop = setInterval(function () {
			if (s > e) clearInterval(loop);
			iris.attr('r', s);
			pupil.attr('r', s/1.5);
			s = s + 0.5;
		}, 30);
		return a = 'Menshe';
	};
	if (s = e) {
		
	}
}

	
//setInterval (function () {console.log (random(iris.attr('r')))}, 1000);
loop = setInterval(function () {irisRadiusAnimation (random(15,30));}, random(1000,3000))