tugas = float(input("masukan nilai tugas:"))
uts = float(input("masukan nilai uts:"))
uas = float(input("masukan nilai uas:"))

nilai = (0.15 * tugas) + (0.35 * uts) + (0.50 * uas)

if nilai > 80:
    grade = 'A'
elif nilai > 70:
    grade = 'B'
elif nilai >60:
    grade ='C'
elif nilai > 50:
    grade ='D'
else:
    grade ='E'


if nilai > 60:
    status = 'lulus'
else:
    status = 'tidak lulus'

print('nilai akhir: %0.2f' % nilai)
print('grade: {}'.format(grade))
print('status: {}'. format(status))