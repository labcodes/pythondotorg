from django.contrib import admin

from cms.admin import (
    ContentManageableModelAdmin,
    NameSlugAdmin,
)
from .models import (
    Job,
    JobCategory,
    JobReviewComment,
    JobType,
)


@admin.register(Job)
class JobAdmin(ContentManageableModelAdmin):
    date_hierarchy = 'created'
    filter_horizontal = ['job_types']
    list_display = ['__str__', 'job_title', 'status', 'company_name']
    list_filter = ['status', 'telecommuting']
    raw_id_fields = ['category', 'submitted_by']
    search_fields = ['id', 'job_title']


@admin.register(JobType)
class JobTypeAdmin(NameSlugAdmin):
    list_display = ['__str__', 'active']
    list_filter = ['active']
    ordering = ('-active', 'name')


@admin.register(JobCategory)
class JobCategoryAdmin(NameSlugAdmin):
    list_display = ['__str__', 'active']
    list_filter = ['active']
    ordering = ('-active', 'name')


@admin.register(JobReviewComment)
class JobReviewCommentAdmin(ContentManageableModelAdmin):
    list_display = ['__str__', 'job']
    ordering = ('-created',)
