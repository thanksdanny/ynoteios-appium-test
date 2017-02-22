import time

class Create_Constant():

    localtime = time.strftime('%Y-%M-%d %H-%M-%S', time.localtime())

    #手写标题
    write_title = unicode('手写') + localtime

    #scan 标题
    scan_title = 'Scan' + localtime

    #英文笔记标题和内容
    english_title = localtime + 'uitest'
    english_article = 'start' + localtime + 'end'

    #中文笔记标题和内容
    chinese_title = localtime + unicode('中文')
    chinese_article = unicode('中文') + localtime + unicode('测试')

    #mk标题
    markdown_title = localtime + 'MarkDown'

    #链接收藏
    link_url='https://www.baidu.com/'