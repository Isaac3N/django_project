const searchField = document.querySelector("#searchField");

searchField.addEventListener("keyup", (e) => {
	const searchValue = e.target.value;

	if (searchValue.length > 0) {
		console.log("searchValue", searchValue);
	}
});
