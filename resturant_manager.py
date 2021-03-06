# in order to create the manager i imported tkinter.
from tkinter import *

# all the fonts and colors that used in this program are bellow
small_font_style = ('Arial', 16)
large_font_style = ('Arial', 16, 'bold')
foods_font_style = ('arial', 15, 'bold')
menu_font = ('arial', 17, 'bold')
chosen_food_font = ('arial', 8, 'bold')
number_font = ('arial', 12, 'bold')
tax_font = ('arial', 9, 'bold')
e_box_font = ('arial', 12)
soft_pink = "PapayaWhip"
test_color = "azure1"
light_grey = '#d3d4d5'
deep_black = '#070808'
off_white = '#F8FAFF'


class RestaurantManager:

    def __init__(self):
        # creating the page the user sees.
        self.window = Tk()
        self.window.title('Restaurant manager')
        self.window.geometry("1000x500")
        self.window.resizable(0, 0)

        # the variables needed across the class.
        self.price_with_tax = '0'
        self.price_no_tax = "0"
        self.chosen_food_text = 'none'
        self.price_text = '0'
        self.number_text = '0'

        # two main frames are used to show the foods,drinks,etc and the other frame is used to show the foods chosen and the number .
        # and the combination of all the prices of foods chosen multiplied by their number.
        self.food_frame = self.create_food_frame()
        self.price_frame = self.create_price_frame()
        self.no_tax, self.with_tax, self.chosen_food, self.number, self.price, self.food_label, self.number_label, \
        self.price_label = self.create_price_labels()

        # the foods in the food column.
        self.foods = {
            "pizza:70000T": (1, 0), "hamburger:50000T": (3, 0), "soup:55000T": (5, 0),
            "sandwich:40000T": (7, 0), "pasta:65000T": (9, 0),
        }
        # buttons for choosing the desired food.
        self.create_food_buttons()

        # drinks in the drinks column
        self.drinks = {
            "pepsi:10000T": (1, 1), "coca_cola:10000T": (3, 1), "water:4000T": (5, 1),
            'energy drink:15000T': (7, 1), 'juice:8000T': (9, 1)
        }
        # buttons for choosing the desired drinks.
        self.create_drinks_buttons()
        self.appetizer = {
            "french fries:30000T": (1, 2), "ice cream:20000T": (3, 2), "garlic bread:35000T": (5, 2),
            "salad:20000T": (7, 2), "chips and cheese:30000T": (9, 2)
        }
        self.create_appetizer_buttons()
        self.create_price_button()

        # creating the rows size
        self.food_frame.rowconfigure(0, weight=1)

        # creating the rows using for loop.
        for x in range(1, 11):
            self.food_frame.rowconfigure(x, weight=1)

        # creating the column using for loop.
        for x in range(0, 3):
            self.food_frame.columnconfigure(x, weight=1)

        # the boxes bellow the food,drink,appetizer buttons that will show the number of times the buttons id pushed.
        self.e_pizza = Entry(self.food_frame, font=e_box_font, borderwidth=1)
        self.e_hamburger = Entry(self.food_frame, font=e_box_font, borderwidth=1)
        self.e_soup = Entry(self.food_frame, font=e_box_font, borderwidth=1)
        self.e_sandwich = Entry(self.food_frame, font=e_box_font, borderwidth=1)
        self.e_pasta = Entry(self.food_frame, font=e_box_font, borderwidth=1)

        self.e_pepsi = Entry(self.food_frame, font=e_box_font, borderwidth=1)
        self.e_coca_cola = Entry(self.food_frame, font=e_box_font, borderwidth=1)
        self.e_water = Entry(self.food_frame, font=e_box_font, borderwidth=1)
        self.e_energy_drink = Entry(self.food_frame, font=e_box_font, borderwidth=1)
        self.e_juice = Entry(self.food_frame, font=e_box_font, borderwidth=1)

        self.e_french_fries = Entry(self.food_frame, font=e_box_font, borderwidth=1)
        self.e_ice_cream = Entry(self.food_frame, font=e_box_font, borderwidth=1)
        self.e_garlic_bread = Entry(self.food_frame, font=e_box_font, borderwidth=1)
        self.e_salad = Entry(self.food_frame, font=e_box_font, borderwidth=1)
        self.e_chips_and_cheese = Entry(self.food_frame, font=e_box_font, borderwidth=1)

        self.food_list = [self.e_pizza, self.e_hamburger, self.e_soup, self.e_sandwich, self.e_pasta]
        self.drink_list = [self.e_pepsi, self.e_coca_cola, self.e_water, self.e_energy_drink, self.e_juice]
        self.appetizer_list = [self.e_french_fries, self.e_ice_cream, self.e_garlic_bread, self.e_salad,
                               self.e_chips_and_cheese]

        # creating the all the enter boxes at once
        self.create_food_entry_boxes()
        self.create_drink_entry_boxes()
        self.create_appetizer_entry_boxes()
        self.create_finish_button()

        # the begining number in the entry boxes.
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0
        self.num4 = 0
        self.num5 = 0
        self.num6 = 0
        self.num7 = 0
        self.num8 = 0
        self.num9 = 0
        self.num10 = 0
        self.num11 = 0
        self.num12 = 0
        self.num13 = 0
        self.num14 = 0
        self.num15 = 0
        self.num = 0

        self.total_price = 0

    def create_price_labels(self):
        chosen_food = Label(self.price_frame, text="CHOSEN FOOD", bg=soft_pink, padx=20, pady=13,
                            fg=deep_black, font=chosen_food_font)
        chosen_food.grid(row=0, column=0, sticky=NSEW, ipady=3)

        number = Label(self.price_frame, text="NUMBER", bg=soft_pink,
                       fg=deep_black, font=chosen_food_font)
        number.grid(row=0, column=1, sticky=NSEW)

        price = Label(self.price_frame, text="PRICE", bg=soft_pink, padx=25,
                      fg=deep_black, font=chosen_food_font)
        price.grid(row=0, column=2, sticky=NSEW)

        food_label = Text(self.price_frame, font=number_font, borderwidth=1, width=10, height=19)
        food_label.grid(row=1, column=0, sticky=NSEW)

        number_label = Text(self.price_frame, font=number_font, borderwidth=1, width=5, height=19)
        number_label.grid(row=1, column=1, sticky=NSEW)

        price_label = Text(self.price_frame, font=number_font, borderwidth=1, width=10, height=19)
        price_label.grid(row=1, column=2, sticky=NSEW)

        no_tax = Label(self.price_frame, text=(self.price_no_tax + " t no tax"), anchor=S, bg=light_grey,
                       fg=deep_black, padx=24, font=tax_font)
        no_tax.grid(row=2, column=0, columnspan=3, sticky=NSEW)

        with_tax = Label(self.price_frame, text=(self.price_with_tax + " t with tax"), anchor=S, bg=light_grey,
                         fg=deep_black, padx=24, font=tax_font)
        with_tax.grid(row=3, column=0, columnspan=3, sticky=NSEW)

        return no_tax, with_tax, chosen_food, number, price, food_label, number_label, price_label

    def create_price_button(self):
        button = Button(self.price_frame, text='CLEAR', bg=soft_pink, font=foods_font_style, borderwidth=1, pady=4,
                        command=self.delete)
        button.grid(row=4, column=0, columnspan=3, sticky=NSEW, ipady=2)

    def create_food_buttons(self):
        a = 1

        for digit, grid_value in self.foods.items():
            button = Button(self.food_frame, text=digit, bg=light_grey, font=foods_font_style, borderwidth=1,
                            command=lambda x=a: self.add_one_food(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=NSEW)
            a += 1
        food_label = Label(self.food_frame, text="FOODS", bg=soft_pink, font=menu_font, fg=deep_black, padx=20)
        food_label.grid(row=0, column=0, sticky=NSEW)

    def create_drinks_buttons(self):
        a = 1

        for digit, grid_value in self.drinks.items():
            button = Button(self.food_frame, text=digit, bg=light_grey, font=foods_font_style, borderwidth=1,
                            command=lambda x=a: self.add_one_drink(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=NSEW)
            a += 1
        drink_label = Label(self.food_frame, text="DRINKS", bg=soft_pink, font=menu_font, fg=deep_black, padx=20)
        drink_label.grid(row=0, column=1, sticky=NSEW)

    def create_appetizer_buttons(self):
        a = 1

        for digit, grid_value in self.appetizer.items():
            button = Button(self.food_frame, text=digit, bg=light_grey, font=foods_font_style, borderwidth=1,
                            command=lambda x=a: self.add_one_appetizer(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=NSEW)
            a += 1
        appetizer_label = Label(self.food_frame, text="APPETIZER", bg=soft_pink, font=menu_font, fg=deep_black, padx=20)
        appetizer_label.grid(row=0, column=2, sticky=NSEW)

    def create_food_entry_boxes(self):
        a = 2

        for food in self.food_list:
            food.grid(row=a, column=0, sticky=NSEW)
            a += 2

    def create_drink_entry_boxes(self):
        b = 2

        for drink in self.drink_list:
            drink.grid(row=b, column=1, sticky=NSEW)
            b += 2

    def create_appetizer_entry_boxes(self):
        c = 2

        for appetizer in self.appetizer_list:
            appetizer.grid(row=c, column=2, sticky=NSEW)
            c += 2

    def create_finish_button(self):
        button = Button(self.food_frame, text="FINISH", bg=soft_pink, font=menu_font, borderwidth=1,
                        command=self.transfer)
        button.grid(row=12, column=0, columnspan=3, sticky=NSEW)

    def create_food_frame(self):
        frame = Frame(self.window, height=500, width=700)
        frame.pack(side=RIGHT, expand=True, fill='both')
        return frame

    def create_price_frame(self):
        frame = Frame(self.window, height=500)
        frame.pack(side=LEFT, fill='both')
        return frame

    def add_one_food(self, kind):
        a = 1
        for food in self.food_list:
            try:
                if kind == a:
                    whole = food.get()
                    food.delete(0, END)
                    food.insert(0, int(whole) + 1)
            except ValueError:
                food.insert(0, '1')
            a += 1

    def add_one_drink(self, kind):
        a = 1
        for drink in self.drink_list:
            try:
                if kind == a:
                    whole = drink.get()
                    drink.delete(0, END)
                    drink.insert(0, int(whole) + 1)
            except ValueError:
                drink.insert(0, '1')
            a += 1

    def add_one_appetizer(self, kind):
        a = 1
        for app in self.appetizer_list:
            try:
                if kind == a:
                    whole = app.get()
                    app.delete(0, END)
                    app.insert(0, int(whole) + 1)
            except ValueError:
                app.insert(0, '1')
            a += 1

    def transfer(self):
        self.food_label.delete('0.1', 'end')
        self.number_label.delete('0.1', 'end')
        self.price_label.delete('0.1', 'end')

        for food in self.food_list:
            try:
                whole = int(food.get())
                if whole > 0:
                    self.number_label.insert(END, f'{whole}\n')
            except ValueError:
                food.insert(0, '0')

        for drink in self.drink_list:
            try:
                whole = int(drink.get())
                if whole > 0:
                    self.number_label.insert(END, f'{whole}\n')
            except ValueError:
                drink.insert(0, '0')

        for appetizer in self.appetizer_list:
            try:
                whole = int(appetizer.get())
                if whole > 0:
                    self.number_label.insert(END, f'{whole}\n')
            except ValueError:
                appetizer.insert(0, '0')

        pizza = self.e_pizza.get()
        hamburger = self.e_hamburger.get()
        soup = self.e_soup.get()
        sandwich = self.e_sandwich.get()
        pasta = self.e_pasta.get()

        pepsi = self.e_pepsi.get()
        coca = self.e_coca_cola.get()
        water = self.e_water.get()
        energy = self.e_energy_drink.get()
        juice = self.e_juice.get()

        french = self.e_french_fries.get()
        ice = self.e_ice_cream.get()
        garlic = self.e_garlic_bread.get()
        salad = self.e_salad.get()
        chips = self.e_chips_and_cheese.get()

        if int(pizza) > 0:
            self.food_label.insert(END, 'pizza \n')
            price = 70000
            self.price_label.insert(END, f'{price}t\n')
            self.get_text('end-8c', 'end-3c')
            self.num1 = self.num * int(pizza)

        if int(hamburger) > 0:
            self.food_label.insert(END, 'hamburger\n')
            price = 50000
            self.price_label.insert(END, f'{price}t\n')
            self.get_text('end-8c', 'end-3c')
            self.num2 = self.num * int(hamburger)

        if int(soup) > 0:
            self.food_label.insert(END, 'soup\n')
            price = 55000
            self.price_label.insert(END, f'{price}t\n')
            self.get_text('end-8c', 'end-3c')
            self.num3 = self.num * int(soup)

        if int(sandwich) > 0:
            self.food_label.insert(END, 'sandwich\n')
            price = 40000
            self.price_label.insert(END, f'{price}t\n')
            self.get_text('end-8c', 'end-3c')
            self.num4 = self.num * int(sandwich)

        if int(pasta) > 0:
            self.food_label.insert(END, 'pasta\n')
            price = 65000
            self.price_label.insert(END, f'{price}t\n')
            self.get_text('end-8c', 'end-3c')
            self.num5 = self.num * int(pasta)

        if int(pepsi) > 0:
            self.food_label.insert(END, 'pepsi\n')
            price = 10000
            self.price_label.insert(END, f'{price}t\n')
            self.get_text('end-8c', 'end-3c')
            self.num6 = self.num * int(pepsi)

        if int(coca) > 0:
            self.food_label.insert(END, 'coca_cola\n')
            price = 10000
            self.price_label.insert(END, f'{price}t\n')
            self.get_text('end-8c', 'end-3c')
            self.num7 = (self.num * int(coca)) / 2

        if int(water) > 0:
            self.food_label.insert(END, 'water\n')
            price = 4000
            self.price_label.insert(END, f'{price}t\n')
            self.get_text('end-7c', 'end-3c')
            self.num8 = self.num * int(water)

        if int(energy) > 0:
            self.food_label.insert(END, 'energy drink\n')
            price = 15000
            self.price_label.insert(END, f'{price}t\n')
            self.get_text('end-8c', 'end-3c')
            self.num9 = self.num * int(energy)

        if int(juice) > 0:
            self.food_label.insert(END, 'juice\n')
            price = 8000
            self.price_label.insert(END, f'{price}t\n')
            self.get_text('end-7c', 'end-3c')
            self.num10 = self.num * int(juice)

        if int(french) > 0:
            self.food_label.insert(END, 'french fries\n')
            price = 30000
            self.price_label.insert(END, f'{price}t\n')
            self.get_text('end-8c', 'end-3c')
            self.num11 = self.num * int(french)

        if int(ice) > 0:
            self.food_label.insert(END, 'ice cream\n')
            price = 20000
            self.price_label.insert(END, f'{price}t\n')
            self.get_text('end-8c', 'end-3c')
            self.num12 = self.num * int(ice)

        if int(garlic) > 0:
            self.food_label.insert(END, 'garlic bread\n')
            price = 35000
            self.price_label.insert(END, f'{price}t\n')
            self.get_text('end-8c', 'end-3c')
            self.num13 = self.num * int(garlic)

        if int(salad) > 0:
            self.food_label.insert(END, 'salad\n')
            price = 20000
            self.price_label.insert(END, f'{price}t\n')
            self.get_text('end-8c', 'end-3c')
            self.num14 = self.num * int(salad)

        if int(chips) > 0:
            self.food_label.insert(END, 'chips\n')
            price = 30000
            self.price_label.insert(END, f'{price}t\n')
            self.get_text('end-8c', 'end-3c')
            self.num15 = self.num * int(chips)

        self.update_total_price()

    def delete(self):
        for food in self.food_list:
            food.delete(0, END)

        for drink in self.drink_list:
            drink.delete(0, END)

        for appetizer in self.appetizer_list:
            appetizer.delete(0, END)

        self.price_label.delete('0.1', 'end')
        self.food_label.delete('0.1', 'end')
        self.number_label.delete('0.1', 'end')
        self.zero()

    def update_total_price(self):
        a = self.num1 + self.num2 + self.num3 + self.num4 + self.num5 + self.num6 + self.num7 + self.num7 + self.num8 + self.num9
        b = self.num10 + self.num11 + self.num12 + self.num13 + self.num14 + self.num15
        self.total_price = a + b
        self.no_tax.config(text=str(self.total_price) + ' t no tax')
        tax = self.total_price + (self.total_price / 4)
        self.with_tax.config(text=str(tax) + ' t with tax')

    def get_text(self, first, end):
        self.num = int(self.price_label.get(first, end))

    def zero(self):
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0
        self.num4 = 0
        self.num5 = 0
        self.num6 = 0
        self.num7 = 0
        self.num8 = 0
        self.num9 = 0
        self.num10 = 0
        self.num11 = 0
        self.num12 = 0
        self.num13 = 0
        self.num14 = 0
        self.num15 = 0
        self.total_price = 0
        self.no_tax.config(text=str(self.total_price) + ' t no tax')
        self.with_tax.config(text=str(self.total_price) + ' t with tax')

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    main = RestaurantManager()
    main.run()
