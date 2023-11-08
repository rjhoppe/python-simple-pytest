import main

def test_main(capsys):
  main.main(['Rick'])

  out, err = capsys.readouterr()
  assert out == 'Hello, Rick\n'
  assert err == ''

def test_main_error_with_empty_string(capsys):
  assert main.main([''])

  out, err = capsys.readouterr()
  assert out == ''
  assert err == "Person's name must not be empty!\n"
