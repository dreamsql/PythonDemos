from common import Input, transpose,cat
from collections import Counter


if __name__ == '__main__':


   data = Input(6).read().split()

   t_data = [col for col in transpose(data)]
   couters = [Counter(m) for m in t_data]

   frequenc_items = [m.most_common(1)[0][0] for m in couters]

   print(cat(frequenc_items))
