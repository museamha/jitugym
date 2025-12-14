import django_filters
from .models import MemberProfile
from django.utils import timezone
class MemberProfileFilter(django_filters.FilterSet):
    active = django_filters.BooleanFilter(
        field_name="user__is_active")
    class Meta:
        model = MemberProfile
        fields = [
            "active",
            "package_type",
            "start_date",
            "end_date",
            "barcode",
            "user__phone_number",  
            "user__first_name",
            "user__last_name"
            
        ]


    def filter_left_days(self, queryset, name, value):
        today = timezone.now().date()
        return queryset.filter(end_date__date=today + timezone.timedelta(days=value))


