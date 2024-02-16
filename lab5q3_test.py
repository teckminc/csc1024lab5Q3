import lab5q3
from io import StringIO
from sys import stderr
def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('2.1\n4.5\n3.2\n5.7\n1.1\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab5q3.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'[1.1, 2.1, 3.2, 4.5, 5.7]') != -1

def test_case2(monkeypatch, capsys):
  with open(f"lab5q3.py") as tf:
    head = [next(tf) for _ in range(18)]
    s = tf.read()
    assert(s.find("while") != -1 )

def test_case3(monkeypatch, capsys):
  with open(f"lab5q3.py") as tf:
    head = [next(tf) for _ in range(18)]
    s = tf.read()
    assert(s.find("my_list") != -1 )

def test_case4(monkeypatch, capsys):
    number_inputs = StringIO('2.1\n4.5\n3.2\n5.7\n1.1\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab5q3.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'[5.7, 4.5, 3.2, 2.1, 1.1]') != -1


def test_case5(monkeypatch, capsys):
  with open(f"lab5q3.py") as tf:
    head = [next(tf) for _ in range(18)]
    s = tf.read()
    assert(s.find("reverse(") == -1 )