print('TTOWG')
loc_D_=float(input('Enter the dolomite mean value'))
scale_D_=float(input('Enter the dolomite SD value'))
loc_S_=float(input('Enther the shale mean value'))
scale_S_=float(input('Enter the shale SD value'))
count_D_=float(input('Enter count value for dolomite'))
count_S_=float(input('Enter count value for shale'))
count_total_=count_D_ + count_S_
p_D_=count_D_ / count_total_
p_S_=count_S_ / count_total_

#p_gamma_D = p(gamma>60|D)
#p_gamma_S = p(gamma>60|S)
#p_D_gamma_60= p(D|gamma>60)

import scipy.stats
p_gamma_D=1-scipy.stats.norm(loc_D_, scale_D_).cdf(0.5)
p_gamma_S=1-scipy.stats.norm(loc_S_, scale_S_).cdf(0.5)
p_D_gamma_60= p_D_* p_gamma_D / p_D_* p_gamma_D + p_S_ * p_gamma_S


if p_D_gamma_60>=0.5:
    print('The interval is Dolomite')
    print('It is a Pay Zone Reservoir')
else:
    print('It is a shale interval')
    print('It is a Non-pay Zone Reservoir')
print('Reservoir formation known')
