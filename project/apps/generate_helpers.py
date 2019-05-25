import io
import os
import zipfile

from jinja2 import Environment, FileSystemLoader, Template

from ..utils import jalali_time, get_current_timestamp

HERE = THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_template(tmp_name, tmp_location=HERE):
    jalali_date = jalali_time
    env = Environment(
        loader=FileSystemLoader(HERE))
    env.filters['jalali_date'] = jalali_date  #defined jalali_date as a filter
    template = env.get_template(tmp_name)
    return template


def make_template(posts, template_file="blank_templates/template.html"):
    return get_template(tmp_name=template_file).render(posts=posts)



def write_template(data, path):
    try:
        with open(path + 'index.html', "w") as template:
            template.write(data)
    except Exception as e:
        raise


def render_template(posts, export_path):
    template = make_template(posts=posts)
    write_template(data=template, path=export_path)
    return True


def retrieve_file_paths(dirname):
    path_list = list()
    for root, directories, files in os.walk(dirname):
        for filename in files:
            filePath = os.path.join(root, filename)
            path_list.append(filePath)
            print(filePath)
    return path_list


def zip_file_func(dir_path):
    file_paths = retrieve_file_paths(dirname=dir_path)
    cur_time = get_current_timestamp()
    zip_path = dir_path + f'export-{cur_time}' + '.zip'
    zip_file = zipfile.ZipFile(zip_path, 'w')
    with zip_file:
        for file in file_paths:
            zip_file.write(file)
    return zip_file.filename


def copy_blank_media(dir_path, curr_path,
                     media_path="project/media/blank_media/"):
    import shutil

    media = os.path.join(curr_path, media_path)
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
    shutil.copytree(src=media, dst=dir_path)


def copy_thumbs(posts, dest):
    import shutil, os
    from ..config import upload_path

    dst = dest + '/media/images/'
    for post in posts:
        if post.thumb:
            src = os.path.join(upload_path + post.thumb)
            if not os.path.exists(dst):
                os.makedirs(name=dst)
            shutil.copy2(src, dst + post.thumb)