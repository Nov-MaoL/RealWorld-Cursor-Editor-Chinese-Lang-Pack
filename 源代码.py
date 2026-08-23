# -*- coding: utf-8 -*-
import os
import sys

def get_appdata():
    return os.environ.get('APPDATA', '')

def get_resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

def install():
    print("=" * 40)
    print("  RealWorld Cursor Editor 中文语言包")
    print("=" * 40)
    print()

    target_dir = os.path.join(get_appdata(), 'RealWorld', 'RWCursorEditor')
    os.makedirs(target_dir, exist_ok=True)

    src = get_resource_path('0804.po')
    dst = os.path.join(target_dir, '0804.po')

    if not os.path.exists(src):
        print("错误：未找到 0804.po 资源文件！")
        input("\n按回车键退出...")
        return 1

    try:
        with open(src, 'rb') as f:
            data = f.read()
        with open(dst, 'wb') as f:
            f.write(data)
        print(f"安装成功！")
        print(f"安装位置：{dst}")
        print("\n请重启 RealWorld Cursor Editor 以生效。")
    except Exception as e:
        print(f"安装失败：{e}")
        print("请以管理员身份运行。")
        input("\n按回车键退出...")
        return 1

    input("\n按回车键退出...")
    return 0

if __name__ == '__main__':
    sys.exit(install())
