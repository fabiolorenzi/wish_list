function createCategory(): void {
    let name = (document.getElementById("nameInput") as HTMLInputElement)?.value;
    fetch("/api/categories", {
        method: "POST",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name,
            user_id: localStorage.getItem("user_id")
        })
    })
    .then(resp => resp.json())
    .then(data => {
        if (data) {
            alert("Category added successfully");
            window.location.reload();
        };
    })
    .catch(err => console.log(err));
};