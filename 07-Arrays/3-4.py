def f():
    a = [-15,8,-31,-2,19]
    m_ax = a[0]
    m_in = a[0]
    
    for i in range(1,len(a)):
        if a[i] > m_ax:
            m_ax = a[i]
        if a[i] < m_in:
            m_in = a[i]
            
    return m_ax,m_in

print(f())