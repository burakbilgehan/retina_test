# retina_test
server-client application created with flask

server ve client uygulamalarının detaylarını anlatmaya başlamadan önce istenen ve yapamadığım üç maddeyi saymak istiyorum.
* iki ayrı virtualbox üzerinden etklileşim sağlayamadım, yani program şimdilik tek makine üzerinden çalışabiliyor.
* json konusunda bilgim olmadığı için count'un sonucunu string olarak kendim return ettim
* sanırım url'lerdeki birtakım kısıtlamalar yüzünden  http://127.0.0.1:8080/increment?key=retina yerine  http://127.0.0.1:8080/increment/retina şeklinde bir request gönderebildim.

virtualbox programını bilgisayarıma yükledikten sonra, iki ayrı klasöre (server-client) vagrant init ubuntu/xenial64 komutuyla kurulum yaptım

daha sonra vagrant up ve vagrant ssh komutlarıyla kendi terminalimden sanal makinelere bağlandım

sanal makineye sırasıyla pip, flask, redis kurulumları yaptım
sudo apt install pyton-pip
pip install Flask
pip install redis

böylece kodun çalışması için her şey tamamlanmış oldu

Server kısmı:
server kısmında temelde 3 tane fonksiyon var, ikisi benden istenenler, diğeri ise /clearall adresi girilirse tüm database'i sıfırlamak için
değişkenlerimi pokemonlar olarak belirledim ve 7 tane pokemon koydum
FLASK_APP=sefver.py flask run komutunu çalıştırınca server kendisine gelecek istekleri beklemeye başlıyor

Client kısmı:
7 pokemon ve 2 action (increment, count) için 2 ayrı rastgele sayı yarattım
"curl localhost:5000/randomaction/randompokemon" şeklinde 2 saniyede bir yeni requesti gönderdim
FLASK_APP=client.py flask run komutunu çalıştırınca client bu istekleri göndermeye başlıyor ama bu kodda flask'lık iş olmadığı için sadece "python client.py" yazmak da yeterli olur

sonuç olarak yukarıda belirttiğim eksikler haricinde (bazen de 404 hatası yerine bilmediğim başka bir errorler karşılaşıyorum) program istenildiği gibi çalışıyor
