import math
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

class Sphere():

    def framework(self, root):
        root.title("SA/V calculator")

        # * Images
        self.sphere_image = ImageTk.PhotoImage(Image.open('Sphere.png'))
        self.pyramid_image = ImageTk.PhotoImage(Image.open('pyramid.png'))
        self.cylinder_image = ImageTk.PhotoImage(Image.open('cylinder.png'))

        # * Basic
        self.image_label = Label(root, image=self.sphere_image)
        self.image_label.grid(row=1, column=1, columnspan=2)
        self.title = Label(root, text="Sphere")
        self.title.grid(row=0, column=1, columnspan=2)

        # *Side Buttons
        self.next = Button(
            root, text=">>", command=lambda: SquarePyramid.framework(self, root))
        self.next.grid(row=1, column=3)
        self.back = Button(root, text="<<", state=DISABLED)
        self.back.grid(row=1, column=0)

        # *Radius
        self.radius_frame = LabelFrame(root)
        self.radius_label = Label(self.radius_frame, text="Radius: ")
        self.radius_label.grid(row=0, column=0)
        self.radius_entry = Entry(self.radius_frame)
        self.radius_entry.grid(row=0, column=1)
        self.radius_frame.grid(row=2, column=1, columnspan=2)

        # *Side
        self.side_frame = LabelFrame(root)
        self.side_label = Label(self.side_frame, text="Base\nlength: ")
        self.side_label.grid(row=0, column=0)
        self.side_entry = Entry(self.side_frame)
        self.side_entry.grid(row=0, column=1)
        # self.side_frame.grid(row=3, column=1, columnspan=2)

        # *Height
        self.height_frame = LabelFrame(root)
        self.height_label = Label(self.height_frame, text="Height: ")
        self.height_label.grid(row=0, column=0)
        self.height_entry = Entry(self.height_frame)
        self.height_entry.grid(row=0, column=1)
        # self.height_frame.grid(row=4, column=1, columnspan=2)

        # *SA
        self.sa_frame = LabelFrame(root)
        self.sa_button = Button(self.sa_frame, text="Calculate \nSurface Area",
                                padx=5, command=lambda: Sphere.sa_calculator(self))
        self.sa_button.grid(row=0, column=0)
        self.sa_label = Label(self.sa_frame, text="")
        self.sa_label.grid(row=1, column=0)
        self.sa_frame.grid(row=5, column=1, sticky=E)

        # *Volume
        self.v_frame = LabelFrame(root)
        self.v_button = Button(self.v_frame, text="Calculate\nVolume",
                               padx=8, command=lambda: Sphere.v_calculator(self))
        self.v_button.grid(row=0, column=0)
        self.v_label = Label(self.v_frame, text="")
        self.v_label.grid(row=1, column=0)
        self.v_frame.grid(row=5, column=2, sticky=W)

    def sa_calculator(self):
        try:
            radius = float(self.radius_entry.get())
            sa = str(round(4 * math.pi * radius ** 2, 5))
        except ValueError:
            sa = ""
        self.sa_label.config(text=sa)

    def v_calculator(self):
        try:
            radius = float(self.radius_entry.get())
            v = str(round(4 * math.pi * radius ** 3 / 3, 5))
        except ValueError:
            v = ""
        self.v_label.config(text=v)

    def all_forget(self):
        self.radius_entry.delete(0, "end")
        self.height_entry.delete(0, "end")
        self.side_entry.delete(0, "end")
        self.title.grid_forget()
        self.image_label.grid_forget()
        self.next.grid_forget()
        self.back.grid_forget()
        self.radius_frame.grid_forget()
        self.height_frame.grid_forget()
        self.side_frame.grid_forget()
        self.sa_label.config(text="")
        self.sa_label.config(text="")
        return Sphere.framework(self, root)

    def reset(self):
        #!This clears the entry
        self.radius_entry.delete(0, "end")
        self.height_entry.delete(0, "end")
        self.side_entry.delete(0, "end")
        self.sa_label.config(text="")
        self.v_label.config(text="")


class SquarePyramid(Sphere):

    def framework(self, root):
        # * Reset answers using inheritance
        SquarePyramid.reset(self)
        # * Basic
        self.image_label.config(image=self.pyramid_image)
        self.title.config(text="Square Pyramid")

        # *Side Buttons
        self.next.config(
            state=NORMAL, command=lambda: Cylinder.framework(self, root))
        self.back.config(
            state=NORMAL, command=lambda: Sphere.all_forget(self))
        # *Radius
        self.radius_frame.grid_forget()

        # * Side
        self.side_frame.grid(row=3, column=1, columnspan=2)
        # *Height
        self.height_frame.grid(row=4, column=1, columnspan=2)
        # * Calculate
        self.sa_button.config(
            command=lambda: SquarePyramid.sa_calculator(self))
        self.v_button.config(command=lambda: SquarePyramid.v_calculator(self))
    #!I have to define a new definition or else it will use the one from Sphere

    def sa_calculator(self):
        try:
            side = float(self.side_entry.get())
            height = float(self.height_entry.get())
            base_area = side ** 2
            slant_height = math.sqrt(((side / 2) ** 2) + (height ** 2))
            side_area = side * slant_height / 2 * 4
            sa = str(round(base_area + side_area, 5))
        except ValueError:
            sa = ""
        self.sa_label.config(text=sa)

    def v_calculator(self):
        try:
            side = float(self.side_entry.get())
            height = float(self.height_entry.get())
            v = str(round(1 / 3 * side ** 2 * height, 5))
        except ValueError:
            v = ""
        self.v_label.config(text=v)


class Cylinder(SquarePyramid):
    # def __init__(self, root):
    #SquarePyramid.__init__(self, root)

    def framework(self, root):
        # * Reset answer
        Cylinder.reset(self)

        # *Basic
        self.image_label.config(image=self.cylinder_image)
        self.title.config(text="Cylinder")

        # *Side Buttons
        self.next.config(state=DISABLED)
        self.back.config(command=lambda: SquarePyramid.framework(self, root))

        # *Base length
        self.side_frame.grid_forget()

        # *Radius
        self.radius_frame.grid(row=3, column=1, columnspan=2)

        # *SA/V
        self.sa_button.config(command=lambda: Cylinder.sa_calculator(self))
        self.v_button.config(command=lambda: Cylinder.v_calculator(self))

    def sa_calculator(self):
        try:
            radius = float(self.radius_entry.get())
            height = float(self.height_entry.get())
            base_area = math.pi * radius ** 2 * 2
            side_area = 2 * math.pi * radius * height
            sa = str(round(base_area + side_area, 5))
        except ValueError:
            sa = ""
        self.sa_label.config(text=sa)

    def v_calculator(self):
        try:
            radius = float(self.radius_entry.get())
            height = float(self.height_entry.get())
            v = str(round(math.pi * radius ** 2 * height, 5))
        except ValueError:
            v = ""
        self.v_label.config(text=v)


a = Sphere()
a.framework(root)
root.mainloop()
