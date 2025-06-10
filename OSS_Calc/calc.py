import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")  # 창 높이 조금 키움

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=', '로마변환']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        elif char == '로마변환':
            result = self.roman_to_arabic(self.expression.upper())
            self.expression = str(result)
            messagebox.showinfo("로마 숫자 변환 결과", f"변환 결과: {result}")
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def roman_to_arabic(self, s):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0

        for char in reversed(s):
            value = roman_dict.get(char, 0)
            if value < prev_value:
                total -= value
            else:
                total += value
                prev_value = value
        return total

# 실행
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
