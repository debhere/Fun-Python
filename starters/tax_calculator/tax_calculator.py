import customtkinter as ctk


class TaxCalculator:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Tax Calculator")
        self.window.geometry('1000 * 1000')

        self.padding: dict = {'padx': 10, 'pady': 10}

        self.income_lbl = ctk.CTkLabel(self.window, text="Income", compound="left")
        self.income_lbl.grid(row=0, column=0, **self.padding)

        self.income_entry = ctk.CTkEntry(self.window, bg_color='blue')
        self.income_entry.grid(row=0, column=1)
        # self.income_entry.bind("<Tab>", self.get_income_entry)
        self.income_entry.bind("<KeyRelease>", self.get_income_entry)

        self.tax_lbl = ctk.CTkLabel(self.window, text="Tax %", compound="left")
        self.tax_lbl.grid(row=1, column=0, **self.padding)

        self.tax_pct = ctk.StringVar()
        self.tax_pct.set('0.00')
        self.tax_pct_lbl = ctk.CTkLabel(self.window, bg_color='blue', fg_color='grey',
                                        width=140, textvariable=self.tax_pct, compound="left")
        self.tax_pct_lbl.grid(row=1, column=1)

        self.tax_calc_lbl = ctk.CTkLabel(self.window, text='Calculated Tax', compound="left")
        self.tax_calc_lbl.grid(row=2, column=0, **self.padding)

        self.tax_op_lbl = ctk.CTkLabel(self.window, text='', compound="left")
        self.tax_op_lbl.grid(row=2, column=1)

        self.tax_calc_btn = ctk.CTkButton(self.window, text="Calculate Tax",
                                          compound="left", command=self.calculate_tax)
        self.tax_calc_btn.grid(row=3, column=0, columnspan=2)

        self.tax_reset_btn = ctk.CTkButton(self.window, text="Reset",
                                           anchor="Right", command=self.clear_window)
        self.tax_reset_btn.grid(row=3, column=3, columnspan=2)

        self.msg_lbl = ctk.CTkLabel(self.window, text='', compound="center")
        self.msg_lbl.grid(row=4, column=0, columnspan=4)

    def run(self):
        self.window.mainloop()

    def calculate_tax(self):
        tax: float = float(self.income_entry.get()) * float(self.tax_pct.get())
        self.tax_op_lbl.configure(text=f"{tax: .2f}")
        self.msg_lbl.configure(text="Tax calculated successfully!!!")

    def clear_window(self):
        var = self.income_entry.get()
        self.tax_calc_btn.configure(state="normal")
        print(var)
        self.income_entry.delete(0, len(var))
        self.tax_pct.set('0.00')
        self.tax_op_lbl.configure(text='')
        self.msg_lbl.configure(text='')

    def get_income_entry(self, event):
        self.tax_calc_btn.configure(state='normal')
        self.msg_lbl.configure(text='')
        try:
            val = self.income_entry.get()
            if 1_000_000 <= int(val) <= 1_500_000:
                self.tax_pct.set('0.1')
            if 1_500_000 < int(val) <= 2_000_000:
                self.tax_pct.set('0.2')
            if int(val) > 2_000_000:
                self.tax_pct.set('0.3')
        except Exception as e:
            print(e)
            self.tax_calc_btn.configure(state='disabled')
            self.msg_lbl.configure(text="Invalid inputs")


if __name__ == "__main__":
    tc = TaxCalculator()
    tc.run()
