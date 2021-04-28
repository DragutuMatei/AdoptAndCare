(function (window) {

	'use strict';

	var support = {
			animations: Modernizr.cssanimations
		},
		animEndEventNames = {
			'WebkitAnimation': 'webkitAnimationEnd',
			'OAnimation': 'oAnimationEnd',
			'msAnimation': 'MSAnimationEnd',
			'animation': 'animationend'
		},
		animEndEventName = animEndEventNames[Modernizr.prefixed('animation')],
		onEndAnimation = function (el, callback) {
			var onEndCallbackFn = function (ev) {
				if (support.animations) {
					if (ev.target != this) return;
					this.removeEventListener(animEndEventName, onEndCallbackFn);
				}
				if (callback && typeof callback === 'function') {
					callback.call();
				}
			};
			if (support.animations) {
				el.addEventListener(animEndEventName, onEndCallbackFn);
			} else {
				onEndCallbackFn();
			}
		};

	// from http://www.sberry.me/articles/javascript-event-throttling-debouncing
	function throttle(fn, delay) {
		var allowSample = true;

		return function (e) {
			if (allowSample) {
				allowSample = false;
				setTimeout(function () {
					allowSample = true;
				}, delay);
				fn(e);
			}
		};
	}

	// sliders - flickity
	var sliders = [].slice.call(document.querySelectorAll('.slider')),
		// array where the flickity instances are going to be stored
		flkties = [],
		// grid element
		grid = document.querySelector('.grid'),
		// isotope instance
		iso;

	function init() {
		// preload images
		imagesLoaded(grid, function () {
			initFlickity();
			initIsotope();
			initEvents();
			classie.remove(grid, 'grid--loading');
		});
	}

	function initFlickity() {
		sliders.forEach(function (slider) {
			var flkty = new Flickity(slider, {
				prevNextButtons: false,
				wrapAround: true,
				cellAlign: 'left',
				contain: true,
				resize: true
			});

			// store flickity instances
			flkties.push(flkty);
		});
	}

	function initIsotope() {
		iso = new Isotope(grid, {
			isResizeBound: false,
			itemSelector: '.grid__item',
			percentPosition: true,
			masonry: {
				columnWidth: '.grid__sizer'
			},
			transitionDuration: '0.5s'
		});
	}

	function initEvents() {

		iso.layout();

		window.addEventListener('resize', throttle(function (ev) {
			recalcFlickities()
			iso.layout();
		}, 50));


	}


	function recalcFlickities() {
		for (var i = 0, len = flkties.length; i < len; ++i) {
			flkties[i].resize();
		}
	}

	init();

})(window);