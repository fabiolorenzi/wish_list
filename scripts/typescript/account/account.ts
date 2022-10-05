function logout(): void {
    localStorage.removeItem("user_id");
    localStorage.removeItem("email");
    localStorage.removeItem("passkey");
    window.location.href = "/login";
};

function deleteAccount(): void {
    let user_id = localStorage.getItem("user_id");
    fetch(`/api/user/${user_id}`, {
        method: "DELETE",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    })
    .then(() => {
        alert("User deleted successfully");
        logout();
    })
    .catch(err => console.log(err));
};