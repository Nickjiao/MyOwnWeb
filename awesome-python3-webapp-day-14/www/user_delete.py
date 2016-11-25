#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jiao Haiquan'

'''
   删除设定email的所有信息
'''
import asyncio
import orm

from models import User, Comment, Blog
from config import configs

@asyncio.coroutine
def delete_User(loop,email='111@qq.com'):
    yield from orm.create_pool(loop=loop, **configs.db)
    users = None
    users = yield from User.findAll('email=?', [email])
    if len(users) > 0:
        for x in users:
            blogs = yield from Blog.findAll('user_id=?', [x['id']])
            comns = yield from Comment.findAll('user_id=?', [x['id']])
            if len(blogs) > 0:
                yield from blogs.remove()
            if len(comns) > 0:
                yield from comns.remove()
            yield from x.remove()
    else:
        print('没有此用户信息!')
    return True

@asyncio.coroutine
def select_User(loop,email='111@qq.com'):
    yield from orm.create_pool(loop=loop, **configs.db)
    users = None
    users = yield from User.findAll('email=?', [email])
    if len(users) > 0:
        for x in users:
            blogs = yield from Blog.findAll('user_id=?', [x['id']])
            print(blogs[0]['name'])
            print(blogs[0]['summary'])
            print(blogs[0]['content'])
    else:
        print('没有此用户信息!')
    return True

if __name__ == '__main__':
    email = 'jiaohaiquan@test.com'
    loop = asyncio.get_event_loop()
    loop.run_until_complete(select_User(loop,email))
    loop.close()
