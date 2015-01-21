from django.utils.translation import ungettext_lazy

from django_tables2 import Table


class DashboardTable(Table):
    _caption = None
    caption = ungettext_lazy('{count} Row', '{count} Rows')

    @property
    def caption(self):
        # Allow overriding the caption with an arbitrary string that we cannot
        # interpolate the number of rows in
        try:
            return self._caption % self.paginator.count
        except TypeError:
            return self._caption

    @caption.setter
    def caption(self, caption):
        self._caption = caption

    class Meta:
        template = 'dashboard/table.html'
        attrs = {'class': 'table table-striped table-bordered'}
