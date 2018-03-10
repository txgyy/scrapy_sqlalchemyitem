#!/usr/bin/env python
# -*- coding: utf-8 -*-

from six import with_metaclass
from scrapy.item import Field, Item, ItemMeta

class SqlalchemyItemMeta(ItemMeta):

    def __new__(mcs, class_name, bases, attrs):
        cls = super(SqlalchemyItemMeta, mcs).__new__(mcs, class_name, bases, attrs)
        if cls.sqlalchemy_model:
            cls._model_fields = []
            for model_field in cls.sqlalchemy_model.__table__.columns:
                    if model_field.name not in cls.fields:
                        cls.fields[model_field.name] = Field()
        return cls

class SqlalchemyItem(with_metaclass(SqlalchemyItemMeta, Item)):
    sqlalchemy_model = None