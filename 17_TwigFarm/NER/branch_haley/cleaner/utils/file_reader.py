import os.path


def read_file(file_obj, is_server):
    raw_text = ''

    try:
        if is_server:
            file_obj.seek(0)
            raw_text = file_obj.read().decode('utf-8')
        else:
            print('file existed', os.path.isfile(file_obj))
            with open(file_obj, encoding='utf-8') as local_file:
                raw_text = local_file.read()
    except OSError as e:
        print('error read_file')
        print(e)

    return raw_text
    # print('read_file', raw_text)
    # return '{ \"labelNew\": \"N\"}'
