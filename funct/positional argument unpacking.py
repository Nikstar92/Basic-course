def config_interface(intf_name, ip_address, mask):
    interface = f'interface {intf_name}'
    ip_addr = f'ip address {ip_address} {mask}'
    result = [interface, ip_addr]
    return result


if __name__ == '__main__':
    print(config_interface('Fa0/0', '10.1.1.1', '255.255.255.0'))
    '''Передаем список из кортежей'''
    interfaces_info = [('Fa0/1', '10.0.1.1', '255.255.255.0'),
                       ('Fa0/2', '10.0.2.1', '255.255.255.0'),
                       ('Fa0/3', '10.0.3.1', '255.255.255.0'),
                       ('Fa0/4', '10.0.4.1', '255.255.255.0'),
                       ('Lo0', '10.0.0.1', '255.255.255.255')]
    for info in interfaces_info:
        '''Распаковка позиоционных аргумента через *'''
        print(config_interface(*info))
