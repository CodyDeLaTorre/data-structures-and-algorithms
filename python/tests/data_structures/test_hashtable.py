import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable

# create an instance of the hash table
ht = Hashtable()

def test_set():
    # test setting a key/value
    ht.set("key1", "value1")
    assert ht.get("key1") == "value1"

def test_get():
    # test retrieving a value based on a key
    ht.set("key2", "value2")
    assert ht.get("key2") == "value2"

def test_get_null():
    # test returning null for a key that doesn't exist
    assert ht.get("key3") is None

def test_keys():
    # test getting a list of all unique keys
    ht.set("key3", "value3")
    assert ht.keys() == ["key1", "key2", "key3"]

def test_collision():
    # test handling a collision
    ht.set("key4", "value4")
    ht.set("key14", "value14")
    assert ht.get("key4") == "value4"
    assert ht.get("key14") == "value14"

def test_collision_bucket():
    # test retrieving a value from a bucket with a collision
    assert ht.get("key4") == "value4"


def test_hash():
    # test hashing a key to an in-range value
    assert ht.hash("key1") == 1

@pytest.mark.skip("TODO")
# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected
