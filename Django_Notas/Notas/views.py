from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from Notas.models import Cat_estatus, Cat_notas
from Notas.forms import CreateNewEstatusForm
from django.core.urlresolvers import reverse_lazy
# from requests import request


class ListStatusView(ListView):
	model = Cat_estatus
	template_name = "cat_estatus_list.html"
	queryset = Cat_estatus.objects.all().order_by('id')

	def get_filter(self, queryset):
		search = self.get_search()
		if search:
			queryset = queryset.filter(
				Q(nombre__icontains=search)
			)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(ListStatusView, self).get_context_data(**kwargs)
		return context


class CreateNewEstatusView(CreateView):
	model = Cat_estatus
	form_class = CreateNewEstatusForm
	success_url = reverse_lazy("ListSsstatus")
	template_name = "cat_estatus_form.html"

	def form_valid(self, form):
		messages.success(self.request, "Se agrego un nuevo estatus")
		return super(CreateNewEstatusView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(CreateNewEstatusView, self).get_context_data(**kwargs)
		return context
