from django.shortcuts import render
from django.conf import settings
from .models import ChatQuery


# create client lazily so that importing views doesn't fail when API key is
# missing (e.g. during migrations or when running tests).
def get_genai_client():
    api_key = getattr(settings, "GEMINI_API_KEY", None)
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY setting is not configured")

    from google import genai

    return genai.Client(api_key=api_key)


def home(request):
    response_text = ""

    if request.method == "POST":
        question = request.POST.get("question")
        if question:
            client = get_genai_client()
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=question,
            )
            response_text = response.text

            # save the query/answer pair to the database
            ChatQuery.objects.create(question=question, answer=response_text)

    return render(request, "index.html", {"response": response_text})
