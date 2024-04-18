import os
import subprocess

def convert_ui_to_py(ui_dir, py_dir):
    if not os.path.exists(ui_dir):
        print(f"Diretório '{ui_dir}' não encontrado")
        return
    
    if not os.path.exists(py_dir):
        os.makedirs(py_dir)
        
    for file_name in os.listdir(ui_dir):
        if file_name.endswith('.ui'):
            ui_path = os.path.join(ui_dir, file_name)
            py_path = os.path.join(py_dir, os.path.splitext(file_name)[0] + '.py')
            subprocess.run(['pyuic6', '-x', ui_path, '-o', py_path])
            print(f"Arquivo '{file_name}' convertido com sucesso para '{os.path.basename(py_path)}'.")
