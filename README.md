# 入门
这个项目属于个人博客, 基于django开发, 代码用git管理, 开发工具用pycharm, 数据库推荐用postgresql,其他数据库也可以. 

# 安装
* cd WangBlog
* python setup.py develop
* wangblog migrate
* wangblog createsuperuser
* wangblog init
* wangblog runserver

# CHANGES LOG
* 解决了之前oauth认证去不掉授权表单的问题
* 重新规划了项目的目录结构
* 扩展了 django 内置auth_user表,比之前使用子表的方式更简单灵活,auth_user表中, 添加了组织, 电话, 等字段
* 重新设置了loginsight的模板
