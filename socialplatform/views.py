from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.urls import reverse_lazy
from .models import Group, groupAdmin, Post, GroupJoinedMembers
from .forms import logInForm, SignUpform, GroupForm, GroupPostForm

def index(request):
    return render(request, 'socialplatform/index.html')

def loginView(request):
    if request.method == 'POST':
        form = logInForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user:
                login(request, user)

                # get created groups from all users
                Groups = Group.objects.annotate(no_of_posts=Count('posts'))

                # get group members 
                total_groups = Group.objects.all()

                group_members = [GroupJoinedMembers.objects.filter(group_name=g.id).count() for g in total_groups]

                # get groups for current user groups

                # filter group admin by email address and get id
                current_user = groupAdmin.objects.filter(email=user.email).values_list("id", flat=True)[0]
                print("current_user", current_user)
                # get groups for current logged-in user
                user_groups = Group.objects.filter(admin=current_user).annotate(no_of_posts = Count('posts'))

                # check if the current user joined the group
                chk = []
                for g in total_groups:
                    if (GroupJoinedMembers.objects.filter(group_name=g.id, member=current_user)):
                        chk.append(1)
                    else: 
                        chk.append(0)

                return render(request, 'socialplatform/register/login_success.html', {'user': user,
                                                                                      'Groups': Groups,
                                                                                      'user_groups': user_groups, 
                                                                                      "current_user": current_user,
                                                                                      'group_members': group_members,
                                                                                      'memberGroupJoined': chk})
            else:
                return render(request, 'socialplatform/index.html', {'msg': 'Invalid credentials'})
    else:
        form = logInForm()
    return render(request, 'socialplatform/register/login.html', {'form': form})

def logoutView(request):
    logout(request)
    return render(request, 'socialplatform/register/logout.html')

def SignupView(request):
    if request.method == 'POST':
        form = SignUpform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = form.save(commit=False)
            user.set_password(cd['password1'])
            user.save()

            # 
            groupAdmin.objects.create(username=cd['username'], email=cd['email'])
            return redirect('social:login')
    else:
        form = SignUpform()
    return render(request, 'socialplatform/register/signup.html', {'form': form})

def groupList(request):
    Groups = Group.objects.all().annotate(no_of_posts = Count('posts'))
    
    return render(request, 'socialplatform/group/list_group.html', {"Groups": Groups})

@login_required
def createGroup(request):
    if request.method == 'POST':
        groupForm = GroupForm(request.POST)
        if groupForm.is_valid():
            cd = groupForm.cleaned_data
            if request.user.is_authenticated:
                # get current logged in user
                admin = request.user
                print(admin)
                print("SessionKey", request.session._session_key)
                # get user model from Admin model
                group_admin = groupAdmin.objects.get(username=admin)
                # create group for logged in user
                Group.objects.create(admin=group_admin, name=cd['name'], description=cd['description'])   

                all_post = Post.objects.filter(group=Group.objects.get(name=cd['name']))
            return render(request, 'socialplatform/group/group_created.html', {'groupName': cd['name'],
                                                                               'groupPosts': all_post})         
    else:
        groupForm = GroupForm()
    return render(request, 'socialplatform/group/group_form.html', {'form':groupForm})

def createPost(request):

    if request.method == 'POST':
        form = GroupPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            select_group = Group.objects.get(name=cd['group'])
            Post.objects.create(group=select_group , message=cd['message'])

            all_post = Post.objects.filter(group=select_group)
            return render(request, 'socialplatform/group/group_created.html', {'groupName': select_group,
                                                                               'groupPosts': all_post})         
    else:
        form = GroupPostForm()
    return render(request, 'socialplatform/post/create_post.html', {'form': form})
    
def postList(request, group_id):
    group = Group.objects.get(pk=group_id)
    all_posts = Post.objects.filter(group=group)

    group_members_count = GroupJoinedMembers.objects.filter(group_name=group_id).count()

    print("group_id: ", group_id)
    print(group_members_count)
    return render(request, 'socialplatform/post/post_display.html', {'Posts': all_posts,
                                                                     'Group': group,
                                                                     'group_members_count': group_members_count})


def join_group(request):
    group = request.POST.get('group_id')
    member = request.POST.get('user_id')
    print("Group ID: ", group)

    print("Current User: ", member)
    action = request.POST.get('action')

    print(action)
    if action == 'join Group':
        get_group = Group.objects.get(pk=group)
        get_member = groupAdmin.objects.get(pk=member)
        GroupJoinedMembers.objects.create(group_name=get_group, member=get_member)
        print("Group Joined")
    else:
        get_member = groupAdmin.objects.get(pk=member)
        GroupJoinedMembers.objects.filter(group_name=group, member=get_member).delete()
        print("Group Leaved")

    return JsonResponse({'status': 'ok'})