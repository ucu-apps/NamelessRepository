def change_tag_value(tag_name, tag_value, process_file_path, new_file):
    """
    :param tag_name: tag name to change
    :param tag_value: new value to change
    :param process_file_path: file to rewrite
    :param new_file: name of rewrited file
    """
    open_tag = '<{}>'.format(tag_name)
    close_tag = '</{}>'.format(tag_name)
    new_line = '{} {} {}\n'.format(open_tag, tag_value, close_tag)

    with open(process_file_path, 'r', errors='ignore') as file:
        content = file.readlines()

    with open(new_file, 'w', errors='ignore') as file:
        for line in content:
            index = line.find(open_tag)
            if index == -1:
                file.write(line)
            else:
                file.write(line[:index] + new_line)


if __name__ == "__main__":
    tag_name = 'ambient'
    tag_value = '0.3 0.3 0.3 1'
    change_tag_value(tag_name, tag_value, 'ucu.world', 'ucu_1.world')
