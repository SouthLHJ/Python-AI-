dict = {'2017' : 'Transformer', '2018' : 'BERT'}

print(dict['2017'])

def Attention(Q,K,V) :     
    """
    Attention(Q, K, V) = Attention Value
    Q = Query : t 시점의 디코더 셀에서의 은닉 상태
    K = Keys : 모든 시점의 인코더 셀의 은닉 상태들
    V = Values : 모든 시점의 인코더 셀의 은닉 상태들
    """
    return (Q,K,V)
