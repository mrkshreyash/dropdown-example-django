from django.shortcuts import render

from .models import PromptCategory, Prompts


def index(request):
    categories = PromptCategory.objects.all()
    selected_category = request.GET.get('category')
    prompts = Prompts.objects.filter(category__id=selected_category).values()
    return render(request, 'dropdown.html', {
        'categories': categories,
        'prompts': prompts,
        'selected_category': selected_category,
    })

def insert_data(request):
    if request.method == 'POST':

        # education = PromptCategory.objects.create(name="Education")

        # List of categories and their corresponding prompts
        categories_prompts = {
            'Medical': [
                'What are the major breakthroughs in medical science?',
                'How does exercise impact overall health?',
                'What are the challenges in healthcare accessibility?',
                'How to prevent common illnesses?',
                'What are the latest trends in medical technology?',
            ],
            'Sports': [
                'What are the benefits of regular physical activity?',
                'How to improve athletic performance?',
                'What are the psychological effects of sports participation?',
                'What are the most popular sports worldwide?',
                'How to prevent sports injuries?',
            ],
            'Technology': [
                'What are the upcoming trends in technology?',
                'How does artificial intelligence impact our daily lives?',
                'What are the benefits of cloud computing?',
                'How to secure your online privacy?',
                'What are the ethical considerations in technology development?',
            ],
            'Education': [
                'What are the benefits of online learning?',
                'How can we improve the education system?',
                'What is the impact of technology on education?',
                'How to make learning more engaging for students?',
                'What are the challenges faced by teachers today?',
            ]
        }

        # Insert prompts for each category
        for category_name, prompts_list in categories_prompts.items():
            category, created = PromptCategory.objects.get_or_create(name=category_name)

            for prompt_text in prompts_list:
                Prompts.objects.get_or_create(prompts=prompt_text, category=category)

        return render(request, "response.html",
                      context={"response": "Data inserted succesfully.", "prompts": Prompts.objects.all(), "categories":PromptCategory.objects.all()})

    else:
        return render(request, "response.html",
                      context={"response": "Data not inserted.", "data": Prompts.objects.all(), "categories":PromptCategory.objects.all()})
