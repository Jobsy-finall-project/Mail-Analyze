from src.Analyze import analyze


def test_analyze():
    res = analyze("yohai, Ruby on rails, java")
    assert "Ruby" in res
    assert "Java" in res
    assert "Ruby on Rails" in res
    assert "JavaScript" not in res


def test_analyze_2():
    res = analyze("yohai, Ruby, Ruby on rails, javascript")
    assert "Ruby" in res
    assert "Ruby on Rails" in res
    assert "JavaScript" in res
    assert "Java" not in res
