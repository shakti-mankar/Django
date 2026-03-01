from django.shortcuts import render

def quiz(request):

    questions = [
        {
            "id": 1,
            "question": "Which keyword is used to create a function in Python?",
            "options": ["func", "define", "def", "function"],
            "answer": "def"
        },
        {
            "id": 2,
            "question": "Which HTTP method is mainly used to submit form data?",
            "options": ["GET", "POST", "PUT", "DELETE"],
            "answer": "POST"
        },
        {
            "id": 3,
            "question": "Which file handles URL routing in Django?",
            "options": ["views.py", "models.py", "urls.py", "settings.py"],
            "answer": "urls.py"
        },
        {
            "id": 4,
            "question": "Which tag is used to insert an image in HTML?",
            "options": ["<img>", "<image>", "<src>", "<pic>"],
            "answer": "<img>"
        },
        {
            "id": 5,
            "question": "Which database is default in a new Django project?",
            "options": ["MySQL", "PostgreSQL", "SQLite", "Oracle"],
            "answer": "SQLite"
        }
    ]

    score = None
    submitted = False

    if request.method == "POST":
        submitted = True
        score = 0

        for q in questions:
            user_answer = request.POST.get(f"question_{q['id']}")
            if user_answer == q["answer"]:
                score += 1

    return render(request, "quiz.html", {
        "questions": questions,
        "score": score,
        "submitted": submitted
    })