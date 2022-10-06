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
            if (window.location.href === "https://wishlist-flask.herokuapp.com/login") {
                window.location.href = `/dashboard?user=${data.id}`;
            };
        } else {
            if (window.location.href !== "https://wishlist-flask.herokuapp.com/login") {
                window.location.href = "/login";
            };
        };
    })
    .catch(err => console.log(err));
};

function securityCheck(): void {
    let params = new URLSearchParams(window.location.search);
    if (params.get("user") != localStorage.getItem("user_id")) {
        window.location.href = "/error";
    };
};

function setLinks(): void {
    let userId = localStorage.getItem("user_id");
    let dashboardLink = document.getElementById("dashboard_link");
    let wishListLink = document.getElementById("wish-list_link");
    let reviewsLink = document.getElementById("reviews_link");
    let accountLink = document.getElementById("account_link");
    let dashboardLinkMobile = document.getElementById("dashboard_linkMobile");
    let wishListLinkMobile = document.getElementById("wish-list_linkMobile");
    let reviewsLinkMobile = document.getElementById("reviews_linkMobile");
    let accountLinkMobile = document.getElementById("account_linkMobile");

    dashboardLink.setAttribute("href", `/dashboard?user=${userId}`);
    wishListLink.setAttribute("href", `/wish-list?user=${userId}`);
    reviewsLink.setAttribute("href", `/reviews?user=${userId}`);
    accountLink.setAttribute("href", `/account?user=${userId}`);
    dashboardLinkMobile.setAttribute("href", `/dashboard?user=${userId}`);
    wishListLinkMobile.setAttribute("href", `/wish-list?user=${userId}`);
    reviewsLinkMobile.setAttribute("href", `/reviews?user=${userId}`);
    accountLinkMobile.setAttribute("href", `/account?user=${userId}`);
    securityCheck();
};

document.addEventListener("DOMContentLoaded", () => {
    permissionCheck();
    setLinks();
});