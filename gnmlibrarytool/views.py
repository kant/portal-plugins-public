from django.views.generic import View, TemplateView

class MainAppView(TemplateView):
    from .forms import ShowSearchForm
    template_name = "gnmlibrarytool/index.html"

    def get_context_data(self, **kwargs):
        context = super(MainAppView, self).get_context_data(**kwargs)
        context['search_form'] = self.ShowSearchForm()
        #context['latest_articles'] = Article.objects.all()[:5]
        return context


class LibraryListView(View):

    def get(self,request):
        from .VSLibrary import VSLibrary, VSLibraryCollection, HttpError
        from django.http import HttpResponse
        import json
        import logging

        onlyAutoRefresh = None
        if 'autoRefresh' in request.GET:
            if request.GET['autoRefresh'].lower() == "true":
                onlyAutoRefresh = True
            else:
                onlyAutoRefresh = False

        from django.conf import settings
        libraries = VSLibraryCollection(url=settings.VIDISPINE_URL,port=settings.VIDISPINE_PORT,
                                        username=settings.VIDISPINE_USERNAME,password=settings.VIDISPINE_PASSWORD)

        if 's' in request.GET:
            libraries.page_size = int(request.GET['s'])
        page = 0
        if 'p' in request.GET:
            page = int(request.GET['p'])

        rtn = []
        try:
            for libname in libraries.scan(page=page, autoRefresh=onlyAutoRefresh):
                try:
                    l=VSLibrary(url=settings.VIDISPINE_URL,port=settings.VIDISPINE_PORT,
                                username=settings.VIDISPINE_USERNAME,password=settings.VIDISPINE_PASSWORD)

                    rtn.append({'id': libname, 'hits': l.get_hits(libname)})
                except HttpError as e:
                    if e.status!=404:
                        raise e #re-raise exception to outer loop, we don't know what happened
                    logging.warning(e.__unicode__())

            return HttpResponse(content=json.dumps({'status': 'ok','total': libraries.count, 'pages': libraries.page_count,
                                                    'results': rtn}),content_type='application/json', status=200)
        except HttpError as e:
            return HttpResponse(content=json.dumps({'status': 'error', 'error': e.__unicode__()}), content_type='application/json', status=500)