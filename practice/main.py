

from common import transpose, first, groupby,cat
import unittest



if __name__ == '__main__':
  
    assert tuple(transpose(((1, 2, 3), (4, 5, 6)))) == ((1, 4), (2, 5), (3, 6))
    assert first('abc') == first(['a', 'b', 'c']) == 'a'
    assert cat(['a', 'b', 'c']) == 'abc'
    assert (groupby(['test', 'one', 'two', 'three', 'four'], key=len) 
        == {3: ['one', 'two'], 4: ['test', 'four'], 5: ['three']})
    unittest.main()
    
  
