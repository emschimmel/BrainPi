import consul


def main():
    c = consul.Consul(host='localhost')

    c.kv.put('mykey', 'myvalue')
    index, data = c.kv.get('mykey')

    print('index: {0}  data: {1}'.format(index, data))

    # To delete the key
    # c.kv.delete('mykey')


if __name__ == "__main__":
    main()