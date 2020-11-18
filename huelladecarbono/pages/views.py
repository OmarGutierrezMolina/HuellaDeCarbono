from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Page
from .forms import PageForm 
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

class StaffRequiredMixin(object):
    """ 
    Verifica que el usuario sea staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        """
        mejor utilizar el decorador
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        """
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
    

class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')
    ### alternativa para comprobar si el usuario esta identificado y pueda usar el crud
   
    

@method_decorator(staff_member_required, name='dispatch')
class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        ### para pasar el identificador y retornar a la pagina en edición
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PageDeleteView( DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')






