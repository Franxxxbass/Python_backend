from django.shortcuts import render, redirect

TASKS = []


def task_create_view(request):

    task = request.POST.get('task') #zwroci None, jezeli nie bedzie taska w querydict,
                                    # mozna dac drugi parametr i w nim cokolwiek - stringa, inta
    if task:
        TASKS.append(task)

        return redirect('taskapp:task_list_view')

    return render(
        request,
        'taskapp/task-form.html',
    )


def task_list_view(request):
    return render(
        request,
        'taskapp/task-list.html',
        context={
            'tasks' : TASKS,
        }
    )