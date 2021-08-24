# decoder
这是一个解析system verilog 组合逻辑电路的项目
将要分析的代码写在一个文件中，例如：
"""
assign a = b[0]&(~(( b[1]// 注释文本
                            |b[3] ) &b[4]
                            |1'b0)|adgn);
            assign  s = ~a | b[3] &(a154[555])|k;
"""
然后执行脚本：
"""python .\decoder.py -f <文件>"""
可以得到这样的输出：
"""
a
|a154_555_
||adgn    
|||b_0_   
||||b_1_  
|||||b_3_ 
||||||b_4_
|||||||k
||||||||    a
||||||||    |s
---1--0-    1-
---100--    1-
--11----    1-
-------1    -1
-1---1--    -1
0-------    -1
"""
