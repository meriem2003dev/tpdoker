from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
import sqlite3

def App():
    popup('أهلا وسهلا بكم في موقعي',
        put_text('عدد المشتركين في الموقع').onclick(lambda: toast('عدد المشتركين في الموقع 1000'))
    )
    
    put_html('<center><h3>نظام تسجيل المشتركين:</h3><img src="https://cdn-icons-png.flaticon.com/512/9187/9187604.png" width=150></center>')

    data = input_group(
        'مشترك جديد',
        [
            input('اسم المشترك', name='user'),
            input('كلمة السر', name='pass', type=PASSWORD)
        ]
    )

    # تحديد المسار الكامل لملف قاعدة البيانات
    # db_path = r"C:\Users\INFOLAB\Desktop\yaoub\U.db"  # لاحظ استخدام r قبل النص للتعامل مع الشرطة العكسية "\"
    db_path = "U.db"

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        # إنشاء الجدول إذا لم يكن موجودًا
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS U (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')

        # التحقق من الإدخال
        if not data['user'].strip() or not data['pass'].strip():
            put_error("يرجى إدخال اسم مستخدم وكلمة مرور صحيحة!")
            return

        # إدخال البيانات
        cursor.execute("INSERT INTO U(user, password) VALUES (?, ?)", (data['user'], data['pass']))
        conn.commit()
        put_success("تم تسجيل المستخدم بنجاح!")

    except sqlite3.IntegrityError:
        put_error("هذا الاسم مستخدم بالفعل!")
    
    except Exception as e:
        put_error(f"حدث خطأ: {str(e)}")
    
    finally:
        cursor.close()
        conn.close()

# تشغيل التطبيق
start_server(App, port=9090, debug=True)
