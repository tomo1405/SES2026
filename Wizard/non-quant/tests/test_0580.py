python
import pytest
from src_0580 import task_func

def test_task_func_valid_csv():
    csv_file = "test_data.csv"
    try:
        with open(csv_file, 'w') as file:
            file.write("word1,word2,word3\n")
            file.write("apple,banana,cherry\n")
            file.write("orange,pear,grape\n")
            file.write("kiwi,mango,peach\n")
            file.write("pineapple,quince,raspberry\n")
        ax, most_common_words = task_func(csv_file)
        assert ax is not None
        assert most_common_words is not None
        assert len(most_common_words) == 10
        assert most_common_words[0][0] == "pineapple"
        assert most_common_words[1][0] == "quince"
        assert most_common_words[2][0] == "raspberry"
        assert most_common_words[3][0] == "apple"
        assert most_common_words[4][0] == "banana"
        assert most_common_words[5][0] == "cherry"
        assert most_common_words[6][0] == "orange"
        assert most_common_words[7][0] == "pear"
        assert most_common_words[8][0] == "grape"
        assert most_common_words[9][0] == "kiwi"
        plt.close()
    finally:
        try:
            with open(csv_file, 'w') as file:
                file.write("")
        except:
            pass

def test_task_func_invalid_csv():
    csv_file = "invalid_file.csv"
    with pytest.raises(FileNotFoundError):
        task_func(csv_file)

def test_task_func_invalid_csv_io():
    csv_file = "invalid_file.csv"
    with open(csv_file, 'w') as file:
        file.write("word1,word2,word3\n")
        file.write("apple,banana,cherry\n")
        file.write("orange,pear,grape\n")
        file.write("kiwi,mango,peach\n")
        file.write("pineapple,quince,raspberry\n")
    with pytest.raises(IOError):
        task_func(csv_file)
    try:
        with open(csv_file, 'w') as file:
            file.write("")
    except:
        pass