import tkinter as tk
import tkinter.messagebox as msgbox  # 주판 출력용 팝업창!

class Calculator:
    def __init__(self, root):
        self.expression = ""
        self.entry = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="ridge")
        self.entry.pack(expand=True, fill="both")

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', 'C', '+'],
            ['=', '주판']  # 주판 버튼 추가!!
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
        elif char == '주판':
            try:
                number = int(self.expression)
                abacus_display = self.get_abacus_display(number)
                msgbox.showinfo("중국식 주판", abacus_display)
            except:
                msgbox.showerror("오류", "유효한 숫자를 입력하세요!")
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def get_abacus_display(self, number):
        digits = list(map(int, str(number)))
        result = "=== 중국식 주판 ===\n"

        for idx, digit in enumerate(digits[::-1]):
            pos = len(digits) - idx
            upper = "●" if digit >= 5 else "○"
            lower = "●" * (digit - 5 if digit >= 5 else digit)
            lower += "○" * (4 - (digit - 5 if digit >= 5 else digit))
            result += f"{pos}의 자리: 上 {upper} 下 {lower}\n"

        result += "==================="
        return result


