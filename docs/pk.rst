.. _pk:

v1/pk
=============
    PK是Package的缩写，表示资源包比如如HISIHIApp安装包

下载包的下载数量+1
~~~~~~~~~~~~~~~~~~~~
URL::

    PUT       /download+1

PUT::

    {
        "oid" : 4
        "channel" : 1
    }

Parameters:

* channel: 1 表示通过online活动的方式下载了一次安装包，可取值 [1 | "1" | "online"]
* oid: 当channel="online"时，表示活动的id号

Response Status `202` ::

    {
        "code": 0,
        "msg": "ok",
        "request": "PUT  /v1/pk/download+1"
    }

