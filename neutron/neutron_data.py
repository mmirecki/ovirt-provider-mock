'''

Entity data for the current mock sessions

'''

# id: network
networks = {
    'network_id_1': {
        'id': 'network_id_1',
        'name': 'public'
    },
    'network_id_2': {
        'id': 'network_id_2',
        'name': 'private'
    },
}

subnets = {
    'subnet_id_1': {
        'id': 'subnet_id_1',
        'name': 'public_subnet',
        'network_id': 'network_id_1',
        'ip_version': 4,
        'cidr': '10.0.0.0/24',
        'gateway_ip': '10.0.0.1',
        'dns_nameservers': ['8.8.8.8']
    }

}


ports = {}
