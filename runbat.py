import subprocess

n = 4  # 运行次数
vina_path = r"H:\DESK2\Vina-GPU-2.0-main\Vina-GPU+\Vina-GPU+.exe"  # Vina可执行文件的路径
config_file = r"H:\DESK2\Vina-GPU-2.0-main\Vina-GPU+\input_file_example\config1.txt"  # Vina配置文件的路径
input_file_name = r"H:\DESK2\Vina-GPU-2.0-main\Vina-GPU+\test"  # Vina输入文件夹名的路径

for i in range(n):
    output_file = f"H:\DESK2\Vina-GPU-2.0-main\Vina-GPU+\out_{i+1} "  # 输出文件的路径
    command = f"{vina_path} --config={config_file} --ligand_directory {input_file_name}\{i+1} --output_directory {output_file} --log log{i+1}.txt"
    subprocess.call(command, shell=True)
