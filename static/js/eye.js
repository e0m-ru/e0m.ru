var iris = document.querySelector('#iris'),
	pupil = document.querySelector('#pupil'),
	hotspot = document.querySelector('#hotspot'),
	logoRect = document.querySelector('#sclera').getBoundingClientRect();

const heightOutput = document.querySelector('#height'),
	widthOutput = document.querySelector('#width');


function report(x, y) {
	widthOutput.textContent = x;
	heightOutput.textContent = y;
}

function eyeAnimation(event) {
	var mouse = {
		x: event.clientX,
		y: event.clientY,
		},
		wnd = {
			x: window.innerWidth, //document.body.clientWidth,
			y: window.innerHeight, //document.body.clientHeight,
		},
		Percent = {
			x: mouse.x / (wnd.x / 100) / 100 -.5,
			y: mouse.y / (wnd.y / 100) / 100 -.1,
		}

	iris.setAttribute('cx', Percent.x * logoRect.width/3 + 145);
	iris.setAttribute('cy', Percent.y * logoRect.height/3 + 35);
	pupil.setAttribute('cx', Percent.x * logoRect.width/2 + 145);
	pupil.setAttribute('cy', Percent.y * logoRect.height/2 + 35);
	pupil.setAttribute('r', Percent.y*-10 + 20);
	hotspot.setAttribute('cx', Percent.x * logoRect.width/3 + 145);
	hotspot.setAttribute('cy', Percent.y * logoRect.height/3 + 35);
}

window.onmousemove = eyeAnimation;