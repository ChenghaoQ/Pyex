"""
1.! x,'y,'z'='6,'5,'4'
2.! if'x'<'y:'
3.! ''''small'='x'
4.! ''''if'z'<'small:'
5.! ''''''''small'='z'
6.! elif'y'<'z:'
7.! ''''small'='y'
8.! else:'
9.! ''''small'='z
"""
＃使用三元操作符
x,y,z=6,5,4
small=x if (x<y and x<z) else (y if y<z else z)
