import subprocess

def test_desktop():
    subprocess.check_call(["python3", "-m", "core_apps.desktop.src.main"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)