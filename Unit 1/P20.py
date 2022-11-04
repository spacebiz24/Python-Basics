for i in range(100, 400):
    if (i % 2 == 0):
        f_dig = i // 100
        m_dig = (i % 100) // 10
        if(f_dig % 2 == 0 and m_dig % 2 == 0):
            print(i, end=",")