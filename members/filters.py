import django_filters
from .models import MemberProfile
from django.utils import timezone
class MemberProfileFilter(django_filters.FilterSet):
    class Meta:
        model = MemberProfile
        fields = {
            "user__phone_number": ["exact", "icontains"],  
            "user__first_name": ["icontains"],
            "user__last_name": ["icontains"],
            "barcode": ["exact", "icontains"],
            "start_date": ["exact", "gte", "lte"],
            "end_date": ["exact", "gte", "lte"],
            "package_type": ["exact"],
        }


    def filter_left_days(self, queryset, name, value):
        today = timezone.now().date()
        return queryset.filter(end_date__date=today + timezone.timedelta(days=value))

