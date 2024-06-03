import os
import shutil


def execute():
    local = '../uploads/'
    destino = '../data/raw/'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    exit(0)

    for file in os.listdir(local):
        print(file)
        if file.endswith('.txt'):
            name_file = os.path.splitext(file)[0]
            os.makedirs(name_file, exist_ok=True)
            with open(os.path.join(root, file), 'r') as f:
                linhas = f.readlines()

            for l in linhas:
                file_part = l.strip()
                if os.path.exists(file_part):
                    shutil.move(
                        file_part,
                        os.path.join(name_file, os.path.basename(file_part)))

            if os.path.exists(os.path.join(destino, name_file)):
                shutil.rmtree(os.path.join(destino, name_file))

            shutil.copytree(name_file, destino)


if __name__ == '__main__':
    execute()
