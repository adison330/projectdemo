#! /usr/bin/env python

from pyecharts import Bar

bar = Bar("这是第一个图标", "这里是副标题")
bar.use_theme("dark")
bar.add("服装",["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 30, 36, 10, 75, 90])
bar.render()
