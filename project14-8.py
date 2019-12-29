import matplotlib.pyplot as plt
import numpy as np

# meghdar haye sabet ke dar masale dade shode
A = 3
B = 2
C = 1
e = np.arctan(C/B)
E0x = A
E0y = np.sqrt(B**2 + C**2)

# baraye x az -5 ta 5 be ezaye 10000 noghte faza ra tarif kon
x = np.linspace(-5, 5, 10000)

# moadele ma : (y/E0y)**2 + (x/E0x)**2 - 2(x/E0x)(y/E0y)cos(e) = sin**2(e)
# baraye hal chon dar har marhale be ezaye x moshakhas hal mikonim
# engar x sabet ast pas yek moadele daraje 2 ba sabet haye b va c darim ke dar payin tarif shode
b = -2*(E0y/E0x)*np.cos(e)*x
c = E0y**2 * ((x**2/E0x**2) - (np.sin(e) * np.sin(e)))

# do javab e moadele daraje 2
y1 = (-b + np.sqrt(b**2 - 4*c))/2
y2 = (-b - np.sqrt(b**2 - 4*c))/2


# bakhsh e tarif e axis ha bara behtar shodan e namayesh e nemoodar
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


# rasm e do nemoodar be ezaye do javabi ke bara moadele daraje 2 be dast ovordim
plt.plot(x, y1, '-r')
plt.plot(x, y2, '-r')
plt.title('nemoodar noor ghotbide beyzavi')
plt.grid()
plt.show()
