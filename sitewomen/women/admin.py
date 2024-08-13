from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Women, Category


# свой собственный фильтр
class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус женщин'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем'),
        ]
    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)

@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    # отображение полей в записи и форме
    fields = ['title', 'slug', 'content', 'photo', 'post_photo', 'cat', 'husband', 'tags']
    # exclude = ['tags', 'is_published']
    # отображаются все поля, в указываем какие не отображаем
    prepopulated_fields = {"slug": ("title", )}
    readonly_fields = ['post_photo']
    # указываем нередактируемые поля, только для чтения
    # поля не применять если небходимо создавать slug(prepopulated_fields)
    # filter_horizontal = ['tags']
    # отображение тегов в фомре, можно сделать и вертикальлно filter_vertical
    filter_vertical = ['tags']
    list_display = ('title', 'post_photo', 'time_create', 'is_published', 'cat')
    list_display_links = ('title',)
    # делает текст кликабельной ссылкой
    ordering = ['time_create', 'title']
    # сортировка
    list_editable = ('is_published',)
    list_per_page = 10
    # пагинация в админке
    actions = ['set_published', 'set_draft']
    # активация действий, прописаны ниже функции
    search_fields = ['title__startswith', 'cat__name']
    # добовление поиска, cat__name поиск через связанную таблицу(категории)
    list_filter = [MarriedFilter, 'cat__name', 'is_published']
    save_on_top = True
    # кнопка сохранить сверху и снизу

    @admin.display(description="Изображение", ordering='content')
    def post_photo(self, women: Women):
        if women.photo:
            return mark_safe(f"<img src='{women.photo.url}' width=50>")
        return "Без фото"
    # отображение картинок в админке


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

