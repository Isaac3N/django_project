const usernameField = document.querySelector("#usernameField");
const feedBackArea = document.querySelector(".invalid_feedback");

usernameField.addEventListener("keyup", (e) => {
	console.log("77777", 77777);

	const usernameVal = e.target.value;

	usernameField.classList.remove("is-invalid");
	feedBackArea.style.display = "none";

	if (usernameVal.length > 0) {
		fetch("/authentication/validate-username", {
			body: JSON.stringify({ username: usernameVal }),
			method: "POST",
		})
			.then((res) => res.json())
			.then((data) => {
				console.log("data", data);
				if (data.username_error) {
					usernameField.classList.add("is-invalid");
					feedBackArea.style.display = "block";
					feedBackArea.innerHTML = `<p>${data.username_error}</p>`;
				}
			});
	}
});
