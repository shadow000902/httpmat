from xml.dom import minidom
from Base.OperateFile import base_file
# web.xml 格式如下
# <?xml version="1.0" encoding="UTF-8" ?>
# <root>
# 	<uu value="cc">ccc-key</uu>
# 	<uu value="dd">dd-key</uu>
# </root>
def read_xml(file='D:/web.xml'):
    base_file(file).check_file()
    doc = minidom.parse(file)
    root = doc.documentElement

    postparams = root.getElementsByTagName("postparams")
    ytitle = root.getElementsByTagName("ytitle")
    xtitle = root.getElementsByTagName("xtitle")
    title = root.getElementsByTagName("title")
    count = root.getElementsByTagName("count")
    baseurl = root.getElementsByTagName("baseurl")
    httpapi = root.getElementsByTagName("httpapi")
    method = root.getElementsByTagName("method")
    mat = root.getElementsByTagName("mat")
    xlim = root.getElementsByTagName("xlim")
    ylim = root.getElementsByTagName("ylim")

    list_xml = {}

    list_xml["ytitle"] = ytitle[0].getAttribute("value")
    list_xml["xtitle"] = xtitle[0].getAttribute("value")
    list_xml["title"] = title[0].getAttribute("value")
    list_xml["count"] = count[0].getAttribute("value")
    list_xml["baseurl"] = baseurl[0].getAttribute("value")
    list_xml["httpapi"] = httpapi[0].getAttribute("value")
    list_xml["method"] = method[0].getAttribute("value")
    list_xml["mat"] = mat[0].getAttribute("value")
    list_xml["xlim"] = xlim[0].getAttribute("value")
    list_xml["ylim"] = ylim[0].getAttribute("value")
    list_xml["postparams"] = postparams[0].getAttribute("value")
    return list_xml




