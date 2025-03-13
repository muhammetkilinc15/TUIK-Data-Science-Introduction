#%% Tanımlayıcı istatistikler

import pandas as pd

df= pd.read_excel(r'D:\unv_workshop\egitim_exceli.xlsx') # Eğitim için veri setinin yüklenmesi aşaması

df.info() # Kolonlar hakkında tanımlayıcı bilgilerin gözlenmesi

df.Motor_hacmi.astype(int) #İlgili değişken tipinin değiştirilmesi

df['Motor_hacmi3']=df.Motor_hacmi.astype(int) #İlgili değişkenin asıl veri seti üzerinde tipinin değiştirilmesi(aşağı yuvarlıyor)

import numpy as np # ceil'in kullanımı için paket yüklüyoruz.

df['Motor_hacmi2']=np.ceil(df['Motor_hacmi']).astype(int) #İlgili değişkenin asıl veri seti üzerinde tipinin değiştirilmesi(.5 yukarı diğer türlü aşağı)

df.describe() #Sayısal değişkenler için tanımlayıcı istatistiklerin elde edilmesi

df.describe(include='all') #Sayısal ve sayısal olmayan tüm değişkenlerin tanımlayıcı istatistiklerinin elde edilmesi

df.describe(include='all').T #İlgili tablonun transpozu alınır.

df_tanımlayici_ist=df.describe(include='all').T

df_tanımlayici_ist=df.describe(include='all').T.reset_index() #İndexin kaldırılması (# df.describe().T.round(2))

df_tanımlayici_ist.info()

#%% Sıklık Dağılımı

df['Marka'].value_counts() #Kategorik veriler için sıklığın alınması

k=int(np.ceil(1+3.3*np.log(df.shape[0]))) #Sıklık dağılımı tablosu oluştururken sınıf sayısının belirlenmesi

df['Sınıf']=pd.cut(df['Sehir_ici'],bins=k) #Sayısal bir değişken için sınıf aralıklarının belirlenmesi

df['Sınıf'].value_counts().sort_index() # Sıklık dağılımının sayısal bir değişken için oluşturulması - Sonuçta köşeli parantez dahil olmamayı, normal parantez dahilliği ifade eder.

#df["Sınıf1"]=  pd.cut(df['Sehir_ici'],bins = [9.95, 12.381, 14.762, 17.143, 19.524, 21.905, 24.286, 26.667, 29.048, 60.0])
#df['Sınıf1'].value_counts().sort_index()
#df["Sınıf3"]=  pd.qcut(df['Sehir_ici'],q=9)
#df['Sınıf3'].value_counts().sort_index()

# bu sonuçlara bakıldığında dağılımın sağa çarpık olduğu görülmekte sınıf sayısını değiştirerek tekrar oluşturalım.

df['Sınıf2']=pd.cut(df['Sehir_ici'],bins=10) 

df['Sınıf2'].value_counts().sort_index()



#%% Sürekli verileri için kullanılabilecek gösterimler (Grafik)

#Veri görselleştirme (görsellerin consola düşmesi için plots tabında sağ üstteki üç çiğiden ilk iki seçenek iptal edilir.)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Histogram

sns.histplot(df['Sehir_ici'], bins=9)  # KDE eğrisi olmadan histogram

sns.histplot(df['Sehir_ici'], bins=9, kde=True)  # KDE eğrisi olan histogram

#Boxplot
 # **📌 Y Ekseni Sınırlarını Belirleme**
ymin, ymax = df['Sehir_ici'].min()*(0.8), df['Sehir_ici'].max()*(1.2)
sns.boxplot(y=df['Sehir_ici'])


fig,ax=plt.subplots()
sns.boxplot(y=df['Sehir_ici'], ax=ax,showmeans=True)
ax.set_title('Başlık')
plt.show()

"""
# Boxplot çizme
fig, ax = plt.subplots(figsize=(6, 4))
sns.boxplot(y=df["Sehir_ici"], ax=ax)

# Aykırı Sehir_icii direkt plot üzerinden alma
outliers = df["Sehir_ici"][(df["Sehir_ici"] < df["Sehir_ici"].quantile(0.25) - 1.5 * (df["Sehir_ici"].quantile(0.75) - df["Sehir_ici"].quantile(0.25))) |
                          (df["Sehir_ici"] > df["Sehir_ici"].quantile(0.75) + 1.5 * (df["Sehir_ici"].quantile(0.75) - df["Sehir_ici"].quantile(0.25)))]

# Aykırı Sehir_icii kutu grafiği üzerine indeksleri ile ekleme
for i in outliers.index:
    ax.text(x=0, y=df["Sehir_ici"][i], s=str(i), color='red', ha='center', fontsize=10, fontweight='bold')

plt.title("Boxplot ve Aykırı Gözlem Numaraları")
plt.show()
"""

#Violin

fig,b=plt.subplots()
sns.violinplot(y=df['Sehir_ici'], ax=b, color="lightgreen")
b.set_title("Başlık")
plt.show()

#Violin ve box plotın birlikte gösterimi

fig,b=plt.subplots()
vp = sns.violinplot(y=df['Sehir_ici'], ax=b, color="lightgreen", linewidth=1.5)
for artist in vp.collections:
    artist.set_alpha(0.4)  # %40 şeffaf yap

sns.boxplot(y=df['Sehir_ici'], ax=b, color="lightcoral", width=0.3)
b.set_title("Violin ve Box Plot Üst Üste")
plt.show()

#QQ Plot
import statsmodels.api as sm  # QQ plot için lazım

fig,b=plt.subplots()
sm.qqplot(df['Sehir_ici'], line='s', ax=b)  # Normal dağılım çizgisi ile
b.set_title("QQ Plot")   
plt.show()

#%% Veri görselleştirme 
#(görsellerin consola düşmesi için plots tabında sağ üstteki üç çiğiden ilk iki seçenek iptal edilir.)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%% Kategorik veriler için kullanılabilecek gösterimler

#Pie Grafiği
#Eski yöntemde eklenecek

# Gruplayarak frekansları otomatik hesapla ve pie chart çiz
df.groupby('Orijin').size().plot.pie(autopct='%1.1f%%', figsize=(6,6))
plt.title("Kategori Dağılımı")
plt.ylabel("")  # Y-etiketini kaldır
plt.show()

""" pieın parçalı gösterimi
df.groupby('Orijin').size().plot.pie(autopct='%1.1f%%', figsize=(6,6), startangle=90, explode=(0.1,0.1,0.1),shadow=True)
plt.title("Kategori Dağılımı")
plt.ylabel("")  # Y-etiketini kaldır
plt.show()
"""

# Kategori frekanslarını hesapla
kategori_sayilari = df.groupby('Orijin').size()

# Çubuk grafiği çiz
kategori_sayilari.plot.bar(color=['red', 'blue', 'green'], figsize=(6, 4))

plt.title("Kategori Dağılımı")
plt.xlabel("Orijin")
plt.ylabel("Frekans")
plt.xticks(rotation=0)  # X eksenindeki yazıları düz hale getir
plt.grid(axis='y', alpha=0.7)  # Daha okunaklı olması için yatay çizgiler ekle
plt.show()

# Çubuk grafiği çizme (Etiketler eklenerek)
kategori_sayilari = df.groupby('Orijin').size()
ax = kategori_sayilari.plot.bar(color=['red', 'blue', 'green'], figsize=(6, 4))

# Her çubuğun üzerine sayıları ekle (etiketleme)
for i, v in enumerate(kategori_sayilari.values):
    ax.text(i, 50, str(v), ha='center', fontsize=12, fontweight='bold', color='white')

# Başlık ve etiketler
plt.title("Kategori Dağılımı")
plt.xlabel("Kategoriler")
plt.ylabel("Frekans")
plt.xticks(rotation=0)  # X eksenindeki yazıları düz hale getir
plt.grid(axis='y', alpha=0.7)  # Daha okunaklı olması için yatay çizgiler ekle
plt.show()

# Scatter plot çizimi

df.plot.scatter(x='Sehir_ici', y='Sehir_disi', title='Scatter Plot Örneği')

#alternatif sns ile scatter plot çizimi
sns.scatterplot(df['Sehir_ici'],df['Sehir_disi'])
plt.title("Başlık")

#%% Uç Aykırı Değer Tespiti

Ort_Sehi=np.round(df['Sehir_ici'].mean(),2)
Std_Sehi=np.round(df['Sehir_ici'].std(),2)

up_b=Ort_Sehi+2*Std_Sehi
low_b=Ort_Sehi-2*Std_Sehi

df['Yeni']=(df['Sehir_ici']-Ort_Sehi)/Std_Sehi

df['Yeni2']=df['Yeni'].apply(lambda x: "anormal" if np.abs(x)>2 else "normal")

df['Yeni2'].value_counts()
df['Yeni2'].value_counts(normalize=True)

#Tekraralayan durum tespiti için fonksiyon yazılması uygundur

def anotest(af, c):
    af[c+'_yeni']=(af[c]-np.round(af[c].mean(),2))/np.round(af[c].std(),2)
    af[c+'_uyarı']=af[c+'_yeni'].apply(lambda x: "anormal" if np.abs(x)>2 else "normal")
    return af

df=anotest(df,"Sehir_disi")

#Uç aykırı değer tespitinde medyan yöntmei eklenecek.

#%% Normal Dağılım Tespiti

import scipy.stats as stats

#Hipotez kurulması - 1.Hipotez:İstenilen değişken ile normal dağılım arasında fark yoktur Alternatif Hipotez:İstenilen değişken ile normal dağılım arasında fark vardır.

ks_stat, ks_p = stats.kstest(df['Sehir_ici'],  "norm", args=(df['Sehir_ici'].mean(), df['Sehir_ici'].std()))

ks_stat, ks_p = stats.kstest(df['Uzunluk'],  "norm", args=(df['Uzunluk'].mean(), df['Uzunluk'].std()))

def ks_t(data,kolon,hata,dagilim="norm"):
    ks_stat, ks_p = stats.kstest(data[kolon], dagilim, args=(data[kolon].mean(), data[kolon].std()))
    ks_result = "Değişken dağılımı normal dağılıma uymaktadır." if ks_p > hata else "Değişken dağılımı normal dağılıma uymamaktadır."
    return ks_result

B=ks_t(df,"Uzunluk",0.05)
C=ks_t(df,"Sehir_ici",0.05)
#Gözlem sayısının büyüklüğüne göre normallik testi farklılık göstermektedir.

#%% Normallik Fonksiyonu

def sw_t(data,kolon,hata):
    shapiro_stat, shapiro_p = stats.shapiro(data[kolon])
    shapiro_result = 0 if shapiro_p > hata else 1
    return shapiro_result

def ks_t(data,kolon,hata,dagilim="norm"):
    ks_stat, ks_p = stats.kstest(data[kolon], dagilim, args=(data[kolon].mean(), data[kolon].std()))
    ks_result = 0 if ks_p > hata else 1
    return ks_result


def ad_t(data,kolon,hata,dagilim="norm"):
    anderson_result = stats.anderson(data[kolon], dist=dagilim)
    anderson_stat = anderson_result.statistic
    
    # Anderson p-değeri hesaplama (kritik değerlere göre tahmini p)
    if anderson_stat < anderson_result.critical_values[0]:
        anderson_p = 0.15
    elif anderson_stat < anderson_result.critical_values[1]:
        anderson_p = 0.10
    elif anderson_stat < anderson_result.critical_values[2]:
        anderson_p = 0.05
    elif anderson_stat < anderson_result.critical_values[3]:
        anderson_p = 0.025
    elif anderson_stat < anderson_result.critical_values[4]:
        anderson_p = 0.01
    else:
        anderson_p = 0.001  # Normal dağılımdan en uzak değer
    
    ad_result = 0 if anderson_p > hata else 1
    return ad_result

    
def cvm_t(data,kolon,hata):
    cvm_result = stats.cramervonmises(data[kolon], 'norm', args=(data[kolon].mean(), data[kolon].std()))
    cvm_stat = cvm_result.statistic
    cvm_p = cvm_result.pvalue
    cvm_result_str = 0 if cvm_p > hata else 1
    return cvm_result_str


def jb_t(data,kolon,hata,grup=None):
    jb_stat, jb_p = stats.jarque_bera(data[kolon])
    jb_result = 0 if jb_p > hata else 1
    return jb_result 
    

def normallik(data,kolon,hata,grup=None):
    try:
        durum=[]
        data[kolon]
        
        #anderson darling (AD)
            #her veri setinde kullanılabilir. Shaphiro wilk'den daha güçlüdür.(küçük verilerde daha güçlüdür.) 
            #Çok büyük verilerde aşırı duyarlılık gösterebilir. 
            #kenarlardaki sapmaları daha iyi yakalar.
        sonuc_ad_t=ad_t(data,kolon,hata,dagilim="norm")
        #print(f"test sonucu1: {sonuc_ad_t}")
        if sonuc_ad_t==0:
            if len(data)<50:
                y1="Yanıt Güçlü"                
            else:
                y1="Aşırı Duyarlılık olabilir"
            durum.append([kolon,"Anderson Darling",sonuc_ad_t,y1])
        else:
            if len(data)<50:
                y2="Yanıt Güçlü, Uç Değer kontrol edilmeli"               
            else:
                y2="Aşırı Duyarlılık olabilir, Uç Değer kontrol edilmeli"
            durum.append([kolon,"Anderson Darling",sonuc_ad_t,y2])
            
        #cramer-von mises (CVM)
            #n<5000 olduğu durumlarda önerilir. (AD) ye benzer ama merkezdeki sapmalara karşı daha duyarlıdır.
            #küçük veri setlerinde daha güçlüdür.
            #Çok büyük verilerde aşırı duyarlılık gösterebilir. 
        sonuc_cvm_t=cvm_t(data,kolon,hata)
        if sonuc_cvm_t==0:
            if len(data)<5000:
                y3="Yanıt Güçlü"
            else:
                y3="Aşırı Duyarlılık olabilir."
            durum.append([kolon,"Cramér-von Mises",sonuc_cvm_t,y3])
        else:
            if len(data)<5000:
                y4="Yanıt Güçlü, Merkezde Sapma olabilir."
                
            else:
                y4="Aşırı Duyarlılık olabilir."
            durum.append([kolon,"Cramér-von Mises",sonuc_cvm_t,y4])
            
            
        
        if len(data)<=50:
            #shaphiro wilk  (SW)
                #küçük verilerde güçlüdür.küçük sapmaları bile yakalayabilir. Büyük verilerde fazla duyarlı olabilir
            
            sonuc_sw=sw_t(data,kolon,hata)
            if sonuc_sw==1:
                y5="Yanıt Güçlü, veri setinde uç değer olaiblir"                
            else:
                y5="Yanıt Güçlü,Normal Dağılıyor"
            durum.append([kolon,"Shaphiro Wilk",sonuc_sw,y5])
            
        
        else:
            #kolmogorov smirnov (KS)
                #normal dağılım dışındaki dağılımlarında test edilmesinde kullanılır.
                   #küçük veri setlerinde duyarsızdır. Uç değerlere dair duyarlılığı azdır. Küçük veri setlerinde önerilmez
            sonuc_ks=ks_t(data,kolon,hata,dagilim="norm")
            if sonuc_ks==0:
                y6="Dağılım normal ancak uç değer olabilir."
            else:
                y6="Normal dağılmıyor. Uç değer kontrolü yapılabilir"
            durum.append([kolon,"Kolmogrov Smirnov",sonuc_ks,y6])
                
            #Jarque-Bera (JB)
                #normal dağılımın çarpıklığı ve basıklığını test eder.
                #küçük veri setlerinde duyarsızdır. Küçük sapmaları kaçırabilir.
                #büyük veri setlerinde çarpıklık ve basıklığı değerlendirmek açısından uygundur.
            sonuc_jb=jb_t(data,kolon,hata)
            if sonuc_jb==0:
                y7="Çarpıkık ve basıklık yönünden sonuçlar uyumlu"
            else:
                y7="Normal dağılmamada çarpıklık veya basıklık etkisi olabilir. Araştırılmalı"
            durum.append([kolon,"Jarque Bera",sonuc_jb,y7])
            
            
        degerlendirme=pd.DataFrame(durum, columns=['kolon adı','Test Adı', 'Değer', 'Açıklama'])
        #print(degerlendirme["Değer"])
        normal_skor=degerlendirme["Değer"].mean()
        if degerlendirme["Değer"].mean()==1:
            ozet="Değişken normal dağılmıyor. Uç aykırı değer kontrol edin veya parametrik olmayan yöntem deneyin."
        elif degerlendirme["Değer"].mean()==0.5:
            ozet="Farklı testler için farklı sonuçlar çıkıyor. Detay tablosunu inceleyin"
        elif degerlendirme["Değer"].mean()==0:
            ozet="Dağılım normal."
        elif degerlendirme["Değer"].mean()<0.5:
            ozet="Testler büyük oranda dağılımı normal göstermekte. Detaylar inceleneilir"
        else:    
            ozet="***Testler büyük oranda dağılımı normal olmadığını göstermekte. Detaylar inceleneilir"
        return ozet,normal_skor,degerlendirme
    except KeyError: #veri setinde yoksa bu hata döner
        print("ilgili kolon veri setinde bulunamadı kontrol ediniz.")
    """
    except TypeError: #değişkenin tipi uygun değilse bu hata döner.
        print("Kolon tipi Sürekli değil kontrol ediniz")
    """    



#%% Güven Aralığı Hesaplanması

from scipy.stats import t,norm


ort = df['Uzunluk'].mean()
std_sap = df['Uzunluk'].std()
n = df['Uzunluk'].count()  # Örneklem büyüklüğü
confidence_level = 0.95
alpha = 1 - confidence_level
degrees_of_freedom = n - 1  #
kritik=norm.ppf(1 - alpha / 2)

margin_of_error = kritik * (std_sap / np.sqrt(n))  # Hata payı
confidence_interval = (ort - margin_of_error, ort + margin_of_error)

print(f"Uzunluk değişkeninin %95 lik güven aralığı {confidence_interval} dır")



def guv_aralik(veri,kolon,guven):
    from scipy.stats import t,norm
    import matplotlib.pyplot as plt
    import numpy as np
    ort = veri[kolon].mean()
    std_sap = veri[kolon].std()
    n = veri[kolon].count()  # Örneklem büyüklüğü

    # %95 güven aralığı için t-dağılımından kritik değeri al
    confidence_level = guven
    alpha = 1 - confidence_level
    degrees_of_freedom = n - 1  # Serbestlik derecesi
    #t_critical = t.ppf(1 - alpha / 2, degrees_of_freedom)  # t-dağılımından kritik değer. gözlem değeri 30'dan küçük ise
    #z_critical = norm.ppf(1 - alpha / 2)  # z-dağılımından kritik değer. gözlem değeri 30'dan büyük ise

    ##gözlem sayısına göre kritik değeri belirle
    if n<30:
        kritik=t.ppf(1 - alpha / 2, degrees_of_freedom)  # t-dağılımından kritik değer. gözlem değeri 30'dan küçük ise
        uyarı="not: gözlem sayısı 30'dan küçük olduğu için t tablosu kullanılmıştır."
    else:
        kritik=norm.ppf(1 - alpha / 2)  # z-dağılımından kritik değer. gözlem değeri 30'dan büyük ise
        uyarı="not: gözlem sayısı 30'dan büyük olduğu için z tablosu kullanılmıştır."
    # Güven aralığını hesapla
    margin_of_error = kritik * (std_sap / np.sqrt(n))  # Hata payı
    confidence_interval = (ort - margin_of_error, ort + margin_of_error)
    # Sonuçları yazdır
    
    print(baslik := f"{kolon} değişkeni için %95 Güven Aralığı:")
    print(ifade2 :=f"  Ortalama: {ort:.2f}")
    print(ifade3 :=f"  Güven Aralığı: ({confidence_interval[0]:.2f}, {confidence_interval[1]:.2f})")
    print(uyarı)
    
    # Grafiksel gösterim
    plt.figure(figsize=(8, 4))
    plt.errorbar(x=kolon, y=ort, yerr=margin_of_error, fmt='o', color='blue', 
                 capsize=5, label='Ortalama ve Güven Aralığı')
    plt.title(f"{kolon} için %95 Güven Aralığı")
    plt.xlabel("Değişken")
    plt.ylabel("Değer")
    
    
    # Y ekseni sınırlarını dinamik olarak ayarla
    plt.ylim(ort - 2 * margin_of_error, ort + 2 * margin_of_error)
    
    # Bilimsel gösterimi kapat
    plt.ticklabel_format(style='plain', axis='y')
    plt.legend()
    plt.grid(True)
    plt.show()
    sonuc=baslik+"\n"+ifade2+"\n"+ifade3+"\n"+uyarı
    return sonuc

#%% Tek örneklem testi

#Hipotez kurulması - 1.Hipotez:İstenilen değişken için test değerinin kitle ortalaması arasında fark yoktur 


print("Gözlem Sayısı 30'dan büyük olduğu için Z istatistiği kullanılacaktır")
n = len(df['Uzunluk'].dropna())
x_bar = np.mean(df['Uzunluk'].dropna())  # Örneklem ortalaması
s = np.std(df['Uzunluk'].dropna(), ddof=1)  # Örneklem standart sapması (n-1 ile düzeltilmiş)
s2 = np.std(df['Uzunluk'].dropna())  # Örneklem standart sapması (n-1 ile düzeltilmiş)
test=185
# Z-istatistiği hesaplama (örneklem sapmasını kullanarak)
z_stat = (x_bar - test) / (s / np.sqrt(n))

# P-değerini hesapla (çift yönlü test için)
p_value = 2 * (1 - norm.cdf(abs(z_stat)))

if p_value>0.05:
    sonuc="Farkı yoktur, Yokluk hipotezi kabul" 
else:
    sonuc="Farkı vardır, Alternatif hipotez kabul"
    
print(f"Uzunluk değişkeninin %95 güven düzeyinde {test} kitle ortalamasından {sonuc}.")

#Eğer veri seti normal dağılmıyorsa non parametrik testlerden wilcoxon testi kullanılır.

test_stat, p_value = stats.wilcoxon(df['Uzunluk'].dropna() - test)
#print(f"Wilcoxon Test İstatistiği: {test_stat:.4f}")
print(f"P-Değeri: {p_value:.2f}")
if p_value < alpha:
    print(f"Sonuç: Medyan {test}'ten anlamlı derecede farklıdır (H0 reddedildi).")
else:
    print(f"Sonuç: Medyan {test} yakın olup anlamlı fark yoktur (H0 kabul edildi).")

#%% Bağımsız iki örneklem testi

#Hipotez kurulması - 1.Hipotez:Asya ve Avrupa'da üretilen araçların uzunlukları arasında %95 güven düzeyinde fark bulunmamaktadır.

grup1=df[["Orijin","Uzunluk"]][df["Orijin"] == "Asya"]
grup2=df[["Orijin","Uzunluk"]][df["Orijin"] == "Avrupa"]
normal_k=0
varyans_k=0
   
for k in [["Asya",grup1],["Avrupa",grup2]]:
    
    print(f"{k[0]} grubundaki gözlem sayısı {len(k[1]['Uzunluk'])}, ortalama değer {k[1]['Uzunluk'].mean():.2f}")
    #print(f"{k[1]},{test_kolon},{alpha}")
    sonuc=ks_t(k[1],"Uzunluk",0.05)
    if sonuc=="Değişken dağılımı normal dağılıma uymaktadır.":
        print(f"{k[0]} verileri normal dağılmaktadır")
    else:
        print(f"**{k[0]} verileri normal dağılmamaktadır")
        normal_k=1
    print("-"*40)
    
    
if normal_k==0:
    print("tüm değişkenler normal dağılmaktadır.")
else:
    print("**normal dağılma varsayımı sağlanmamıştır.")
print("-"*40)
    
print("Eşit Varyanslılık için Levene Testi uygulanacaktır")
levene_stat, levene_p = stats.levene(grup1['Uzunluk'], grup2['Uzunluk'])
# p değeri 0.05'ten büyükse varyanslar eşittir, değilse eşit değildir
equal_var = True if levene_p > alpha else False
if equal_var:
    print("İki grubun varyans dağılımı benzerdir.")
else:
    print("**İki grubun varyans dağılımı farklıdır.")
    varyans_k=1
print("-"*40)    
if normal_k==0:
    print("Veriler normal dağıldığı için parametrik test uygulanacaktır.")
    # Bağımsız İki Örneklem T-Testi
    t_stat, p_value = stats.ttest_ind(grup1['Uzunluk'], grup2['Uzunluk'], equal_var=equal_var)
    print(f"T-istatistiği: {t_stat.item():.4f}, p-değeri: {p_value.item():.4f}")
    
    
else:
    print("***Normallik varsayımı sağlanmamıştır. Parametrik olmayan test uygulanacaktır.")
    print("Man whitney U testi yapılacaktır.")
    stat, p_value = stats.mannwhitneyu(grup1['Uzunluk'], grup2['Uzunluk'], alternative='two-sided')
    print(f"U-istatistiği: {stat.item():.4f}, p-değeri: {p_value.item():.4f}")
    
if p_value<alpha:
    print("***Sonuç: H0 reddedildi, gruplar arasında anlamlı bir fark vardır.")
else:
    print("Sonuç: H0 kabul edildi, gruplar arasında anlamlı bir fark bulunamamıştır.")
print("-"*40)
   
D=guv_aralik(grup1,"Uzunluk",0.95)
E=guv_aralik(grup2,"Uzunluk",0.95)

#%% Bağımlı iki grup testi

#Hipotez kurulması - 1.Hipotez:Veri setindeki araçların şehir içi yakıt tüketimleri ile şehir dışı yakıt tüketimleri arasında fark yoktur.


df["Fark"]=df['Sehir_ici']-df['Sehir_disi']
sonuc=ks_t(df,"Fark",0.05)

if sonuc=="Değişken dağılımı normal dağılıma uymaktadır.":
    print("Fark verileri normal dağılmaktadır.\nParametrik test kullanılacaktır")
    t_stat, p_value = stats.ttest_rel(df['Sehir_ici'], df['Sehir_disi'])
    print(f"Eşleştirilmiş t-Testi Sonucu: T-istatistiği = {t_stat:.4f}, p-değeri = {p_value:.4f}")

else:
    print("**Fark verileri normal dağılmamaktadır.\nParametrik olmayan Wilcoxon işaret testi kullanılacaktır")
    wilcoxon_stat, p_value = stats.wilcoxon(df['Sehir_ici'], df['Sehir_disi'])
    
    print(f"Wilcoxon Test Sonucu: Test istatistiği = {wilcoxon_stat:.4f}, p-değeri = {p_value:.4f}")
    
if p_value < alpha:
    print("Sonuç: Karşılaştırılan değişkenler arasında anlamlı bir fark vardır. (H0 reddedildi).")
else:
    print("Sonuç: Karşılaştırılan değişkenler anlamlı bir fark bulunamamıştır. (H0 kabul edildi).")


#%% Varyans Analizi

"""def varyans_analiz(veri,grup_kolon,test_kolon,alpha):
    normal_k=0
    varyans_k=0
    post_h=0
    for grup in veri[grup_kolon].unique():
        secim=veri[veri[grup_kolon] == grup][[test_kolon,grup_kolon]]
        print(f"{grup} grubundaki gözlem sayısı {len(secim)}, ortalama değer {secim[test_kolon].mean():.2f}")
        sonuc=normallik(secim,test_kolon,alpha)
        if sonuc[1]<=0.5:
            print(f"{grup} verileri normal dağılmaktadır")
        else:
            print(f"**{grup} verileri normal dağılmamaktadır")
            normal_k=1
        print("-"*40)
    if normal_k==0:
        print("Tüm altgruplar için normal dağılma koşulu sağlanmaktadır.")
    else:
        print("***Normallik varsayımı sağlanmamıştır.")
    print("-"*40)
    
    ##gruplar varyans homojenliği testi
    grup_listesi = [veri[veri[grup_kolon] == grup2][test_kolon].values for grup2 in veri[grup_kolon].unique()]
    stat, p = stats.levene(*grup_listesi)
    print(f"Levene Testi: p-değeri = {p:.4f}")
    equal_var = True if p > alpha else False
    if equal_var:
        print("Grupların varyansları homojendir.")
    else:
        print("***Gruplardan az 1 tanesinin varyansı diğerlerinden farklıdır. ")
        varyans_k=1
    print("-"*40)
    
    
    # Welch ANOVA modeli oluşturma
    model = ols(f"{test_kolon} ~ {grup_kolon}", data=veri).fit()
    welch_anova = sm.stats.anova_lm(model, typ=2, robust="hc3")  # HC3 Welch düzeltmesi

    # Sonuçları yazdır
    print("Welch ANOVA sonucu:\n", welch_anova)
    
    if normal_k==0 and varyans_k==0:
        print("Hem Normallik hem de eşit varyanslılık sağlanmaktadır. Parametrik ANOVA testi yapılacaktır.")
        anova_stat, p_anv_value = stats.f_oneway(*grup_listesi)
        print(f"ANOVA Testi Sonucu: F-istatistiği = {anova_stat:.4f}, p-değeri = {p_anv_value:.4f}")
        
        if p_anv_value>alpha:
            print("Grupların varyans dağılımı benzerdir.")
        else:
            print("Gruplardan en az 1 tanesi diğerlerinden farklı ortalamaya sahiptir")
            print("post-hoc test yapılmalıdır (parametrik)")
            post_h=1
        
    elif normal_k==0 and varyans_k==1:
        print("Normallik Sağlanmakta ancak Eşit varyanslılık sağlanmamaktadır. Welch ANOVA testi yapılaca**ktır.")
    elif normal_k==1 and varyans_k==0:
        print("***Normallik Sağlanmamakta ancak Eşit varyanslılık sağlanmaktadır. Kruskal Wallis testi yapılacaktır.")
    else:
        print("***Normallik ve Eşit varyanslılık sağlanmamaktadır. Kruskal Wallis testi yapılacaktır.")
    print("-"*40)
#Fonksiyon eksik - """

# Kruskal-Wallis Testi

grup1=df["Uzunluk"][df["Orijin"] == "Asya"]
grup2=df["Uzunluk"][df["Orijin"] == "Avrupa"]
grup3=df["Uzunluk"][df["Orijin"] == "Amerika"]

h_stat, p_value_kw = stats.kruskal(grup1, grup2, grup3)

print("\n=== Kruskal-Wallis Testi ===")
print(f"H istatistiği: {h_stat}")
print(f"P-değeri: {p_value_kw}")

if p_value_kw < 0.05:
    print("Gruplar arasında en az bir fark var (H0 reddedildi).")
else:
    print("Gruplar arasında fark yok (H0 kabul edildi).")

# Kruskal sonrası Dunn-Bonferroni
import scikit_posthocs as sp

df_dunn = sp.posthoc_dunn([grup1, grup2, grup3], p_adjust='bonferroni')
print(np.round(df_dunn,8))

#Parametrik post-doc testi

from statsmodels.stats.multicomp import pairwise_tukeyhsd
# Veriyi uzun formata getir
"""data = np.concatenate([grup1, grup2, grup3])
groups = (['Group 1'] * len(grup1)) + (['Group 2'] * len(grup2)) + (['Group 3'] * len(grup3))

# DataFrame oluştur
dfd = pd.DataFrame({"Values": data, "Groups": groups})

# Tukey's HSD testi
tukey_results = pairwise_tukeyhsd(dfd['Values'], dfd['Groups'], alpha=0.05)"""
tukey_results2 = pairwise_tukeyhsd(df['Uzunluk'], df['Orijin'], alpha=0.05)

print(tukey_results2)

#%% Korelasyon

df.select_dtypes(include=[np.number]).corr(method="pearson")

from scipy.stats import pearsonr
df_numeric = df.select_dtypes(include=[np.number])
p_values = pd.DataFrame(index=df_numeric.columns, columns=df_numeric.columns)
r_values = pd.DataFrame(index=df_numeric.columns, columns=df_numeric.columns)
for col1 in df_numeric.columns:
    for col2 in df_numeric.columns:
        if col1 != col2:  # Aynı sütunların korelasyonuna gerek yok
            r, p = pearsonr(df_numeric[col1], df_numeric[col2])
            p_values.loc[col1, col2] = p
            r_values.loc[col1, col2] = r
        else:
            p_values.loc[col1, col2] = np.nan
            r_values.loc[col1, col2] = np.nan


# Tüm değişken çiftleri için Pearson korelasyonu ve p-değerlerini hesaplama
results=[]
columns = df_numeric.columns
for i in range(len(columns)):
    for j in range(i + 1, len(columns)):  # Aynı çiftleri tekrar hesaplamamak için
        col1, col2 = columns[i], columns[j]
        r, p = pearsonr(df_numeric[col1], df_numeric[col2])
        results.append([f"{col1} - {col2}", round(r, 2), round(p, 3)])

# Sonuçları DataFrame'e çevir
results_df = pd.DataFrame(results, columns=["Değişken Çifti", "Pearson r", "P-Değeri"])

r_values

#%% Regresyon

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.stattools import durbin_watson

y = df["Beygir_gucu"]
X = df[["Motor_hacmi"]]

# 🔹 Sabit terimi ekleme
X = sm.add_constant(X)

# 🔹 Regresyon Modeli
model = sm.OLS(y, X).fit()

# 🔹 Model Özetini Yazdırma
print(model.summary())

### 🔥 Varsayım Testleri

## 1️⃣ Çoklu Doğrusal Bağıntı (Multicollinearity) - VIF
vif_data = pd.DataFrame()
vif_data["Değişken"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print("\n📌 VIF Değerleri (Çoklu Doğrusal Bağıntı):\n", vif_data) #VIF değerleri const harici 10 dan küçük olduğunda çoklu bağlantı olmadığını gösterir.

## 2️⃣ Hata Terimlerinin Normalliği - Shapiro-Wilk Testi
residuals = model.resid
shapiro_test = shapiro(residuals)
print(f"\n📌 Shapiro-Wilk Testi Sonucu: Test İstatistiği={shapiro_test.statistic}, p-değeri={shapiro_test.pvalue}")

## 3️⃣ Hata Terimlerinin Değişen Varyanslılığı (Homoskedasticity) - Breusch-Pagan Testi
bp_test = het_breuschpagan(residuals, X)
print(f"\n📌 Breusch-Pagan Testi Sonucu: LM Stat={bp_test[0]}, p-değeri={bp_test[1]}")

## 4️⃣ Otokorelasyon (Bağımlılık) - Durbin-Watson Testi
dw_stat = durbin_watson(residuals)
print(f"\n📌 Durbin-Watson Testi (Otokorelasyon): {dw_stat}")

### 📊 Görselleştirmeler

# 🔹 Artıkların Dağılımı (Normallik Kontrolü)
plt.figure(figsize=(12, 5))
sns.histplot(residuals, kde=True, bins=20)
plt.title("Hata Terimlerinin Histogramı")
plt.xlabel("Hata Terimleri")
plt.show()

# 🔹 Q-Q Plot (Normalliği Kontrol Etmek İçin)
sm.qqplot(residuals, line="45", fit=True)
plt.title("Q-Q Plot (Normallik Kontrolü)")
plt.show()

# 🔹 Artıkların Serpme Grafiği (Homoskedastisite Kontrolü)
plt.figure(figsize=(10, 5))
plt.scatter(model.fittedvalues, residuals, alpha=0.6)
plt.axhline(0, linestyle='dashed', color='red')
plt.title("Artıkların Dağılımı")
plt.xlabel("Tahmin Edilen Değerler")
plt.ylabel("Artıklar")
plt.show()

# 🔹 Tahmin ile Gerçekleşen İlişki Grafiği
plt.figure(figsize=(10, 5))
plt.scatter(model.fittedvalues, df["Beygir_gucu"], alpha=0.6)
plt.title("Tahmin ile Gerçekleşen İlişki Grafiği")
plt.xlabel("Tahmin Edilen Değerler")
plt.ylabel("Gerçek Değer")
plt.show()

#%% RxC Tabloları

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, fisher_exact

cross_tab = pd.crosstab(df["Orijin"], df["Tip"])

# 🔹 Ki-Kare Testi
chi2, p, dof, expected = chi2_contingency(cross_tab)

expected.round(2)
# 📌 Varsayım 1: Bağımsızlık Varsayımı (Bireylerin birden fazla kez sayılmadığını kontrol et)
# (Bunu test etmek için genellikle veri toplama yöntemine bakılır, kod ile doğrudan test edilemez.)

# 📌 Varsayım 2: Beklenen Frekanslar 5’ten Büyük mü?
expected_df = pd.DataFrame(expected, index=cross_tab.index, columns=cross_tab.columns)
print("\n📊 Beklenen Frekanslar:")
print(expected_df)

# 🔹 Minimum beklenen frekansı kontrol et
min_expected = np.min(expected)
if min_expected < 5:
    print("\n⚠️ En küçük beklenen frekans değeri:", min_expected)
    print("❌ Ki-Kare testi uygun olmayabilir. Fisher's Exact Test kullanılabilir.")

# 🔹 Artık Hesaplama
observed = cross_tab.values
expected = np.array(expected)

# Standartlaştırılmış Artıklar (Standardized Residuals)
std_residuals = (observed - expected) / np.sqrt(expected)

# 🔹 Artıkları DataFrame olarak göster
std_residuals_df = pd.DataFrame(std_residuals, index=cross_tab.index, columns=cross_tab.columns)

print("\n📌 Standartlaştırılmış Artıklar (Standardized Residuals):")
print(std_residuals_df)

# 🔹 Anlamlı Artıkları Belirleme (Z-test'e Göre)
significant_residuals = np.abs(std_residuals) > 2  # |SR| > 2 olan hücreler anlamlı farklıdır

print("\n📌 Anlamlı Artıklar (|SR| > 2 olan hücreler):")
print(pd.DataFrame(significant_residuals, index=cross_tab.index, columns=cross_tab.columns))
# 🔹 Yorumlama:
print("\n📌 Yorum:")
for i in range(std_residuals.shape[0]):
    for j in range(std_residuals.shape[1]):
        if np.abs(std_residuals[i, j]) > 2:
            print(f"🚨 '{cross_tab.index[i]}' & '{cross_tab.columns[j]}' hücresinde beklenenden ÖNEMLİ DERECEDE farklı bir ilişki var! (SR = {std_residuals[i, j]:.2f})")




#%% Notlar

def bagimli_ornek(veri,kolon1,kolon2,alpha):
    veri["Fark"]=veri[kolon1]-veri[kolon2]
    ##fark verilerin normal dağılıp dağılmadığı kontrol edilir.
    print(f'Fark verilerindeki gözlem sayısı {len(veri["Fark"])}, ortalama fark {veri["Fark"].mean() :.2f}')
    sonuc=normallik(veri,"Fark",alpha)
    #print(sonuc[0],"---",sonuc[1])
    if sonuc[1]<=0.5:
        print("Fark verileri normal dağılmaktadır.\nParametrik test kullanılacaktır")
        t_stat, p_value = stats.ttest_rel(veri[kolon1], veri[kolon2])
        print(f"Eşleştirilmiş t-Testi Sonucu: T-istatistiği = {t_stat:.4f}, p-değeri = {p_value:.4f}")

    else:
        print("**Fark verileri normal dağılmamaktadır.\nParametrik olmayan Wilcoxon işaret testi kullanılacaktır")
        wilcoxon_stat, p_value = stats.wilcoxon(veri[kolon1], veri[kolon2])
        
        print(f"Wilcoxon Test Sonucu: Test istatistiği = {wilcoxon_stat:.4f}, p-değeri = {p_value:.4f}")
        
    if p_value < alpha:
        print("Sonuç: Karşılaştırılan değişkenler arasında anlamlı bir fark vardır. (H0 reddedildi).")
    else:
        print("Sonuç: Karşılaştırılan değişkenler anlamlı bir fark bulunamamıştır. (H0 kabul edildi).")
    
    return sonuc




def tek_ornek(veri,kolon,test,alpha):
    #ilk olarak veri büyüklüğü kontrol edilir
    from scipy.stats import ttest_1samp
    from scipy.stats import norm
    
    ##ilk olarak verinin normalliği kontrol edilir.
    print(f"Veri setindeki gözlem sayısı {len(veri[kolon])}, ortalama değer {round(veri[kolon].mean(),2)}")
    sonuc=normallik(veri,kolon,alpha)
    print(f"{sonuc[1]}")
    if sonuc[1]<=0.5:
        print("değişken normal dağılmaktadır")
        if len(veri[kolon].dropna())>30:
            print("Gözlem Sayısı 30'dan büyük olduğu için Z istatistiği kullanılacaktır")
            n = len(veri[kolon].dropna())
            x_bar = np.mean(veri[kolon].dropna())  # Örneklem ortalaması
            s = np.std(veri[kolon].dropna(), ddof=1)  # Örneklem standart sapması (n-1 ile düzeltilmiş)
    
            # Z-istatistiği hesaplama (örneklem sapmasını kullanarak)
            z_stat = (x_bar - test) / (s / np.sqrt(n))
    
            # P-değerini hesapla (çift yönlü test için)
            p_value = 2 * (1 - norm.cdf(abs(z_stat)))
        else:
            print("Gözlem Sayısı 30'dan küçük olduğu için t istatistiği kullanılacaktır")
            t_statistic, p_value = ttest_1samp(veri[kolon].dropna(), test)  # NaN değerleri kaldır
        
        if p_value < alpha:
            print(f"**Sonuç: H0 hipotezi reddedildi, örneklem ortalaması {test} değerinden farklıdır.")
        else:
            print(f"Sonuç: H0 hipotezi reddedilemedi, örneklem ortalaması {test} değerinden farksızdır.")
       
    else:
        print("**değişken normal dağılmamaktadır")
        print("veri setinde non parametrik test uygulanmalıdır")
        # Wilcoxon İşaretli Sıralar Testi
        test_stat, p_value = stats.wilcoxon(veri[kolon].dropna() - test)
        #print(f"Wilcoxon Test İstatistiği: {test_stat:.4f}")
        print(f"P-Değeri: {p_value:.2f}")
        if p_value < alpha:
            print(f"Sonuç: Medyan {test}'ten anlamlı derecede farklıdır (H0 reddedildi).")
        else:
            print(f"Sonuç: Medyan {test} yakın olup anlamlı fark yoktur (H0 kabul edildi).")



def guv_aralik(veri,kolon,guven):
    from scipy.stats import t,norm
    import matplotlib.pyplot as plt
    import numpy as np
    ort = veri[kolon].mean()
    std_sap = veri[kolon].std()
    n = veri[kolon].count()  # Örneklem büyüklüğü

    # %95 güven aralığı için t-dağılımından kritik değeri al
    confidence_level = guven
    alpha = 1 - confidence_level
    degrees_of_freedom = n - 1  # Serbestlik derecesi
    #t_critical = t.ppf(1 - alpha / 2, degrees_of_freedom)  # t-dağılımından kritik değer. gözlem değeri 30'dan küçük ise
    #z_critical = norm.ppf(1 - alpha / 2)  # z-dağılımından kritik değer. gözlem değeri 30'dan büyük ise

    ##gözlem sayısına göre kritik değeri belirle
    if n<30:
        kritik=t.ppf(1 - alpha / 2, degrees_of_freedom)  # t-dağılımından kritik değer. gözlem değeri 30'dan küçük ise
        uyarı="not: gözlem sayısı 30'dan küçük olduğu için t tablosu kullanılmıştır."
    else:
        kritik=norm.ppf(1 - alpha / 2)  # z-dağılımından kritik değer. gözlem değeri 30'dan büyük ise
        uyarı="not: gözlem sayısı 30'dan büyük olduğu için z tablosu kullanılmıştır."
    # Güven aralığını hesapla
    margin_of_error = kritik * (std_sap / np.sqrt(n))  # Hata payı
    confidence_interval = (ort - margin_of_error, ort + margin_of_error)
    # Sonuçları yazdır
    
    print(baslik := f"{kolon} değişkeni için %95 Güven Aralığı:")
    print(ifade2 :=f"  Ortalama: {ort:.2f}")
    print(ifade3 :=f"  Güven Aralığı: ({confidence_interval[0]:.2f}, {confidence_interval[1]:.2f})")
    print(uyarı)
    
    # Grafiksel gösterim
    plt.figure(figsize=(8, 4))
    plt.errorbar(x=kolon, y=ort, yerr=margin_of_error, fmt='o', color='blue', 
                 capsize=5, label='Ortalama ve Güven Aralığı')
    plt.title(f"{kolon} için %95 Güven Aralığı")
    plt.xlabel("Değişken")
    plt.ylabel("Değer")
    
    
    # Y ekseni sınırlarını dinamik olarak ayarla
    plt.ylim(ort - 2 * margin_of_error, ort + 2 * margin_of_error)
    
    # Bilimsel gösterimi kapat
    plt.ticklabel_format(style='plain', axis='y')
    plt.legend()
    plt.grid(True)
    plt.show()
    sonuc=baslik+"\n"+ifade2+"\n"+ifade3+"\n"+uyarı
    return sonuc





plt.figure(figsize=(10, 10))
plt.pie(fmark["Ori"], labels=fmark["Marka"], autopct='%1.1f%%', startangle=140, wedgeprops={'edgecolor': 'black'})

 Başlık ekleme
plt.title("Otomobil Markalarının Dağılımı (%)")

 Grafiği gösterme
plt.show()


plt.figure(figsize=(10, 10))
plt.pie(fmark["Percent"], labels=fmark["Marka"], autopct='%1.1f%%', startangle=140, wedgeprops={'edgecolor': 'black'})

#%%


































df['Sınıf_3'], bins = pd.qcut(df['Sehir_ici'],q=9, retbins=True)
plt.figure(figsize=(10, 5))

plt.xlabel("Sınıf Aralıkları")
plt.ylabel("Frekans")
plt.title("Sabit Aralıklı Histogram (cut ile)")
plt.xticks(bins, rotation=45)
plt.show()

sns.histplot(df['Sehir_ici'], bins=9, kde=False, color="skyblue")








df_null_sayisi=df.isnull().sum().to_frame().reset_index().rename(columns={'index':'Değişken',0:'sayı'})

df_tanımlayici_ist=df.describe(include='all').T.reset_index().rename(columns={'index':'Değişken'})

df_tanımlayici_ist.merge(df_null_sayisi,how="left",on="Değişken")


df1=df.describe(include='all').T.reset_index()
df1.iloc[5:13,5:11].info()


#deneme=df.groupby('Orijin').describe(include='all').reset_index()
#df_grouped = df.groupby('Orijin').describe(include='all').stack().unstack(level=0).reset_index() # Sütun isimlerini değiştirme df_grouped.columns = ['Orijin', 'İstatistik', 'Değer']
