# file_sorter.py
# 自用文件分类小工具 - 按后缀名自动整理文件
import os
import shutil

def sort_files(path='./'):
    # 分类规则
    file_types = {
        '图片': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'],
        '文档': ['.doc', '.docx', '.pdf', '.txt', '.md', '.xlsx', '.ppt'],
        '代码': ['.py', '.java', '.c', '.cpp', '.html', '.css', '.js'],
        '压缩包': ['.zip', '.rar', '.7z', '.tar'],
        '视频': ['.mp4', '.mov', '.avi', '.mkv'],
        '音乐': ['.mp3', '.flac', '.wav']
    }

    # 遍历目录文件
    for f in os.listdir(path):
        file_path = os.path.join(path, f)
        if os.path.isfile(file_path):
            ext = os.path.splitext(f)[1].lower()
            # 匹配分类
            for folder, exts in file_types.items():
                if ext in exts:
                    target_folder = os.path.join(path, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, f))
                    print(f'已移动：{f} -> {folder}')
                    break

if __name__ == '__main__':
    print("=== 文件自动分类工具 ===")
    sort_files()
    print("整理完成！")