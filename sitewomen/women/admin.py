from django.contrib import admin, messages
from .models import Women, Category


# Register your models here.
@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create', 'is_published', 'cat', 'brief_info')
    list_display_links = ('title',)
    # делает текст кликабельной ссылкой
    ordering = ['time_create', 'title']
    # сортировка
    list_editable = ('is_published',)
    list_per_page = 5
    # пагинация в админке
    actions = ['set_published', 'set_draft']
    # активация действий, прописаны ниже функции

    @admin.display(description="Краткое описание", ordering='content')
    def brief_info(self, women: Women):
        return f"Описание {len(women.content)} символов."


    @admin.display(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")
    #     новое действие в админке. Зеленый знак


    @admin.display(description="Снять с публикации")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f"{count} записей снято с публикации.", messages.WARNING)
#         Новое действие в админке. Знак внимания


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

