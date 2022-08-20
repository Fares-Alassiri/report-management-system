from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import transaction

from core.models import *
# from core.forms import ReportForm

# Create your views here.

def home(request):
    return render(request, 'core/dashboard.html')

def reports(request):
    # TODO: filter reports by groups of user
    reports = Report.objects.all()
    context = {
        'reports': reports,
    }
    return render(request, 'core/reports.html', context)

def report(request, pk):
    report = Report.objects.get(id=pk)
    context = {
        'report': report,
    }
    return render(request, 'core/report.html', context)

def create_report(request):
    if request.method == 'POST':
        try:
            request.POST.get('Name')[0]
            with transaction.atomic():
                report = Report.objects.create(
                    name = request.POST.get('Name'),
                    author = Profile.objects.get(user=1),
                    content = request.POST.get('Content'),
                )

                tags = str(request.POST.get('Tags')).split(',')
                for t in tags:
                    tag, created_tag = Tag.objects.get_or_create(name=t)
                    report.tags.add(tag)
                
                groups = request.POST.getlist('Groups')
                for g in groups:
                    group = Group.objects.get(id=int(g))
                    report.groups.add(group)

                report.editors.add(Profile.objects.get(user=1))

                files = request.FILES.getlist('Files')
                for file in files:
                    Attachment.objects.create(
                        file = file,
                        report = report
                    )
        except:
            groups = Group.objects.filter(profiles=Profile.objects.get(user=1))
            context = { 
                'groups': groups,
                'error': 'Please make sure that you entered valid inputs and try again'
            }

            return render(request, 'core/create_report.html', context)
        # Attachment.objects.create(file=request.FILES.get('Files'))
        return redirect('/report')
    # TODO: filter reports by groups of user
    groups = Group.objects.filter(profiles=Profile.objects.get(user=1))
    context = { 
        'groups': groups,
    }

    return render(request, 'core/create_report.html', context)

def update_report(request, pk):
    if request.method == 'POST':
        try:
            request.POST.get('Name')[0]
            with transaction.atomic():
                report = Report.objects.get(id=pk)

                report.name = request.POST.get('Name')
                report.content = request.POST.get('Content')

                report.tags.clear()
                tags = str(request.POST.get('Tags')).split(',')
                for t in tags:
                    tag, created_tag = Tag.objects.get_or_create(name=t)
                    report.tags.add(tag)
                
                report.groups.clear()
                groups = request.POST.getlist('Group')
                groups[0]
                for g in groups:
                    group = Group.objects.get(id=int(g))
                    report.groups.add(group)

                report.editors.add(Profile.objects.get(user=1))
                report.editors.add(Profile.objects.get(user=1))

                report.save()

                files = request.FILES.getlist('Files')
                for file in files:
                    Attachment.objects.create(
                        file = file,
                        report = report
                    )
        except Exception as e:
            print(e)
            report = Report.objects.get(id=pk)
            # TODO: filter reports by groups of user
            groups = Group.objects.filter(profiles=Profile.objects.get(user=1))
            rgroups = report.groups.all()
            temp3 = []
            for element in rgroups:
                if element not in groups:
                    temp3.append(element)
            dgroups = temp3
            context = { 
                'report': report,
                'groups': groups,
                'rgroups': rgroups,
                'dgroups': dgroups,
                'error': 'Please make sure that you entered valid inputs and try again'
            }

            return render(request, 'core/update_report.html', context)
        # Attachment.objects.create(file=request.FILES.get('Files'))
        return redirect('/report/{}'.format(pk))
    report = Report.objects.get(id=pk)
    # TODO: filter reports by groups of user
    groups = Group.objects.filter(profiles=Profile.objects.get(user=1))
    rgroups = report.groups.all()
    temp3 = []
    for element in rgroups:
        if element not in groups:
            temp3.append(element)
    dgroups = temp3
    context = { 
        'report': report,
        'groups': groups,
        'rgroups': rgroups,
        'dgroups': dgroups
    }

    return render(request, 'core/update_report.html', context)

def delete_report(request, pk):
    report = Report.objects.get(id=pk).delete()
    return redirect('/report')

def delete_attachment(request, rid, aid):
    attachment = Attachment.objects.get(id=aid).delete()
    return redirect('/report/{}/update'.format(rid))