document.addEventListener("DOMContentLoaded", function () {
    let categorySelect = document.getElementById("category");
    let subcategorySelect = document.getElementById("subcategory");

    categorySelect.addEventListener("change", function () {
        let selectedCategory = this.value;
        subcategorySelect.innerHTML = '<option value="">Загрузка...</option>';
        subcategorySelect.disabled = true;

        fetch(`/get_subcategories/?category_id=${selectedCategory}`)
            .then(response => response.json())
            .then(data => {
                subcategorySelect.innerHTML = '<option value="">Выберите подкатегорию</option>';
                data.forEach(subcategory => {
                    let option = document.createElement("option");
                    option.value = subcategory.id;
                    option.textContent = subcategory.name;
                    subcategorySelect.appendChild(option);
                });
                subcategorySelect.disabled = false;
            })
            .catch(error => console.error("Ошибка загрузки подкатегорий:", error));
    });
});

document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".delete-btn").forEach(button => {
        button.addEventListener("click", function () {
            let recordId = this.dataset.recordId;
            

            if (confirm("Вы уверены, что хотите удалить эту запись?")) {
                fetch(`/delete_cashflow/${recordId}/`, {
                    method: "POST",
                    headers: { "X-CSRFToken": getCookie("csrftoken") },
                })
                .then(response => response.json())
                .then(data => {
                    if (data.message) {
                        alert(data.message);
                        location.reload();  // Обновляем страницу после удаления
                    } else {
                        alert("Ошибка при удалении");
                    }
                })
                .catch(error => console.error("Ошибка:", error));
            }
        });
    });
});

document.getElementById('filterCategory').addEventListener('change', function () {
    const categoryId = this.value;
    const subcategorySelect = document.getElementById('filterSubcategory');

    subcategorySelect.innerHTML = '<option value="">Загрузка...</option>';
    subcategorySelect.disabled = true;

    if (categoryId) {
        fetch(`/get_subcategories/?category_id=${categoryId}`)
            .then(response => response.json())
            .then(data => {
                subcategorySelect.innerHTML = '<option value="">Выберите подкатегорию</option>';
                data.forEach(sub => {
                    const option = document.createElement('option');
                    option.value = sub.id;
                    option.textContent = sub.name;
                    subcategorySelect.appendChild(option);
                });
                subcategorySelect.disabled = false;
            });
    } else {
        subcategorySelect.innerHTML = '<option value="">Сначала выберите категорию</option>';
        subcategorySelect.disabled = true;
    }
});

// Функция для получения CSRF-токена
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