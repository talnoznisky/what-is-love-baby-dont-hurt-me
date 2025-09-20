import subprocess, sys

def test_success():
    cp = subprocess.run([sys.executable, "-m", "wut", "is", "luv"],
                        capture_output=True, text=True)
    assert cp.returncode == 0, cp.stderr
    assert "dont hurt me" in cp.stdout.lower()

def test_fail():
    cp = subprocess.run([sys.executable, "-m", "wut", "is", "ham"],
                        capture_output=True, text=True)
    assert cp.returncode == 2, cp.stderr
    assert "dont hurt me" not in cp.stdout.lower()
