from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Subject, SubjectEnrollment, Resources
from students.models import StudentProfile
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages


@login_required(login_url='/login/')
def subject_list(request):
    user = request.user
    profile = StudentProfile.objects.get(user=user)


    # 1. Enrolled Subjects
    enrolled_subjects = profile.enrolled_subjects.all()
    # 2. Featured Subjects (not already enrolled)
    featured_subjects = Subject.objects.filter(
        is_featured=True,
        is_active=True
    ).exclude(
        id__in=enrolled_subjects.values_list("id", flat=True)
    )[:10]

    # 3. Recommended Subjects (based on user’s enrolled stream & class)
    #    -> Strategy: take user's enrolled subjects, infer stream/class
    recommended_subjects = Subject.objects.none()
    if enrolled_subjects.exists():
        # take first subject's stream/class as a hint
        stream = enrolled_subjects.first().stream
        class_level = enrolled_subjects.first().class_level

        recommended_subjects = Subject.objects.filter(
            stream__in=[stream],
            class_level=class_level,
        ).exclude(
            id__in=enrolled_subjects.values_list("id", flat=True)
        )[:10]

    context = {
        "enrolled_subjects": enrolled_subjects,
        "featured_subjects": featured_subjects,
        "recommended_subjects": recommended_subjects,
    }
    return render(request, "subjects/subject_list.html", context)



@login_required(login_url='/login/')
def subject_all(request):
    """ Full catalog page with all active subjects grouped logically """
    subjects = Subject.objects.filter(is_active=True).order_by("stream", "class_level", "name")

    context = {
        "all_subjects": subjects,
    }
    return render(request, "subjects/subject_all.html", context)


@login_required
@require_POST
def subject_enroll(request):
    """View to handle AJAX (or form) enrollment requests"""
    subject_id = request.POST.get('subject_id')
    
    if not subject_id:
        # Handle error if no subject ID is provided
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': 'No subject ID provided.'})
        else:
            messages.error(request, "No subject selected.")
            return redirect('subject_list')
    
    try:
        subject = Subject.objects.get(id=subject_id)
    except Subject.DoesNotExist:
        # Handle error if subject doesn't exist or is inactive
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': 'Subject not found.'})
        else:
            messages.error(request, "Subject not found.")
            return redirect('subject_list')
    
    # Get the user's profile
    profile = StudentProfile.objects.get(user=request.user)
    
    # Check if already enrolled to avoid duplicates
    if profile.enrolled_subjects.filter(id=subject.id).exists():
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': 'Already enrolled in this subject.'})
        else:
            messages.info(request, f"You are already enrolled in {subject.name}.")
            return redirect('subject_list')
    
    # Add the subject to the enrolled list
    profile.enrolled_subjects.add(subject)
    profile.save()
    
    # Success response
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': True, 'message': f'Successfully enrolled in {subject.name}!'})
    else:
        messages.success(request, f"Successfully enrolled in {subject.name}!")
        return redirect('subject_list')

@login_required
def subject_remove(request, pk):
    student_profile = get_object_or_404(StudentProfile, user=request.user)
    subject = get_object_or_404(Subject, pk=pk)

    if request.method == "POST":
        student_profile.enrolled_subjects.remove(subject)
        messages.success(request, "Subject removed from your enrolled list!")
    return redirect("subject_list")


@login_required(login_url='/login/')
def Materials(req):
    user = req.user

    profile = StudentProfile.objects.get(user=user)

    enl_subjects = profile.enrolled_subjects.all()
    active_type = req.GET.get("subjects_type")
    docs = Resources.objects.filter(user=req.user)

    if active_type:
        docs = docs.filter(subjects_type_id=active_type)

    return render(req, 'resources/resources.html', {"subjects": enl_subjects, "documents": docs, "active_type": int(active_type) if active_type else None,})


@login_required
def upload_document(request):
    if request.method == "POST":
        subject_id = request.POST.get("subjects_type")
        file = request.FILES.get("file")

        if subject_id and file:
            subject = Subject.objects.get(id=subject_id)
            Resources.objects.create(user=request.user, subjects_type=subject, file=file)
        return redirect("material") # or wherever you show uploaded files
    return redirect("material")

@login_required
def delete_document(request, pk):
    doc = get_object_or_404(Resources, pk=pk, user=request.user)
    if request.method == "POST":
        doc.file.delete(save=False)   # remove actual file
        doc.delete()
        messages.success(request, "Document deleted successfully!")
        return redirect("material")
    return redirect("material")