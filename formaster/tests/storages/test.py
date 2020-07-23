def myfunc():
    return 2

def test_mything(snapshot):
    return_value = myfunc()
    assert return_value==2
    snapshot.assert_match(return_value,'gpg_response')
    
def suming(a,b):
    sum = a+b
    return sum
    
def test_summing(snapshot):
    a=10
    b=13
    return_value = suming(a,b)
    assert return_value==23
    snapshot.assert_match(return_value,'gpg_response')
    