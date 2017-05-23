//extend jQuery
(function($){
	/*
	 * showIf is a jQuery extension which shows an element if the test evaluates to true, and hides the element otherwise
	 */
	$.fn.showIf = function(test){
		if (test) {
			return this.show();
		}
		return this.hide();
	};
	/*
	 * visibleIf sets the visibilty of an element to visible or hidden if the test evalutes to true or false, respectively
	 */
	$.fn.visibleIf = function(test){
		return this.css('visibility', test ? 'visible' : 'hidden');
	};
}(jQuery));