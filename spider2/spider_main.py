# coding:utf8
from spider2 import url_manager,html_downloader,html_outputer,html_parser
class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()
    def craw(selfself,root_url):
        count=1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url=self.urls.get_new_url()
                print('craw %d : %s'%(count,new_url))
                html_cont=self.downloader.download(new_url)
                new_urls,new_data=self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_url)
                self.outputer.collect_data(new_data)
                count+=1
                if count==1000:
                    break
            except:
                print('craw faild')
         self.outputer.output_html()




if __name__=="__main__":
    root_url="http://baike.baidu.com/link?url=IR_BZBmRfoV28zQtBEPdIrUlbDfypV5FHNUevIkNv_7J4cvZiMzgCsLPzd6JxiT6jdtP80kez_QgbyBmEn_de_"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)