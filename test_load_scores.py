from load_scores import load_scores
def test_정상_파일을_읽는다():
    kept, skipped = load_scores("scores.csv")
    assert len(kept) == 5

def test_빈_줄은_건너뛴다():
    kept, skipped = load_scores("scores.csv")
    assert len(kept) == 5

def test_이름에_쉼표가_있어도_읽는다():
    kept, skipped = load_scores("scores.csv")
    assert len(kept) == 5

import pytest
def test_없는_파일이면_오류가_난다():
    with pytest.raises(FileNotFoundError): # 예상한 에러가 일어나면 테스트 통과함.
        load_scores("없는파일.csv")
