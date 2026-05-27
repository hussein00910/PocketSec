from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import subprocess

class PocketSec(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.btn = Button(text="بدء فحص Nmap")
        self.btn.bind(on_press=self.run_nmap)
        self.result = Label(text="النتائج ستظهر هنا")
        self.layout.add_widget(self.btn)
        self.layout.add_widget(self.result)
        return self.layout

    def run_nmap(self, instance):
        try:
            # تشغيل nmap (يجب أن يكون مثبتاً في البيئة)
            res = subprocess.check_output(["nmap", "scanme.nmap.org"]).decode()
            self.result.text = res[:100] # عرض أول 100 حرف
        except Exception as e:
            self.result.text = "فشل تشغيل الأداة: تأكد من التثبيت"

if __name__ == '__main__':
    PocketSec().run()

