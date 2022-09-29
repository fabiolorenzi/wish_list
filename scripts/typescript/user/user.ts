function login() {
    let username = (document.getElementById("username") as HTMLInputElement)?.value;
    let password = (document.getElementById("password") as HTMLInputElement)?.value;
    console.log(username);
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