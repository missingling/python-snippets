from subprocess import check_output

def MakeFile(file_name):
    command = 'copy NUL'
    check_output(command + ' ' + file_name, shell = True)

MakeFile('.gitignore')
