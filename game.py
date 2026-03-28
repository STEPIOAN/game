import tkinter as tk
from tkinter import messagebox
game={
    "nba 2k":9000,
    "doom":102,
    "madden26":25,
    "volleyball legends":0,
    "supper mini games":1762000,}
spend =[]
#item to the cart
def cart (item,price):
    spend.append(price)
    card_list.insert(tk.END,f"{item}-${price}")
    total()
def updatetotal():
    total=sum(spend)
    total_label.config(text=f"total:${total}")
#checkout function
def checkout():
    if not cart:
        messagebox.showwarning("cart no items")
    else:
        messagebox.showwarning("Thank you. You have succesfully made your purchase!")
        spend.clear()
        card_list.delete(0,tk.END)
        updatetotal()
root=tk.TK()
root.title("STEAM STEAM STORE")
root.geometry("500x400")
root.resizable(False)
