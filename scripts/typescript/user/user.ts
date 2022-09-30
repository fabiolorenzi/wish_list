function loginUser() {
    let emailLogin = (document.getElementById("emailLogin") as HTMLInputElement)?.value;
    let password = (document.getElementById("password") as HTMLInputElement)?.value;
    fetch("/api/login", {
        method: "POST",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email: emailLogin,
            password: password
        })
    })
    .then(resp => resp.json())
    .then(data => {
        if (data.email !== "unavailable") {
            sessionStorage.setItem("user_id", data.id);
            sessionStorage.setItem("email", data.email);
            sessionStorage.setItem("passkey", data.password);
            window.location.href = "/dashboard";
        } else {
            alert("Login failed");
        };
    })
    .catch(err => console.log(err));
};

function createUser() {
    let name = (document.getElementById("nameInput") as HTMLInputElement)?.value;
    let surname = (document.getElementById("surnameInput") as HTMLInputElement)?.value;
    let email = (document.getElementById("emailInput") as HTMLInputElement)?.value;
    let password = (document.getElementById("passwordInput") as HTMLInputElement)?.value;
    fetch("/api/user", {
        method: "POST",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name,
            surname: surname,
            email: email,
            password: password
        })
    })
    .then(resp => resp.json())
    .then(data => {
        if (data) {
            alert("User added successfully");
            window.location.reload();
        };
    })
    .catch(err => console.log(err));
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

function cancel(): void {
    window.location.reload();
};