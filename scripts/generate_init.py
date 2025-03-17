import os

def generate_init_file(directory):
    """自動生成 `__init__.py`，匯入所有模組內的可用變數、函式和類別"""
    init_file_path = os.path.join(directory, "__init__.py")
    module_names = [
        f[:-3] for f in os.listdir(directory) 
        if f.endswith(".py") and f != "__init__.py"
    ]

    imports = []
    for module in module_names:
        module_path = f".{module}"
        imports.append(f"from {module_path} import *")

    with open(init_file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(imports) + "\n")

    print(f"✅ 生成 {init_file_path}")

def auto_generate_init(root_dir):
    """自動遍歷專案，為每個子目錄生成 `__init__.py`"""
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if any(f.endswith(".py") for f in filenames):  # 只有含有 .py 檔案的目錄才建立 __init__.py
            generate_init_file(dirpath)

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.abspath(__file__))  # 設定當前專案根目錄
    auto_generate_init(project_root)