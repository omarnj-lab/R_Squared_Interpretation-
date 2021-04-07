# R_Squared_Interpretation : R-Kare Yorumlama: 
Bu proje, doğrusal regresyon modelinin R-Kare'sinin bir açıklamasını sağlar. 

**1- Doğrusal Regresyon ML Model:**

- Basitçe, Doğrusal regresyon, gözlemlenen verilere doğrusal bir denklem uydurarak iki değişken arasındaki ilişkiyi modellemeye çalışır.
- Bir değişken açıklayıcı bir değişken olarak kabul edilir ve diğeri bağımlı bir değişken olarak kabul edilir.
- Doğrusal regresyon, uyan çizgi ile tüm veri noktaları arasındaki mesafeyi en aza indiren bir denklem hesaplar.

Genel olarak, bir model, gözlemlenen değerler ile modelin tahmin edilen değerleri arasındaki farklar küçük ve tarafsız ise verilere iyi uyar. 

- Doğrusal regresyon, bir ürünün satışındaki pazarlama etkinliğini, fiyatlandırmayı ve promosyonları analiz etmek için de kullanılabilir.
- Doğrusal Regresyon, finansal hizmetler veya sigorta alanındaki riski değerlendirmek için de kullanılabilir. 

**2- R-kara Yorumlama:**

- R-kare, verilerin uyan regresyon çizgisine ne kadar yakın olduğunun istatistiksel bir ölçüsüdür. 
- Aynı zamanda belirleme katsayısı veya çoklu regresyon için çoklu belirleme katsayısı olarak da bilinir.
- R-karenin tanımı oldukça basittir; doğrusal bir model tarafından açıklanan yanıt değişkeni varyasyonunun yüzdesidir. Veya:

**R-kare = Açıklanan varyasyon / Toplam varyasyon**

- R kare her zaman 0 ile 1  arasındadır:

- 0, modelin ortalama çevresindeki yanıt verilerinin hiçbir değişkenliğini açıklamadığını gösterir.
- 1, modelin ortalama etrafında yanıt verilerinin tüm değişkenliğini açıkladığını gösterir.
- 
Genel olarak, R kare ne kadar yüksekse, model verilerinize o kadar iyi uyar. 

------------------------------------------------------------------------------------------------

**3- Proje:**

- Doğrusal regresyon ve R-kare arasındaki ilişkiyi anlamak için basit bir proje yapalım : 

**A : Verileri:**

Aşağıdaki gibi kullanılan veriler:
1- Birinci Sütun: Çalışanların yıllık tecrübesi içindir.
2- İkinci Sütun: çalışanların maaşıdır

Amaç:

- DOĞRUSAL REGRESYON MODELİ kullanarak, maaş ve yılların deneyimi arasındaki ilişkiyi incelemeye çalışacağız. 

![DATA](https://github.com/omarnj-lab/R_Squared_Interpretation-/blob/main/Data.png)

**B : Model:** 

bu projenin kodunu ekledim ve önemli kısmı açıklayacağım:

ilk önce, kitaplığıdan import 

`<addr>` from sklearn.metrics import r2_score
`<addr>` from sklearn.linear_model import LinearRegression

daha sonra, 

Verileri yükler, ön işleme tabi tutar ve ardından regresyon modelini uygularız. 

`<addr>` X = np.array(df['YearsExperience']).reshape(-1, 1)
`<addr>` y = df['Salary']
`<addr>` rf = LinearRegression()
`<addr>` rf.fit(X, y)
`<addr>` y_pred = rf.predict(X)

**C : Regresyon Grafiği :** 

Regresyon modelini uyguladıktan sonra, şimdi verilere uyan en iyi çizgiyi görmek için regresyon grafiğini çizmeliyiz. 

`<addr>`plt.scatter(df['YearsExperience'], df['Salary'])
`<addr>`plt.plot(X, y_pred, color='red')

![Result](https://github.com/omarnj-lab/R_Squared_Interpretation-/blob/main/RegressionGraph.png)

**C : R-Kare:** 

- Regresyon grafiğini anlamak için, tahmin yüzdesinin ne olduğunu ve tahmin edilen verilerin gerçek verilere ne kadar yakın olduğunu bilmeliyiz.
-  Bu nedenle, R kare değerini hesaplayalım >>> 

R-kareyi hesaplamanın yollarından biri şu formülle: 
     
     R² = (var(mean) - var(line)) / var(mean)
     
Bu formülü kullanarak sonuç şudur: 0.95695666414


Şimdi sklearn kitaplığını kullanarak aynı hesaplamayı yapabiliriz 

`<addr>` r2_score(y, y_pred)

ve sonuç : 0.95695666414

Bununla ve daha önce açıkladığımız gibi, R-kare değeri% 95'tir, bu da regresyon çizgisinin çok iyi uyduğunu gösterir.

Bu konuya buradan erişebilir ve daha fazla bilgi edinebilirsiniz: 

https://towardsdatascience.com/statistics-for-machine-learning-r-squared-explained-425ddfebf667
--------------------------------------------------------------------------------------------------------

Omar Najar.













