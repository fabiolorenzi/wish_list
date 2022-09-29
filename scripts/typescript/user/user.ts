function login() {
    let username = (document.getElementById("username") as HTMLInputElement)?.value;
    let password = (document.getElementById("password") as HTMLInputElement)?.value;
    fetch(`${process.env.CLEARDB_DATABASE_URL}/api/login`, {
        method: "POST",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify({username, password})
    })
    .then(resp => resp.json())
    .then(data => {
        if (data.email !== "unavailable" && data.password !== "unavailable") {
            sessionStorage.setItem("user", data.id);
            sessionStorage.setItem("session", process.env.SESSION);
            window.location.href = "/dashboard";
        }
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