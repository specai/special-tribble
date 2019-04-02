# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline
from urllib.parse import urlparse
import os

class ItbooksPipeline(object):
    def process_item(self, item, spider):
        return item

class SelfDefineFilePipline(FilesPipeline):
    """
    继承FilesPipeline，更改其存储文件的方式
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def file_path(self, request, response=None, info=None):
        parse_result = urlparse(request.url)
        path = parse_result.path
        basename = os.path.basename(path)
        return basename
