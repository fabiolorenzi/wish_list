function loginFunc() {
    var emailLogin = (document.getElementById("emailLogin") as HTMLInputElement)?.value;
    let password = (document.getElementById("password") as HTMLInputElement)?.value;
    console.log(emailLogin);
};

function createUser() {
    let name = (document.getElementById("nameInput") as HTMLInputElement)?.value;
    let surname = (document.getElementById("surnameInput") as HTMLInputElement)?.value;
    let email = (document.getElementById("emailInput") as HTMLInputElement)?.value;
    let password = (document.getElementById("passwordInput") as HTMLInputElement)?.value;
};

function moveRight(): void {
    let bar = document.getElementById("user_bar");
    if (bar.classList.contains("user_barRight")) {
        bar.classList.remove("user_barRight");
    };
    bar.classList.add("user_barLeft");
};

function moveLeft(): void {
    let bar = document.getElementById("user_bar");
    if (bar.classList.contains("user_barLeft")) {
        bar.classList.remove("user_barLeft");
    };
    bar.classList.add("user_barRight");
};