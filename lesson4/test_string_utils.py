
from string_utils import StringUtils

def test_capitilize():
    string_utils = StringUtils()
    assert string_utils.capitilize("skypro") == "Skypro"
    assert string_utils.capitilize("SkyPro") == "Skypro"
    assert string_utils.capitilize("") == ""

def test_trim():
    string_utils = StringUtils()
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("skypro") == "skypro"
    assert string_utils.trim("   ") == ""
    assert string_utils.trim("") == ""

def test_to_list():
    string_utils = StringUtils()
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert string_utils.to_list("1:2:3", ":") == ["1", "2", "3"]
    assert string_utils.to_list("", ",") == []
    assert string_utils.to_list("a,,c", ",") == ["a", "", "c"]

def test_contains():
    string_utils = StringUtils()
    assert string_utils.contains("SkyPro", "S") is True
    assert string_utils.contains("SkyPro", "U") is False
    assert string_utils.contains("", "U") is False

def test_delete_symbol():
    string_utils = StringUtils()
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert string_utils.delete_symbol("SkyPro", "X") == "SkyPro"

def test_starts_with():
    string_utils = StringUtils()
    assert string_utils.starts_with("SkyPro", "S") is True
    assert string_utils.starts_with("SkyPro", "P") is False
    assert string_utils.starts_with("", "S") is False

def test_end_with():
    string_utils = StringUtils()
    assert string_utils.end_with("SkyPro", "o") is True
    assert string_utils.end_with("SkyPro", "y") is False
    assert string_utils.end_with("", "o") is False

def test_is_empty():
    string_utils = StringUtils()
    assert string_utils.is_empty("") is True
    assert string_utils.is_empty(" ") is True
    assert string_utils.is_empty("SkyPro") is False

def test_list_to_string():
    string_utils = StringUtils()
    assert string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert string_utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert string_utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
    assert string_utils.list_to_string([]) == ""
