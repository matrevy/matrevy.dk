from django.contrib import admin

from .models import Revue, Scene


@admin.register(Revue)
class RevueAdmin(admin.ModelAdmin):
    pass

@admin.register(Scene)
class SceneAdmin(admin.ModelAdmin):
    pass
