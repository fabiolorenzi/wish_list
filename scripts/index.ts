function permissionCheck(): boolean {
    let id = sessionStorage.getItem("user_id");
    let email = sessionStorage.getItem("email");
    let passkey = sessionStorage.getItem("passkey");
    let result: boolean

    fetch(`/api/user/${id}`, {
        method: "POST",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email: email,
            password: passkey
        })
    })
    .then(resp => resp.json())
    .then(data => result = data)
    .catch(err => {
        console.log(err);
        result = false;
    });
    return result;
};

document.addEventListener("DOMContentLoaded", () => {
    if (permissionCheck()) {
        if (window.location.href === "/login") {
            window.location.href = "/dashboard";
        };
    } else {
        window.location.href = "/login";
    };
});