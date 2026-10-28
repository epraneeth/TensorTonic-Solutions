import numpy as np

def chi2_independence(C: list) -> dict:
    """
    Returns a dictionary with chi2 and expected.
    """
    CC = np.array(C)
    ans={"chi2":0.0,"expected":[]}
    N=len(C[0])
    Rows=np.sum(CC,axis=1,keepdims=True)
    Cols=np.sum(CC,axis=0,keepdims=True)
    G=np.sum(CC)

    expected = (Rows@Cols)/G
    ans["expected"]=expected

    chi = np.sum(((CC-expected)**2)/expected)
    ans["chi2"]=float(chi)
    return ans
    