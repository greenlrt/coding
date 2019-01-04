// When the user clicks on <div>, open the popup
function myFunction() {
	alert("Hello World!");
}

window.onload = function() {
document.getElementsByClassName('main')[0].insertAdjacentHTML('beforeend', '<br>Will use this to test table component');
};
