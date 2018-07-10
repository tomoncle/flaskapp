#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-5 上午9:56
# @Author         : Tom.Lee
# @File           : error_view.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 
try:
    from config import HOME_PATH
except ImportError:
    HOME_PATH = '/'


def view_html(status=500, message=None, home=HOME_PATH):
    return "<!DOCTYPE html>\n" + \
           "<html>\n" + \
           "<head>\n" + \
           "    <meta http-equiv=\"Content-type\" " \
           "content=\"text/html; " \
           "charset=utf-8\">\n" + \
           "    <!--<meta http-equiv=\"Content-Security-Policy\" " \
           "content=\"default-src 'none'; " \
           "base-uri 'self'; connect-src 'self'; " \
           "form-action 'self'; img-src data:; script-src 'self'; " \
           "style-src 'unsafe-inline'\">-->\n" + \
           "    <meta content=\"origin\" name=\"referrer\">\n" + \
           "    <title>" + '{name} page'.format(name=status) + "</title>\n" + \
           "    <style type=\"text/css\" media=\"screen\">\n" + \
           "        body {\n" + \
           "            background-color: #f1f1f1;\n" + \
           "            margin: 0;\n" + \
           "        }\n" + \
           "\n" + \
           "        body,\n" + \
           "        input,\n" + \
           "        button {\n" + \
           "            font-family: \"Helvetica Neue\", " \
           "Helvetica, Arial, sans-serif;\n" + \
           "        }\n" + \
           "\n" + \
           "        .container {\n" + \
           "            margin: 30px auto 40px auto;\n" + \
           "            width: 800px;\n" + \
           "            text-align: center;\n" + \
           "        }\n" + \
           "\n" + \
           "        a {\n" + \
           "            color: #4183c4;\n" + \
           "            text-decoration: none;\n" + \
           "            font-weight: bold;\n" + \
           "        }\n" + \
           "\n" + \
           "        a:hover {\n" + \
           "            text-decoration: underline;\n" + \
           "        }\n" + \
           "\n" + \
           "        h3 {\n" + \
           "            color: #666;\n" + \
           "        }\n" + \
           "\n" + \
           "        ul {\n" + \
           "            list-style: none;\n" + \
           "            padding: 25px 0;\n" + \
           "        }\n" + \
           "\n" + \
           "        li {\n" + \
           "            display: inline;\n" + \
           "            margin: 10px 50px 10px 0px;\n" + \
           "        }\n" + \
           "\n" + \
           "        input[type=text],\n" + \
           "        input[type=password] {\n" + \
           "            font-size: 13px;\n" + \
           "            min-height: 32px;\n" + \
           "            margin: 0;\n" + \
           "            padding: 7px 8px;\n" + \
           "            outline: none;\n" + \
           "            color: #333;\n" + \
           "            background-color: #fff;\n" + \
           "            background-repeat: no-repeat;\n" + \
           "            background-position: right center;\n" + \
           "            border: 1px solid #ccc;\n" + \
           "            border-radius: 3px;\n" + \
           "            box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.075);\n" + \
           "            -moz-box-sizing: border-box;\n" + \
           "            box-sizing: border-box;\n" + \
           "            -webkit-transition: all 0.15s ease-in;\n" + \
           "            transition: all 0.15s ease-in;\n" + \
           "            vertical-align: middle;\n" + \
           "        }\n" + \
           "\n" + \
           "        .btn {\n" + \
           "            position: relative;\n" + \
           "            display: inline-block;\n" + \
           "            padding: 6px 12px;\n" + \
           "            font-size: 13px;\n" + \
           "            font-weight: bold;\n" + \
           "            line-height: 20px;\n" + \
           "            color: #333;\n" + \
           "            white-space: nowrap;\n" + \
           "            vertical-align: middle;\n" + \
           "            cursor: pointer;\n" + \
           "            background-color: #EEE;\n" + \
           "            background-image: -webkit-linear-gradient(#FCFCFC, #EEE);\n" + \
           "            background-image: linear-gradient(#FCFCFC, #EEE);\n" + \
           "            background-repeat: repeat-x;\n" + \
           "            border: 1px solid #d5d5d5;\n" + \
           "            border-radius: 3px;\n" + \
           "            user-select: none;\n" + \
           "            -webkit-appearance: none;\n" + \
           "        }\n" + \
           "\n" + \
           "        .btn:focus,\n" + \
           "        input[type=text]:focus,\n" + \
           "        input[type=password]:focus {\n" + \
           "            text-decoration: none;\n" + \
           "            border-color: #51a7e8;\n" + \
           "            outline: none;\n" + \
           "            box-shadow: 0 0 5px rgba(81, 167, 232, 0.5);\n" + \
           "        }\n" + \
           "\n" + \
           "        .btn:hover,\n" + \
           "        .btn:active {\n" + \
           "            text-decoration: none;\n" + \
           "            background-color: #ddd;\n" + \
           "            background-image: -webkit-linear-gradient(#eee, #ddd);\n" + \
           "            background-image: linear-gradient(#eee, #ddd);\n" + \
           "            background-repeat: repeat-x;\n" + \
           "            border-color: #ccc;\n" + \
           "        }\n" + \
           "\n" + \
           "        .btn:active {\n" + \
           "            background-color: #dcdcdc;\n" + \
           "            background-image: none;\n" + \
           "            border-color: #b5b5b5;\n" + \
           "            box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.15);\n" + \
           "        }\n" + \
           "\n" + \
           "        #auth {\n" + \
           "            position: absolute;\n" + \
           "            top: 0;\n" + \
           "            right: 0;\n" + \
           "            z-index: 50;\n" + \
           "            min-height: 32px;\n" + \
           "            background-color: rgba(53, 95, 120, .4);\n" + \
           "            padding: 7px 10px;\n" + \
           "            border-bottom-right-radius: 10px;\n" + \
           "            border-bottom-left-radius: 10px;\n" + \
           "            box-shadow: 0 3px 0 rgba(0, 0, 0, 0.28);\n" + \
           "            display: none;\n" + \
           "        }\n" + \
           "\n" + \
           "        #auth h1, #auth p, #auth label {\n" + \
           "            display: none;\n" + \
           "        }\n" + \
           "\n" + \
           "        .auth-form-body {\n" + \
           "            display: inline;\n" + \
           "        }\n" + \
           "\n" + \
           "        #auth input[type=text],\n" + \
           "        #auth input[type=password] {\n" + \
           "            float: left;\n" + \
           "            width: 175px;\n" + \
           "            margin-right: 9px;\n" + \
           "            border: 0;\n" + \
           "            background-color: #f5f5f5;\n" + \
           "        }\n" + \
           "\n" + \
           "        #auth input[type=text]:focus,\n" + \
           "        #auth input[type=password]:focus {\n" + \
           "            background-color: #fff;\n" + \
           "            box-shadow: 0 0 5px rgba(255, 255, 255, .5);\n" + \
           "        }\n" + \
           "\n" + \
           "        #auth .btn {\n" + \
           "            border: 0;\n" + \
           "        }\n" + \
           "\n" + \
           "        #auth .btn:focus {\n" + \
           "            box-shadow: 0 0 5px rgba(255, 255, 255, .5);\n" + \
           "        }\n" + \
           "\n" + \
           "        label[for=search] {\n" + \
           "            display: block;\n" + \
           "            text-align: left;\n" + \
           "        }\n" + \
           "\n" + \
           "        #search label {\n" + \
           "            font-weight: 200;\n" + \
           "            padding: 5px 0;\n" + \
           "        }\n" + \
           "\n" + \
           "        #search input[type=text] {\n" + \
           "            font-size: 18px;\n" + \
           "            width: 705px;\n" + \
           "        }\n" + \
           "\n" + \
           "        #search .btn {\n" + \
           "            padding: 10px;\n" + \
           "            width: 90px;\n" + \
           "        }\n" + \
           "\n" + \
           "        .logo {\n" + \
           "            display: inline-block;\n" + \
           "            margin-top: 35px;\n" + \
           "        }\n" + \
           "\n" + \
           "        .logo-img-2x {\n" + \
           "            display: none;\n" + \
           "        }\n" + \
           "\n" + \
           "        @media only screen and (" \
           "-webkit-min-device-pixel-ratio: 2), only screen and (   " \
           "min--moz-device-pixel-ratio: 2), only screen and (     " \
           "-o-min-device-pixel-ratio: 2/1), only screen and (        " \
           "min-device-pixel-ratio: 2), only screen and (                " \
           "min-resolution: 192dpi), only screen and (                " \
           "min-resolution: 2dppx) {\n" + \
           "            .logo-img-1x {\n" + \
           "                display: none;\n" + \
           "            }\n" + \
           "\n" + \
           "            .logo-img-2x {\n" + \
           "                display: inline-block;\n" + \
           "            }\n" + \
           "        }\n" + \
           "\n" + \
           "        #suggestions {\n" + \
           "            margin-top: 35px;\n" + \
           "            color: #ccc;\n" + \
           "        }\n" + \
           "\n" + \
           "        #suggestions a {\n" + \
           "            color: #666666;\n" + \
           "            font-weight: 200;\n" + \
           "            font-size: 14px;\n" + \
           "            margin: 0 10px;\n" + \
           "        }\n" + \
           "\n" + \
           "        #parallax_wrapper {\n" + \
           "            position: relative;\n" + \
           "            z-index: 0;\n" + \
           "            -webkit-transition: all 0.25s ease-in;\n" + \
           "            transition: all 0.25s ease-in;\n" + \
           "        }\n" + \
           "\n" + \
           "        #parallax_field {\n" + \
           "            overflow: hidden;\n" + \
           "            position: absolute;\n" + \
           "            left: 0;\n" + \
           "            top: 0;\n" + \
           "            height: 370px;\n" + \
           "            width: 100%;\n" + \
           "        }\n" + \
           "\n" + \
           "        #parallax_field #parallax_bg {\n" + \
           "            position: absolute;\n" + \
           "            top: -20px;\n" + \
           "            left: -20px;\n" + \
           "            width: 110%;\n" + \
           "            height: 425px;\n" + \
           "            z-index: 1;\n" + \
           "        }\n" + \
           "\n" + \
           "        #parallax_illustration {\n" + \
           "            display: block;\n" + \
           "            margin: 0 auto;\n" + \
           "            width: 940px;\n" + \
           "            height: 370px;\n" + \
           "            position: relative;\n" + \
           "            overflow: hidden;\n" + \
           "            clear: both;\n" + \
           "        }\n" + \
           "\n" + \
           "        #parallax_illustration img {\n" + \
           "            position: absolute;\n" + \
           "        }\n" + \
           "\n" + \
           "        #parallax_illustration #parallax_error_text {\n" + \
           "            top: 72px;\n" + \
           "            left: 72px;\n" + \
           "            z-index: 10;\n" + \
           "        }\n" + \
           "\n" + \
           "        #parallax_illustration #parallax_octocat {\n" + \
           "            top: 94px;\n" + \
           "            left: 356px;\n" + \
           "            z-index: 9;\n" + \
           "        }\n" + \
           "\n" + \
           "        #parallax_illustration #parallax_speeder {\n" + \
           "            top: 150px;\n" + \
           "            left: 432px;\n" + \
           "            z-index: 8;\n" + \
           "        }\n" + \
           "\n" + \
           "        #parallax_illustration #parallax_octocatshadow {\n" + \
           "            top: 297px;\n" + \
           "            left: 371px;\n" + \
           "            z-index: 7;\n" + \
           "        }\n" + \
           "\n" + \
           "        #parallax_illustration #parallax_speedershadow {\n" + \
           "            top: 263px;\n" + \
           "            left: 442px;\n" + \
           "            z-index: 6;\n" + \
           "        }\n" + \
           "\n" + \
           "        #parallax_illustration #parallax_building_1 {\n" + \
           "            top: 73px;\n" + \
           "            left: 467px;\n" + \
           "            z-index: 5;\n" + \
           "        }\n" + \
           "\n" + \
           "        #parallax_illustration #parallax_building_2 {\n" + \
           "            top: 113px;\n" + \
           "            left: 762px;\n" + \
           "            z-index: 4;\n" + \
           "        }\n" + \
           "    </style>\n" + \
           "\n" + \
           "\n" + \
           "</head>\n" + \
           "<body>\n" + \
           "<div id=\"parallax_wrapper\">\n" + \
           "</div>\n" + \
           "<div class=\"container\">\n" + \
           "    <label for=\"search\" style=\"color: red\">\n" + \
           "        <h1 style=\"color: red\">" + \
           "{status}".format(status=status) + \
           "</h1>\n" + \
           "        " + "{message}".format(message=message) + "\n" + \
           "        <div><br /></div>\n" + \
           "        <div id=\"showTime\" style=\"color: green; " \
           "font-size: x-small\"></div>\n" + \
           "    </label>\n" + \
           "    <a href=\"" + "{home}".format(home=home) + \
           "\" class=\"logo logo-img-1x\">返回首页</a>\n" + \
           "</div>\n" + \
           "<script>\n" + \
           "    setInterval(\"fun()\", 1);\n" + \
           "    function fun() {\n" + \
           "        var date = new Date();  " \
           "//创建对象\n" + \
           "        var y = date.getFullYear();     " \
           "//获取年份\n" + \
           "        var m = date.getMonth() + 1;   " \
           "//获取月份  返回0-11\n" + \
           "        var d = date.getDate(); " \
           "// 获取日\n" + \
           "        var w = date.getDay();   " \
           "//获取星期几  返回0-6   (0=星期天)\n" + \
           "        var ww = ' 星期' + '日一二三四五六'.charAt(new Date().getDay());" \
           "//星期几\n" + \
           "        var h = date.getHours();  //时\n" + \
           "        var minute = date.getMinutes()  //分\n" + \
           "        var s = date.getSeconds(); //秒\n" + \
           "        var sss = date.getMilliseconds(); //毫秒\n" + \
           "        if (m < 10) {\n" + \
           "            m = \"0\" + m;\n" + \
           "        }\n" + \
           "        if (d < 10) {\n" + \
           "            d = \"0\" + d;\n" + \
           "        }\n" + \
           "        if (h < 10) {\n" + \
           "            h = \"0\" + h;\n" + \
           "        }\n" + \
           "\n" + \
           "        if (minute < 10) {\n" + \
           "            minute = \"0\" + minute;\n" + \
           "        }\n" + \
           "\n" + \
           "        if (s < 10) {\n" + \
           "            s = \"0\" + s;\n" + \
           "        }\n" + \
           "\n" + \
           "        if (sss < 10) {\n" + \
           "            sss = \"00\" + sss;\n" + \
           "        } else if (sss < 100) {\n" + \
           "            sss = \"0\" + sss;\n" + \
           "        }\n" + "\n" + \
           "        document.getElementById(\"showTime\").innerHTML = " \
           "y + \"-\" " \
           "+ m + \"-\" " \
           "+ d + \"   \" " \
           "+ h + \":\" " \
           "+ minute + \":\" " \
           "+ s + \".\" " \
           "+ sss + \"  \" " \
           "+ ww;\n" + \
           "    }\n" + \
           "</script>\n" + \
           "</body>\n" + \
           "\n" + \
           "</html>\n"
