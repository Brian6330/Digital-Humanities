
#
#
#


# %%
import pandas as pd
import numpy as np
from scipy import stats



# fix a seed for being ablor to reproduce the same random sampling
np.random.seed(123759)

valuesA = np.random.randint(0, 6, size=100)

valuesA[0:5]

print('mean:', np.mean(valuesA), 'range:', min(valuesA), ':', max(valuesA))

result = stats.ttest_1samp(valuesA, 3.5)

result.statistic
result.pvalue

valuesB = np.random.randint(0, 7, size=100)

valuesB[0:5]


print('mean:', np.mean(valuesB), 'range:', min(valuesB), ':', max(valuesB))


result = stats.ttest_1samp(valuesB, 3.5)

result.statistic
result.pvalue


result = stats.ttest_ind(valuesA, valuesB, equal_var=True)

result.statistic
result.pvalue


result = stats.ttest_ind(valuesA, valuesB)

result.statistic
result.pvalue

result = stats.ttest_ind(valuesA, valuesB, equal_var=False)

result.statistic
result.pvalue



result = stats.ttest_ind(valuesA, valuesB, usevar='unequal', alternative='larger')
result.statistic
result.pvalue


#
# chi-square test
#
import pandas as pd
import numpy as np
from scipy import stats

regions_oi = sorted(['new england', 'mountain', 'pacific', 'foreign'])
df_regions = df.loc[df['reg16'].isin(regions_oi)].copy()
df_regions['reg16'] = df_regions['reg16'].cat.remove_unused_categories()
df_regions.groupby('reg16')['degree'].value_counts(normalize=True).round(1).to_frame();
df_regions.groupby('reg16')['degree'].value_counts().to_frame();


subjects = pd.DataFrame(
    [
        [134, 120, 152, 318],
        [80, 72, 69, 112],
        [63, 34, 20, 63], 
        [57, 19, 19, 48], 
        [32, 17, 16, 42], 
    ],
    index=['high school', 'bachelor', 'graduate', 'lt high school', 'junior college'],
    columns=['foreign', 'new england','mountain', 'pacific'])
subjects

chi, pval, dof, exp = stats.chi2_contingency(subjects)
print('p-value is: ', pval)

significance = 0.05
p = 1 - significance
critical_value = stats.chi2.ppf(p, dof)
print('chi=%.6f, critical value=%.6f\n' % (chi, critical_value))


#
# Second example
#

tshirts = pd.DataFrame(
    [
        [48,22,33,47],
        [35,36,42,27]
    ],
    index=["Male","Female"],
    columns=["Balck","White","Red","Blue"])
tshirts

tshirts.columns

results = stats.chi2_contingency(tshirts)

results[0]   # x2 value
results[1]   # p-value

results[2]   # dof
myTable = results[3]  # expected values
myTable

myTable.transpose()  # transpose the values

significance = 0.01
p = 1- significance
dof = results[2]
critical_value = stats.chi.ppf(p, dof)
critical_value

