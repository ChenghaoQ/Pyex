brand=['李宁','耐克','阿迪达斯','FishQ']
slogan=['一切皆有可能','Just do it','Impossible nothing','balabalabala']
#using list
print('FishQ:',slogan[brand.index('FishQ')])
#using dict
merged=dict(zip(brand,slogan))
print('FishQ:',merged['FishQ'])
