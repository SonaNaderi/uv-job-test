from uv_job_test import main


def test_main_prints_greeting(capsys) -> None:
    main()

    captured = capsys.readouterr()
    assert captured.out == "Hello from uv-job-test!\n"
    assert captured.err == ""
