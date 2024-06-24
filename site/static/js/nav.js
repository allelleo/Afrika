const clearNav = () => {
	const elements = document.getElementById('selectnav1')
	for (var i = 0; i < elements.length; i++) {
		let el = elements[i]
		console.log(el)
		console.log(el.value)
		if (el.value.length < 1) {
			el.remove()
		}
		if (el.text.length < 1) {
			el.remove()
		}
		// Do stuff
	}
}
clearNav()
clearNav()
clearNav()
clearNav()
clearNav()
