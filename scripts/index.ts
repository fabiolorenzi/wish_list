function permissionCheck(): void {
    let id = sessionStorage.getItem("user_id");
    let email = sessionStorage.getItem("email");
    let passkey = sessionStorage.getItem("passkey");

    fetch(`/api/user/${id}`, {
        method: "GET",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    })
    .then(resp => resp.json())
    .then(data => {
        if (data.email === email && data.password === passkey) {
            if (window.location.href === "http://127.0.0.1:5000/login") {
                window.location.href = "/dashboard";
            };
        } else {
            if (window.location.href !== "http://127.0.0.1:5000/login") {
                window.location.href = "/login";
            };
        };
    })
    .catch(err => console.log(err));
};

document.addEventListener("DOMContentLoaded", () => {
    permissionCheck();
});