# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TestscrapyPipeline:
    def process_item(self, item, spider):
        print(f"Đang xử lý item {item['name']}")
        for key in item:
            if item[key] is None:
                print('------------------------------------------')
                print(f'ERROR item {item["name"]} with {key}')
        return item

    # def open_spider(self, spider):
    #     print('Mở spider')

    # def close_spider(self, spider):
    #     print('Đóng spider')
