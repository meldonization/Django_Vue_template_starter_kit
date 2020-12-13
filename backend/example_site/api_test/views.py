from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class Test(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, *args, **kwargs):
        """
        Return a list of all users.
        """
        return Response({'data': 'Echo from Django.'})
