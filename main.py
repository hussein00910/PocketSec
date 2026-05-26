def main():
    print("--- PocketSec: أداة الاختراق الأخلاقي ---")
    print("1. Nmap (فحص الشبكة)")
    print("2. SQLmap (فحص المواقع)")
    choice = input("اختر الأداة: ")
    target = input("أدخل IP أو الرابط: ")
    
    if choice == "1":
        print(f"جاري تشغيل Nmap على {target}...")
    elif choice == "2":
        print(f"جاري تشغيل SQLmap على {target}...")

if __name__ == "__main__":
    main()
