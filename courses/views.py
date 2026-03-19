from django.shortcuts import render
from .models import Question, Choice, Submission


# Submit exam answers
def submit(request):
    if request.method == "POST":
        score = 0
        total = 0

        questions = Question.objects.all()

        for question in questions:
            selected_choice_id = request.POST.get(str(question.id))
            total += 1

            if selected_choice_id:
                selected_choice = Choice.objects.get(id=selected_choice_id)

                # Save submission
                Submission.objects.create(
                    question=question,
                    selected_choice=selected_choice
                )

                if selected_choice.is_correct:
                    score += 1

        return render(request, "result.html", {
            "score": score,
            "total": total
        })

    return render(request, "submit.html")


# Show exam result
def show_exam_result(request):
    submissions = Submission.objects.all()

    score = 0
    total = submissions.count()

    for submission in submissions:
        if submission.selected_choice.is_correct:
            score += 1

    return render(request, "result.html", {
        "score": score,
        "total": total
    })
