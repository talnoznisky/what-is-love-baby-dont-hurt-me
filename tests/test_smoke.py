import subprocess, sys

def test_cli_via_module():
    cp = subprocess.run([sys.executable, "-m", "what", "is", "love"],
                        capture_output=True, text=True)
    assert cp.returncode == 0, cp.stderr
    assert "don't hurt me" in cp.stdout.lower()
