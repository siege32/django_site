from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from .models import *

def main_page(request): # Представление страницы
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    posts = Cashflow.objects.all()
    statuses = Status.objects.all()
    types_cashflow = Type_cashflow.objects.all()

    return render(request, "main_page/main_page.html", {
        "categories": categories,
        "subcategories": subcategories,
        "posts": posts,
        "statuses": statuses,
        "types_cashflow": types_cashflow,
    })

def add_cashflow(request): # Представление сбора данных
    if request.method == "POST":
        status_id = request.POST.get("status")
        type_cashflow_id = request.POST.get("type_cashflow")
        category_id = request.POST.get("category")
        subcategory_id = request.POST.get("subcategory")
        sum_cashflow = request.POST.get("sum_cashflow")
        comment = request.POST.get("comment")

        category = Category.objects.get(id=category_id) if category_id else None
        subcategory = Subcategory.objects.get(id=subcategory_id) if subcategory_id else None
        status = Status.objects.get(id=status_id) if status_id else None
        type_cashflow = Type_cashflow.objects.get(id=type_cashflow_id) if type_cashflow_id else None

        Cashflow.objects.create(
            status=status,
            type_cashflow=type_cashflow,
            category=category,
            subcategory=subcategory,
            sum_cashflow=sum_cashflow,
            comment=comment
        )

        return JsonResponse({"success": True})

    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)

def get_subcategories(request): # Представление сбора подкатегории
    category_id = request.GET.get("category_id")
    subcategories = Subcategory.objects.filter(category_id=category_id).values("id", "name")
    return JsonResponse(list(subcategories), safe=False)

def edit_cashflow(request, record_id): # Представление редактирования записей
    if request.method == "POST":
        record = get_object_or_404(Cashflow, id=record_id)

        # Преобразуем ID в объекты соответствующих моделей
        record.status = get_object_or_404(Status, id=request.POST.get("status"))
        record.type_cashflow = get_object_or_404(Type_cashflow, id=request.POST.get("type_cashflow"))
        record.category = get_object_or_404(Category, id=request.POST.get("category"))
        record.subcategory = get_object_or_404(Subcategory, id=request.POST.get("subcategory"))
        
        # Обычные строковые и числовые поля можно присваивать напрямую
        record.sum_cashflow = request.POST.get("sum_cashflow")
        record.comment = request.POST.get("comment")

        record.save()
        return JsonResponse({"message": "Запись успешно обновлена"})
    
def delete_cashflow(request, record_id): # Представление удаления записей
    if request.method == "POST":  # Используем POST-запрос для удаления
        record = get_object_or_404(Cashflow, id=record_id)
        record.delete()
        return JsonResponse({"message": "Запись успешно удалена"})
    return JsonResponse({"error": "Неверный метод запроса"}, status=400)

@csrf_exempt
def add_status(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            Status.objects.create(name=name)
            return JsonResponse({"message": "Статус добавлен!"})
    return JsonResponse({"error": "Ошибка добавления статуса"}, status=400)

@csrf_exempt
def add_type(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            Type_cashflow.objects.create(name=name)
            return JsonResponse({"message": "Тип добавлен!"})
    return JsonResponse({"error": "Ошибка добавления типа"}, status=400)

@csrf_exempt
def add_category(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            Category.objects.create(name=name)
            return JsonResponse({"message": "Категория добавлена!"})
    return JsonResponse({"error": "Ошибка добавления категории"}, status=400)

@csrf_exempt
def add_subcategory(request):
    if request.method == "POST":
        name = request.POST.get("subcategory")
        category_id = request.POST.get("category")
        if name and category_id:
            category = Category.objects.get(id=category_id)
            Subcategory.objects.create(name=name, category=category)
            return JsonResponse({"message": "Подкатегория добавлена!"})
    return JsonResponse({"error": "Ошибка добавления подкатегории"}, status=400)

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
