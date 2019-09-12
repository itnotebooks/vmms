#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author         : Eric Winn
# @Email          : eng.eric.winn@gmail.com
# @Time           : 19-9-12 下午10:17
# @Version        : 1.0
# @File           : vmware
# @Software       : PyCharm

import atexit
import ssl
import platform
from pyVmomi import vim, vmodl
import logging

if platform.system() == 'Darwin':
    from pyvim import connect

else:
    from pyVim import connect

logger = logging.getLogger(__file__)


def vm_connect(vcenter):
    try:
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        context.verify_mode = ssl.CERT_NONE

        try:
            service_instance = connect.SmartConnect(host=vcenter.host,
                                                    user=vcenter.username,
                                                    pwd=vcenter.password,
                                                    port=int(vcenter.port),
                                                    sslContext=context)
        except Exception as e:
            logger.error(e)
            return -1

        if not service_instance:
            logger.error("Could not connect to the specified host using specified "
                         "username and password")
            return -1
        atexit.register(connect.Disconnect, service_instance)

    except vmodl.MethodFault as e:
        logger.error("Caught vmodl fault : {}".format(e.msg))
        return -1
    return service_instance
