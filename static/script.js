window.onload = function() { // после загрузки страницы

	var scrollUp = document.getElementById('up'); // найти элемент

	scrollUp.onclick = function() { //обработка клика
		window.scrollTo(0,0);
	};

// show button

	window.onscroll = function () { // при скролле показывать и прятать блок
		if ( window.pageYOffset > 0 ) {
			scrollUp.style.opacity = 1;
			scrollUp.style.cursor = 'pointer';
			//scrollUp.style.display = 'block';
		} else {
			scrollUp.style.opacity = 0;
			scrollUp.style.cursor = 'default';
			//scrollUp.style.display = 'none';
		}
	};
};