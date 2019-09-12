import uuid
from django.db import models

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.cache import cache

__all__ = [
    'IaasVirtualMachine', 'Iaas_ClusterInfo'
]


# Create your models here.
class IaasVirtualMachine(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    vmname = models.CharField(max_length=64, verbose_name=_("Name"))
    hostname = models.CharField(max_length=64, verbose_name=_("HostName"))
    ip = models.GenericIPAddressField(max_length=32, null=True, verbose_name=_('IP'), db_index=True)
    mac = models.CharField(null=True, max_length=17, verbose_name=_('MAC'))
    cpu = models.IntegerField(null=True, verbose_name=_('CPU'), db_index=True)
    memory = models.CharField(max_length=64, null=True, blank=True, verbose_name=_('Memory'))
    disk_size = models.CharField(max_length=64, null=True, blank=True, verbose_name=_('Disk Size'))
    power_state = models.CharField(max_length=12, null=True, blank=True, verbose_name=_('Status'))
    host = models.GenericIPAddressField(max_length=32, null=True, verbose_name=_('Host'), db_index=True)
    clustername = models.CharField(max_length=64, verbose_name=_("ClusterName"))
    datacentername = models.CharField(max_length=64, verbose_name=_("DatacenterName"))
    vcenter = models.CharField(max_length=64, verbose_name=_("Vcenter"))

    def __str__(self):
        return self.vmname

    class Meta:
        db_table = "iaas_virtual_machine"


class Iaas_ClusterInfo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    ip = models.GenericIPAddressField(max_length=32, null=True, verbose_name=_('IP'))
    clustername = models.CharField(max_length=64, null=True, verbose_name=('ClusterName'))
    overallstatus = models.CharField(max_length=64, null=True, verbose_name=('OverallStatus'))
    numhosts = models.CharField(max_length=64, null=True, verbose_name=('NumHosts'))
    cpuused = models.CharField(max_length=64, null=True, verbose_name=('CpuUsed'))
    cputotal = models.CharField(max_length=64, null=True, verbose_name=('CpuTotal'))
    cpuusedp = models.CharField(max_length=64, null=True, verbose_name=('CpuUsedp'))
    memtotal = models.CharField(max_length=64, null=True, verbose_name=('MemTotal'))
    memused = models.CharField(max_length=64, null=True, verbose_name=('MemUsed'))
    mempercent = models.CharField(max_length=64, null=True, verbose_name=('Mempercent'))
    totaldatastore = models.CharField(max_length=64, null=True, verbose_name=('TotalDatastore'))
    datastoreuse = models.CharField(max_length=64, null=True, verbose_name=('Datastoreuse'))
    datastorefree = models.CharField(max_length=64, null=True, verbose_name=('DatastoreFree'))
    datastoreusedp = models.CharField(max_length=64, null=True, verbose_name=('DatastoreUsedp'))
    vmcount = models.CharField(max_length=64, null=True, verbose_name=('VMCount'))
    datacentername = models.CharField(max_length=64, null=True, verbose_name=('Datacentername'))

    class Meta:
        db_table = "iaas_clusterinfo"
