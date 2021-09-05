import os
"""
Author: xiaopch
Date  : 2021-8-30
"""
 
"""	get Header """
def printHead(html_list):
	html_list.append('''<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <title>Bootstrap 101 Template</title>

    <!-- Bootstrap -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">

    <!-- HTML5 shim 和 Respond.js 是为了让 IE8 支持 HTML5 元素和媒体查询（media queries）功能 -->
    <!-- 警告：通过 file:// 协议（就是直接将 html 页面拖拽到浏览器中）访问页面时 Respond.js 不起作用 -->
    <!--[if lt IE 9]>
      <script src="https://cdn.jsdelivr.net/npm/html5shiv@3.7.3/dist/html5shiv.min.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/respond.js@1.4.2/dest/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    
	<div class="container">
    <div class="col-sm-4">
    <h1>你好，世界！</h1>
    <a href="../">[+]</a>
      <h2>目录</h2>
      
      <ul class="nav nav-pills nav-stacked">''')
         
"""	walk the certain dir,and process the dirname """
def printBody(dirname,html_list):
    try:
        ls=os.listdir(dirname)
    except:
        print('access deny')
    else:
        for file in ls:
            if file == 'index.html':
                continue
            temp=os.path.join(dirname,file)
            if(os.path.isdir(temp)):
                html_list.append('<li><a style="background-color:pink;" href="./%s/">%s</a></li>\n' % (file,file))
            else:
                html_list.append('<li><a href="./%s">%s</a></li>\n' % (file,file))
 
"""	get Header """
def printEnd(html_list):
    html_list.append('''      </ul>
      <hr class="hidden-sm hidden-md hidden-lg">
    </div>
	 </div>

    <!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) -->
    <script src="https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js" integrity="sha384-nvAa0+6Qg9clwYCGGPpDQLVpLNn0fRaROjHqs13t4Ggj3Ez50XnGQqc/r8MhnRDZ" crossorigin="anonymous"></script>
    <!-- 加载 Bootstrap 的所有 JavaScript 插件。你也可以根据需要只加载单个插件。 -->
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js" integrity="sha384-aJ21OjlMXNL5UyIl/XNwTMqvzeRMZH2w8c5cRVpzpU8Y5bApTppSuUkhZXN0VxHd" crossorigin="anonymous"></script>
  </body>
</html>''')

def generate_index_links(dirname):
        content_list=[]

        """	Main"""
        _dir = dirname#os.getcwd()
        printHead(content_list)
        printBody(dirname,content_list)
        printEnd(content_list)
        print(dirname)
        with open(os.path.join(dirname,'index.html'),'w',encoding='utf-8') as fd:
                fd.writelines(content_list)
        

if __name__=='__main__':
        print(os.getcwd())
        exclude = set(['.git'])
        for root,dirs,files in os.walk(os.getcwd()):
                dirs[:] = [d for d in dirs if d not in exclude]
                generate_index_links(root)
                for _dir in dirs:
                        print(_dir)
##                        if _dir.startswith('.git'):continue
                        generate_index_links(os.path.join(root,_dir))

        
