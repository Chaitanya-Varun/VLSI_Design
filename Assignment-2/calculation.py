

k = 115*1e-6
Vt = 0.43
Vdsat = 0.63
ratio=3
Vgs = 2.5
Vds = Vdsat
Ids = k*ratio*((Vgs-Vt)*Vds - (Vds**2/2))
print(Ids)
