import tkinter as tk
import threading
import time
import random

class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("가계부")
        self.root.geometry("400x400")

        # 원래 배경 저장
        self.default_bg = self.root.cget("bg")

        # 금액 입력창
        self.amount_label = tk.Label(root, text="금액:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        # 추가 버튼
        self.add_button = tk.Button(root, text="지출 추가", command=self.add_expense)
        self.add_button.pack()

        # 지출 내역 표시
        self.expense_list = tk.Listbox(root)
        self.expense_list.pack(fill="both", expand=True)

    def add_expense(self):
        try:
            amount = int(self.amount_entry.get())
            self.expense_list.insert(tk.END, f"{amount}원 지출")

            # 💥 5만원 이상이면 눈뽕 모드 발동!
            if amount >= 50000:
                self.eye_blast_mode()

            self.amount_entry.delete(0, tk.END)
        except ValueError:
            self.expense_list.insert(tk.END, "❌ 잘못된 금액 입력")

    def eye_blast_mode(self):
        def blast():
            colors = ["red", "blue", "green", "yellow", "magenta", "cyan", "orange"]
            end_time = time.time() + 10
            while time.time() < end_time:
                color = random.choice(colors)
                self.root.configure(bg=color)
                time.sleep(0.2)
            self.root.configure(bg=self.default_bg)

        threading.Thread(target=blast).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()sss
