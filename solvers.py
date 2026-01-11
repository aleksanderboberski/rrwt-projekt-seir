'''
Ten plik musi zostać całkowicie zintegrowany z notatnikiem do momentu oddania pracy
'''
def euler_solver(f, y0, tlim, step = 0.1): #f powinna być funkcją postaci f(y:float, t:float)->float
    y, t = [y0], 0 #lista przybliżonych wartości, czas
    while t < tlim:
        dy = f(y[-1], t) #pochodna w punkcie
        y.append(y[-1] + (dy*step)) #przybliżenie wartości y za pomocą pochodnej
        t += step
    return y

def midpoint_solver(f, y0, tlim, step = 0.1): #taka sama konwencja jak w euler_solver
    y, t = [y0], 0 #lista przybliżonych wartości, czas
    while t < tlim:
        dy = f(y[-1], t) #przybliżenie punktu środkowego metodą Eulera
        midpoint = y[-1] + (dy*(step/2))

        dy = f(midpoint, t+(step/2)) #pochodna w punkcie środkowym
        y.append(y[-1] + (dy*step)) #przybliżenie wartości y za pomocą pochodnej w punkcie środkowym
        
        t += step
    return y

def vector_midpoint(f, y0, tlim, step = 0.1): #f musi zwracac iterable wszystkich pochodnych, y0 to wektor warunkow poczatkowych
    y, t = [y0], 0
    while t < tlim:
        dy = f(y[-1], t)
        midpoint = [y[-1][i] + (dy[i]*(step/2)) for i in range(len(dy))] #moze zamiast tego jakies numpy zeby to lepiej wygladalo i chodzilo
        print(map(lambda a, b: a+(b*(step/2)), y[-1], dy))

        dy = f(midpoint, t+(step/2))
        y.append([y[-1][i] + (dy[i]*step) for i in range(len(dy))])
        
        t += step
    return y


if __name__ == "__main__": #DEMO
    import matplotlib.pyplot as plt
    from math import e

    def func(y, t):
        return y
    
    y1 = euler_solver(func, 1, 5, step=0.05)
    y2 = [e**(t/20) for t in range(100)]
    y3 = midpoint_solver(func, 1, 5, step=0.05)
    fig, (ax1, ax2) = plt.subplots(ncols=2)
    for i in [ax1, ax2]:
        i.plot(y1, color='red')
        i.plot(y2, color='green')
        i.plot(y3, color='blue')
    ax2.set_ylim(110,115)
    ax2.set_xlim(94,95)
    plt.show()
    
    '''def f(y, t):
        return [y[0], y[1]+t]
    import matplotlib.pyplot as plt
    y = vector_midpoint(f, (1,1), 5)
    y1, y2 = [i[0] for i in y], [i[1] for i in y]
    plt.plot(y1)
    plt.plot(y2)
    plt.show()'''