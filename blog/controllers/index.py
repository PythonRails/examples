from rails.response import Response
from rails.views import render_template


class Index(object):
    """
    Index controller is a root project controller.

    With this controller you can show welcome page and handle all non-existing pages.
    """

    def index(self, request):
        """
        Show welcome page of the project.
        """
        data = render_template('index/index.html')
        return Response(data)

    def not_found(self, request):
        """
        Handle all requests that can't be handled by any controller.

        You can open page '/index/blabla' or '/blabla' to see this page.
        """
        data = render_template('index/not_found.html', {
            'requested_path': request.path,
        })
        return Response(data)
