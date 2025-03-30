document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("cashflowForm").addEventListener("submit", function (event) {
        event.preventDefault();

        let formData = {
            date_create: document.getElementById("date_create").value,
            status: document.getElementById("status").value,
            type_cashflow: document.getElementById("type_cashflow").value,
            category: document.getElementById("category").value,
            subcategory: document.getElementById("subcategory").value,
            sum_cashflow: document.getElementById("sum_cashflow").value,
            comment: document.getElementById("comment").value
        };

        fetch("/add_cashflow/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                location.reload();
            }
        })
        .catch(error => console.error("Ошибка:", error));
    });
});

// Функция для получения CSRF-токена из куков
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        let cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
