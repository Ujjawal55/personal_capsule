from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
# NOTE: have to remove the admin url form here


class GlobalAuthMiddleware:
    # creating the constructor class that has been called in the above middleware which passed the response object
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # first gettting the list of the exempt urls and converting it into the actual urls
        exempt_urls_names = getattr(settings, "AUTH_EXEMPT_URLS", [])  # type: ignore
        exempt_urls_path = [reverse(url) for url in exempt_urls_names]
        exempt_urls_path.append("/admin/")
        print(exempt_urls_path)
        # for the saver side just adding the login url if it is not present in the exempt_urls
        login_url = settings.LOGIN_URL
        if login_url not in exempt_urls_path:
            exempt_urls_path.append(login_url)

        # now the main login here
        # first check if the user is not autheticated and then check if the url path the user currently in is not in the exempt_urls_path variable
        if (
            not request.user.is_authenticated
            and request.path_info not in exempt_urls_path
        ):
            return redirect("home:login")

        # if the user is authenticaed or the user has in the path which is in the exempt_urls_path variable then just allow the middleware to pass the response to the next middleware

        response = self.get_response(request)
        return response
