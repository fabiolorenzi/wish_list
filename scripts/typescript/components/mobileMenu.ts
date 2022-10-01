var buttonStatus: boolean = false;

function openClose(): void {
    buttonStatus = !buttonStatus;
    let targetId = document.getElementById("mobileMenu");
    if (buttonStatus) {
        targetId.classList.remove("mobileMenu_off");
        targetId.classList.add("mobileMenu_on");
    } else {
        targetId.classList.remove("mobileMenu_on");
        targetId.classList.add("mobileMenu_off");
    };
};