from django.views.generic import DetailView, ListView

from .models import Revue


class RevueListView(ListView):
    model = Revue
    context_object_name = "revues"
    template_name = "revues/revues_list.html"


class RevueDetailView(DetailView):
    model = Revue
    context_object_name = "revue"
    template_name = "revues/revue_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            next_revue = self.object.get_next_by_opening_date()
        except Revue.DoesNotExist:
            next_revue = None

        try:
            prev_revue = self.object.get_previous_by_opening_date()
        except Revue.DoesNotExist:
            prev_revue = None

        context.update({
            "next": next_revue,
            "prev": prev_revue,
        })
        return context
