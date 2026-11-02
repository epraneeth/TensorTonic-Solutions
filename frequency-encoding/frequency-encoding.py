def frequency_encoding(values: list) -> list:
    """
    Returns the relative frequency of every input value.
    """
    l=len(values)
    d={}
    for i in values:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    ans=[]
    for j in values:
        ans.append(d[j])
    x = [count/l for count in ans ]
    return x
        
        
        