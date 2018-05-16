def change_tag_value(tag_name, tag_value, new_value, process_file_path, new_file):
    """
    :param tag_name: tag name to change
    :param tag_value: new value to change
    :param process_file_path: file to rewrite
    :param new_file: name of rewrited file
    """
    open_tag = '<{}>'.format(tag_name)
    close_tag = '</{}>'.format(tag_name)
    new_line = '{}{}{}\n'.format(open_tag, new_value, close_tag)

    file1 = open(process_file_path, 'r')
    content = file1.readlines()

    file1 = open(new_file, 'w')
    for i, line in enumerate(content):
        index = line.find(open_tag + tag_value)
        if index == -1:
            file1.write(line)
        else:
            if 'diffuse' in content[i + 1]:
                file1.write(line[:index] + new_line +
                            line[:index] + '<diffuse>0.9 0.9 0.9 1</diffuse>')
            else:
                file1.write(line[:index] + new_line)


if __name__ == "__main__":
    tag_name = 'name'
    tag_value = 'Gazebo/White'
    new_value = 'Gazebo/Grey'
    change_tag_value(tag_name, tag_value, new_value,
                     'ucu.world', 'ucu.world')
