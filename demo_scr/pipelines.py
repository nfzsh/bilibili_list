import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DemoScrPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect('localhost', 'root', 'root', 'python')
        self.cursor = self.connect.cursor()
        print("连接数据库成功")

    def process_item(self, item, spider):
        print(item)
        # sql语句
        insert_sql = """
                insert into bilibili_list(`rank`, `name`, `pic`, `url`, `aid`, `bv`, `view`, `up`, `upId`, `date`, `type`)
                 VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')
                """ % (item['rank'], item['name'], item['pic'], item['url'],
                                         item['aid'], item['bv'], item['view'], item['up'],
                                         item['upId'], item['date'], item['type'])
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql)
        # 提交，不进行提交无法保存到数据库
        self.connect.commit()

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.connect.close()
