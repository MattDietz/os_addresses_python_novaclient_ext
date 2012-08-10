# Copyright 2011 OpenStack, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from novaclient import base
from novaclient import utils


class Address(base.Resource):
    def delete(self):
        self.manager.delete(network=self)


class AddressManager(base.ManagerWithFind):
    resource_class = base.Resource

    def create(self, network_id, instance_id):
        body = {'address': {'network_id': network_id,
                            'instance_id': instance_id}}
        return self._create('/os-addresses', body, 'address')


@utils.arg('network_id', metavar='<network_id>',
           help='Network ID to add an IP address from')
@utils.arg('instance_id', metavar='<instance_id>',
           help="Instance to adding an IP to")
def do_address_create(cs, args):
    """
    Add a new address to an instance
    """
    addresses = cs.os_addresses_python_novaclient_ext.create(args.network_id,
                                                             args.instance_id)
    utils.print_dict(addresses._info)
