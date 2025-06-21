import subprocess


subprocess.run(
    ["C:/Python27/python.exe", "nao_speak.py"],
    input="HOLA SOY NAO",
    capture_output=False,  # Captura stdout y stderr
    text=True,
    timeout=10  # Opcional: evita que se congele si hay problemas
)