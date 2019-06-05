#!/usr/bin/python
#-*- coding:utf8 -*-
#BY:  H.c
repository_list=['id','name','full_name','private','owner','html_url','description','fork','tags_url','created_at','updated_at','pushed_at','clone_url','size','language','archived','disabled','forks','default_branch','master_branch']
rep_dict_list=['name','email','login','id','avatar_url','html_url','repos_url']
sender_list=['login','id']

atuo_commits = ['id','message','timestamp','url','committer','added','removed','modified']

'auth_list,atuo_commits,sender_list,rep_dict_list,repository_list'
class Y_Dict(object):
    abc = []

    def head_commit(self,data):
        del data['tree_id']
        del data['distinct']
        data.update({'commits_id': data.pop('id')})
        return data

    def rep_owner(self,data):
        abc=[]
        for k in data.keys():
            if k not in rep_dict_list:  # .clear()
                abc.append(k)
        for a in abc:
            del data[a]
        data.update({'login_id': data.pop('id')})  # 这字典owner的值
        return data


    def repository(self,data):
        clear_list= []
        owner = self.rep_owner(data.pop('owner'))   # owner -> dict

        for i in data.keys():   # 清除掉不要的信息
            if i not in repository_list:
                clear_list.append(i)
        for a in clear_list:
            del data[a]

        # return data

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

def test_q(request):
    # 白名单 即 想要存入的数据字典
    auth_list = ['ref', 'before', 'after', 'created', 'deleted', 'forced', 'compare']
    keys_list = []

    head_commit_del_list = ['tree_id','distinct']
    if request.method == 'GET':
        data = '{"ref":"refs/heads/master","before":"49bb0b1930f23fda499f86e0c60f472881e39075","after":"8e7bd0ae38672c1ae1a5d8dff71adc9998f740eb","created":false,"deleted":false,"forced":false,"base_ref":null,"compare":"https://github.com/huidou74/huidou/compare/49bb0b1930f2...8e7bd0ae3867","commits":[{"id":"8e7bd0ae38672c1ae1a5d8dff71adc9998f740eb","tree_id":"b9ad117b38174da516a63e0eaaa35c2f6f756b88","distinct":true,"message":"v0.5.3","timestamp":"2019-05-24T16:40:59+08:00","url":"https://github.com/huidou74/huidou/commit/8e7bd0ae38672c1ae1a5d8dff71adc9998f740eb","author":{"name":"H.c","email":"liangyonghui123@qq.com","username":"huidou74"},"committer":{"name":"H.c","email":"liangyonghui123@qq.com","username":"huidou74"},"added":[],"removed":[],"modified":["hello.py"]}],"head_commit":{"id":"8e7bd0ae38672c1ae1a5d8dff71adc9998f740eb","tree_id":"b9ad117b38174da516a63e0eaaa35c2f6f756b88","distinct":true,"message":"v0.5.3","timestamp":"2019-05-24T16:40:59+08:00","url":"https://github.com/huidou74/huidou/commit/8e7bd0ae38672c1ae1a5d8dff71adc9998f740eb","author":{"name":"H.c","email":"liangyonghui123@qq.com","username":"huidou74"},"committer":{"name":"H.c","email":"liangyonghui123@qq.com","username":"huidou74"},"added":[],"removed":[],"modified":["hello.py"]},"repository":{"id":124529225,"node_id":"MDEwOlJlcG9zaXRvcnkxMjQ1MjkyMjU=","name":"huidou","full_name":"huidou74/huidou","private":false,"owner":{"name":"huidou74","email":"37212138+huidou74@users.noreply.github.com","login":"huidou74","id":37212138,"node_id":"MDQ6VXNlcjM3MjEyMTM4","avatar_url":"https://avatars3.githubusercontent.com/u/37212138?v=4","gravatar_id":"","url":"https://api.github.com/users/huidou74","html_url":"https://github.com/huidou74","followers_url":"https://api.github.com/users/huidou74/followers","following_url":"https://api.github.com/users/huidou74/following{/other_user}","gists_url":"https://api.github.com/users/huidou74/gists{/gist_id}","starred_url":"https://api.github.com/users/huidou74/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/huidou74/subscriptions","organizations_url":"https://api.github.com/users/huidou74/orgs","repos_url":"https://api.github.com/users/huidou74/repos","events_url":"https://api.github.com/users/huidou74/events{/privacy}","received_events_url":"https://api.github.com/users/huidou74/received_events","type":"User","site_admin":false},"html_url":"https://github.com/huidou74/huidou","description":"项目代码","fork":false,"url":"https://github.com/huidou74/huidou","forks_url":"https://api.github.com/repos/huidou74/huidou/forks","keys_url":"https://api.github.com/repos/huidou74/huidou/keys{/key_id}","collaborators_url":"https://api.github.com/repos/huidou74/huidou/collaborators{/collaborator}","teams_url":"https://api.github.com/repos/huidou74/huidou/teams","hooks_url":"https://api.github.com/repos/huidou74/huidou/hooks","issue_events_url":"https://api.github.com/repos/huidou74/huidou/issues/events{/number}","events_url":"https://api.github.com/repos/huidou74/huidou/events","assignees_url":"https://api.github.com/repos/huidou74/huidou/assignees{/user}","branches_url":"https://api.github.com/repos/huidou74/huidou/branches{/branch}","tags_url":"https://api.github.com/repos/huidou74/huidou/tags","blobs_url":"https://api.github.com/repos/huidou74/huidou/git/blobs{/sha}","git_tags_url":"https://api.github.com/repos/huidou74/huidou/git/tags{/sha}","git_refs_url":"https://api.github.com/repos/huidou74/huidou/git/refs{/sha}","trees_url":"https://api.github.com/repos/huidou74/huidou/git/trees{/sha}","statuses_url":"https://api.github.com/repos/huidou74/huidou/statuses/{sha}","languages_url":"https://api.github.com/repos/huidou74/huidou/languages","stargazers_url":"https://api.github.com/repos/huidou74/huidou/stargazers","contributors_url":"https://api.github.com/repos/huidou74/huidou/contributors","subscribers_url":"https://api.github.com/repos/huidou74/huidou/subscribers","subscription_url":"https://api.github.com/repos/huidou74/huidou/subscription","commits_url":"https://api.github.com/repos/huidou74/huidou/commits{/sha}","git_commits_url":"https://api.github.com/repos/huidou74/huidou/git/commits{/sha}","comments_url":"https://api.github.com/repos/huidou74/huidou/comments{/number}","issue_comment_url":"https://api.github.com/repos/huidou74/huidou/issues/comments{/number}","contents_url":"https://api.github.com/repos/huidou74/huidou/contents/{+path}","compare_url":"https://api.github.com/repos/huidou74/huidou/compare/{base}...{head}","merges_url":"https://api.github.com/repos/huidou74/huidou/merges","archive_url":"https://api.github.com/repos/huidou74/huidou/{archive_format}{/ref}","downloads_url":"https://api.github.com/repos/huidou74/huidou/downloads","issues_url":"https://api.github.com/repos/huidou74/huidou/issues{/number}","pulls_url":"https://api.github.com/repos/huidou74/huidou/pulls{/number}","milestones_url":"https://api.github.com/repos/huidou74/huidou/milestones{/number}","notifications_url":"https://api.github.com/repos/huidou74/huidou/notifications{?since,all,participating}","labels_url":"https://api.github.com/repos/huidou74/huidou/labels{/name}","releases_url":"https://api.github.com/repos/huidou74/huidou/releases{/id}","deployments_url":"https://api.github.com/repos/huidou74/huidou/deployments","created_at":1520593227,"updated_at":"2019-05-24T08:34:42Z","pushed_at":1558687287,"git_url":"git://github.com/huidou74/huidou.git","ssh_url":"git@github.com:huidou74/huidou.git","clone_url":"https://github.com/huidou74/huidou.git","svn_url":"https://github.com/huidou74/huidou","homepage":null,"size":6,"stargazers_count":1,"watchers_count":1,"language":"Python","has_issues":true,"has_projects":true,"has_downloads":true,"has_wiki":true,"has_pages":false,"forks_count":0,"mirror_url":null,"archived":false,"disabled":false,"open_issues_count":0,"license":null,"forks":0,"open_issues":0,"watchers":1,"default_branch":"master","stargazers":1,"master_branch":"master"},"pusher":{"name":"huidou74","email":"37212138+huidou74@users.noreply.github.com"},"sender":{"login":"huidou74","id":37212138,"node_id":"MDQ6VXNlcjM3MjEyMTM4","avatar_url":"https://avatars3.githubusercontent.com/u/37212138?v=4","gravatar_id":"","url":"https://api.github.com/users/huidou74","html_url":"https://github.com/huidou74","followers_url":"https://api.github.com/users/huidou74/followers","following_url":"https://api.github.com/users/huidou74/following{/other_user}","gists_url":"https://api.github.com/users/huidou74/gists{/gist_id}","starred_url":"https://api.github.com/users/huidou74/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/huidou74/subscriptions","organizations_url":"https://api.github.com/users/huidou74/orgs","repos_url":"https://api.github.com/users/huidou74/repos","events_url":"https://api.github.com/users/huidou74/events{/privacy}","received_events_url":"https://api.github.com/users/huidou74/received_events","type":"User","site_admin":false}}'
        new_data = eval(str(data).replace('true', '\'true\'').replace('false', '\'false\'').replace('null','\'null\''))  # 转换格式  str -> dict

        class Diff_Data_Webhook(object):
            webhook_id = 0
            committer_id = 0
            def __init__(self,data,auth_list,atuo_commits,sender_list,rep_dict_list,repository_list):
                self.data = data
                self.keys_list = []
                self.model_dict = {}
                self.tem_rep_list = []  # tem repository_list
                self.auth_list = auth_list
                self.atuo_commits = atuo_commits
                self.sender_list = sender_list
                self.rep_dict_list = rep_dict_list
                self.repository_list = repository_list

            def commits(self,data):
                data_list=[]
                for list_dict in data:
                    blacklist_commits = []
                    for i in list_dict.keys():
                        if i not in atuo_commits:
                            blacklist_commits.append(i)
                    for x in blacklist_commits:
                        del list_dict[x]
                    data_list.append(list_dict)
                if data_list:
                    return data_list

            def one_list(slef,data):
                committer = data.pop('committer')  # commit -> committer
                commit.update({'commits_id': data.pop('id')})  # chenger id
                committer_username_obj = models.WebHook_Committer.objects.filter(
                    username=committer.get('username')).first()
                if not committer_username_obj:  # 首次写入数据  获取到了ID ，通过这个ID 再添加剩下的数据
                    committer_obj = models.WebHook_Committer.objects.create(**committer)
                return committer_username_obj.id

            def one_list_data(self,data):
                comm_list = self.commits(data)
                if len(comm_list) == 1:
                    Diff_Data_Webhook.committer_id = self.one_list(comm_list[0])
                else:
                    for comm_dict in comm_list:
                        Diff_Data_Webhook.id = self.one_list(comm_dict)


            def head_commit(self, data):
                for i in head_commit_del_list:
                    del data[i]
                data.update({'commits_id': data.pop('id')})
                return data

            def repository(self, data):
                for y_v in data.values():
                    if isinstance(y_v, dict):
                        for k in y_v.keys():
                            if k not in self.rep_dict_list:  # .clear()
                                self.tem_rep_list.append(k)
                        for a in self.tem_rep_list:
                            del y_v[a]
                        y_v.update({'login_id': y_v.pop('id')})  # 这字典owner的值
                        self.tem_rep_list.clear()  # 清除临时列表
                for key in data.keys():
                    if key not in self.repository_list:
                        self.tem_rep_list.append(key)
                for tem in self.tem_rep_list:
                    del data[tem]
                return data

            def sender(self, data):
                for i in data.keys():
                    if i not in self.sender_list:
                        self.tem_rep_list.append(i)
                for a in self.tem_rep_list:
                    del data[a]
                data.update({'login_id': data.pop('id')})
                return data

            def pusher(self, data):
                webhook_obj = models.WebHook.objects.filter(id=Diff_Data_Webhook.webhook_id)first()
                pusher_name = models.WebHook_Pusher.object.create(**data,pusher=webhook_obj)
                return data


            def run_diff(self):
                for k, v in self.data.items():
                    if isinstance(v, list):  # ->  []  list
                        self.one_list_data(v)   # 存入 写的那一条数据的ID

                    elif isinstance(v, dict):  # ->  {}  dict
                        # print(x)
                        JG = getattr(Diff_Data_Webhook, k)
                        # print(JG(x, y))  # 再次写入数据

                    elif k in auth_list:  # 单纯的字符型就传入列表等待写入数据库
                        self.keys_list.append(k)

                if self.keys_list:  # 写入
                    self.wite_one_datadict(self.keys_list)

            def wite_one_datadict(self,data_list):
                for i in data_list:
                    self.model_dict.update({i: new_data.get(i)})
                    if i == 'ref':
                        ref_class = new_data.get(i)
                        if 'heads' in ref_class:
                            self.model_dict.update({'ref_class': new_data.get(i).split('/')[-1]})
                        elif 'tags' in ref_class:
                            self.model_dict.update({'ref_class': new_data.get(i).split('/')[-1]})
                if self.model_dict:
                    webhook_obj = models.WebHook.objects.create(**model_dict)
                    commit_obj = models.WebHook_Commits.objects.create(**commit, webhook_commits=webhook_obj)
                    Diff_Data_Webhook.webhook_id = webhook_obj.id
                    if committer_username_obj:
                        commit_obj.committer.add(committer_username_obj.id)  # 已存在的用户
                    else:
                        commit_obj.committer.add(committer_obj.id)  # 不存在的用户 需要创建




        # 第一入口 判断values是什么类型再跳转
        commit = {}
        for x, y in new_data.items():
            # print (type(x),x)
            if isinstance(y, list):    #  ->  []  list
                comm_list = commits(y)
                for comm_dict in comm_list:    # list to one  in dict
                    committer = comm_dict.pop('committer')  # commit -> committer
                    commit.update({'commits_id': comm_dict.pop('id')})  # chenger id
                    committer_username_obj = models.WebHook_Committer.objects.filter(username=committer.get('username')).first()
                    if not committer_username_obj:   # 首次写入数据  获取到了ID ，通过这个ID 再添加剩下的数据
                        committer_obj = models.WebHook_Committer.objects.create(**committer)


            elif isinstance(y, dict):  #  ->  {}  dict
                print(x)
                JG = getattr(Y_Dict, x)
                print(JG(x, y))       #  再次写入数据
                # data_list(x,y)
            elif x in auth_list:  # 单纯的字符型就传入列表等待写入数据库
                keys_list.append(x)

        # string   字符串类型 解析出字典存入数据库
        model_dict = {}
        for i in keys_list:
            model_dict.update({i: new_data.get(i)})
            if i == 'ref':
                ref_class = new_data.get(i)
                if 'heads' in ref_class:
                    model_dict.update({'ref_class':new_data.get(i).split('/')[-1]})
                elif 'tags' in ref_class:
                    model_dict.update({'ref_class': new_data.get(i).split('/')[-1]})
        if model_dict:

            webhook_obj = models.WebHook.objects.create(**model_dict)
            commit_obj = models.WebHook_Commits.objects.create(**commit, webhook_commits=webhook_obj)
            if committer_username_obj:
                commit_obj.committer.add(committer_username_obj.id) # 已存在的用户
            else:
                commit_obj.committer.add(committer_obj.id)   # 不存在的用户 需要创建



        return HttpResponse('OK')







# liang = {'LYH':'aaa'}
# test_list = ['abc','ccc']
# class Aaa(object):
#     def abc(self,data):
#         # print (data,type(data))
#         data.update({'a':'zxc'})
#         return data
#     def ccc(self,data):
#
#         return data['LYH']
#
# for i in test_list:
#     c = getattr(Aaa,i)
#
#     z = c(test_list,liang)
#
#     print (' z -> ',z)
#
# cxz = {'cxz':'123'}
# cxz.update({'cxz':'a'})
# print (cxz)