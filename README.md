# 📰 Django Yangiliklar Sayti

Bu loyiha mening **birinchi Django frameworkida yaratgan yangiliklar portalim** hisoblanadi. Sayt oddiy va tushunarli bo‘lib, unda foydalanuvchilar yangiliklarni ko‘rishlari, ro‘yxatdan o‘tishlari mumkin. **Yangiliklar qo‘shish, tahrirlash va o‘chirish faqat admin foydalanuvchiga ruxsat etilgan.**

## 📌 Asosiy imkoniyatlar

- 👤 **Foydalanuvchilar ro‘yxatdan o‘tishi va tizimga kirishi**
- 🔐 **Admin panel orqali yangiliklar qo‘shish, tahrirlash va o‘chirish**
- 📚 **Yangiliklar ro‘yxatini ko‘rish (barcha foydalanuvchilar uchun ochiq)**
- 🖼️ **Har bir yangilikka rasm biriktirish imkoniyati**
- 📅 **Sana va vaqt bilan yangiliklar chiqariladi**
- 🗃️ **Kategoriyalar orqali saralash**
- 🔎 **Yangiliklarda matn bo‘yicha qidirish (search funksiyasi)**

## ⚙️ Texnologiyalar

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Ma’lumotlar bazasi:** SQLite (lokal) / PostgreSQL (serverda)
- **Deploy:** Render.com (bepul va doimiy hosting)

## 🚀 Ishga tushurish (localda)

```bash
git clone https://github.com/makhmudovamunira/news_project.git
cd news_project
python -m venv venv
source venv/bin/activate  # Windows uchun: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
