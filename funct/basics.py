def configure_intf(intf_name, ip, mask):
    '''Функция генерирует конфигурацию интерфейса
    config_intf и config_ip - локальные переменные и недоступна за пределами функции'''
    config_intf = f'interface {intf_name}\n'
    config_ip = f'ip address {ip} {mask}'
    return config_intf, config_ip


if __name__ == '__main__':
    result = configure_intf('Fa0/0', '10.1.1.1', '255.255.255.0')
    print(result)
    intf, ip_addr = configure_intf('Fa0/0', '10.1.1.1', '255.255.255.0')
    print(intf)
    print(ip_addr)
