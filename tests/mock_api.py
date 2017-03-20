import os
from libcloud.utils.py3 import PY3
from libcloud.utils.py3 import u
from libcloud.utils.py3 import httplib
from libcloud.test import MockHttp
try:
    from lxml import etree as ET
except ImportError:
    from xml.etree import ElementTree as ET


class FileFixtures(object):
    def __init__(self):
        script_dir = os.path.abspath(os.path.split(__file__)[0])
        self.root = os.path.join(script_dir, 'fixtures')

    def load(self, file):
        path = os.path.join(self.root, file)
        if os.path.exists(path):
            if PY3:
                kwargs = {'encoding': 'utf-8'}
            else:
                kwargs = {}

            with open(path, 'r', **kwargs) as fh:
                content = fh.read()
            return u(content)
        else:
            raise IOError(path)


class ComputeFileFixtures(FileFixtures):
    def __init__(self):
        super(ComputeFileFixtures, self).__init__()


class InvalidRequestError(Exception):
    def __init__(self, tag):
        super(InvalidRequestError, self).__init__("Invalid Request - %s" % tag)


class DimensionDataMockHttp(MockHttp):

    fixtures = ComputeFileFixtures()

    def _oec_0_9_myaccount_UNAUTHORIZED(self, method, url, body, headers):
        return (httplib.UNAUTHORIZED, "", {}, httplib.responses[httplib.UNAUTHORIZED])

    def _oec_0_9_myaccount(self, method, url, body, headers):
        body = self.fixtures.load('oec_0_9_myaccount.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_myaccount_INPROGRESS(self, method, url, body, headers):
        body = self.fixtures.load('oec_0_9_myaccount.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_myaccount_PAGINATED(self, method, url, body, headers):
        body = self.fixtures.load('oec_0_9_myaccount.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_myaccount_ALLFILTERS(self, method, url, body, headers):
        body = self.fixtures.load('oec_0_9_myaccount.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_base_image(self, method, url, body, headers):
        body = self.fixtures.load('oec_0_9_base_image.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_base_imageWithDiskSpeed(self, method, url, body, headers):
        body = self.fixtures.load('oec_0_9_base_imageWithDiskSpeed.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_deployed(self, method, url, body, headers):
        body = self.fixtures.load(
            'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_deployed.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_pendingDeploy(self, method, url, body, headers):
        body = self.fixtures.load(
            'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_pendingDeploy.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_datacenter(self, method, url, body, headers):
        body = self.fixtures.load(
            'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_datacenter.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_11(self, method, url, body, headers):
        body = None
        action = url.split('?')[-1]

        if action == 'restart':
            body = self.fixtures.load(
                'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_11_restart.xml')
        elif action == 'shutdown':
            body = self.fixtures.load(
                'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_11_shutdown.xml')
        elif action == 'delete':
            body = self.fixtures.load(
                'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_11_delete.xml')
        elif action == 'start':
            body = self.fixtures.load(
                'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_11_start.xml')
        elif action == 'poweroff':
            body = self.fixtures.load(
                'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_11_poweroff.xml')

        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_11_INPROGRESS(self, method, url, body, headers):
        body = None
        action = url.split('?')[-1]

        if action == 'restart':
            body = self.fixtures.load(
                'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_11_restart_INPROGRESS.xml')
        elif action == 'shutdown':
            body = self.fixtures.load(
                'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_11_shutdown_INPROGRESS.xml')
        elif action == 'delete':
            body = self.fixtures.load(
                'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_11_delete_INPROGRESS.xml')
        elif action == 'start':
            body = self.fixtures.load(
                'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_11_start_INPROGRESS.xml')
        elif action == 'poweroff':
            body = self.fixtures.load(
                'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_11_poweroff_INPROGRESS.xml')

        return (httplib.BAD_REQUEST, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server(self, method, url, body, headers):
        body = self.fixtures.load(
            '_oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_networkWithLocation(self, method, url, body, headers):
        if method is "POST":
            request = ET.fromstring(body)
            if request.tag != "{http://oec.api.opsource.net/schemas/network}NewNetworkWithLocation":
                raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_networkWithLocation.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_networkWithLocation_NA9(self, method, url, body, headers):
        body = self.fixtures.load(
            'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_networkWithLocation.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_4bba37be_506f_11e3_b29c_001517c4643e(self, method,
                                                                                                   url, body, headers):
        body = self.fixtures.load(
            'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_4bba37be_506f_11e3_b29c_001517c4643e.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87_disk_1_changeSize(self, method, url, body, headers):
        body = self.fixtures.load(
            'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87_disk_1_changeSize.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87_disk_1_changeSpeed(self, method, url, body, headers):
        body = self.fixtures.load(
            'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87_disk_1_changeSpeed.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87_disk_1(self, method, url, body, headers):
        action = url.split('?')[-1]
        if action == 'delete':
            body = self.fixtures.load(
                'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87_disk_1.xml')
            return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87(self, method, url, body, headers):
        if method == 'GET':
            body = self.fixtures.load(
                'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87.xml')
            return (httplib.OK, body, {}, httplib.responses[httplib.OK])
        if method == 'POST':
            body = self.fixtures.load(
                'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87_POST.xml')
            return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_antiAffinityRule(self, method, url, body, headers):
        body = self.fixtures.load(
            'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_antiAffinityRule_create.xml'
        )
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_antiAffinityRule_FAIL_EXISTING(self, method, url, body, headers):
        body = self.fixtures.load(
            'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_antiAffinityRule_create_FAIL.xml'
        )
        return (httplib.BAD_REQUEST, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_antiAffinityRule_07e3621a_a920_4a9a_943c_d8021f27f418(self, method, url, body, headers):
        body = self.fixtures.load(
            'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_antiAffinityRule_delete.xml'
        )
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_antiAffinityRule_07e3621a_a920_4a9a_943c_d8021f27f418_FAIL(self, method, url, body, headers):
        body = self.fixtures.load(
            'oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_antiAffinityRule_delete_FAIL.xml'
        )
        return (httplib.BAD_REQUEST, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server(self, method, url, body, headers):
        body = self.fixtures.load(
            'server.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_deleteServer(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}deleteServer":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'server_deleteServer.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_deleteServer_INPROGRESS(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}deleteServer":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'server_deleteServer_RESOURCEBUSY.xml')
        return (httplib.BAD_REQUEST, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_rebootServer(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}rebootServer":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'server_rebootServer.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_rebootServer_INPROGRESS(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}rebootServer":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'server_rebootServer_RESOURCEBUSY.xml')
        return (httplib.BAD_REQUEST, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_server(self, method, url, body, headers):
        if url.endswith('datacenterId=NA3'):
            body = self.fixtures.load(
                '2.4/server_server_NA3.xml')
            return (httplib.OK, body, {}, httplib.responses[httplib.OK])

        body = self.fixtures.load(
            '2.4/server_server.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_server_PAGESIZE50(self, method, url, body, headers):
        if not url.endswith('pageSize=50'):
            raise ValueError("pageSize is not set as expected")
        body = self.fixtures.load(
            '2.4/server_server.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_server_EMPTY(self, method, url, body, headers):
        body = self.fixtures.load(
            'server_server_paginated_empty.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_server_PAGED_THEN_EMPTY(self, method, url, body, headers):
        if 'pageNumber=2' in url:
            body = self.fixtures.load(
                'server_server_paginated_empty.xml')
            return (httplib.OK, body, {}, httplib.responses[httplib.OK])
        else:
            body = self.fixtures.load(
                '2.4/server_server_paginated.xml')
            return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_server_PAGINATED(self, method, url, body, headers):
        if 'pageNumber=2' in url:
            body = self.fixtures.load(
                '2.4/server_server.xml')
            return (httplib.OK, body, {}, httplib.responses[httplib.OK])
        else:
            body = self.fixtures.load(
                '2.4/server_server_paginated.xml')
            return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_server_PAGINATEDEMPTY(self, method, url, body, headers):
        body = self.fixtures.load(
            'server_server_paginated_empty.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_server_ALLFILTERS(self, method, url, body, headers):
        (_, params) = url.split('?')
        parameters = params.split('&')
        for parameter in parameters:
            (key, value) = parameter.split('=')
            if key == 'datacenterId':
                assert value == 'fake_loc'
            elif key == 'networkId':
                assert value == 'fake_network'
            elif key == 'networkDomainId':
                assert value == 'fake_network_domain'
            elif key == 'vlanId':
                assert value == 'fake_vlan'
            elif key == 'ipv6':
                assert value == 'fake_ipv6'
            elif key == 'privateIpv4':
                assert value == 'fake_ipv4'
            elif key == 'name':
                assert value == 'fake_name'
            elif key == 'state':
                assert value == 'fake_state'
            elif key == 'started':
                assert value == 'True'
            elif key == 'deployed':
                assert value == 'True'
            elif key == 'sourceImageId':
                assert value == 'fake_image'
            else:
                raise ValueError("Could not find in url parameters {0}:{1}".format(key, value))
        body = self.fixtures.load(
            '2.4/server_server.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_antiAffinityRule(self, method, url, body, headers):
        body = self.fixtures.load(
            'server_antiAffinityRule_list.xml'
        )
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_antiAffinityRule_ALLFILTERS(self, method, url, body, headers):
        (_, params) = url.split('?')
        parameters = params.split('&')
        for parameter in parameters:
            (key, value) = parameter.split('=')
            if key == 'id':
                assert value == 'FAKE_ID'
            elif key == 'state':
                assert value == 'FAKE_STATE'
            elif key == 'pageSize':
                assert value == '250'
            elif key == 'networkDomainId':
                pass
            else:
                raise ValueError("Could not find in url parameters {0}:{1}".format(key, value))
        body = self.fixtures.load(
            'server_antiAffinityRule_list.xml'
        )
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_antiAffinityRule_PAGINATED(self, method, url, body, headers):
        if 'pageNumber=2' in url:
            body = self.fixtures.load(
                'server_antiAffinityRule_list.xml')
            return (httplib.OK, body, {}, httplib.responses[httplib.OK])
        else:
            body = self.fixtures.load(
                'server_antiAffinityRule_list_PAGINATED.xml')
            return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_infrastructure_datacenter(self, method, url, body, headers):
        if url.endswith('id=NA9'):
            body = self.fixtures.load(
                'infrastructure_datacenter_NA9.xml')
            return (httplib.OK, body, {}, httplib.responses[httplib.OK])

        body = self.fixtures.load(
            'infrastructure_datacenter.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_infrastructure_datacenter_ALLFILTERS(self, method, url, body, headers):
        if url.endswith('id=NA9'):
            body = self.fixtures.load(
                'infrastructure_datacenter_NA9.xml')
            return (httplib.OK, body, {}, httplib.responses[httplib.OK])

        body = self.fixtures.load(
            'infrastructure_datacenter.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_updateVmwareTools(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}updateVmwareTools":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'server_updateVmwareTools.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_startServer(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}startServer":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'server_startServer.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_startServer_INPROGRESS(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}startServer":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'server_startServer_INPROGRESS.xml')
        return (httplib.BAD_REQUEST, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_shutdownServer(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}shutdownServer":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'server_shutdownServer.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_shutdownServer_INPROGRESS(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}shutdownServer":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'server_shutdownServer_INPROGRESS.xml')
        return (httplib.BAD_REQUEST, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_resetServer(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}resetServer":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'server_resetServer.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_powerOffServer(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}powerOffServer":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'server_powerOffServer.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_powerOffServer_INPROGRESS(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}powerOffServer":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'server_powerOffServer_INPROGRESS.xml')
        return (httplib.BAD_REQUEST, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_server_11_INPROGRESS(
            self, method, url, body, headers):
        body = self.fixtures.load('2.4/server_GetServer.xml')
        return (httplib.BAD_REQUEST, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_networkDomain(self, method, url, body, headers):
        body = self.fixtures.load(
            'network_networkDomain.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_networkDomain_ALLFILTERS(self, method, url, body, headers):
        (_, params) = url.split('?')
        parameters = params.split('&')
        for parameter in parameters:
            (key, value) = parameter.split('=')
            if key == 'datacenterId':
                assert value == 'fake_location'
            elif key == 'type':
                assert value == 'fake_plan'
            elif key == 'name':
                assert value == 'fake_name'
            elif key == 'state':
                assert value == 'fake_state'
            else:
                raise ValueError("Could not find in url parameters {0}:{1}".format(key, value))
        body = self.fixtures.load(
            'network_networkDomain.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_vlan(self, method, url, body, headers):
        body = self.fixtures.load(
            'network_vlan.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_vlan_ALLFILTERS(self, method, url, body, headers):
        (_, params) = url.split('?')
        parameters = params.split('&')
        for parameter in parameters:
            (key, value) = parameter.split('=')
            if key == 'datacenterId':
                assert value == 'fake_location'
            elif key == 'networkDomainId':
                assert value == 'fake_network_domain'
            elif key == 'ipv6Address':
                assert value == 'fake_ipv6'
            elif key == 'privateIpv4Address':
                assert value == 'fake_ipv4'
            elif key == 'name':
                assert value == 'fake_name'
            elif key == 'state':
                assert value == 'fake_state'
            else:
                raise ValueError("Could not find in url parameters {0}:{1}".format(key, value))
        body = self.fixtures.load(
            'network_vlan.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_deployServer(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}deployServer":
            raise InvalidRequestError(request.tag)

        # Make sure the we either have a network tag with an IP or networkId
        # Or Network info with a primary nic that has privateip or vlanid
        network = request.find(fixxpath('network', TYPES_URN))
        network_info = request.find(fixxpath('networkInfo', TYPES_URN))
        if network is not None:
            if network_info is not None:
                raise InvalidRequestError("Request has both MCP1 and MCP2 values")
            ipv4 = findtext(network, 'privateIpv4', TYPES_URN)
            networkId = findtext(network, 'networkId', TYPES_URN)
            if ipv4 is None and networkId is None:
                raise InvalidRequestError('Invalid request MCP1 requests need privateIpv4 or networkId')
        elif network_info is not None:
            if network is not None:
                raise InvalidRequestError("Request has both MCP1 and MCP2 values")
            primary_nic = network_info.find(fixxpath('primaryNic', TYPES_URN))
            ipv4 = findtext(primary_nic, 'privateIpv4', TYPES_URN)
            vlanId = findtext(primary_nic, 'vlanId', TYPES_URN)
            if ipv4 is None and vlanId is None:
                raise InvalidRequestError('Invalid request MCP2 requests need privateIpv4 or vlanId')
        else:
            raise InvalidRequestError('Invalid request, does not have network or network_info in XML')

        body = self.fixtures.load(
            'server_deployServer.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_server_e75ead52_692f_4314_8725_c8a4f4d13a87(self, method, url, body, headers):
        body = self.fixtures.load(
            '2.4/server_server_e75ead52_692f_4314_8725_c8a4f4d13a87.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_deployNetworkDomain(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}deployNetworkDomain":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'network_deployNetworkDomain.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_networkDomain_8cdfd607_f429_4df6_9352_162cfc0891be(self, method, url, body, headers):
        body = self.fixtures.load(
            'network_networkDomain_8cdfd607_f429_4df6_9352_162cfc0891be.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_networkDomain_8cdfd607_f429_4df6_9352_162cfc0891be_ALLFILTERS(self, method, url, body, headers):
        body = self.fixtures.load(
            'network_networkDomain_8cdfd607_f429_4df6_9352_162cfc0891be.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_editNetworkDomain(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}editNetworkDomain":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'network_editNetworkDomain.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_deleteNetworkDomain(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}deleteNetworkDomain":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'network_deleteNetworkDomain.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_deployVlan(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}deployVlan":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'network_deployVlan.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_vlan_0e56433f_d808_4669_821d_812769517ff8(self, method, url, body, headers):
        body = self.fixtures.load(
            'network_vlan_0e56433f_d808_4669_821d_812769517ff8.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_editVlan(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}editVlan":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'network_editVlan.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_deleteVlan(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}deleteVlan":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'network_deleteVlan.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_expandVlan(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}expandVlan":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'network_expandVlan.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_addPublicIpBlock(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}addPublicIpBlock":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'network_addPublicIpBlock.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_publicIpBlock_4487241a_f0ca_11e3_9315_d4bed9b167ba(self, method, url, body, headers):
        body = self.fixtures.load(
            'network_publicIpBlock_4487241a_f0ca_11e3_9315_d4bed9b167ba.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_publicIpBlock(self, method, url, body, headers):
        body = self.fixtures.load(
            'network_publicIpBlock.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_publicIpBlock_9945dc4a_bdce_11e4_8c14_b8ca3a5d9ef8(self, method, url, body, headers):
        body = self.fixtures.load(
            'network_publicIpBlock_9945dc4a_bdce_11e4_8c14_b8ca3a5d9ef8.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_removePublicIpBlock(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}removePublicIpBlock":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'network_removePublicIpBlock.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_firewallRule(self, method, url, body, headers):
        body = self.fixtures.load(
            'network_firewallRule.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_createFirewallRule(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}createFirewallRule":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'network_createFirewallRule.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_firewallRule_d0a20f59_77b9_4f28_a63b_e58496b73a6c(self, method, url, body, headers):
        body = self.fixtures.load(
            'network_firewallRule_d0a20f59_77b9_4f28_a63b_e58496b73a6c.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_editFirewallRule(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}editFirewallRule":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'network_editFirewallRule.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_deleteFirewallRule(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}deleteFirewallRule":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'network_deleteFirewallRule.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_createNatRule(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}createNatRule":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'network_createNatRule.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_natRule(self, method, url, body, headers):
        body = self.fixtures.load(
            'network_natRule.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_natRule_2187a636_7ebb_49a1_a2ff_5d617f496dce(self, method, url, body, headers):
        body = self.fixtures.load(
            'network_natRule_2187a636_7ebb_49a1_a2ff_5d617f496dce.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_deleteNatRule(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}deleteNatRule":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'network_deleteNatRule.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_addNic(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}addNic":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'server_addNic.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_removeNic(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}removeNic":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'server_removeNic.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_disableServerMonitoring(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}disableServerMonitoring":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'server_disableServerMonitoring.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_enableServerMonitoring(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}enableServerMonitoring":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'server_enableServerMonitoring.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_changeServerMonitoringPlan(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}changeServerMonitoringPlan":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'server_changeServerMonitoringPlan.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_image_osImage(self, method, url, body, headers):
        body = self.fixtures.load(
            '2.4/image_osImage.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_image_osImage_c14b1a46_2428_44c1_9c1a_b20e6418d08c(self, method, url, body, headers):
        body = self.fixtures.load(
            '2.4/image_osImage_c14b1a46_2428_44c1_9c1a_b20e6418d08c.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_image_osImage_6b4fb0c7_a57b_4f58_b59c_9958f94f971a(self, method, url, body, headers):
        body = self.fixtures.load(
            '2.4/image_osImage_6b4fb0c7_a57b_4f58_b59c_9958f94f971a.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_image_osImage_5234e5c7_01de_4411_8b6e_baeb8d91cf5d(self, method, url, body, headers):
        body = self.fixtures.load(
            'image_osImage_BAD_REQUEST.xml')
        return (httplib.BAD_REQUEST, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_image_osImage_2ffa36c8_1848_49eb_b4fa_9d908775f68c(self, method, url, body, headers):
        body = self.fixtures.load(
            'image_osImage_BAD_REQUEST.xml')
        return (httplib.BAD_REQUEST, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_image_osImage_FAKE_IMAGE_ID(self, method, url, body, headers):
        body = self.fixtures.load(
            'image_osImage_BAD_REQUEST.xml')
        return (httplib.BAD_REQUEST, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_image_customerImage(self, method, url, body, headers):
        body = self.fixtures.load(
            '2.4/image_customerImage.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_image_customerImage_5234e5c7_01de_4411_8b6e_baeb8d91cf5d(self, method, url, body, headers):
        body = self.fixtures.load(
            '2.4/image_customerImage_5234e5c7_01de_4411_8b6e_baeb8d91cf5d.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_image_customerImage_2ffa36c8_1848_49eb_b4fa_9d908775f68c(self, method, url, body, headers):
        body = self.fixtures.load(
            '2.4/image_customerImage_2ffa36c8_1848_49eb_b4fa_9d908775f68c.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_image_customerImage_FAKE_IMAGE_ID(self, method, url, body, headers):
        body = self.fixtures.load(
            'image_customerImage_BAD_REQUEST.xml')
        return (httplib.BAD_REQUEST, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_reconfigureServer(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}reconfigureServer":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'server_reconfigureServer.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_cleanServer(self, method, url, body, headers):
        body = self.fixtures.load(
            'server_cleanServer.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_addDisk(self, method, url, body, headers):
        body = self.fixtures.load(
            'server_addDisk.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_removeDisk(self, method, url, body, headers):
        body = self.fixtures.load(
            'server_removeDisk.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_tag_createTagKey(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}createTagKey":
            raise InvalidRequestError(request.tag)
        name = findtext(request, 'name', TYPES_URN)
        description = findtext(request, 'description', TYPES_URN)
        value_required = findtext(request, 'valueRequired', TYPES_URN)
        display_on_report = findtext(request, 'displayOnReport', TYPES_URN)
        if name is None:
            raise ValueError("Name must have a value in the request")
        if description is not None:
            raise ValueError("Default description for a tag should be blank")
        if value_required is None or value_required != 'true':
            raise ValueError("Default valueRequired should be true")
        if display_on_report is None or display_on_report != 'true':
            raise ValueError("Default displayOnReport should be true")

        body = self.fixtures.load(
            'tag_createTagKey.xml'
        )
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_tag_createTagKey_ALLPARAMS(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}createTagKey":
            raise InvalidRequestError(request.tag)
        name = findtext(request, 'name', TYPES_URN)
        description = findtext(request, 'description', TYPES_URN)
        value_required = findtext(request, 'valueRequired', TYPES_URN)
        display_on_report = findtext(request, 'displayOnReport', TYPES_URN)
        if name is None:
            raise ValueError("Name must have a value in the request")
        if description is None:
            raise ValueError("Description should have a value")
        if value_required is None or value_required != 'false':
            raise ValueError("valueRequired should be false")
        if display_on_report is None or display_on_report != 'false':
            raise ValueError("displayOnReport should be false")

        body = self.fixtures.load(
            'tag_createTagKey.xml'
        )
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_tag_createTagKey_BADREQUEST(self, method, url, body, headers):
        body = self.fixtures.load(
            'tag_createTagKey_BADREQUEST.xml')
        return (httplib.BAD_REQUEST, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_tag_tagKey(self, method, url, body, headers):
        body = self.fixtures.load(
            'tag_tagKey_list.xml'
        )
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_tag_tagKey_SINGLE(self, method, url, body, headers):
        body = self.fixtures.load(
            'tag_tagKey_list_SINGLE.xml'
        )
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_tag_tagKey_ALLFILTERS(self, method, url, body, headers):
        (_, params) = url.split('?')
        parameters = params.split('&')
        for parameter in parameters:
            (key, value) = parameter.split('=')
            if key == 'id':
                assert value == 'fake_id'
            elif key == 'name':
                assert value == 'fake_name'
            elif key == 'valueRequired':
                assert value == 'false'
            elif key == 'displayOnReport':
                assert value == 'false'
            elif key == 'pageSize':
                assert value == '250'
            else:
                raise ValueError("Could not find in url parameters {0}:{1}".format(key, value))
        body = self.fixtures.load(
            'tag_tagKey_list.xml'
        )
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_tag_tagKey_d047c609_93d7_4bc5_8fc9_732c85840075(self, method, url, body, headers):
        body = self.fixtures.load(
            'tag_tagKey_5ab77f5f_5aa9_426f_8459_4eab34e03d54.xml'
        )
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_tag_tagKey_d047c609_93d7_4bc5_8fc9_732c85840075_NOEXIST(self, method, url, body, headers):
        body = self.fixtures.load(
            'tag_tagKey_5ab77f5f_5aa9_426f_8459_4eab34e03d54_BADREQUEST.xml'
        )
        return (httplib.BAD_REQUEST, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_tag_editTagKey_NAME(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}editTagKey":
            raise InvalidRequestError(request.tag)
        name = findtext(request, 'name', TYPES_URN)
        description = findtext(request, 'description', TYPES_URN)
        value_required = findtext(request, 'valueRequired', TYPES_URN)
        display_on_report = findtext(request, 'displayOnReport', TYPES_URN)
        if name is None:
            raise ValueError("Name must have a value in the request")
        if description is not None:
            raise ValueError("Description should be empty")
        if value_required is not None:
            raise ValueError("valueRequired should be empty")
        if display_on_report is not None:
            raise ValueError("displayOnReport should be empty")
        body = self.fixtures.load(
            'tag_editTagKey.xml'
        )
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_tag_editTagKey_NOTNAME(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}editTagKey":
            raise InvalidRequestError(request.tag)
        name = findtext(request, 'name', TYPES_URN)
        description = findtext(request, 'description', TYPES_URN)
        value_required = findtext(request, 'valueRequired', TYPES_URN)
        display_on_report = findtext(request, 'displayOnReport', TYPES_URN)
        if name is not None:
            raise ValueError("Name should be empty")
        if description is None:
            raise ValueError("Description should not be empty")
        if value_required is None:
            raise ValueError("valueRequired should not be empty")
        if display_on_report is None:
            raise ValueError("displayOnReport should not be empty")
        body = self.fixtures.load(
            'tag_editTagKey.xml'
        )
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_tag_editTagKey_NOCHANGE(self, method, url, body, headers):
        body = self.fixtures.load(
            'tag_editTagKey_BADREQUEST.xml'
        )
        return (httplib.BAD_REQUEST, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_tag_deleteTagKey(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}deleteTagKey":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'tag_deleteTagKey.xml'
        )
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_tag_deleteTagKey_NOEXIST(self, method, url, body, headers):
        body = self.fixtures.load(
            'tag_deleteTagKey_BADREQUEST.xml'
        )
        return (httplib.BAD_REQUEST, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_tag_applyTags(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}applyTags":
            raise InvalidRequestError(request.tag)
        asset_type = findtext(request, 'assetType', TYPES_URN)
        asset_id = findtext(request, 'assetId', TYPES_URN)
        tag = request.find(fixxpath('tag', TYPES_URN))
        tag_key_name = findtext(tag, 'tagKeyName', TYPES_URN)
        value = findtext(tag, 'value', TYPES_URN)
        if asset_type is None:
            raise ValueError("assetType should not be empty")
        if asset_id is None:
            raise ValueError("assetId should not be empty")
        if tag_key_name is None:
            raise ValueError("tagKeyName should not be empty")
        if value is None:
            raise ValueError("value should not be empty")

        body = self.fixtures.load(
            'tag_applyTags.xml'
        )
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_tag_applyTags_NOVALUE(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}applyTags":
            raise InvalidRequestError(request.tag)
        asset_type = findtext(request, 'assetType', TYPES_URN)
        asset_id = findtext(request, 'assetId', TYPES_URN)
        tag = request.find(fixxpath('tag', TYPES_URN))
        tag_key_name = findtext(tag, 'tagKeyName', TYPES_URN)
        value = findtext(tag, 'value', TYPES_URN)
        if asset_type is None:
            raise ValueError("assetType should not be empty")
        if asset_id is None:
            raise ValueError("assetId should not be empty")
        if tag_key_name is None:
            raise ValueError("tagKeyName should not be empty")
        if value is not None:
            raise ValueError("value should be empty")

        body = self.fixtures.load(
            'tag_applyTags.xml'
        )
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_tag_applyTags_NOTAGKEY(self, method, url, body, headers):
        body = self.fixtures.load(
            'tag_applyTags_BADREQUEST.xml'
        )
        return (httplib.BAD_REQUEST, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_tag_removeTags(self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}removeTags":
            raise InvalidRequestError(request.tag)
        body = self.fixtures.load(
            'tag_removeTag.xml'
        )
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_tag_removeTags_NOTAG(self, method, url, body, headers):
        body = self.fixtures.load(
            'tag_removeTag_BADREQUEST.xml'
        )
        return (httplib.BAD_REQUEST, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_tag_tag(self, method, url, body, headers):
        body = self.fixtures.load(
            'tag_tag_list.xml'
        )
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_tag_tag_ALLPARAMS(self, method, url, body, headers):
        (_, params) = url.split('?')
        parameters = params.split('&')
        for parameter in parameters:
            (key, value) = parameter.split('=')
            if key == 'assetId':
                assert value == 'fake_asset_id'
            elif key == 'assetType':
                assert value == 'fake_asset_type'
            elif key == 'valueRequired':
                assert value == 'false'
            elif key == 'displayOnReport':
                assert value == 'false'
            elif key == 'pageSize':
                assert value == '250'
            elif key == 'datacenterId':
                assert value == 'fake_location'
            elif key == 'value':
                assert value == 'fake_value'
            elif key == 'tagKeyName':
                assert value == 'fake_tag_key_name'
            elif key == 'tagKeyId':
                assert value == 'fake_tag_key_id'
            else:
                raise ValueError("Could not find in url parameters {0}:{1}".format(key, value))
        body = self.fixtures.load(
            'tag_tag_list.xml'
        )
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_ipAddressList(
            self, method, url, body, headers):
        body = self.fixtures.load('ip_address_lists.xml')
        return httplib.OK, body, {}, httplib.responses[httplib.OK]

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_ipAddressList_FILTERBYNAME(
            self, method, url, body, headers):
        body = self.fixtures.load('ip_address_lists_FILTERBYNAME.xml')
        return httplib.OK, body, {}, httplib.responses[httplib.OK]

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_createIpAddressList(
            self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}" \
                          "createIpAddressList":
            raise InvalidRequestError(request.tag)

        net_domain = findtext(request, 'networkDomainId', TYPES_URN)
        if net_domain is None:
            raise ValueError("Network Domain should not be empty")

        name = findtext(request, 'name', TYPES_URN)
        if name is None:
            raise ValueError("Name should not be empty")

        ip_version = findtext(request, 'ipVersion', TYPES_URN)
        if ip_version is None:
            raise ValueError("IP Version should not be empty")

        ip_address_col_required = findall(request, 'ipAddress', TYPES_URN)
        child_ip_address_required = findall(request, 'childIpAddressListId',
                                            TYPES_URN)

        if 0 == len(ip_address_col_required) and \
                0 == len(child_ip_address_required):
            raise ValueError("At least one ipAddress element or "
                             "one childIpAddressListId element must be "
                             "provided.")

        if ip_address_col_required[0].get('begin') is None:
            raise ValueError("IP Address should not be empty")

        body = self.fixtures.load(
            'ip_address_list_create.xml'
        )
        return httplib.OK, body, {}, httplib.responses[httplib.OK]

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_editIpAddressList(
            self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}" \
                          "editIpAddressList":
            raise InvalidRequestError(request.tag)

        ip_address_list = request.get('id')
        if ip_address_list is None:
            raise ValueError("IpAddressList ID should not be empty")

        name = findtext(request, 'name', TYPES_URN)
        if name is not None:
            raise ValueError("Name should not exists in request")

        ip_version = findtext(request, 'ipVersion', TYPES_URN)
        if ip_version is not None:
            raise ValueError("IP Version should not exists in request")

        ip_address_col_required = findall(request, 'ipAddress', TYPES_URN)
        child_ip_address_required = findall(request, 'childIpAddressListId',
                                            TYPES_URN)

        if 0 == len(ip_address_col_required) and \
                0 == len(child_ip_address_required):
            raise ValueError("At least one ipAddress element or "
                             "one childIpAddressListId element must be "
                             "provided.")

        if ip_address_col_required[0].get('begin') is None:
            raise ValueError("IP Address should not be empty")

        body = self.fixtures.load(
            'ip_address_list_edit.xml'
        )
        return httplib.OK, body, {}, httplib.responses[httplib.OK]

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_deleteIpAddressList(
            self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}" \
                          "deleteIpAddressList":
            raise InvalidRequestError(request.tag)

        ip_address_list = request.get('id')
        if ip_address_list is None:
            raise ValueError("IpAddressList ID should not be empty")

        body = self.fixtures.load(
            'ip_address_list_delete.xml'
        )

        return httplib.OK, body, {}, httplib.responses[httplib.OK]

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_portList(
            self, method, url, body, headers):
        body = self.fixtures.load(
            'port_list_lists.xml'
        )

        return httplib.OK, body, {}, httplib.responses[httplib.OK]

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_portList_c8c92ea3_2da8_4d51_8153_f39bec794d69(
            self, method, url, body, headers):
        body = self.fixtures.load(
            'port_list_get.xml'
        )

        return httplib.OK, body, {}, httplib.responses[httplib.OK]

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_createPortList(
            self, method, url, body, headers):

        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}" \
                          "createPortList":
            raise InvalidRequestError(request.tag)

        net_domain = findtext(request, 'networkDomainId', TYPES_URN)
        if net_domain is None:
            raise ValueError("Network Domain should not be empty")

        ports_required = findall(request, 'port', TYPES_URN)
        child_port_list_required = findall(request, 'childPortListId',
                                           TYPES_URN)

        if 0 == len(ports_required) and \
                0 == len(child_port_list_required):
            raise ValueError("At least one port element or one "
                             "childPortListId element must be provided")

        if ports_required[0].get('begin') is None:
            raise ValueError("PORT begin value should not be empty")

        body = self.fixtures.load(
            'port_list_create.xml'
        )

        return httplib.OK, body, {}, httplib.responses[httplib.OK]

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_editPortList(
            self, method, url, body, headers):

        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}" \
                          "editPortList":
            raise InvalidRequestError(request.tag)

        ports_required = findall(request, 'port', TYPES_URN)
        child_port_list_required = findall(request, 'childPortListId',
                                           TYPES_URN)

        if 0 == len(ports_required) and \
                0 == len(child_port_list_required):
            raise ValueError("At least one port element or one "
                             "childPortListId element must be provided")

        if ports_required[0].get('begin') is None:
            raise ValueError("PORT begin value should not be empty")

        body = self.fixtures.load(
            'port_list_edit.xml'
        )

        return httplib.OK, body, {}, httplib.responses[httplib.OK]

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_network_deletePortList(
            self, method, url, body, headers):
        request = ET.fromstring(body)
        if request.tag != "{urn:didata.com:api:cloud:types}" \
                          "deletePortList":
            raise InvalidRequestError(request.tag)

        port_list = request.get('id')
        if port_list is None:
            raise ValueError("Port List ID should not be empty")

        body = self.fixtures.load(
            'ip_address_list_delete.xml'
        )

        return httplib.OK, body, {}, httplib.responses[httplib.OK]

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_cloneServer(
            self, method, url, body, headers):
        body = self.fixtures.load(
            '2.4/server_clone_response.xml'
        )
        return httplib.OK, body, {}, httplib.responses[httplib.OK]

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_image_importImage(
            self, method, url, body, headers):
        body = self.fixtures.load(
            '2.4/import_image_response.xml'
        )
        return httplib.OK, body, {}, httplib.responses[httplib.OK]

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_exchangeNicVlans(
            self, method, url, body, headers):
        body = self.fixtures.load(
            '2.4/exchange_nic_vlans_response.xml'
        )
        return httplib.OK, body, {}, httplib.responses[httplib.OK]

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_changeNetworkAdapter(
            self, method, url, body, headers):
        body = self.fixtures.load(
            '2.4/change_nic_networkadapter_response.xml'
        )
        return httplib.OK, body, {}, httplib.responses[httplib.OK]

    def _caas_2_4_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_deployUncustomizedServer(
            self, method, url, body, headers):
        body = self.fixtures.load(
            '2.4/deploy_customised_server.xml'
        )
        return httplib.OK, body, {}, httplib.responses[httplib.OK]

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87_backup_client_type(self, method, url, body, headers):
        body = self.fixtures.load(
            '_backup_client_type.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87_backup_client_storagePolicy(
            self, method, url, body, headers):
        body = self.fixtures.load(
            '_backup_client_storagePolicy.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87_backup_client_schedulePolicy(
            self, method, url, body, headers):
        body = self.fixtures.load(
            '_backup_client_schedulePolicy.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87_backup_client(
            self, method, url, body, headers):
        if method == 'POST':
            body = self.fixtures.load(
                '_backup_client_SUCCESS_PUT.xml')
            return (httplib.OK, body, {}, httplib.responses[httplib.OK])
        else:
            raise ValueError("Unknown Method {0}".format(method))

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87_backup_NOCLIENT(
            self, method, url, body, headers):
        # only gets here are implemented
        # If we get any other method something has gone wrong
        assert(method == 'GET')
        body = self.fixtures.load(
            '_backup_INFO_NOCLIENT.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87_backup_DISABLED(
            self, method, url, body, headers):
        # only gets here are implemented
        # If we get any other method something has gone wrong
        assert(method == 'GET')
        body = self.fixtures.load(
            '_backup_INFO_DISABLED.xml')
        return (httplib.BAD_REQUEST, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87_backup_NOJOB(
            self, method, url, body, headers):
        # only gets here are implemented
        # If we get any other method something has gone wrong
        assert(method == 'GET')
        body = self.fixtures.load(
            '_backup_INFO_NOJOB.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87_backup_DEFAULT(
            self, method, url, body, headers):
        if method != 'POST':
            raise InvalidRequestError('Only POST is accepted for this test')
        request = ET.fromstring(body)
        service_plan = request.get('servicePlan')
        if service_plan != DEFAULT_BACKUP_PLAN:
            raise InvalidRequestError('The default plan %s should have been passed in.  Not %s' % (DEFAULT_BACKUP_PLAN, service_plan))
        body = self.fixtures.load(
            '_backup_ENABLE.xml')
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87_backup(
            self, method, url, body, headers):
        if method == 'POST':
            body = self.fixtures.load(
                '_backup_ENABLE.xml')
            return (httplib.OK, body, {}, httplib.responses[httplib.OK])
        elif method == 'GET':
            if url.endswith('disable'):
                body = self.fixtures.load(
                    '_backup_DISABLE.xml')
                return (httplib.OK, body, {}, httplib.responses[httplib.OK])
            body = self.fixtures.load(
                '_backup_INFO.xml')
            return (httplib.OK, body, {}, httplib.responses[httplib.OK])

        else:
            raise ValueError("Unknown Method {0}".format(method))

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87_backup_EXISTS(
            self, method, url, body, headers):
        # only POSTs are implemented
        # If we get any other method something has gone wrong
        assert(method == 'POST')
        body = self.fixtures.load(
            '_backup_EXISTS.xml')
        return (httplib.BAD_REQUEST, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87_backup_modify(
            self, method, url, body, headers):
        request = ET.fromstring(body)
        service_plan = request.get('servicePlan')
        if service_plan != 'Essentials':
            raise InvalidRequestError("Expected Essentials backup plan in request")
        body = self.fixtures.load('_backup_modify.xml')

        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87_backup_modify_DEFAULT(
            self, method, url, body, headers):
        request = ET.fromstring(body)
        service_plan = request.get('servicePlan')
        if service_plan != DEFAULT_BACKUP_PLAN:
            raise InvalidRequestError("Expected % backup plan in test" % DEFAULT_BACKUP_PLAN)
        body = self.fixtures.load('_backup_modify.xml')

        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87_backup_client_30b1ff76_c76d_4d7c_b39d_3b72be0384c8(
            self, method, url, body, headers):
        if url.endswith('disable'):
            body = self.fixtures.load(
                ('_remove_backup_client.xml')
            )
        elif url.endswith('cancelJob'):
            body = self.fixtures.load(
                (''
                 '_backup_client_30b1ff76_c76d_4d7c_b39d_3b72be0384c8_cancelJob.xml')
            )
        else:
            raise ValueError("Unknown URL: %s" % url)
        return (httplib.OK, body, {}, httplib.responses[httplib.OK])

    def _oec_0_9_8a8f6abc_2745_4d8a_9cbc_8dabe5a7d0e4_server_e75ead52_692f_4314_8725_c8a4f4d13a87_backup_client_30b1ff76_c76d_4d7c_b39d_3b72be0384c8_FAIL(
            self, method, url, body, headers):
        if url.endswith('disable'):
            body = self.fixtures.load(
                ('_remove_backup_client_FAIL.xml')
            )
        elif url.endswith('cancelJob'):
            body = self.fixtures.load(
                (''
                 '_backup_client_30b1ff76_c76d_4d7c_b39d_3b72be0384c8_cancelJob_FAIL.xml')
            )
        else:
            raise ValueError("Unknown URL: %s" % url)
        return (httplib.BAD_REQUEST, body, {}, httplib.responses[httplib.OK])
