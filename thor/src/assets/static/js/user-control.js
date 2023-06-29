// active link for pc sidebar
const links = document.querySelectorAll(".nav-links > li > a");

links.forEach((link) => {
	if (link.pathname === window.location.pathname) {
		link.classList.add("active");
	}
});

// toggling password for settings page
const passwordTogglers = document.querySelectorAll(".modal#edit-user-password form em");

passwordTogglers.forEach(function (icon) {
	icon.addEventListener("click", function () {
		let InputValue = icon.previousElementSibling;
		if (InputValue.type === "password") {
			InputValue.type = "text";
			icon.classList.add("bi-eye-slash");
			icon.classList.remove("bi-eye");
		} else {
			InputValue.type = "password";
			icon.classList.remove("bi-eye-slash");
			icon.classList.add("bi-eye");
		}
	});
});

// custom input form for settings page
// const InputButton = document.querySelector(".modal#edit-user-details form  button.custom-image-input");
// const fileName = document.querySelector(".modal#edit-user-details form .file-input-value");
// // InputButton.onclick = function (e) {
// // 	e.preventDefault();
// // 	e.stopPropagation();
// // 	let fileFormValue = InputButton.previousElementSibling;
// // 	fileFormValue.click();
// // 	fileFormValue.addEventListener("change", function () {
// // 		if (fileFormValue.files.length == 0) {
// // 			return;
// // 		} else {
// // 			const fakePathFileName = fileFormValue.value.substr(0, 12);
// // 			const newFileName = fileFormValue.value.replace(fakePathFileName, "");
// // 			fileName.innerHTML = `${newFileName}`;
// // 		}
// // 	});
// // };
