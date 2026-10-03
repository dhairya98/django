from django.contrib import admin
from .models import FirstModel, EngineerReview, Store, ProfileExpansion

# 2. Setup the Inline block for the One-to-Many relationship
class EngineerReviewInline(admin.TabularInline):
    model = EngineerReview
    extra = 2

class FirstModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'tech', 'date_added')
    inlines = [EngineerReviewInline]

# 4. Setup the Admin class for your Many-to-Many model
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('first_models',) # Links the ManyToManyField name

# class ProfileExpansionInline(admin.TabularInline):
#     model = ProfileExpansion
#     extra = 1

# 5. Register all models at the bottom using their respective Admin classes
admin.site.register(FirstModel, FirstModelAdmin)
admin.site.register(Store, StoreAdmin)

# Register the remaining standalone models
admin.site.register(EngineerReview)  # Optional: You can register this if you want to manage reviews separately
admin.site.register(ProfileExpansion)