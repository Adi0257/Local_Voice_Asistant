from app.core.pipeline import run_pipeline

def test_query():
    result = run_pipeline("What is this document about?")
    assert "answer" in result
