# coding: utf-8
# author: Henry

DEBUG = False                            # 调试开关
configs = {
    'svn': {
        'cmd': "",                       # 指定SVN命令路径, 为空则默认在系统PATH中可以找到
        'dir': "/work/test_group",       # 目标SVN目录路径
    },
    'include_dir': True,                 # 输出结果中是否包含文件夹
    'keep_empty_record': False,          # 输出结果中是否包含空的动作记录
    'print_filter': True,                # 是否开启结果过滤
    'filter': ["\.zip$"],                # 结果过滤条件配置, 满足列表中任意一个条件都匹配成功
    'match': False,                      # 输出匹配结果或输出不匹配的结果
    'push': True,                        # 是否推送到远程服务器
    'go_on_fail': False,                  # 推送中有文件推送失败是继续还是结束
    'upgrade': False,                    # 是直接推送到目标目录还是更新目标目录结构
    'backup': True,                      # 更新目标目录结构是否需要备份
    'app': [                             # 远程服务器设置, 列表中的每个字典中都是一个单独的服务器配置
        {
            'ip': "192.168.12.208",      # 服务器IP
            'port': "22",                # 服务器的SSH端口, 如果未更改过则默认为22
            'user': "root",              # 登录用户名
            'password': "1qaz!QAZ",      # 登录用户密码
            'dist': "/home/tangl/test",  # 目标目录
            'temp': "/tmp/uploads"       # 上传的临时目录
        },
    ],
    'log': 'error.log',                  # 日志文件输出路径
}