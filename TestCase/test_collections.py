# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 下午4:14
# @Author  : WangJuan
# @File    : Test_Collections.py

import allure
from Params.params import Collections
from Conf.Config import Config
from Common import Request
from Common import Consts
from Common import Assert


class TestCollections:

    @allure.feature('Home')
    @allure.severity('normal')
    @allure.story('Collections')
    def test_collections_01(self, action):
        """
            用例描述：查看用户'da1677475c27'的Collections
        """
        conf = Config()
        data = Collections()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'http://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[0]
        response = request.post_request(api_url, params[0], headers[0])
        assert test.assert_code(response['code'], 200)
        assert test.assert_in_text(response['body'], '软件测试-各种技能集合')
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Collections')
    def test_collections_02(self, action):
        """
            用例描述：查看用户'95c34f9cc50c'的Collections
        """
        conf = Config()
        data = Collections()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'http://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[1]
        response = request.post_request(api_url, params[1], headers[1])
        assert test.assert_code(response['code'], 208)
        assert test.assert_in_text(response['body'], '每日一篇技术文')
        Consts.RESULT_LIST.append('True')




