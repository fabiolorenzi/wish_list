function permissionCheck(): void {
    let id = localStorage.getItem("user_id");
    let email = localStorage.getItem("email");
    let passkey = localStorage.getItem("passkey");

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