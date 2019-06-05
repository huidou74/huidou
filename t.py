#!/usr/bin/python
#-*- coding:utf8 -*-
#BY:  H.c

repository_list=['id','name','full_name','private','owner','html_url','description','fork','tags_url','created_at','updated_at','pushed_at','clone_url','size','language','archived','disabled','forks','default_branch','master_branch']
rep_dict_list=['name','email','login','id','avatar_url','html_url','repos_url']
sender_list=['login','id']

commit_del_list = ['tree_id','distinct','author']
auth_commits = ['id','message','timestamp','url','committer','added','removed','modified']

auth_data_list = ['ref', 'before', 'after', 'created', 'deleted', 'forced', 'compare']

q = ['repository_list','rep_dict_list','sender_list','commit_del_list','auth_commits','auth_data_list']
for i in q:
    print (i.upper())

# a= {'id': 124529225, 'node_id': 'MDEwOlJlcG9zaXRvcnkxMjQ1MjkyMjU=', 'name': 'huidou', 'full_name': 'huidou74/huidou', 'private': 'false', 'html_url': 'https://github.com/huidou74/huidou', 'description': '项目代码', 'fork': 'false', 'url': 'https://github.com/huidou74/huidou', 'forks_url': 'https://api.github.com/repos/huidou74/huidou/forks', 'keys_url': 'https://api.github.com/repos/huidou74/huidou/keys{/key_id}', 'collaborators_url': 'https://api.github.com/repos/huidou74/huidou/collaborators{/collaborator}', 'teams_url': 'https://api.github.com/repos/huidou74/huidou/teams', 'hooks_url': 'https://api.github.com/repos/huidou74/huidou/hooks', 'issue_events_url': 'https://api.github.com/repos/huidou74/huidou/issues/events{/number}', 'events_url': 'https://api.github.com/repos/huidou74/huidou/events', 'assignees_url': 'https://api.github.com/repos/huidou74/huidou/assignees{/user}', 'branches_url': 'https://api.github.com/repos/huidou74/huidou/branches{/branch}', 'tags_url': 'https://api.github.com/repos/huidou74/huidou/tags', 'blobs_url': 'https://api.github.com/repos/huidou74/huidou/git/blobs{/sha}', 'git_tags_url': 'https://api.github.com/repos/huidou74/huidou/git/tags{/sha}', 'git_refs_url': 'https://api.github.com/repos/huidou74/huidou/git/refs{/sha}', 'trees_url': 'https://api.github.com/repos/huidou74/huidou/git/trees{/sha}', 'statuses_url': 'https://api.github.com/repos/huidou74/huidou/statuses/{sha}', 'languages_url': 'https://api.github.com/repos/huidou74/huidou/languages', 'stargazers_url': 'https://api.github.com/repos/huidou74/huidou/stargazers', 'contributors_url': 'https://api.github.com/repos/huidou74/huidou/contributors', 'subscribers_url': 'https://api.github.com/repos/huidou74/huidou/subscribers', 'subscription_url': 'https://api.github.com/repos/huidou74/huidou/subscription', 'commits_url': 'https://api.github.com/repos/huidou74/huidou/commits{/sha}', 'git_commits_url': 'https://api.github.com/repos/huidou74/huidou/git/commits{/sha}', 'comments_url': 'https://api.github.com/repos/huidou74/huidou/comments{/number}', 'issue_comment_url': 'https://api.github.com/repos/huidou74/huidou/issues/comments{/number}', 'contents_url': 'https://api.github.com/repos/huidou74/huidou/contents/{+path}', 'compare_url': 'https://api.github.com/repos/huidou74/huidou/compare/{base}...{head}', 'merges_url': 'https://api.github.com/repos/huidou74/huidou/merges', 'archive_url': 'https://api.github.com/repos/huidou74/huidou/{archive_format}{/ref}', 'downloads_url': 'https://api.github.com/repos/huidou74/huidou/downloads', 'issues_url': 'https://api.github.com/repos/huidou74/huidou/issues{/number}', 'pulls_url': 'https://api.github.com/repos/huidou74/huidou/pulls{/number}', 'milestones_url': 'https://api.github.com/repos/huidou74/huidou/milestones{/number}', 'notifications_url': 'https://api.github.com/repos/huidou74/huidou/notifications{?since,all,participating}', 'labels_url': 'https://api.github.com/repos/huidou74/huidou/labels{/name}', 'releases_url': 'https://api.github.com/repos/huidou74/huidou/releases{/id}', 'deployments_url': 'https://api.github.com/repos/huidou74/huidou/deployments', 'created_at': 1520593227, 'updated_at': '2019-05-24T08:34:42Z', 'pushed_at': 1558687287, 'git_url': 'git://github.com/huidou74/huidou.git', 'ssh_url': 'git@github.com:huidou74/huidou.git', 'clone_url': 'https://github.com/huidou74/huidou.git', 'svn_url': 'https://github.com/huidou74/huidou', 'homepage': 'null', 'size': 6, 'stargazers_count': 1, 'watchers_count': 1, 'language': 'Python', 'has_issues': 'true', 'has_projects': 'true', 'has_downloads': 'true', 'has_wiki': 'true', 'has_pages': 'false', 'forks_count': 0, 'mirror_url': 'null', 'archived': 'false', 'disabled': 'false', 'open_issues_count': 0, 'license': 'null', 'forks': 0, 'open_issues': 0, 'watchers': 1, 'default_branch': 'master', 'stargazers': 1, 'master_branch': 'master'}
# aa = ['node_id', 'gravatar_id', 'url', 'followers_url', 'following_url', 'gists_url', 'starred_url', 'subscriptions_url', 'organizations_url', 'events_url', 'received_events_url', 'type', 'site_admin', 'node_id', 'url', 'forks_url', 'keys_url', 'collaborators_url', 'teams_url', 'hooks_url', 'issue_events_url', 'events_url', 'assignees_url', 'branches_url', 'blobs_url', 'git_tags_url', 'git_refs_url', 'trees_url', 'statuses_url', 'languages_url', 'stargazers_url', 'contributors_url', 'subscribers_url', 'subscription_url', 'commits_url', 'git_commits_url', 'comments_url', 'issue_comment_url', 'contents_url', 'compare_url', 'merges_url', 'archive_url', 'downloads_url', 'issues_url', 'pulls_url', 'milestones_url', 'notifications_url', 'labels_url', 'releases_url', 'deployments_url', 'git_url', 'ssh_url', 'svn_url', 'homepage', 'stargazers_count', 'watchers_count', 'has_issues', 'has_projects', 'has_downloads', 'has_wiki', 'has_pages', 'forks_count', 'mirror_url', 'open_issues_count', 'license', 'open_issues', 'watchers', 'stargazers']
# for i in aa:
#     del a[i]


# a = ['node_id', 'gravatar_id', 'url', 'followers_url', 'following_url', 'gists_url', 'starred_url', 'subscriptions_url', 'organizations_url', 'events_url', 'received_events_url', 'type', 'site_admin', 'node_id', 'url', 'forks_url', 'keys_url', 'collaborators_url', 'teams_url', 'hooks_url', 'issue_events_url', 'events_url', 'assignees_url', 'branches_url', 'blobs_url', 'git_tags_url', 'git_refs_url', 'trees_url', 'statuses_url', 'languages_url', 'stargazers_url', 'contributors_url', 'subscribers_url', 'subscription_url', 'commits_url', 'git_commits_url', 'comments_url', 'issue_comment_url', 'contents_url', 'compare_url', 'merges_url', 'archive_url', 'downloads_url', 'issues_url', 'pulls_url', 'milestones_url', 'notifications_url', 'labels_url', 'releases_url', 'deployments_url', 'git_url', 'ssh_url', 'svn_url', 'homepage', 'stargazers_count', 'watchers_count', 'has_issues', 'has_projects', 'has_downloads', 'has_wiki', 'has_pages', 'forks_count', 'mirror_url', 'open_issues_count', 'license', 'open_issues', 'watchers', 'stargazers']
# if 'gravatar_id' in a:
#     print ('gravatar_id')
# else:
#     print ('none')






# a={'id': 124529225, 'name': 'huidou', 'full_name': 'huidou74/huidou', 'private': 'false', 'owner': {'name': 'huidou74', 'email': '37212138+huidou74@users.noreply.github.com', 'login': 'huidou74', 'avatar_url': 'https://avatars3.githubusercontent.com/u/37212138?v=4', 'html_url': 'https://github.com/huidou74', 'repos_url': 'https://api.github.com/users/huidou74/repos', 'login_id': 37212138}, 'html_url': 'https://github.com/huidou74/huidou', 'description': '项目代码', 'fork': 'false', 'tags_url': 'https://api.github.com/repos/huidou74/huidou/tags', 'created_at': 1520593227, 'updated_at': '2019-05-24T08:34:42Z', 'pushed_at': 1558687287, 'clone_url': 'https://github.com/huidou74/huidou.git', 'size': 6, 'language': 'Python', 'archived': 'false', 'disabled': 'false', 'forks': 0, 'default_branch': 'master', 'master_branch': 'master'}
# print (a)
# owner = a.pop('owner')
#
# for  k , y in a.items():
#     print (k)
#     print (y)
#     print ('---'*20)
#
#
# print (owner)


# bb={'aa':'aa','vv':'vv'}
# a={'a':'1','b':'2','c':'3','d':'4','e':bb}
#
# # x = a.items()
# # print (a.values())
#
# # print (a.values())
# # print (len(a.values()))
# # print (y,type(y))
# class ABC(object):
#     def __init__(self,a):
#         self.a=a
#         self.v=[]
#         self.abc = {}
#         self.zxc = None
#
#     def asd(self):
#         self.zxc = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
#         print (self.zxc)
#
#     def dict_data(self):
#         xxx={'a':'z','xx':'123'}
#         self.abc.update(xxx)
#         self.asd()
#
#         return self.abc
#     def data(self):
#         self.v.append(self.a)
#         self.v.append('123')
#         # print (self.v)
#         # print (self.a)
#         print (self.abc)
#         self.dict_data()
#         print (self.abc)
#         data = 'asd'
#         JG = getattr(AAA, 'qwe')
#         JG(self,'asd')
#
# class AAA(ABC):
#
#     def qwe(self,data):
#         print (data)
#         print (self.abc)
#
# az=ABC('data')
# az.data()