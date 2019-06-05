#!/usr/bin/python
#-*- coding:utf8 -*-
#BY:  H.c
# from hc import models
#test  new data to dict
data = '{"ref":"refs/heads/master","before":"49bb0b1930f23fda499f86e0c60f472881e39075","after":"8e7bd0ae38672c1ae1a5d8dff71adc9998f740eb","created":false,"deleted":false,"forced":false,"base_ref":null,"compare":"https://github.com/huidou74/huidou/compare/49bb0b1930f2...8e7bd0ae3867","commits":[{"id":"8e7bd0ae38672c1ae1a5d8dff71adc9998f740eb","tree_id":"b9ad117b38174da516a63e0eaaa35c2f6f756b88","distinct":true,"message":"v0.5.3","timestamp":"2019-05-24T16:40:59+08:00","url":"https://github.com/huidou74/huidou/commit/8e7bd0ae38672c1ae1a5d8dff71adc9998f740eb","author":{"name":"H.c","email":"liangyonghui123@qq.com","username":"huidou74"},"committer":{"name":"H.c","email":"liangyonghui123@qq.com","username":"huidou74"},"added":[],"removed":[],"modified":["hello.py"]}],"head_commit":{"id":"8e7bd0ae38672c1ae1a5d8dff71adc9998f740eb","tree_id":"b9ad117b38174da516a63e0eaaa35c2f6f756b88","distinct":true,"message":"v0.5.3","timestamp":"2019-05-24T16:40:59+08:00","url":"https://github.com/huidou74/huidou/commit/8e7bd0ae38672c1ae1a5d8dff71adc9998f740eb","author":{"name":"H.c","email":"liangyonghui123@qq.com","username":"huidou74"},"committer":{"name":"H.c","email":"liangyonghui123@qq.com","username":"huidou74"},"added":[],"removed":[],"modified":["hello.py"]},"repository":{"id":124529225,"node_id":"MDEwOlJlcG9zaXRvcnkxMjQ1MjkyMjU=","name":"huidou","full_name":"huidou74/huidou","private":false,"owner":{"name":"huidou74","email":"37212138+huidou74@users.noreply.github.com","login":"huidou74","id":37212138,"node_id":"MDQ6VXNlcjM3MjEyMTM4","avatar_url":"https://avatars3.githubusercontent.com/u/37212138?v=4","gravatar_id":"","url":"https://api.github.com/users/huidou74","html_url":"https://github.com/huidou74","followers_url":"https://api.github.com/users/huidou74/followers","following_url":"https://api.github.com/users/huidou74/following{/other_user}","gists_url":"https://api.github.com/users/huidou74/gists{/gist_id}","starred_url":"https://api.github.com/users/huidou74/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/huidou74/subscriptions","organizations_url":"https://api.github.com/users/huidou74/orgs","repos_url":"https://api.github.com/users/huidou74/repos","events_url":"https://api.github.com/users/huidou74/events{/privacy}","received_events_url":"https://api.github.com/users/huidou74/received_events","type":"User","site_admin":false},"html_url":"https://github.com/huidou74/huidou","description":"项目代码","fork":false,"url":"https://github.com/huidou74/huidou","forks_url":"https://api.github.com/repos/huidou74/huidou/forks","keys_url":"https://api.github.com/repos/huidou74/huidou/keys{/key_id}","collaborators_url":"https://api.github.com/repos/huidou74/huidou/collaborators{/collaborator}","teams_url":"https://api.github.com/repos/huidou74/huidou/teams","hooks_url":"https://api.github.com/repos/huidou74/huidou/hooks","issue_events_url":"https://api.github.com/repos/huidou74/huidou/issues/events{/number}","events_url":"https://api.github.com/repos/huidou74/huidou/events","assignees_url":"https://api.github.com/repos/huidou74/huidou/assignees{/user}","branches_url":"https://api.github.com/repos/huidou74/huidou/branches{/branch}","tags_url":"https://api.github.com/repos/huidou74/huidou/tags","blobs_url":"https://api.github.com/repos/huidou74/huidou/git/blobs{/sha}","git_tags_url":"https://api.github.com/repos/huidou74/huidou/git/tags{/sha}","git_refs_url":"https://api.github.com/repos/huidou74/huidou/git/refs{/sha}","trees_url":"https://api.github.com/repos/huidou74/huidou/git/trees{/sha}","statuses_url":"https://api.github.com/repos/huidou74/huidou/statuses/{sha}","languages_url":"https://api.github.com/repos/huidou74/huidou/languages","stargazers_url":"https://api.github.com/repos/huidou74/huidou/stargazers","contributors_url":"https://api.github.com/repos/huidou74/huidou/contributors","subscribers_url":"https://api.github.com/repos/huidou74/huidou/subscribers","subscription_url":"https://api.github.com/repos/huidou74/huidou/subscription","commits_url":"https://api.github.com/repos/huidou74/huidou/commits{/sha}","git_commits_url":"https://api.github.com/repos/huidou74/huidou/git/commits{/sha}","comments_url":"https://api.github.com/repos/huidou74/huidou/comments{/number}","issue_comment_url":"https://api.github.com/repos/huidou74/huidou/issues/comments{/number}","contents_url":"https://api.github.com/repos/huidou74/huidou/contents/{+path}","compare_url":"https://api.github.com/repos/huidou74/huidou/compare/{base}...{head}","merges_url":"https://api.github.com/repos/huidou74/huidou/merges","archive_url":"https://api.github.com/repos/huidou74/huidou/{archive_format}{/ref}","downloads_url":"https://api.github.com/repos/huidou74/huidou/downloads","issues_url":"https://api.github.com/repos/huidou74/huidou/issues{/number}","pulls_url":"https://api.github.com/repos/huidou74/huidou/pulls{/number}","milestones_url":"https://api.github.com/repos/huidou74/huidou/milestones{/number}","notifications_url":"https://api.github.com/repos/huidou74/huidou/notifications{?since,all,participating}","labels_url":"https://api.github.com/repos/huidou74/huidou/labels{/name}","releases_url":"https://api.github.com/repos/huidou74/huidou/releases{/id}","deployments_url":"https://api.github.com/repos/huidou74/huidou/deployments","created_at":1520593227,"updated_at":"2019-05-24T08:34:42Z","pushed_at":1558687287,"git_url":"git://github.com/huidou74/huidou.git","ssh_url":"git@github.com:huidou74/huidou.git","clone_url":"https://github.com/huidou74/huidou.git","svn_url":"https://github.com/huidou74/huidou","homepage":null,"size":6,"stargazers_count":1,"watchers_count":1,"language":"Python","has_issues":true,"has_projects":true,"has_downloads":true,"has_wiki":true,"has_pages":false,"forks_count":0,"mirror_url":null,"archived":false,"disabled":false,"open_issues_count":0,"license":null,"forks":0,"open_issues":0,"watchers":1,"default_branch":"master","stargazers":1,"master_branch":"master"},"pusher":{"name":"huidou74","email":"37212138+huidou74@users.noreply.github.com"},"sender":{"login":"huidou74","id":37212138,"node_id":"MDQ6VXNlcjM3MjEyMTM4","avatar_url":"https://avatars3.githubusercontent.com/u/37212138?v=4","gravatar_id":"","url":"https://api.github.com/users/huidou74","html_url":"https://github.com/huidou74","followers_url":"https://api.github.com/users/huidou74/followers","following_url":"https://api.github.com/users/huidou74/following{/other_user}","gists_url":"https://api.github.com/users/huidou74/gists{/gist_id}","starred_url":"https://api.github.com/users/huidou74/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/huidou74/subscriptions","organizations_url":"https://api.github.com/users/huidou74/orgs","repos_url":"https://api.github.com/users/huidou74/repos","events_url":"https://api.github.com/users/huidou74/events{/privacy}","received_events_url":"https://api.github.com/users/huidou74/received_events","type":"User","site_admin":false}}'
new_data = eval(str(data).replace('true','\'true\'').replace('false','\'false\'').replace('null','\'null\''))  #  转换格式  str -> dict
print (type(new_data))

# references 参考 路径
# ref = new_data.get('ref')
# # before ID 修改前的代码。仅包含被修改和被删除的文件。
# before = new_data.get('before')
# # after ID 修改后的代码。仅包含被修改和新追加的文件。
# after = new_data.get('after')
# # 是否创建
# created = new_data.get('created')
# # 是否删除
# deleted = new_data.get('deleted')
# # 是否强制推代码
# forced = new_data.get('forced')
# # 对比 修改前的代码 WEB网页显示
# compare = new_data.get('compare')
# print('ref     ', ref)
# print('before     ', before)
# print('created     ', created)
# print('deleted     ', deleted)
# print('forced     ', forced)
# print('compare     ', compare)
auth_list = ['ref', 'before', 'after', 'created', 'deleted', 'forced', 'compare']
keys_list=[]

tow_dict={}
three_list=[]
three_dict={}

class Abc_data(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.user_list = [ i for i in self.value.values()]

    def diff_data(self):
        for i in self.value.values():
            if isinstance(i, dict):
                pass
            else:
                tow_dict.update({kk: vv})

    def values_list(self):
        pass

    def values_dict(self):
        pass


def data_list(v,k):   # v -> dict
    for kk,vv in v.items():
        if isinstance(vv, dict):
            print (k)
            print('---',kk)
            # for kkk,vvv in vv.items():
            #     print ('------',{kkk:vvv})
            #     three_dict.update({kkk:vvv})
            three_list.append({kk:vv})

            print ('***********************')
        else:
            print (k)
            print ('---',{kk:vv})
            tow_dict.update({kk: vv})
    if tow_dict and three_list:
        del tow_dict['tree_id']
        del tow_dict['distinct']
        commits_id = tow_dict.pop('id')
        tow_dict.update({'commits_id': commits_id})
        three_list.append(tow_dict)
        print (three_list)
'''
data_list()  上面解析的结果
commits
--- {'id': '8e7bd0ae38672c1ae1a5d8dff71adc9998f740eb'}
commits
--- {'tree_id': 'b9ad117b38174da516a63e0eaaa35c2f6f756b88'}
commits
--- {'distinct': 'true'}
commits
--- {'message': 'v0.5.3'}
commits
--- {'timestamp': '2019-05-24T16:40:59+08:00'}
commits
--- {'url': 'https://github.com/huidou74/huidou/commit/8e7bd0ae38672c1ae1a5d8dff71adc9998f740eb'}
commits
--- author
------ {'name': 'H.c'}
------ {'email': 'liangyonghui123@qq.com'}
------ {'username': 'huidou74'}
***********************
commits
--- committer
------ {'name': 'H.c'}
------ {'email': 'liangyonghui123@qq.com'}
------ {'username': 'huidou74'}
***********************
commits
--- {'added': []}
commits
--- {'removed': []}
commits
--- {'modified': ['hello.py']}
'''


def data_dict(k,v):
    pass

# head_commit_list=['tree_id','distinct']
repository_list=['id','name','full_name','private','owner','html_url','description','fork','tags_url','created_at','updated_at','pushed_at','clone_url','size','language','archived','disabled','forks','default_branch','master_branch']
rep_dict_list=['name','email','login','id','avatar_url','html_url','repos_url']
sender_list=['login','id']
'''
del tow_dict['tree_id']
del tow_dict['distinct']
tow_dict.update({'commits_id': tow_dict.pop('id')})
'''
class Y_Dict(object):
    abc = []

    def head_commit(self,data):
        del data['tree_id']
        del data['distinct']
        data.update({'commits_id': data.pop('id')})
        return data

    def repository(self,data):
        for y_v in data.values():
            if isinstance(y_v, dict):
                for k in y_v.keys():
                    if k not in rep_dict_list:  # .clear()
                        Y_Dict.abc.append(k)
                for a in Y_Dict.abc:
                    del y_v[a]
                y_v.update({'login_id': y_v.pop('id')}) # 这字典owner的值
                Y_Dict.abc.clear()  # 清除临时列表
        for i in data.keys():
            if i not in repository_list:
                Y_Dict.abc.append(i)
        for a in Y_Dict.abc:
            del data[a]
        Y_Dict.abc.clear()
        return data

    def sender(self,data):
        for i in data.keys():
            if i not in sender_list:
                Y_Dict.abc.append(i)
        for a in Y_Dict.abc:
            del data[a]
        data.update({'login_id': data.pop('id')})
        Y_Dict.abc.clear()
        return data

    def pusher(self,data):
        return data
atuo_commits = ['id','message','timestamp','url','committer','added','removed','modified']
blacklist_commits=[]
for x,y in new_data.items():
    if isinstance(y, list):   # -> commits
        for list_dict in y:
            for i in list_dict.keys():
                if i not in atuo_commits:
                    blacklist_commits.append(i)
            for x in blacklist_commits:
                del list_dict[x]
            print (list_dict)
            # data_list(list_dict,x)
        # pass

    elif isinstance(y, dict):
        # print (x)
        # JG = getattr(Y_Dict,x)
        # print (JG(x,y))
        pass
        # if x == 'head_commit':
        #     JG = getattr(Y_Dict,'head_commit')
        #     print (JG('head_commit',y))
        # elif x == 'repository':
        #     JG = getattr(Y_Dict,'repository')
        #     print (JG('repository',y))
        # elif x == 'sender':
        #     JG = getattr(Y_Dict,'sender')
        #     print (JG('sender',y))
        # else:
        #     print (y)
        print( '--------------============++++++++++++')
        # data_list(x,y)

    # string
    elif x in auth_list:
        keys_list.append(x)
# print (keys_list)
'''
head_commit
{'message': 'v0.5.3', 'timestamp': '2019-05-24T16:40:59+08:00', 'url': 'https://github.com/huidou74/huidou/commit/8e7bd0ae38672c1ae1a5d8dff71adc9998f740eb', 'author': {'name': 'H.c', 'email': 'liangyonghui123@qq.com', 'username': 'huidou74'}, 'committer': {'name': 'H.c', 'email': 'liangyonghui123@qq.com', 'username': 'huidou74'}, 'added': [], 'removed': [], 'modified': ['hello.py'], 'commits_id': '8e7bd0ae38672c1ae1a5d8dff71adc9998f740eb'}
--------------
repository
{'id': 124529225, 'name': 'huidou', 'full_name': 'huidou74/huidou', 'private': 'false', 'owner': {'name': 'huidou74', 'email': '37212138+huidou74@users.noreply.github.com', 'login': 'huidou74', 'avatar_url': 'https://avatars3.githubusercontent.com/u/37212138?v=4', 'html_url': 'https://github.com/huidou74', 'repos_url': 'https://api.github.com/users/huidou74/repos', 'login_id': 37212138}, 'html_url': 'https://github.com/huidou74/huidou', 'description': '项目代码', 'fork': 'false', 'tags_url': 'https://api.github.com/repos/huidou74/huidou/tags', 'created_at': 1520593227, 'updated_at': '2019-05-24T08:34:42Z', 'pushed_at': 1558687287, 'clone_url': 'https://github.com/huidou74/huidou.git', 'size': 6, 'language': 'Python', 'archived': 'false', 'disabled': 'false', 'forks': 0, 'default_branch': 'master', 'master_branch': 'master'}
--------------
pusher
{'name': 'huidou74', 'email': '37212138+huidou74@users.noreply.github.com'}
--------------
sender
{'login': 'huidou74', 'login_id': 37212138}
--------------
'''

# string   字符串类型 解析出字典存入数据库
for i in keys_list:
    if i == 'ref':
        ref_class = new_data.get(i)
        if 'heads' in ref_class:
            # pass
            print ({'ref_class_branch':ref_class.split('/')[-1]})
        elif 'tags' in ref_class:
            # pass
            print({'ref_class_tag': ref_class.split('/')[-1]})
    print ({i: new_data.get(i)})













# data1='{"ref":"refs/heads/master","before":"543effa7629de569f592b397669fcdafc3d96dd9","after":"2c8271a923fb7bcbcb299831599ed5f12e2d8a2b","created":false,"deleted":false,"forced":false,"base_ref":null,"compare":"https://github.com/huidou74/huidou/compare/543effa7629d...2c8271a923fb","commits":[{"id":"2c8271a923fb7bcbcb299831599ed5f12e2d8a2b","tree_id":"4f03da060cd4436eb83ff9e4f7f4341f442548fc","distinct":true,"message":"V 0.5","timestamp":"2019-05-23T17:52:30+08:00","url":"https://github.com/huidou74/huidou/commit/2c8271a923fb7bcbcb299831599ed5f12e2d8a2b","author":{"name":"H.c","email":"liangyonghui123@qq.com","username":"huidou74"},"committer":{"name":"H.c","email":"liangyonghui123@qq.com","username":"huidou74"},"added":[],"removed":[],"modified":["hello.py"]}],"head_commit":{"id":"2c8271a923fb7bcbcb299831599ed5f12e2d8a2b","tree_id":"4f03da060cd4436eb83ff9e4f7f4341f442548fc","distinct":true,"message":"V 0.5","timestamp":"2019-05-23T17:52:30+08:00","url":"https://github.com/huidou74/huidou/commit/2c8271a923fb7bcbcb299831599ed5f12e2d8a2b","author":{"name":"H.c","email":"liangyonghui123@qq.com","username":"huidou74"},"committer":{"name":"H.c","email":"liangyonghui123@qq.com","username":"huidou74"},"added":[],"removed":[],"modified":["hello.py"]},"repository":{"id":124529225,"node_id":"MDEwOlJlcG9zaXRvcnkxMjQ1MjkyMjU=","name":"huidou","full_name":"huidou74/huidou","private":false,"owner":{"name":"huidou74","email":"37212138+huidou74@users.noreply.github.com","login":"huidou74","id":37212138,"node_id":"MDQ6VXNlcjM3MjEyMTM4","avatar_url":"https://avatars3.githubusercontent.com/u/37212138?v=4","gravatar_id":"","url":"https://api.github.com/users/huidou74","html_url":"https://github.com/huidou74","followers_url":"https://api.github.com/users/huidou74/followers","following_url":"https://api.github.com/users/huidou74/following{/other_user}","gists_url":"https://api.github.com/users/huidou74/gists{/gist_id}","starred_url":"https://api.github.com/users/huidou74/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/huidou74/subscriptions","organizations_url":"https://api.github.com/users/huidou74/orgs","repos_url":"https://api.github.com/users/huidou74/repos","events_url":"https://api.github.com/users/huidou74/events{/privacy}","received_events_url":"https://api.github.com/users/huidou74/received_events","type":"User","site_admin":false},"html_url":"https://github.com/huidou74/huidou","description":"项目代码","fork":false,"url":"https://github.com/huidou74/huidou","forks_url":"https://api.github.com/repos/huidou74/huidou/forks","keys_url":"https://api.github.com/repos/huidou74/huidou/keys{/key_id}","collaborators_url":"https://api.github.com/repos/huidou74/huidou/collaborators{/collaborator}","teams_url":"https://api.github.com/repos/huidou74/huidou/teams","hooks_url":"https://api.github.com/repos/huidou74/huidou/hooks","issue_events_url":"https://api.github.com/repos/huidou74/huidou/issues/events{/number}","events_url":"https://api.github.com/repos/huidou74/huidou/events","assignees_url":"https://api.github.com/repos/huidou74/huidou/assignees{/user}","branches_url":"https://api.github.com/repos/huidou74/huidou/branches{/branch}","tags_url":"https://api.github.com/repos/huidou74/huidou/tags","blobs_url":"https://api.github.com/repos/huidou74/huidou/git/blobs{/sha}","git_tags_url":"https://api.github.com/repos/huidou74/huidou/git/tags{/sha}","git_refs_url":"https://api.github.com/repos/huidou74/huidou/git/refs{/sha}","trees_url":"https://api.github.com/repos/huidou74/huidou/git/trees{/sha}","statuses_url":"https://api.github.com/repos/huidou74/huidou/statuses/{sha}","languages_url":"https://api.github.com/repos/huidou74/huidou/languages","stargazers_url":"https://api.github.com/repos/huidou74/huidou/stargazers","contributors_url":"https://api.github.com/repos/huidou74/huidou/contributors","subscribers_url":"https://api.github.com/repos/huidou74/huidou/subscribers","subscription_url":"https://api.github.com/repos/huidou74/huidou/subscription","commits_url":"https://api.github.com/repos/huidou74/huidou/commits{/sha}","git_commits_url":"https://api.github.com/repos/huidou74/huidou/git/commits{/sha}","comments_url":"https://api.github.com/repos/huidou74/huidou/comments{/number}","issue_comment_url":"https://api.github.com/repos/huidou74/huidou/issues/comments{/number}","contents_url":"https://api.github.com/repos/huidou74/huidou/contents/{+path}","compare_url":"https://api.github.com/repos/huidou74/huidou/compare/{base}...{head}","merges_url":"https://api.github.com/repos/huidou74/huidou/merges","archive_url":"https://api.github.com/repos/huidou74/huidou/{archive_format}{/ref}","downloads_url":"https://api.github.com/repos/huidou74/huidou/downloads","issues_url":"https://api.github.com/repos/huidou74/huidou/issues{/number}","pulls_url":"https://api.github.com/repos/huidou74/huidou/pulls{/number}","milestones_url":"https://api.github.com/repos/huidou74/huidou/milestones{/number}","notifications_url":"https://api.github.com/repos/huidou74/huidou/notifications{?since,all,participating}","labels_url":"https://api.github.com/repos/huidou74/huidou/labels{/name}","releases_url":"https://api.github.com/repos/huidou74/huidou/releases{/id}","deployments_url":"https://api.github.com/repos/huidou74/huidou/deployments","created_at":1520593227,"updated_at":"2019-05-23T09:39:34Z","pushed_at":1558605234,"git_url":"git://github.com/huidou74/huidou.git","ssh_url":"git@github.com:huidou74/huidou.git","clone_url":"https://github.com/huidou74/huidou.git","svn_url":"https://github.com/huidou74/huidou","homepage":null,"size":5,"stargazers_count":1,"watchers_count":1,"language":"Python","has_issues":true,"has_projects":true,"has_downloads":true,"has_wiki":true,"has_pages":false,"forks_count":0,"mirror_url":null,"archived":false,"disabled":false,"open_issues_count":0,"license":null,"forks":0,"open_issues":0,"watchers":1,"default_branch":"master","stargazers":1,"master_branch":"master"},"pusher":{"name":"huidou74","email":"37212138+huidou74@users.noreply.github.com"},"sender":{"login":"huidou74","id":37212138,"node_id":"MDQ6VXNlcjM3MjEyMTM4","avatar_url":"https://avatars3.githubusercontent.com/u/37212138?v=4","gravatar_id":"","url":"https://api.github.com/users/huidou74","html_url":"https://github.com/huidou74","followers_url":"https://api.github.com/users/huidou74/followers","following_url":"https://api.github.com/users/huidou74/following{/other_user}","gists_url":"https://api.github.com/users/huidou74/gists{/gist_id}","starred_url":"https://api.github.com/users/huidou74/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/huidou74/subscriptions","organizations_url":"https://api.github.com/users/huidou74/orgs","repos_url":"https://api.github.com/users/huidou74/repos","events_url":"https://api.github.com/users/huidou74/events{/privacy}","received_events_url":"https://api.github.com/users/huidou74/received_events","type":"User","site_admin":false}}'
# data2='{"ref":"refs/tags/v0.5.1","before":"0000000000000000000000000000000000000000","after":"2c8271a923fb7bcbcb299831599ed5f12e2d8a2b","created":true,"deleted":false,"forced":false,"base_ref":"refs/heads/master","compare":"https://github.com/huidou74/huidou/compare/v0.5.1","commits":[],"head_commit":{"id":"2c8271a923fb7bcbcb299831599ed5f12e2d8a2b","tree_id":"4f03da060cd4436eb83ff9e4f7f4341f442548fc","distinct":true,"message":"V 0.5","timestamp":"2019-05-23T17:52:30+08:00","url":"https://github.com/huidou74/huidou/commit/2c8271a923fb7bcbcb299831599ed5f12e2d8a2b","author":{"name":"H.c","email":"liangyonghui123@qq.com","username":"huidou74"},"committer":{"name":"H.c","email":"liangyonghui123@qq.com","username":"huidou74"},"added":[],"removed":[],"modified":["hello.py"]},"repository":{"id":124529225,"node_id":"MDEwOlJlcG9zaXRvcnkxMjQ1MjkyMjU=","name":"huidou","full_name":"huidou74/huidou","private":false,"owner":{"name":"huidou74","email":"37212138+huidou74@users.noreply.github.com","login":"huidou74","id":37212138,"node_id":"MDQ6VXNlcjM3MjEyMTM4","avatar_url":"https://avatars3.githubusercontent.com/u/37212138?v=4","gravatar_id":"","url":"https://api.github.com/users/huidou74","html_url":"https://github.com/huidou74","followers_url":"https://api.github.com/users/huidou74/followers","following_url":"https://api.github.com/users/huidou74/following{/other_user}","gists_url":"https://api.github.com/users/huidou74/gists{/gist_id}","starred_url":"https://api.github.com/users/huidou74/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/huidou74/subscriptions","organizations_url":"https://api.github.com/users/huidou74/orgs","repos_url":"https://api.github.com/users/huidou74/repos","events_url":"https://api.github.com/users/huidou74/events{/privacy}","received_events_url":"https://api.github.com/users/huidou74/received_events","type":"User","site_admin":false},"html_url":"https://github.com/huidou74/huidou","description":"项目代码","fork":false,"url":"https://github.com/huidou74/huidou","forks_url":"https://api.github.com/repos/huidou74/huidou/forks","keys_url":"https://api.github.com/repos/huidou74/huidou/keys{/key_id}","collaborators_url":"https://api.github.com/repos/huidou74/huidou/collaborators{/collaborator}","teams_url":"https://api.github.com/repos/huidou74/huidou/teams","hooks_url":"https://api.github.com/repos/huidou74/huidou/hooks","issue_events_url":"https://api.github.com/repos/huidou74/huidou/issues/events{/number}","events_url":"https://api.github.com/repos/huidou74/huidou/events","assignees_url":"https://api.github.com/repos/huidou74/huidou/assignees{/user}","branches_url":"https://api.github.com/repos/huidou74/huidou/branches{/branch}","tags_url":"https://api.github.com/repos/huidou74/huidou/tags","blobs_url":"https://api.github.com/repos/huidou74/huidou/git/blobs{/sha}","git_tags_url":"https://api.github.com/repos/huidou74/huidou/git/tags{/sha}","git_refs_url":"https://api.github.com/repos/huidou74/huidou/git/refs{/sha}","trees_url":"https://api.github.com/repos/huidou74/huidou/git/trees{/sha}","statuses_url":"https://api.github.com/repos/huidou74/huidou/statuses/{sha}","languages_url":"https://api.github.com/repos/huidou74/huidou/languages","stargazers_url":"https://api.github.com/repos/huidou74/huidou/stargazers","contributors_url":"https://api.github.com/repos/huidou74/huidou/contributors","subscribers_url":"https://api.github.com/repos/huidou74/huidou/subscribers","subscription_url":"https://api.github.com/repos/huidou74/huidou/subscription","commits_url":"https://api.github.com/repos/huidou74/huidou/commits{/sha}","git_commits_url":"https://api.github.com/repos/huidou74/huidou/git/commits{/sha}","comments_url":"https://api.github.com/repos/huidou74/huidou/comments{/number}","issue_comment_url":"https://api.github.com/repos/huidou74/huidou/issues/comments{/number}","contents_url":"https://api.github.com/repos/huidou74/huidou/contents/{+path}","compare_url":"https://api.github.com/repos/huidou74/huidou/compare/{base}...{head}","merges_url":"https://api.github.com/repos/huidou74/huidou/merges","archive_url":"https://api.github.com/repos/huidou74/huidou/{archive_format}{/ref}","downloads_url":"https://api.github.com/repos/huidou74/huidou/downloads","issues_url":"https://api.github.com/repos/huidou74/huidou/issues{/number}","pulls_url":"https://api.github.com/repos/huidou74/huidou/pulls{/number}","milestones_url":"https://api.github.com/repos/huidou74/huidou/milestones{/number}","notifications_url":"https://api.github.com/repos/huidou74/huidou/notifications{?since,all,participating}","labels_url":"https://api.github.com/repos/huidou74/huidou/labels{/name}","releases_url":"https://api.github.com/repos/huidou74/huidou/releases{/id}","deployments_url":"https://api.github.com/repos/huidou74/huidou/deployments","created_at":1520593227,"updated_at":"2019-05-23T09:39:34Z","pushed_at":1558605234,"git_url":"git://github.com/huidou74/huidou.git","ssh_url":"git@github.com:huidou74/huidou.git","clone_url":"https://github.com/huidou74/huidou.git","svn_url":"https://github.com/huidou74/huidou","homepage":null,"size":5,"stargazers_count":1,"watchers_count":1,"language":"Python","has_issues":true,"has_projects":true,"has_downloads":true,"has_wiki":true,"has_pages":false,"forks_count":0,"mirror_url":null,"archived":false,"disabled":false,"open_issues_count":0,"license":null,"forks":0,"open_issues":0,"watchers":1,"default_branch":"master","stargazers":1,"master_branch":"master"},"pusher":{"name":"huidou74","email":"37212138+huidou74@users.noreply.github.com"},"sender":{"login":"huidou74","id":37212138,"node_id":"MDQ6VXNlcjM3MjEyMTM4","avatar_url":"https://avatars3.githubusercontent.com/u/37212138?v=4","gravatar_id":"","url":"https://api.github.com/users/huidou74","html_url":"https://github.com/huidou74","followers_url":"https://api.github.com/users/huidou74/followers","following_url":"https://api.github.com/users/huidou74/following{/other_user}","gists_url":"https://api.github.com/users/huidou74/gists{/gist_id}","starred_url":"https://api.github.com/users/huidou74/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/huidou74/subscriptions","organizations_url":"https://api.github.com/users/huidou74/orgs","repos_url":"https://api.github.com/users/huidou74/repos","events_url":"https://api.github.com/users/huidou74/events{/privacy}","received_events_url":"https://api.github.com/users/huidou74/received_events","type":"User","site_admin":false}}'

# for i in [data1,data2]:
#     new_data = eval(i.replace('true','\'true\'').replace('false','\'false\'').replace('null','\'null\''))  #  转换格式  str -> dict
#     # yield new_data   # 要用函数
# print (new_data,type(new_data))  # dict
# for i in data.keys():
#     # try:
#     #     eval(i)
#     # except Exception as e:
#     #     pass
#     print(i, type(data.get(i)))
#     if isinstance(data.get(i), dict):
#         print ('********dict********')
#         for x,y in data.get(i).items():
#             print ({x:y})
#             print ('*********')
#     elif isinstance(data.get(i), list):
#         print('********list********')
#         for x in data.get(i):
#             if isinstance(x, dict):
#                 for xx,yy in x.items():
#                     print ({xx:yy})
#                     print ('################')
#             else:
#                 print (x)
#     else:
#         print (data.get(i))
#     print ('-'*10)
