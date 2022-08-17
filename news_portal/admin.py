from django.contrib import admin
from.models import Post,Category,Author,UserSubscribers


admin.site.register(Author)
admin.site.register(UserSubscribers)

class CategorylineAdmin(admin.TabularInline):
    model = Post.postCategory.through


class PostAdmin(admin.ModelAdmin):
    model = Post
    fields = ['author', 'title', 'categoryType', 'text']
    inlines = (CategorylineAdmin,)

admin.site.register(Post, PostAdmin)


class subscriberslineAdmin(admin.TabularInline):
    model = Category.subscribers.through

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {"slug": ("name",)}
    inlines = (subscriberslineAdmin,)

admin.site.register(Category, CategoryAdmin)