from django.shortcuts import render
from google import genai
from django.conf import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

def home(request):
    response_text = ""

    if request.method == "POST":
        question = request.POST.get("question")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question,
        )

        response_text = response.text

    return render(request, "index.html", {"response": response_text})
