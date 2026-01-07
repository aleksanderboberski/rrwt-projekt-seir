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