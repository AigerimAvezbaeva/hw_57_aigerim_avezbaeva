from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from tracker_app.models.issues import Issue

from tracker_app.forms import IssueForm


class IssueDetail(TemplateView):
    template_name = 'issue_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        return context


class IssueAddView(TemplateView):
    template_name = 'add_issue.html'

    def get(self, request, *args, **kwargs):
        form = IssueForm()
        return render(request, 'add_issue.html', context={
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save()
            return redirect('issue_detail', pk=issue.pk)
        else:
            return self.render_to_response({'form': form})


class IssueUpdateView(TemplateView):
    template_name = 'update_issue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        context['form'] = IssueForm(instance=context['issue'])
        return context

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('issue_detail', pk=issue.pk)
        return render(request, 'issue_update.html', context={
            'form': form,
            'article': issue
        })


class DeleteView(TemplateView):
    template_name = 'delete_issue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        issue.delete()
        return redirect('index')
